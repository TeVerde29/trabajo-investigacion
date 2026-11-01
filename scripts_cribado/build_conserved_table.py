import json
import re

from verify_conserved_detail import verified_conserved

def extract_quote(abstract, title):
    # Try to find a concise sentence (<= 15 words) that summarizes the attack and defense / production evaluation
    sentences = re.split(r'\. |\.\n', abstract)
    best_quote = ""
    best_sec = "Resumen"
    
    # Priority patterns: defense & production / attack
    for s in sentences:
        s_clean = s.strip()
        words = s_clean.split()
        if 4 <= len(words) <= 15:
            if re.search(r'defense|mitigat|jailbreak|injection|poison|gpt-4|commercial|agent', s_clean, re.I):
                return s_clean, "Resumen"
                
    # If not found, truncate a key clause
    for s in sentences:
        s_clean = s.strip()
        if re.search(r'defense|mitigat|guardrail|injection|jailbreak', s_clean, re.I):
            words = s_clean.split()
            if len(words) > 15:
                # Take first 12 words
                return " ".join(words[:12]) + "...", "Resumen"
            else:
                return s_clean, "Resumen"
                
    # Fallback to title
    words_t = title.split()
    if len(words_t) <= 15:
        return title, "Título"
    else:
        return " ".join(words_t[:12]) + "...", "Título"

final_conserved_table = []
for item in verified_conserved:
    quote, sec = extract_quote(item['abstract'], item['title'])
    final_conserved_table.append({
        'id': item['id'],
        'db': item['db'],
        'title': item['title'],
        'year': item['year'],
        'doc_type': item['doc_type'],
        'doi': item['doi'],
        'vector': item['vector'],
        'def_eval': item['def_eval'],
        'mitre': item['mitre'],
        'quote': quote,
        'section': sec
    })

print(f"Generated quotes for {len(final_conserved_table)} records.")
for r in final_conserved_table[:5]:
    print(f"[{r['id']}] {r['title'][:40]} | Vector: {r['vector']} | DefEval: {r['def_eval']} | MITRE: {r['mitre']} | Quote: \"{r['quote']}\" ({r['section']})")

with open("final_conserved.json", "w", encoding="utf-8") as f:
    json.dump(final_conserved_table, f, indent=2, ensure_ascii=False)
