import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
import json

# Load base Excel data
wb_orig = openpyxl.load_workbook('Base de Datos.xlsx', data_only=True)
ws_scopus = wb_orig['Scopus']
h_s = [ws_scopus.cell(1, c).value for c in range(1, ws_scopus.max_column + 1)]

# Load conserved records
with open("final_conserved.json", "r", encoding="utf-8") as f:
    conserved = json.load(f)

# Enrich with full Scopus metadata
enriched = []
for item in conserved:
    r = item['id']
    row_vals = {h_s[col-1]: ws_scopus.cell(r, col).value for col in range(1, ws_scopus.max_column + 1)}
    enriched.append({
        'id': r,
        'db': item['db'],
        'title': item['title'],
        'authors': row_vals.get('Authors') or '',
        'year': item['year'],
        'doc_type': item['doc_type'],
        'source': row_vals.get('Source title') or '',
        'doi': item['doi'],
        'link': row_vals.get('Link') or f"https://doi.org/{item['doi']}",
        'oa': row_vals.get('Open Access') or '',
        'vector': item['vector'],
        'def_eval': item['def_eval'],
        'mitre': item['mitre'],
        'quote': item['quote'],
        'section': item['section'],
        'abstract': row_vals.get('Abstract') or ''
    })

# Sort by ID
enriched.sort(key=lambda x: x['id'])

# Create new workbook
wb = openpyxl.Workbook()

# Define Color Palette (Design Ricra - Tea Green)
FOREST_GREEN = "294635"
DEEP_LEAF = "4F7256"
TEA_GREEN = "AFC49A"
LIGHT_MATCHA = "DDE8C8"
BG_LIGHT = "F7F8F1"
SURFACE_SEC = "EEF2E8"
TEXT_MAIN = "1E2A21"
BORDER_COLOR = "D9E2D5"
SUCCESS_COLOR = "E1EFE6"
WARN_COLOR = "FEF5E7"

# Styles
font_title = Font(name="Segoe UI", size=15, bold=True, color="FFFFFF")
font_subtitle = Font(name="Segoe UI", size=10, italic=True, color="FFFFFF")
font_header = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
font_subhdr = Font(name="Segoe UI", size=10, bold=True, color="1E2A21")
font_data = Font(name="Segoe UI", size=9, color="1E2A21")
font_data_bold = Font(name="Segoe UI", size=9, bold=True, color="1E2A21")
font_chip_yes = Font(name="Segoe UI", size=9, bold=True, color="1E6B37")
font_chip_no = Font(name="Segoe UI", size=9, bold=True, color="8A5314")

fill_title = PatternFill(start_color=FOREST_GREEN, end_color=FOREST_GREEN, fill_type="solid")
fill_header = PatternFill(start_color=FOREST_GREEN, end_color=FOREST_GREEN, fill_type="solid")
fill_subhdr = PatternFill(start_color=LIGHT_MATCHA, end_color=LIGHT_MATCHA, fill_type="solid")
fill_zebra = PatternFill(start_color=SURFACE_SEC, end_color=SURFACE_SEC, fill_type="solid")
fill_white = PatternFill(start_color="FFFFFF", end_color="FFFFFF", fill_type="solid")
fill_yes = PatternFill(start_color="E2F0D9", end_color="E2F0D9", fill_type="solid")
fill_no = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

thin_border_side = Side(style="thin", color=BORDER_COLOR)
border_data = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)
border_header = Border(left=thin_border_side, right=thin_border_side, top=thin_border_side, bottom=thin_border_side)

# -------------------------------------------------------------
# SHEET 1: REGISTROS CONSERVADOS (56)
# -------------------------------------------------------------
ws1 = wb.active
ws1.title = "Conservados (56)"
ws1.views.sheetView[0].showGridLines = True

# Title banner
ws1.merge_cells("A1:P1")
ws1["A1"] = "REVISIÓN SISTEMÁTICA DE SEGURIDAD EN LLMs EN PRODUCCIÓN (MITRE ATLAS) — REGISTROS CONSERVADOS (N=56)"
ws1["A1"].font = font_title
ws1["A1"].fill = fill_title
ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[1].height = 36

# Subtitle banner
ws1.merge_cells("A2:P2")
ws1["A2"] = "Cribado Estricto de 484 Registros Originales (Scopus, IEEE Xplore, EBSCO HOST) | Criterios F0 a F12 Superados | Base: Base de Datos.xlsx"
ws1["A2"].font = font_subtitle
ws1["A2"].fill = PatternFill(start_color=DEEP_LEAF, end_color=DEEP_LEAF, fill_type="solid")
ws1["A2"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[2].height = 20

# Column Headers
headers_ws1 = [
    ("ID Original", 11, "center"),
    ("Base de Datos", 14, "center"),
    ("Título de la Publicación", 42, "left"),
    ("Autores", 28, "left"),
    ("Año", 8, "center"),
    ("Tipo Documento", 18, "center"),
    ("Revista / Conferencia", 32, "left"),
    ("DOI", 26, "left"),
    ("Enlace Scopus / URL", 30, "left"),
    ("Modalidad Open Access", 24, "left"),
    ("Vector Central", 22, "center"),
    ("Defensa Empírica", 16, "center"),
    ("Técnica MITRE ATLAS", 32, "left"),
    ("Cita Textual de Respaldo (<= 15 palabras)", 35, "left"),
    ("Sección Cita", 14, "center"),
    ("Resumen (Abstract)", 50, "left")
]

ws1.row_dimensions[3].height = 28
for col_idx, (h_name, width, align) in enumerate(headers_ws1, 1):
    cell = ws1.cell(3, col_idx, h_name)
    cell.font = font_header
    cell.fill = fill_header
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    cell.border = border_header
    col_letter = get_column_letter(col_idx)
    ws1.column_dimensions[col_letter].width = width

# Populate Data
for row_idx, item in enumerate(enriched, 4):
    ws1.row_dimensions[row_idx].height = 45
    fill_row = fill_white if row_idx % 2 == 0 else fill_zebra
    
    row_data = [
        item['id'],
        item['db'],
        item['title'],
        item['authors'],
        item['year'],
        item['doc_type'],
        item['source'],
        item['doi'],
        item['link'],
        item['oa'],
        item['vector'],
        item['def_eval'],
        item['mitre'],
        item['quote'],
        item['section'],
        item['abstract']
    ]
    
    for col_idx, val in enumerate(row_data, 1):
        cell = ws1.cell(row_idx, col_idx, val)
        cell.font = font_data
        cell.border = border_data
        cell.fill = fill_row
        align_type = headers_ws1[col_idx-1][2]
        
        # Specific formatting
        if col_idx in [1, 5]: # ID, Year
            cell.alignment = Alignment(horizontal="center", vertical="center")
            cell.font = font_data_bold
        elif col_idx in [2, 6, 11, 15]: # Base, Doc Type, Vector, Section
            cell.alignment = Alignment(horizontal="center", vertical="center")
        elif col_idx == 12: # Def. Empírica
            cell.alignment = Alignment(horizontal="center", vertical="center")
            if val == "Sí":
                cell.fill = fill_yes
                cell.font = font_chip_yes
            else:
                cell.fill = fill_no
                cell.font = font_chip_no
        elif col_idx in [8, 9]: # DOI, Link
            cell.alignment = Alignment(horizontal="left", vertical="center")
            if val and val.startswith("10."):
                cell.hyperlink = f"https://doi.org/{val}"
                cell.font = Font(name="Segoe UI", size=9, color="1B5E20", underline="single")
            elif val and val.startswith("http"):
                cell.hyperlink = val
                cell.font = Font(name="Segoe UI", size=9, color="1B5E20", underline="single")
        else:
            cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

# Enable AutoFilter
ws1.auto_filter.ref = f"A3:P{len(enriched)+3}"
ws1.freeze_panes = "C4"


# -------------------------------------------------------------
# SHEET 2: RESUMEN Y EMBUDO METODOLÓGICO
# -------------------------------------------------------------
ws2 = wb.create_sheet(title="Embudo y Métricas")
ws2.views.sheetView[0].showGridLines = True

ws2.merge_cells("A1:G1")
ws2["A1"] = "RESUMEN METODOLÓGICO Y EMBUDO DE CRIBADO SISTEMÁTICO (F0 A F12)"
ws2["A1"].font = font_title
ws2["A1"].fill = fill_title
ws2["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[1].height = 34

ws2.merge_cells("A2:G2")
ws2["A2"] = "Eje: Ciberseguridad | Mapeo Taxonómico MITRE ATLAS | Periodo 2023–2026 | Muestra Final N=56"
ws2["A2"].font = font_subtitle
ws2["A2"].fill = PatternFill(start_color=DEEP_LEAF, end_color=DEEP_LEAF, fill_type="solid")
ws2["A2"].alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[2].height = 18

# Funnel Table Header
funnel_headers = [("Filtro", 10), ("Etapa / Criterio Metodológico", 36), ("Entran", 12), ("Salen", 12), ("Excluidos", 12), ("Razón Principal de Exclusión", 45)]
ws2.row_dimensions[4].height = 24
for col_idx, (h, w) in enumerate(funnel_headers, 1):
    c = ws2.cell(4, col_idx, h)
    c.font = font_header
    c.fill = fill_header
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = border_header
    ws2.column_dimensions[get_column_letter(col_idx)].width = w

funnel_data = [
    ("F0", "Base de partida inicial (Scopus 470, IEEE 4, EBSCO 10)", 484, 484, 0, "Verificación de base de datos completa"),
    ("F1", "Control de duplicados inter-base (DOI y Título)", 484, 484, 0, "0 duplicados encontrados en muestra consolidada"),
    ("F2", "Tipo de documento y periodo (2023–2026)", 484, 474, 10, "4 capítulos libro y 1 nota (Scopus); 5 noticias/comunicados (EBSCO)"),
    ("F3", "Libre acceso (Open Access en Scopus / CC BY en IEEE)", 474, 225, 249, "247 Scopus sin Open Access; 2 IEEE con licencia cerrada"),
    ("F4", "Alcance temático general (C3)", 225, 222, 3, "Trabajos pedagógicos/educativos o IA general no-LLM"),
    ("F5", "Verificación de objeto de estudio (C4)", 222, 184, 38, "El LLM no es el activo tecnológico primario atacado o defendido"),
    ("F6", "Vector central (Prompt Inj., Jailbreak, Data Poisoning)", 184, 163, 21, "Vectores no prioritarios (fuga pasiva, sesgo sin ataque, sintaxis)"),
    ("F7", "Modalidad exclusiva de texto (C5)", 163, 146, 17, "Modelos multimodales (VLM, MLLM, audio, imagen)"),
    ("F8", "LLM como objeto de estudio (re-verificación C5)", 146, 146, 0, "Confirmación explícita de activo LLM / agente / RAG"),
    ("F9", "Co-ocurrencia de ataque y defensa (C5)", 146, 134, 12, "Solo ataque sin defensa o defensa sin ataque"),
    ("F10", "Contexto de producción (C6)", 134, 58, 76, "Evaluación en modelos base de laboratorio sin APIs/sistemas desplegados"),
    ("F11", "Evaluación empírica de defensa", 58, 56, 2, "29 evaluados con medición empírica ('Sí'); 2 pasan a Revisión Manual"),
    ("F12", "Mapeo taxonómico MITRE ATLAS", 56, 56, 0, "Mapeo completo en AML.T0051, AML.T0054, AML.T0020, AML.T0099")
]

for r_idx, row in enumerate(funnel_data, 5):
    ws2.row_dimensions[r_idx].height = 20
    fill_row = fill_white if r_idx % 2 == 1 else fill_zebra
    for c_idx, val in enumerate(row, 1):
        c = ws2.cell(r_idx, c_idx, val)
        c.font = font_data
        c.border = border_data
        c.fill = fill_row
        if c_idx in [1, 3, 4, 5]:
            c.alignment = Alignment(horizontal="center", vertical="center")
            if c_idx in [3, 4, 5]:
                c.font = font_data_bold
        else:
            c.alignment = Alignment(horizontal="left", vertical="center")

# Taxonomy Distribution Tables
ws2.cell(19, 1, "DISTRIBUCIÓN POR VECTOR DE ATAQUE").font = Font(name="Segoe UI", size=11, bold=True, color=FOREST_GREEN)
ws2.cell(20, 1, "Vector de Ataque").font = font_subhdr
ws2.cell(20, 1).fill = fill_subhdr
ws2.cell(20, 2, "Registros").font = font_subhdr
ws2.cell(20, 2).fill = fill_subhdr
ws2.cell(20, 3, "Porcentaje").font = font_subhdr
ws2.cell(20, 3).fill = fill_subhdr

vector_counts = [
    ("Jailbreaking", 33, "58.9%"),
    ("Prompt Injection", 19, "33.9%"),
    ("Prompt Injection / Jailbreaking", 1, "1.8%"),
    ("Prompt Injection / Data Poisoning", 2, "3.6%"),
    ("Data Poisoning (PoisonedRAG)", 1, "1.8%")
]
for r_idx, (v_name, cnt, pct) in enumerate(vector_counts, 21):
    ws2.cell(r_idx, 1, v_name).font = font_data
    ws2.cell(r_idx, 2, cnt).font = font_data_bold
    ws2.cell(r_idx, 3, pct).font = font_data
    ws2.cell(r_idx, 2).alignment = Alignment(horizontal="center")
    ws2.cell(r_idx, 3).alignment = Alignment(horizontal="center")

ws2.cell(19, 5, "DISTRIBUCIÓN MITRE ATLAS").font = Font(name="Segoe UI", size=11, bold=True, color=FOREST_GREEN)
ws2.cell(20, 5, "Técnica MITRE ATLAS").font = font_subhdr
ws2.cell(20, 5).fill = fill_subhdr
ws2.cell(20, 6, "N°").font = font_subhdr
ws2.cell(20, 6).fill = fill_subhdr

mitre_counts = [
    ("AML.T0054 (LLM Jailbreak Injection)", 34),
    ("AML.T0051.000 (Prompt Injection: Direct)", 11),
    ("AML.T0051.001 (Prompt Injection: Indirect)", 8),
    ("AML.T0099 (AI Agent / Context Poisoning)", 3)
]
for r_idx, (m_name, cnt) in enumerate(mitre_counts, 21):
    ws2.cell(r_idx, 5, m_name).font = font_data
    ws2.cell(r_idx, 6, cnt).font = font_data_bold
    ws2.cell(r_idx, 6).alignment = Alignment(horizontal="center")


# -------------------------------------------------------------
# SHEET 3: REVISIÓN MANUAL (2 REGISTROS)
# -------------------------------------------------------------
ws3 = wb.create_sheet(title="Revisión Manual (2)")
ws3.views.sheetView[0].showGridLines = True

ws3.merge_cells("A1:G1")
ws3["A1"] = "REGISTROS IDENTIFICADOS PARA REVISIÓN MANUAL (REGLA G)"
ws3["A1"].font = font_title
ws3["A1"].fill = PatternFill(start_color="8A5314", end_color="8A5314", fill_type="solid")
ws3["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws3.row_dimensions[1].height = 34

ws3.merge_cells("A2:G2")
ws3["A2"] = "Registros que requieren juicio experto para su inclusión/exclusión definitiva según entorno experimental o encuadre temático"
ws3["A2"].font = font_subtitle
ws3["A2"].fill = PatternFill(start_color="B47728", end_color="B47728", fill_type="solid")
ws3["A2"].alignment = Alignment(horizontal="center", vertical="center")
ws3.row_dimensions[2].height = 18

manual_headers = [
    ("ID Original", 12),
    ("Base", 14),
    ("Título de la Publicación", 38),
    ("DOI", 28),
    ("Razón Detallada de Revisión Manual", 45),
    ("Cita Textual de Respaldo", 35),
    ("Sección", 14)
]
ws3.row_dimensions[4].height = 24
for col_idx, (h, w) in enumerate(manual_headers, 1):
    c = ws3.cell(4, col_idx, h)
    c.font = font_header
    c.fill = PatternFill(start_color="8A5314", end_color="8A5314", fill_type="solid")
    c.alignment = Alignment(horizontal="center", vertical="center")
    c.border = border_header
    ws3.column_dimensions[get_column_letter(col_idx)].width = w

manual_records = [
    (
        128,
        "Scopus",
        "Jailbreaking LLM-Controlled Robots",
        "10.1109/ICRA55743.2025.11128119",
        "Evalúa vectores de jailbreak en robots gobernados por LLMs; requiere verificar si el entorno corresponde a un despliegue productivo ciberfísico real o a un simulador de laboratorio.",
        "Jailbreaking LLM-Controlled Robots",
        "Título"
    ),
    (
        4,
        "IEEE Xplore",
        "Are Large Language Models Trained Fairly Across Demographic Categories?",
        "10.1109/ACCESS.2026.3746887",
        "Evalúa empíricamente ataques de jailbreak ('translation-distraction') contra modelos comerciales (Claude Haiku) y propone políticas a nivel de prompt de sistema; sin embargo, el encuadre central del estudio es la disparidad demográfica y equidad.",
        "Safety alignment in large language models is often assumed to protect all categories equally",
        "Resumen"
    )
]

for r_idx, r_data in enumerate(manual_records, 5):
    ws3.row_dimensions[r_idx].height = 40
    for c_idx, val in enumerate(r_data, 1):
        c = ws3.cell(r_idx, c_idx, val)
        c.font = font_data
        c.border = border_data
        c.fill = PatternFill(start_color="FEF5E7", end_color="FEF5E7", fill_type="solid")
        if c_idx in [1, 2, 7]:
            c.alignment = Alignment(horizontal="center", vertical="center")
            if c_idx == 1: c.font = font_data_bold
        else:
            c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

# Save workbook
output_path = "Registros_Conservados_56_LLM.xlsx"
wb.save(output_path)
print(f"Workbook saved successfully as {output_path}")
