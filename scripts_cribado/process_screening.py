import openpyxl
import json
import re

wb = openpyxl.load_workbook('Base de Datos.xlsx', data_only=True)

# Scopus headers
ws_s = wb['Scopus']
h_s = [ws_s.cell(1, c).value for c in range(1, ws_s.max_column + 1)]
scopus_records = []
for r in range(2, ws_s.max_row + 1):
    rec = {h_s[c-1]: ws_s.cell(r, c).value for c in range(1, ws_s.max_column + 1)}
    rec['row'] = r
    rec['source_db'] = 'Scopus'
    scopus_records.append(rec)

# IEEE headers
ws_i = wb['IEEE']
h_i = [ws_i.cell(1, c).value for c in range(1, ws_i.max_column + 1)]
ieee_records = []
for r in range(2, ws_i.max_row + 1):
    rec = {h_i[c-1]: ws_i.cell(r, c).value for c in range(1, ws_i.max_column + 1)}
    rec['row'] = r
    rec['source_db'] = 'IEEE Xplore'
    ieee_records.append(rec)

# EBSCO headers
ws_e = wb['EBSCO HOST']
h_e = [ws_e.cell(1, c).value for c in range(1, ws_e.max_column + 1)]
ebsco_records = []
for r in range(2, ws_e.max_row + 1):
    rec = {h_e[c-1]: ws_e.cell(r, c).value for c in range(1, ws_e.max_column + 1)}
    rec['row'] = r
    rec['source_db'] = 'EBSCO HOST'
    ebsco_records.append(rec)

print(f"Loaded: Scopus={len(scopus_records)}, IEEE={len(ieee_records)}, EBSCO={len(ebsco_records)}")
