import json

with open("full_audit_log.json", "r", encoding="utf-8") as f:
    full_log = json.load(f)

with open("final_conserved.json", "r", encoding="utf-8") as f:
    conserved = json.load(f)

# Sort
db_order = {'Scopus': 1, 'IEEE Xplore': 2, 'EBSCO HOST': 3}
full_log.sort(key=lambda x: (db_order[x['db']], x['id']))

# Generate Markdown lines
lines = []
lines.append("# Auditoría y Cribado Sistemático de la Base Bibliográfica (484 Registros)")
lines.append("\n**Tema:** Vulnerabilidades de evasión y defensas de seguridad en LLMs en producción bajo MITRE ATLAS (2023–2026)")
lines.append("**Bases:** Scopus (470 registros), IEEE Xplore (4 registros), EBSCO HOST (10 registros)")
lines.append(f"**Fecha de ejecución:** 01/11/2026 | **Total procesados:** {len(full_log)} | **Conservados:** {len(conserved)} | **Revisión Manual:** 2 | **No Verificados:** 0\n")

lines.append("## 1. Tabla Resumen del Embudo Metodológico (F0 a F12)\n")
lines.append("| Filtro | Descripción | Entran | Salen | Excluidos | Criterio y Razón Principal de Exclusión |")
lines.append("| :---: | :--- | :---: | :---: | :---: | :--- |")
lines.append("| **F0** | Base de partida inicial | 484 | 484 | 0 | Verificación inicial de conteo exacto (Scopus 470, IEEE 4, EBSCO 10) |")
lines.append("| **F1** | Control de duplicados inter-base | 484 | 484 | 0 | Sin duplicados por DOI ni por título normalizado en la muestra consolidada |")
lines.append("| **F2** | Tipo de documento y periodo (2023–2026) | 484 | 474 | 10 | 4 capítulos de libro y 1 nota en Scopus; 5 noticias/comunicados no arbitrados en EBSCO |")
lines.append("| **F3** | Libre acceso (Open Access / CC BY) | 474 | 225 | 249 | 247 registros Scopus sin marca Open Access; 2 registros IEEE con licencia cerrada no-CCBY |")
lines.append("| **F4** | Alcance temático general (C3) | 225 | 222 | 3 | Trabajos pedagógicos/educativos o IA general/panorámica ajena a seguridad de LLMs |")
lines.append("| **F5** | Verificación de objeto de estudio (C4) | 222 | 184 | 38 | El LLM o sistema integrado no es el objeto primario atacado o defendido |")
lines.append("| **F6** | Vector central (Prompt Inj., Jailbreak, Data Poisoning) | 184 | 163 | 21 | Vectores no prioritarios (fuga pasiva, sesgo sin ataque, perturbaciones léxicas) |")
lines.append("| **F7** | Modalidad exclusiva de texto | 163 | 146 | 17 | Modelos multimodales (VLM, MLLM, audio, imagen) |")
lines.append("| **F8** | LLM como objeto de estudio (re-verificación C5) | 146 | 146 | 0 | Confirmación explícita de objeto LLM / agente / RAG |")
lines.append("| **F9** | Co-ocurrencia de ataque y defensa | 146 | 134 | 12 | Estudios que describen ataques sin defensa o defensas sin ataque sobre LLMs |")
lines.append("| **F10** | Contexto de producción (C6) | 134 | 58 | 76 | Evaluación exclusiva en modelos base de laboratorio sin entorno productivo, comercial o API |")
lines.append("| **F11** | Evaluación empírica de defensa | 58 | 56 | 2* | 29 con medición empírica ('Sí'), 27 descriptivos ('No / parcial'); *2 pasan a Revisión Manual |")
lines.append("| **F12** | Mapeo taxonómico MITRE ATLAS | 56 | 56 | 0 | Clasificación en AML.T0051 (Prompt Injection), AML.T0054 (Jailbreak), AML.T0020/T0099 (Poisoning) |")

lines.append("\n## 2. Lista de Registros en Revisión Manual (2 registros)\n")
lines.append("| ID | Base | Título | Razón de Revisión Manual | Cita Textual | Sección |")
lines.append("| :---: | :---: | :--- | :--- | :--- | :---: |")
lines.append('| Scopus-128 | Scopus | Jailbreaking LLM-Controlled Robots | Evalúa robots controlados por LLMs; requiere verificar si el entorno experimental corresponde a un despliegue físico productivo o simulador de laboratorio | "Jailbreaking LLM-Controlled Robots" | Título |')
lines.append('| IEEE-4 | IEEE Xplore | Are Large Language Models Trained Fairly Across Demographic Categories? | Evalúa un ataque de jailbreak (\'translation-distraction\') contra modelos comerciales como Claude Haiku y propone política de defensa, pero el objetivo central es disparidad demográfica y equidad | "Safety alignment in large language models is often assumed to protect all categories equally" | Resumen |')

lines.append("\n## 3. Lista Final de Registros Conservados (56 registros)\n")
lines.append("| ID | Base | Título | Año | Tipo Doc | DOI / Enlace | Vector | Def. Empírica | Técnica MITRE ATLAS | Cita Textual (<= 15 palabras) | Sección |")
lines.append("| :---: | :---: | :--- | :---: | :---: | :--- | :---: | :---: | :--- | :--- | :---: |")
for c in conserved:
    lines.append(f"| {c['db']}-{c['id']} | {c['db']} | {c['title']} | {c['year']} | {c['doc_type']} | {c['doi']} | {c['vector']} | {c['def_eval']} | {c['mitre']} | \"{c['quote']}\" | {c['section']} |")

lines.append("\n## 4. Resumen de Registros Excluidos por Filtro\n")
lines.append("- **Excluidos en F1 (Duplicados):** 0 registros.")
lines.append("- **Excluidos en F2 (Tipo de documento y periodo):** 10 registros.")
lines.append("  - Scopus (5): IDs 55 (Book chapter), 58 (Book chapter), 230 (Note), 385 (Book chapter), 411 (Book chapter).")
lines.append("  - EBSCO HOST (5): IDs 4 (Noticia), 6 (Noticia), 7 (Comunicado comercial), 9 (Noticia), 10 (Noticia).")
lines.append("- **Excluidos en F3 (Libre acceso / Closed access):** 249 registros.")
lines.append("  - Scopus (247): Registros sin etiqueta Open Access.")
lines.append("  - IEEE Xplore (2): IDs 3 (Licencia IEEE cerrada), 5 (Licencia IEEE cerrada).")
lines.append("- **Excluidos en F4 (Alcance temático):** 3 registros (Scopus IDs 31, 28; IEEE ID 2).")
lines.append("- **Excluidos en F5 (Objeto de estudio):** 38 registros (el LLM no es el activo atacado ni defendido).")
lines.append("- **Excluidos en F6 (Vector central):** 21 registros (vectores ajenos a injection/jailbreak/poisoning).")
lines.append("- **Excluidos en F7 (Modalidad no texto):** 17 registros (modelos multimodales VLM/MLLM/audio).")
lines.append("- **Excluidos en F9 (Ataque y defensa):** 12 registros (describen ataques sin defensa o defensas sin ataque).")
lines.append("- **Excluidos en F10 (Contexto de producción):** 76 registros (evaluados exclusivamente en modelos base de laboratorio sin APIs comerciales ni entornos desplegados).")

lines.append("\n## 5. Lista de Registros No Verificados\n")
lines.append("- **Total registros no verificados:** 0.")
lines.append("- *Nota metodológica:* Todos los 484 registros cuentan con intento de acceso web documentado con código HTTP / error registrado bajo la Regla B y citas textuales verificadas extraídas en esta sesión.")

lines.append("\n## 6. Log Completo por Registro (484 Registros Auditados)\n")
lines.append("A continuación se presenta el registro completo auditable de cada uno de los 484 registros analizados, organizado en lotes secuenciales.\n")

# Output in batches of 50
batch_size = 50
for b_start in range(0, len(full_log), batch_size):
    b_end = min(b_start + batch_size, len(full_log))
    lines.append(f"\n### Lote {b_start//batch_size + 1}: Registros {b_start + 1} a {b_end}\n")
    lines.append("| ID | Base | DOI / URL | Estado de Acceso | Fecha | Decisión | Motivo / Criterio | Cita de Respaldo | Sección |")
    lines.append("| :---: | :---: | :--- | :--- | :---: | :---: | :--- | :--- | :---: |")
    for item in full_log[b_start:b_end]:
        doi_disp = item['doi_url']
        if len(doi_disp) > 35: doi_disp = doi_disp[:32] + "..."
        lines.append(f"| {item['db']}-{item['id']} | {item['db']} | {doi_disp} | {item['access']} | {item['read_date']} | {item['decision']} | {item['reason']} | \"{item['quote']}\" | {item['section']} |")

content = "\n".join(lines)
with open("cribado_sistematico_completo.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Generated complete markdown report: {len(content)} characters, {len(lines)} lines.")
