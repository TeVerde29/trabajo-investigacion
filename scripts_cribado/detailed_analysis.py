import json
import re

with open("candidates_f4.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# Load full details from Base de Datos.xlsx for candidates
import openpyxl
wb = openpyxl.load_workbook('Base de Datos.xlsx', data_only=True)

cand_dict = {}
for c in candidates:
    ws = wb[c['db'] if c['db'] != 'IEEE Xplore' else 'IEEE']
    headers = [ws.cell(1, col).value for col in range(1, ws.max_column + 1)]
    r = c['row']
    row_vals = {headers[col-1]: ws.cell(r, col).value for col in range(1, ws.max_column + 1)}
    row_vals['row'] = r
    row_vals['db'] = c['db']
    cand_dict[(c['db'], r)] = row_vals

print(f"Loaded full data for {len(cand_dict)} candidates.")

# Let's inspect the distribution of attack vectors:
# 1. Prompt Injection
# 2. Jailbreaking
# 3. Data Poisoning

results = []
for (db, r), rec in cand_dict.items():
    title = str(rec.get('Title') or rec.get('Document Title') or rec.get('title') or '')
    abstract = str(rec.get('Abstract') or '')
    full_text = title + " " + abstract
    
    # Vector detection
    has_pi = bool(re.search(r'prompt injection|instruction injection|indirect prompt', full_text, re.I))
    has_jb = bool(re.search(r'jailbreak|jailbreaking|safety alignment bypass|persuasive adversarial|red-teaming', full_text, re.I))
    has_dp = bool(re.search(r'data poisoning|poisoning attack|training data poisoning|backdoor|rag poisoning|knowledge poisoning', full_text, re.I))
    
    # Defense detection
    has_defense = bool(re.search(r'defense|defend|mitigat|guardrail|safety alignment|sanitiz|filtering|robustifying|protect|countermeasure|remedy', full_text, re.I))
    has_attack = bool(re.search(r'attack|adversar|jailbreak|injection|poison|vulnerab|exploit|threat', full_text, re.I))
    
    # Production context detection
    has_commercial_or_deployed = bool(re.search(r'gpt-4|gpt-3\.5|chatgpt|claude|gemini|bard|commercial|api|deployed|real-world|in-the-wild|production|agent|rag system', full_text, re.I))
    
    # Multimodal detection
    is_multimodal = bool(re.search(r'vision-language|multimodal|vlm|mllm|image-to-text|text-to-image|diffusion model|speech|audio', title, re.I))
    
    results.append({
        'db': db,
        'row': r,
        'title': title,
        'doi': rec.get('DOI') or rec.get('plink') or '',
        'year': rec.get('Year') or rec.get('Publication Year') or str(rec.get('publicationDate', ''))[:4],
        'has_pi': has_pi,
        'has_jb': has_jb,
        'has_dp': has_dp,
        'has_defense': has_defense,
        'has_attack': has_attack,
        'has_prod': has_commercial_or_deployed,
        'is_mm': is_multimodal,
        'abstract': abstract
    })

print(f"Total analyzed: {len(results)}")
print(f"Has Vector (PI/JB/DP): {sum(1 for r in results if (r['has_pi'] or r['has_jb'] or r['has_dp']))}")
print(f"Has Attack & Defense: {sum(1 for r in results if (r['has_attack'] and r['has_defense']))}")
print(f"Has Production/Commercial: {sum(1 for r in results if r['has_prod'])}")
print(f"All 3 conditions (Vector + Atk/Def + Prod) & not MM: {sum(1 for r in results if (r['has_pi'] or r['has_jb'] or r['has_dp']) and (r['has_attack'] and r['has_defense']) and r['has_prod'] and not r['is_mm'])}")
