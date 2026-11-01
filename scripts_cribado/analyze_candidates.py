import openpyxl
import re

wb = openpyxl.load_workbook('Base de Datos.xlsx', data_only=True)

# Scopus
ws_s = wb['Scopus']
h_s = [ws_s.cell(1, c).value for c in range(1, ws_s.max_column + 1)]
scopus_f3_pass = []
for r in range(2, ws_s.max_row + 1):
    rec = {h_s[c-1]: ws_s.cell(r, c).value for c in range(1, ws_s.max_column + 1)}
    rec['row'] = r
    rec['db'] = 'Scopus'
    dt = rec.get('Document Type') or ''
    yr = rec.get('Year')
    oa = rec.get('Open Access') or ''
    if dt in ['Book chapter', 'Note'] or yr not in [2023, 2024, 2025, 2026]:
        continue
    if not oa:
        continue
    scopus_f3_pass.append(rec)

# IEEE
ws_i = wb['IEEE']
h_i = [ws_i.cell(1, c).value for c in range(1, ws_i.max_column + 1)]
ieee_f3_pass = []
for r in [2, 4]: # Rows with CCBY
    rec = {h_i[c-1]: ws_i.cell(r, c).value for c in range(1, ws_i.max_column + 1)}
    rec['row'] = r
    rec['db'] = 'IEEE Xplore'
    ieee_f3_pass.append(rec)

# EBSCO
ws_e = wb['EBSCO HOST']
h_e = [ws_e.cell(1, c).value for c in range(1, ws_e.max_column + 1)]
ebsco_f3_pass = []
for r in [2, 3, 5, 8, 11]: # Non-news rows
    rec = {h_e[c-1]: ws_e.cell(r, c).value for c in range(1, ws_e.max_column + 1)}
    rec['row'] = r
    rec['db'] = 'EBSCO HOST'
    ebsco_f3_pass.append(rec)

all_candidates = scopus_f3_pass + ieee_f3_pass + ebsco_f3_pass
print(f"Total candidate records reaching F4: {len(all_candidates)}")
print(f"  Scopus: {len(scopus_f3_pass)}")
print(f"  IEEE: {len(ieee_f3_pass)}")
print(f"  EBSCO: {len(ebsco_f3_pass)}")

with open("candidates_f4.json", "w", encoding="utf-8") as f:
    import json
    json.dump([{
        'db': c['db'],
        'row': c['row'],
        'title': c.get('Title') or c.get('Document Title') or c.get('title'),
        'doi': c.get('DOI') or '',
        'year': c.get('Year') or c.get('Publication Year') or str(c.get('publicationDate', ''))[:4],
        'abstract': c.get('Abstract') or ''
    } for c in all_candidates], f, indent=2, ensure_ascii=False)

print("Saved candidates_f4.json")
