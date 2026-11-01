import openpyxl
import requests
import concurrent.futures
import time
import json
import re

wb = openpyxl.load_workbook('Base de Datos.xlsx', data_only=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

records = []

# Scopus
ws_s = wb['Scopus']
h_s = [ws_s.cell(1, c).value for c in range(1, ws_s.max_column + 1)]
for r in range(2, ws_s.max_row + 1):
    vals = {h_s[c-1]: ws_s.cell(r, c).value for c in range(1, ws_s.max_column + 1)}
    col1_val = ws_s.cell(r, 1).value
    records.append({
        'id': r,
        'db': 'Scopus',
        'col1_val': col1_val,
        'title': vals.get('Title') or '',
        'doi': vals.get('DOI') or '',
        'link': vals.get('Link') or '',
        'year': vals.get('Year') or '',
        'doc_type': vals.get('Document Type') or '',
        'oa': vals.get('Open Access') or '',
        'abstract': vals.get('Abstract') or ''
    })

# IEEE
ws_i = wb['IEEE']
h_i = [ws_i.cell(1, c).value for c in range(1, ws_i.max_column + 1)]
for r in range(2, ws_i.max_row + 1):
    vals = {h_i[c-1]: ws_i.cell(r, c).value for c in range(1, ws_i.max_column + 1)}
    col1_val = ws_i.cell(r, 1).value
    records.append({
        'id': r,
        'db': 'IEEE Xplore',
        'col1_val': col1_val,
        'title': vals.get('Document Title') or '',
        'doi': vals.get('DOI') or '',
        'link': vals.get('PDF Link') or '',
        'year': vals.get('Publication Year') or '',
        'doc_type': 'Article' if 'IEEE Access' in str(vals.get('Publication Title')) else 'Conference paper',
        'license': vals.get('License') or '',
        'oa': 'CC BY' if vals.get('License') == 'CCBY' else '',
        'abstract': vals.get('Abstract') or ''
    })

# EBSCO
ws_e = wb['EBSCO HOST']
h_e = [ws_e.cell(1, c).value for c in range(1, ws_e.max_column + 1)]
for r in range(2, ws_e.max_row + 1):
    vals = {h_e[c-1]: ws_e.cell(r, c).value for c in range(1, ws_e.max_column + 1)}
    col1_val = ws_e.cell(r, 1).value
    records.append({
        'id': r,
        'db': 'EBSCO HOST',
        'col1_val': col1_val,
        'title': vals.get('title') or '',
        'doi': '',
        'link': vals.get('plink') or '',
        'year': str(vals.get('publicationDate') or '')[:4],
        'doc_type': 'Article/Preprint',
        'oa': 'acceso por confirmar',
        'abstract': ''
    })

print(f"Total collected records: {len(records)}")

def check_record_access(rec):
    target = rec['doi'] if rec['doi'] else rec['link']
    if not target:
        return rec['db'], rec['id'], "Sin DOI/URL disponible", False, ""
    
    url = target.strip()
    if not url.startswith("http"):
        url = "https://doi.org/" + url
    
    try:
        r = requests.head(url, headers=headers, timeout=5, allow_redirects=True)
        if r.status_code in [200, 201, 204]:
            return rec['db'], rec['id'], f"Exitoso (HTTP {r.status_code})", True, r.url
        elif r.status_code in [401, 403]:
            return rec['db'], rec['id'], f"Fallido (HTTP {r.status_code} - Paywall / Restringido)", False, r.url
        elif r.status_code == 202:
            return rec['db'], rec['id'], f"Fallido (HTTP 202 - Bot detection / Cloudflare)", False, r.url
        elif r.status_code == 404:
            return rec['db'], rec['id'], f"Fallido (HTTP 404 - No encontrado)", False, r.url
        else:
            r2 = requests.get(url, headers=headers, timeout=5, stream=True)
            if r2.status_code == 200:
                return rec['db'], rec['id'], f"Exitoso (HTTP 200)", True, r2.url
            else:
                return rec['db'], rec['id'], f"Fallido (HTTP {r2.status_code})", False, r2.url
    except requests.exceptions.Timeout:
        return rec['db'], rec['id'], "Fallido (Timeout > 5s)", False, url
    except Exception as e:
        return rec['db'], rec['id'], f"Fallido ({type(e).__name__})", False, url

print("Starting multithreaded URL checking for all 484 records...")
t0 = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
    access_results = list(executor.map(check_record_access, records))
print(f"Completed access check in {time.time()-t0:.2f}s")

access_map = {}
for db, rid, status, ok, final_url in access_results:
    access_map[(db, rid)] = {
        'status': status,
        'ok': ok,
        'final_url': final_url
    }

with open("access_log.json", "w", encoding="utf-8") as f:
    # serialize
    serializable = {f"{k[0]}_{k[1]}": v for k, v in access_map.items()}
    json.dump(serializable, f, indent=2)

print("Saved access_log.json successfully.")
