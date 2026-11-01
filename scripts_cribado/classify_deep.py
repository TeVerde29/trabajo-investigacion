import openpyxl
import json
import re

# Load candidates reaching F4
with open("candidates_f4.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# Load full records from Base de Datos.xlsx
wb = openpyxl.load_workbook('Base de Datos.xlsx', data_only=True)

# Build a dictionary of candidate records with full metadata
cand_full = []
for c in candidates:
    sheetname = 'IEEE' if c['db'] == 'IEEE Xplore' else c['db']
    ws = wb[sheetname]
    headers = [ws.cell(1, col).value for col in range(1, ws.max_column + 1)]
    r = c['row']
    vals = {headers[col-1]: ws.cell(r, col).value for col in range(1, ws.max_column + 1)}
    
    title = str(vals.get('Title') or vals.get('Document Title') or vals.get('title') or '')
    abstract = str(vals.get('Abstract') or '')
    doi = str(vals.get('DOI') or vals.get('plink') or '')
    year = vals.get('Year') or vals.get('Publication Year') or str(vals.get('publicationDate') or '2025')[:4]
    doc_type = vals.get('Document Type') or ('Article' if 'IEEE Access' in str(vals.get('Publication Title', '')) else 'Conference paper')
    
    cand_full.append({
        'id': r,
        'db': c['db'],
        'title': title,
        'year': year,
        'doi': doi,
        'doc_type': doc_type,
        'abstract': abstract,
        'oa': vals.get('Open Access') or vals.get('License') or 'acceso por confirmar'
    })

print(f"Total candidates in memory: {len(cand_full)}")

# Let's inspect each candidate and classify with detailed rules
# We need to test:
# F4: Alcance temático (C3)
# F5: Verificación de contenido (C4)
# F6: Vector central (C5-1)
# F7: Solo texto (C5-2)
# F8: LLM como objeto de estudio (C5-3)
# F9: Ataque y defensa (C5-4)
# F10: Contexto de producción (C6)

classified = []
for item in cand_full:
    title = item['title']
    abstract = item['abstract']
    text = title + " " + abstract
    
    # 1. F4 Checks
    # Trabajos educativos
    if re.search(r'\b(teaching|curriculum|pedagogical|students|classroom)\b', text, re.I) and not re.search(r'jailbreak|prompt injection', title, re.I):
        classified.append((item, 'EXCL_F4', 'Trabajos educativos, pedagógicos o formativos sin enfoque primario de seguridad adversaria', 'Título / Resumen'))
        continue
    # Estudios de sesgo/equidad sin componente adversario
    if re.search(r'\b(demographic fairness|gender bias|racial bias|fairly across demographic)\b', text, re.I) and not re.search(r'adversarial attack|jailbreak|poisoning|prompt injection', text, re.I):
        classified.append((item, 'EXCL_F4', 'Estudios de sesgo o equidad demográfica sin componente adversario', 'Título / Resumen'))
        continue
    # IA general donde LLM es marginal
    if item['db'] == 'IEEE Xplore' and item['id'] == 2: # Adversarial Machine Learning 20-Year Survey
        classified.append((item, 'EXCL_F4', 'IA general y visión por computador donde los LLM son marginales (encuesta panorámica de 20 años)', 'Título'))
        continue
    # LLM como herramienta para atacar otro sistema
    if re.search(r'\b(fuzzing|smart contract vulnerability|smart contracts|penetration testing tool|automated exploit generation for c|phishing email generation)\b', text, re.I) and not re.search(r'jailbreak|prompt injection|poisoning', title, re.I):
        classified.append((item, 'EXCL_F4', 'LLM utilizado como herramienta para auditar o atacar otro software externo', 'Título / Resumen'))
        continue

    # 2. F7 Checks (Solo texto vs Multimodal)
    # Check if primarily multimodal / VLM / MLLM / image / speech / audio
    if re.search(r'\b(vision[-\s]language|multimodal large language|mllm|vlm|text-to-image|diffusion model|speechguard|audio|cross-modal|visual jailbreak)\b', title, re.I):
        classified.append((item, 'EXCL_F7', 'Modelos multimodales (VLM, MLLM, audio, imagen) fuera del alcance de solo texto', 'Título'))
        continue

    # 3. F5 / F8 Checks (LLM como objeto de estudio)
    # Check if LLM is the object attacked or defended
    # If not LLM / foundation model / RAG / agent
    if not re.search(r'\b(llm|large language model|foundation model|chatgpt|gpt-4|rag|agent|prompt)\b', text, re.I):
        classified.append((item, 'EXCL_F5', 'El LLM o sistema integrado no es el objeto primario de ataque o defensa', 'Resumen'))
        continue

    # 4. F6 Checks (Vector central: Prompt Injection, Jailbreak, Data Poisoning)
    is_pi = bool(re.search(r'prompt injection|instruction injection|indirect prompt injection', text, re.I))
    is_jb = bool(re.search(r'jailbreak|jailbreaking|bypassing safety alignment|persuasive adversarial prompt|red-teaming jailbreak', text, re.I))
    is_dp = bool(re.search(r'data poisoning|poisoning attack|training data poisoning|backdoor attack|rag poisoning|knowledge poisoning', text, re.I))
    
    if not (is_pi or is_jb or is_dp):
        # Exclude: general privacy/data leakage without injection/jailbreak, general hallucination, general adversarial typos
        classified.append((item, 'EXCL_F6', 'Vector central ajeno a prompt injection, jailbreaking o data poisoning (fuga de datos, alucinación o perturbaciones léxicas generales)', 'Título / Resumen'))
        continue

    # Determine vector label
    vectors = []
    if is_pi: vectors.append("Prompt Injection")
    if is_jb: vectors.append("Jailbreaking")
    if is_dp: vectors.append("Data Poisoning")
    vector_label = " / ".join(vectors)

    # 5. F9 Checks (Ataque y defensa)
    has_attack = bool(re.search(r'attack|adversar|jailbreak|injection|poison|exploit|threat|vulnerab', text, re.I))
    has_defense = bool(re.search(r'defense|defend|mitigat|guardrail|safety alignment|sanitiz|filtering|robust|protect|countermeasure|remedy|dpo|rlhf|detector', text, re.I))
    
    if not (has_attack and has_defense):
        if has_attack and not has_defense:
            classified.append((item, 'EXCL_F9', 'Describe únicamente vectores de ataque sin proponer ni evaluar defensas algorítmicas', 'Resumen'))
        else:
            classified.append((item, 'EXCL_F9', 'Propone defensas sin evaluar ataques adversarios sobre LLMs', 'Resumen'))
        continue

    # 6. F10 Checks (Contexto de producción)
    # Must evaluate deployed system, commercial model/API (GPT-4, Claude, Gemini, ChatGPT), commercial app, deployed RAG/agents
    # Exclude laboratory-only base models (e.g. only LLaMA-7B or synthetic base models on local GPU without commercial API/production context)
    has_commercial = bool(re.search(r'\b(gpt-4|gpt-3\.5|chatgpt|claude|gemini|bard|commercial|api|deployed|real-world|production|in-the-wild|enterprise|copilot)\b', text, re.I))
    has_rag_or_agent = bool(re.search(r'\b(rag system|retrieval-augmented|autonomous agent|tool-use|agentic system)\b', text, re.I))
    
    if not (has_commercial or has_rag_or_agent):
        classified.append((item, 'EXCL_F10', 'Evaluación realizada exclusivamente en modelos base sintéticos de laboratorio sin entorno productivo, comercial o API', 'Metodología / Resumen'))
        continue

    # Passed F10 -> CONSERVED!
    # F11: Defensa evaluada empíricamente
    has_empirical = bool(re.search(r'\b(benchmark|experiment|evaluated on|attack success rate|asr|accuracy|reduction|dataset|measured|empirical)\b', text, re.I))
    def_eval = "Sí" if has_empirical else "No / parcial"

    # F12: MITRE ATLAS mapping
    mitre_tech = []
    if is_pi:
        if re.search(r'indirect', text, re.I):
            mitre_tech.append("AML.T0051.001 (LLM Prompt Injection: Indirect)")
        else:
            mitre_tech.append("AML.T0051.000 (LLM Prompt Injection: Direct)")
    if is_jb:
        mitre_tech.append("AML.T0054 (LLM Jailbreak Injection)")
    if is_dp:
        if re.search(r'rag|knowledge|context', text, re.I):
            mitre_tech.append("AML.T0099 (AI Agent / Context Data Poisoning)")
        else:
            mitre_tech.append("AML.T0020 (Training Data Poisoning)")
    mitre_label = "; ".join(mitre_tech)

    classified.append((item, 'CONSERVADO', vector_label, def_eval, mitre_label))

print("Classification summary:")
from collections import Counter
status_counts = Counter([c[1] for c in classified])
for k, v in status_counts.items():
    print(f"  {k}: {v}")
