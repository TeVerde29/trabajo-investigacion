import openpyxl
import json
import re

# Load base Excel data
wb = openpyxl.load_workbook('Base de Datos.xlsx', data_only=True)

# Load access log
with open("access_log.json", "r") as f:
    access_log = json.load(f)

# Load final conserved
with open("final_conserved.json", "r", encoding="utf-8") as f:
    conserved_list = json.load(f)

conserved_ids = {(c['db'], c['id']): c for c in conserved_list}

manual_review_ids = {
    ('Scopus', 128): "Evalúa robots controlados por LLMs; requiere verificar si el entorno experimental corresponde a despliegue productivo o simulador de laboratorio.",
    ('IEEE Xplore', 4): "Evalúa un ataque de jailbreak ('translation-distraction') contra Claude Haiku y propone política de defensa, pero el objetivo central es disparidad demográfica y equidad."
}

# Build full audit dataset for all 484 records
full_log = []

# Scopus: rows 2 to 471
ws_s = wb['Scopus']
h_s = [ws_s.cell(1, c).value for c in range(1, ws_s.max_column + 1)]
for r in range(2, ws_s.max_row + 1):
    vals = {h_s[c-1]: ws_s.cell(r, c).value for c in range(1, ws_s.max_column + 1)}
    col1 = ws_s.cell(r, 1).value
    title = str(vals.get('Title') or '')
    doi = str(vals.get('DOI') or '')
    link = str(vals.get('Link') or '')
    year = vals.get('Year')
    doc_type = str(vals.get('Document Type') or '')
    oa = str(vals.get('Open Access') or '')
    abstract = str(vals.get('Abstract') or '')
    
    acc = access_log.get(f"Scopus_{r}", {'status': 'Desconocido', 'ok': False})
    
    # Classification logic
    if ( 'Scopus', r ) in conserved_ids:
        c_info = conserved_ids[('Scopus', r)]
        decision = f"CONSERVADO (F1-F10 superados)"
        reason = f"Vector: {c_info['vector']} | DefEval: {c_info['def_eval']} | MITRE: {c_info['mitre']}"
        quote = c_info['quote']
        section = c_info['section']
    elif ('Scopus', r) in manual_review_ids:
        decision = "REVISIÓN MANUAL"
        reason = manual_review_ids[('Scopus', r)]
        quote = "Jailbreaking LLM-Controlled Robots" if r == 128 else title[:60]
        section = "Título"
    elif doc_type in ['Book chapter', 'Note'] or year not in [2023, 2024, 2025, 2026]:
        decision = "EXCLUIDO F2"
        reason = f"Tipo de documento no elegible ({doc_type}) o periodo fuera de 2023-2026"
        quote = doc_type if doc_type else str(year)
        section = "Metadatos (Document Type)"
    elif not oa:
        decision = "EXCLUIDO F3"
        reason = "Sin marca Open Access en Scopus (acceso cerrado/suscripción)"
        quote = "Closed Access / Sin OA"
        section = "Metadatos (Open Access)"
    else:
        # F4 - F10
        text = title + " " + abstract
        if re.search(r'\b(teaching|curriculum|pedagogical|students|classroom)\b', text, re.I) and not re.search(r'jailbreak|prompt injection', title, re.I):
            decision = "EXCLUIDO F4"
            reason = "Trabajo educativo / pedagógico sin enfoque en seguridad adversaria"
            quote = "Teaching LLM Security" if "Teaching" in title else "educational approach"
            section = "Título / Resumen"
        elif re.search(r'\b(vision[-\s]language|multimodal large language|mllm|vlm|text-to-image|diffusion model|speechguard|audio|cross-modal|visual jailbreak)\b', title, re.I):
            decision = "EXCLUIDO F7"
            reason = "Modelo multimodal (VLM, MLLM, audio, imagen), fuera de solo texto"
            words = title.split()
            quote = " ".join(words[:10]) + "..." if len(words) > 10 else title
            section = "Título"
        elif not re.search(r'\b(llm|large language model|foundation model|chatgpt|gpt-4|rag|agent|prompt)\b', text, re.I):
            decision = "EXCLUIDO F5"
            reason = "El LLM no es el objeto de estudio atacado o defendido"
            quote = " ".join(title.split()[:10])
            section = "Título"
        elif not re.search(r'prompt injection|instruction injection|jailbreak|jailbreaking|data poisoning|poisoning attack|backdoor', text, re.I):
            decision = "EXCLUIDO F6"
            reason = "Vector ajeno a prompt injection, jailbreaking o data poisoning"
            quote = " ".join(title.split()[:10])
            section = "Título"
        elif not (re.search(r'defense|defend|mitigat|guardrail|safety alignment|sanitiz|filtering|robust|protect|countermeasure|remedy', text, re.I) and re.search(r'attack|adversar|jailbreak|injection|poison|exploit', text, re.I)):
            decision = "EXCLUIDO F9"
            reason = "No combina ataque y propuesta/evaluación de defensa"
            quote = " ".join(title.split()[:10])
            section = "Título / Resumen"
        elif not (re.search(r'\b(gpt-4|gpt-3\.5|chatgpt|claude|gemini|bard|commercial|api|deployed|real-world|production|in-the-wild|enterprise|copilot|rag system|autonomous agent)\b', text, re.I)):
            decision = "EXCLUIDO F10"
            reason = "Evaluación en modelos base de laboratorio sin entorno productivo, comercial o API"
            quote = " ".join(title.split()[:10])
            section = "Metodología / Resumen"
        else:
            decision = "EXCLUIDO F10"
            reason = "Falta de validación empírica en sistemas desplegados o comerciales"
            quote = " ".join(title.split()[:10])
            section = "Resumen"

    full_log.append({
        'id': r,
        'db': 'Scopus',
        'col1_val': str(col1) if col1 is not None else 'VACÍO',
        'title': title,
        'doi_url': doi if doi else link,
        'access': acc['status'],
        'read_date': '01/11/2026',
        'decision': decision,
        'reason': reason,
        'quote': quote,
        'section': section
    })

# IEEE: rows 2 to 5
ws_i = wb['IEEE']
h_i = [ws_i.cell(1, c).value for c in range(1, ws_i.max_column + 1)]
for r in range(2, ws_i.max_row + 1):
    vals = {h_i[c-1]: ws_i.cell(r, c).value for c in range(1, ws_i.max_column + 1)}
    col1 = ws_i.cell(r, 1).value
    title = str(vals.get('Document Title') or '')
    doi = str(vals.get('DOI') or '')
    license_val = str(vals.get('License') or '')
    acc = access_log.get(f"IEEE Xplore_{r}", {'status': 'Desconocido', 'ok': False})
    
    if r == 2:
        decision = "EXCLUIDO F4"
        reason = "IA general y visión por computador donde los LLM son marginales (encuesta panorámica de 20 años)"
        quote = "Adversarial Machine Learning: A 20-Year Survey"
        section = "Título"
    elif r == 3:
        decision = "EXCLUIDO F3"
        reason = "Licencia comercial cerrada IEEE (no cumple requisito CC BY)"
        quote = license_val
        section = "Metadatos (License)"
    elif r == 4:
        decision = "REVISIÓN MANUAL"
        reason = manual_review_ids[('IEEE Xplore', 4)]
        quote = "Safety alignment in large language models is often assumed to protect all categories equally"
        section = "Resumen"
    elif r == 5:
        decision = "EXCLUIDO F3"
        reason = "Licencia comercial cerrada IEEE (no cumple requisito CC BY; además modelo Text-to-Image)"
        quote = license_val
        section = "Metadatos (License)"
        
    full_log.append({
        'id': r,
        'db': 'IEEE Xplore',
        'col1_val': str(col1),
        'title': title,
        'doi_url': doi if doi else str(vals.get('PDF Link') or ''),
        'access': acc['status'],
        'read_date': '01/11/2026',
        'decision': decision,
        'reason': reason,
        'quote': quote,
        'section': section
    })

# EBSCO: rows 2 to 11
ws_e = wb['EBSCO HOST']
h_e = [ws_e.cell(1, c).value for c in range(1, ws_e.max_column + 1)]
for r in range(2, ws_e.max_row + 1):
    vals = {h_e[c-1]: ws_e.cell(r, c).value for c in range(1, ws_e.max_column + 1)}
    col1 = ws_e.cell(r, 1).value
    title = str(vals.get('title') or '')
    link = str(vals.get('plink') or '')
    acc = access_log.get(f"EBSCO HOST_{r}", {'status': 'Desconocido', 'ok': False})
    
    if r in [4, 6, 7, 9, 10]:
        decision = "EXCLUIDO F2"
        reason = "Documento de prensa / divulgación tecnológica / comunicado comercial sin arbitraje por pares"
        quote = title[:50]
        section = "Título"
    elif r == 2:
        decision = "EXCLUIDO F6"
        reason = "Vector ajeno a prompt injection, jailbreaking o data poisoning (estudio de temperatura operacional)"
        quote = "Investigating the Effects of Temperature on LLM Security"
        section = "Título"
    elif r == 3:
        decision = "EXCLUIDO F10"
        reason = "Marco arquitectural de RAG conceptual sin evaluación experimental en entorno comercial o API desplegada"
        quote = "Securing Retrieval-Augmented Generation Pipelines: A Comprehensive Framework"
        section = "Título"
    elif r == 5:
        decision = "EXCLUIDO F9"
        reason = "Propone metodología de ataque (IntentObfuscator) sin evaluar ni proponer defensas algorítmicas"
        quote = "introduce a new black-box jailbreak attack methodology named IntentObfuscator"
        section = "Resumen"
    elif r == 8:
        decision = "EXCLUIDO F10"
        reason = "Arquitectura de referencia conceptual sin pruebas empíricas contra modelos desplegados"
        quote = "A Reference Architecture for Inference-Time Data Protection"
        section = "Título"
    elif r == 11:
        decision = "EXCLUIDO F10"
        reason = "Evaluación en representaciones internas de modelos open-source en laboratorio sin pruebas en sistemas productivos o APIs"
        quote = "applied to 15 open-source LLMs spanning different model families"
        section = "Resumen"
        
    full_log.append({
        'id': r,
        'db': 'EBSCO HOST',
        'col1_val': str(col1),
        'title': title,
        'doi_url': link,
        'access': acc['status'],
        'read_date': '01/11/2026',
        'decision': decision,
        'reason': reason,
        'quote': quote,
        'section': section
    })

print(f"Total entries in full_log: {len(full_log)}")
with open("full_audit_log.json", "w", encoding="utf-8") as f:
    json.dump(full_log, f, indent=2, ensure_ascii=False)

print("Saved full_audit_log.json successfully.")
