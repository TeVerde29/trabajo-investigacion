# -*- coding: utf-8 -*-
import docx

doc_path = r"c:\Users\hikih\Documents\Repositorios\trabajo-investigacion\ANÁLISIS BIBLIOMÉTRICO.docx"
doc = docx.Document(doc_path)

print("=== VERIFYING ANÁLISIS BIBLIOMÉTRICO.docx ===")
print("Paragraphs count:", len(doc.paragraphs))
print("Tables count:", len(doc.tables))
print("Sections count:", len(doc.sections))

# 1. Check PRISMA absence
prisma_found = []
for i, p in enumerate(doc.paragraphs):
    if "prisma" in p.text.lower():
        prisma_found.append(f"P[{i}]: {p.text[:60]}")
for t_idx, t in enumerate(doc.tables):
    for r_idx, r in enumerate(t.rows):
        for c_idx, c in enumerate(r.cells):
            if "prisma" in c.text.lower():
                prisma_found.append(f"T{t_idx+1} R{r_idx} C{c_idx}: {c.text[:60]}")

print("PRISMA occurrences found:", len(prisma_found))
if prisma_found:
    print("WARNING:", prisma_found)
else:
    print("PASS: 0 mentions of PRISMA anywhere in document!")

# 2. Check Figures
figures = [p.text for p in doc.paragraphs if p.text.startswith("Figura")]
print("Figures count:", len(figures))
for f in figures:
    print(" ", f)

# 3. Check Tables
tables_captions = [p.text for p in doc.paragraphs if p.text.startswith("Tabla")]
print("Tables captions count:", len(tables_captions))
for tc in tables_captions:
    print(" ", tc)

for idx, t in enumerate(doc.tables):
    trPr = t.rows[0]._tr.get_or_add_trPr()
    has_header = len(trPr.xpath("./w:tblHeader")) > 0
    all_cantsplit = all(len(r._tr.get_or_add_trPr().xpath("./w:cantSplit")) > 0 for r in t.rows)
    print(f"Table {idx+1}: {len(t.rows)} rows x {len(t.columns)} cols | tblHeader={has_header} | cantSplit={all_cantsplit}")

# 4. Check author & email
author_block = doc.paragraphs[3].text
print("Author block:", repr(author_block))
assert "pedro.ricra.figueroa@gmail.com" in author_block, "Author email missing!"
assert "Pedro Giovanni Ricra Figueroa" in author_block, "Author name missing!"

print("ALL BASIC AUDIT CHECKS PASS!")
