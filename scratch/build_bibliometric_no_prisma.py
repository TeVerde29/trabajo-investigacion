# -*- coding: utf-8 -*-
"""
Script to generate the definitive 'ANÁLISIS BIBLIOMÉTRICO.docx' strictly aligned
with the two reference models in Ejemplos:
  1. Articulo_Bibliometrico_BigData_VOSviewer.docx
  2. Analisis_Bibliometrico_Madurez_Gobernanza_TI_VOSviewer.docx

CRITICAL COMPLIANCE:
- ZERO PRISMA: No PRISMA flowchart, no PRISMA-ScR references, no SLR terminology.
- 5-stage bibliometric methodology: Rivera-Arroyo et al. (2021) & Olivares-Fong et al. (2026) [Paper 40-4865].
- Figures:
  * Figura 1: Mapa bibliométrico de red de co-ocurrencia y clústeres temáticos en VOSviewer.
  * Figura 2: Visualización global por años de la evolución temática en VOSviewer (escala 2023–2026).
  * Figura 3: Mapa de densidad térmica de palabras clave en VOSviewer.
  * Figura 4: Número de publicaciones por año entre 2023 y 2026 (N = 3,273).
  * Figura 5: Número de artículos publicados por país (Distribución geográfica).
  * Figura 6: Prevalencia multi-etiqueta de tácticas y mitigaciones bajo taxonomía MITRE ATLAS v5.1.0.
- Tables:
  * Tabla 1: Ejes temáticos, tipos de documento, idioma y volumen de publicaciones por periodo (2023–2026).
  * Tabla 2: Palabras clave de autor más frecuentes, cobertura por base de datos y países líderes por periodo.
  * Tabla 3: Revistas y fuentes principales y autores más productivos por periodo (2023–2026).
  * Tabla 4: Síntesis comparativa de los estudios clave seleccionados sobre vulnerabilidades y defensas algorítmicas en LLMs.
- Format: BigData 4-section layout (1 col -> 2 col -> 1 col -> 2 col), Arial, #1F4E78 headings, #E9EDF4 table headers.
"""

import os
import sys
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

WORKSPACE_DIR = r"c:\Users\hikih\Documents\Repositorios\trabajo-investigacion"
EVIDENCIAS_DIR = os.path.join(WORKSPACE_DIR, "Evidencias")
OUTPUT_DOCX = os.path.join(WORKSPACE_DIR, "ANÁLISIS BIBLIOMÉTRICO.docx")

# Figures paths
FIG1_PATH = os.path.join(EVIDENCIAS_DIR, "Figura_1_Mapa_Bibliometrico_Palabras_Clave.png")
FIG2_PATH = os.path.join(EVIDENCIAS_DIR, "Figura_2_Visualizacion_Global_Anos.png")
FIG3_PATH = os.path.join(EVIDENCIAS_DIR, "Figura_3_Densidad_Palabras_Clave.png")
FIG4_PATH = os.path.join(EVIDENCIAS_DIR, "Figura_Evolucion_Temporal_Anual.png")
FIG5_PATH = os.path.join(EVIDENCIAS_DIR, "Figura_Distribucion_Geografica.png")
FIG6_PATH = os.path.join(EVIDENCIAS_DIR, "Figura_Taxonomia_MITRE_ATLAS.png")

NAVY_COLOR = RGBColor(0x1F, 0x4E, 0x78)
GRAY_COLOR = RGBColor(0x59, 0x59, 0x59)
BLACK_COLOR = RGBColor(0x00, 0x00, 0x00)

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="A6A6A6", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="none"/>'
        f'<w:left w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def set_section_layout(section, num_cols=1, space_dxa=503):
    sectPr = section._sectPr
    cols = sectPr.xpath("./w:cols")
    if cols:
        col_elem = cols[0]
    else:
        col_elem = parse_xml(r'<w:cols xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>')
        sectPr.append(col_elem)
    if num_cols == 1 or num_cols is None:
        col_elem.set(qn("w:num"), "1")
        if qn("w:space") in col_elem.attrib:
            del col_elem.attrib[qn("w:space")]
    else:
        col_elem.set(qn("w:num"), str(num_cols))
        col_elem.set(qn("w:space"), str(space_dxa))

def add_page_number(run):
    fldChar1 = parse_xml(r'<w:fldChar %s w:fldCharType="begin"/>' % nsdecls('w'))
    instrText = parse_xml(r'<w:instrText %s xml:space="preserve"> PAGE </w:instrText>' % nsdecls('w'))
    fldChar2 = parse_xml(r'<w:fldChar %s w:fldCharType="separate"/>' % nsdecls('w'))
    fldChar3 = parse_xml(r'<w:fldChar %s w:fldCharType="end"/>' % nsdecls('w'))
    run._r.append(fldChar1)
    run._r.append(instrText)
    run._r.append(fldChar2)
    run._r.append(fldChar3)

def generate_paper():
    doc = Document()
    
    # Page setup
    for s in doc.sections:
        s.top_margin = Inches(0.9)
        s.bottom_margin = Inches(0.9)
        s.left_margin = Inches(0.85)
        s.right_margin = Inches(0.85)
        s.page_width = Inches(8.5)
        s.page_height = Inches(11.0)
        footer = s.footer
        f_p = footer.paragraphs[0]
        f_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        f_run = f_p.add_run()
        f_run.font.name = "Arial"
        f_run.font.size = Pt(9)
        f_run.font.color.rgb = GRAY_COLOR
        add_page_number(f_run)

    # Base style
    normal = doc.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(10)
    normal.font.color.rgb = BLACK_COLOR
    normal.paragraph_format.line_spacing = 1.15
    normal.paragraph_format.space_after = Pt(4)
    normal.paragraph_format.space_before = Pt(0)

    def add_p(text, bold=False, italic=False, font_size=10, color=BLACK_COLOR, align=WD_ALIGN_PARAGRAPH.JUSTIFY, space_after=4, space_before=0):
        p = doc.add_paragraph()
        p.alignment = align
        p.paragraph_format.space_after = Pt(space_after)
        p.paragraph_format.space_before = Pt(space_before)
        p.paragraph_format.line_spacing = 1.15
        run = p.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.name = "Arial"
        run.font.size = Pt(font_size)
        run.font.color.rgb = color
        return p

    def add_heading_bigdata(title_text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(title_text)
        run.bold = True
        run.font.name = "Arial"
        run.font.size = Pt(11)
        run.font.color.rgb = NAVY_COLOR
        return p

    def add_substage_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.bold = True
        run.italic = True
        run.font.name = "Arial"
        run.font.size = Pt(10)
        run.font.color.rgb = NAVY_COLOR
        return p

    def add_figure_block(img_path, caption, source_text, width_in=6.2):
        if os.path.exists(img_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(3)
            p_img.paragraph_format.keep_with_next = True
            run_img = p_img.add_run()
            run_img.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(2)
        p_cap.paragraph_format.keep_with_next = True
        r_cap = p_cap.add_run(caption)
        r_cap.bold = True
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(9.5)
        r_cap.font.color.rgb = NAVY_COLOR

        p_src = doc.add_paragraph()
        p_src.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_src.paragraph_format.space_before = Pt(0)
        p_src.paragraph_format.space_after = Pt(6)
        r_src = p_src.add_run(source_text)
        r_src.italic = True
        r_src.font.name = "Arial"
        r_src.font.size = Pt(8.5)
        r_src.font.color.rgb = GRAY_COLOR

    def add_table_header(caption, source_text):
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_cap.paragraph_format.space_before = Pt(8)
        p_cap.paragraph_format.space_after = Pt(2)
        p_cap.paragraph_format.keep_with_next = True
        r_cap = p_cap.add_run(caption)
        r_cap.bold = True
        r_cap.font.name = "Arial"
        r_cap.font.size = Pt(9.5)
        r_cap.font.color.rgb = NAVY_COLOR

        p_src = doc.add_paragraph()
        p_src.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p_src.paragraph_format.space_before = Pt(0)
        p_src.paragraph_format.space_after = Pt(4)
        p_src.paragraph_format.keep_with_next = True
        r_src = p_src.add_run(source_text)
        r_src.italic = True
        r_src.font.name = "Arial"
        r_src.font.size = Pt(8.5)
        r_src.font.color.rgb = GRAY_COLOR

    # =========================================================================
    # SECTION 1: COVER PAGE (1 COLUMN)
    # =========================================================================
    sec1 = doc.sections[0]
    set_section_layout(sec1, num_cols=1)

    # Paragraph 0: Fechas
    add_p(
        "Fecha de presentación: 15 de noviembre, 2026     "
        "Fecha de Aceptación: xx de xx, 202x     "
        "Fecha de publicación: xx, 202x",
        bold=False, font_size=8.5, color=GRAY_COLOR, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=12
    )

    # Paragraph 1: Título en español
    add_p(
        "ANÁLISIS BIBLIOMÉTRICO DE VULNERABILIDADES, TÉCNICAS DE EVASIÓN Y DEFENSAS ALGORÍTMICAS "
        "EN LA SEGURIDAD DE MODELOS DE LENGUAJE GRANDE (LLMS) UTILIZANDO VOSVIEWER",
        bold=True, font_size=13, color=NAVY_COLOR, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=6
    )

    # Paragraph 2: Título en inglés
    add_p(
        "BIBLIOMETRIC ANALYSIS OF VULNERABILITIES, EVASION TECHNIQUES, AND ALGORITHMIC DEFENSES "
        "IN LARGE LANGUAGE MODEL (LLM) SECURITY USING VOSVIEWER",
        bold=True, font_size=11, color=NAVY_COLOR, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10
    )

    # Paragraph 3: Autor y afiliación
    add_p(
        "Pedro Giovanni Ricra Figueroa 1*\n"
        "E-mail: pedro.ricra.figueroa@gmail.com\n"
        "1 Escuela Profesional de Ingeniería de Sistemas, Facultad de Ingeniería de Sistemas e Informática, "
        "Universidad Nacional de Ucayali, Pucallpa, Perú.\n"
        "* Autor para correspondencia",
        bold=False, font_size=9.5, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=8
    )

    # Paragraph 4: Cita sugerida
    add_p(
        "Cita sugerida (APA, séptima edición):\n"
        "Ricra-Figueroa, P. G. (2026). Análisis bibliométrico de vulnerabilidades, técnicas de evasión y defensas algorítmicas "
        "en la seguridad de modelos de lenguaje grande (LLMs) utilizando VOSviewer. Revista Conrado, 22(108), (1-15).",
        italic=False, font_size=8.5, color=GRAY_COLOR, align=WD_ALIGN_PARAGRAPH.LEFT, space_after=12
    )

    # =========================================================================
    # SECTION 2: RESUMEN, ABSTRACT, INTRODUCCIÓN, MATERIALES Y MÉTODOS (2 COLS)
    # =========================================================================
    sec2 = doc.add_section(docx.enum.section.WD_SECTION.CONTINUOUS)
    set_section_layout(sec2, num_cols=2, space_dxa=503)

    add_heading_bigdata("RESUMEN:")
    add_p(
        "En la ingeniería de software y la ciberseguridad contemporánea, el aseguramiento de los modelos de lenguaje grande (LLMs) "
        "frente a vectores adversariales se ha consolidado como un desafío crítico debido a la ausencia de separación física entre instrucciones "
        "del sistema y datos no confiables. El objetivo de esta revisión bibliométrica fue analizar la evolución de la producción científica, "
        "identificar las principales tendencias de investigación y caracterizar las técnicas de evasión y defensas algorítmicas en la seguridad "
        "de LLMs entre 2023 y 2026. La metodología siguió un análisis bibliométrico descriptivo concluyente estructurado en cinco etapas "
        "(Rivera-Arroyo et al., 2021; Olivares-Fong et al., 2026): 1) formulación de objetivos; 2) identificación de datos y bases de datos; "
        "3) selección de datos; 4) confirmación de datos; y 5) análisis de datos mediante software especializado. Los registros se obtuvieron "
        "de cinco bases científicas internacionales (Scopus, ScienceDirect, IEEE Xplore, EBSCOhost e IOPscience; 4,037 registros brutos) y, "
        "tras excluir 63 registros pre-indexados a 2027, 16 en idiomas distintos a inglés/español y depurar 685 duplicados (669 inter-base y 16 intra-Scopus), "
        "se consolidó un corpus único de 3,273 publicaciones procesadas en Python y VOSviewer. Los resultados muestran un crecimiento exponencial, "
        "pasando de 412 artículos en 2023 a 1,328 en 2025 y un incremento acumulado de 449 publicaciones hasta noviembre de 2026, con predominio "
        "de prompt injection, jailbreaking, adversarial machine learning, retrieval-augmented generation (RAG) y guardrails en los mapas de co-ocurrencia, "
        "evolución temporal y densidad térmica. Asimismo, la categorización bajo MITRE ATLAS v5.1.0 y la síntesis comparativa de diez estudios clave "
        "evidencian que las defensas perimetrales y de descontextualización logran exactitudes del 93.9% al 96.8% frente a jailbreaks, pero imponen "
        "sobrecargas de latencia (de <5 ms a 1.1 s en APIs y hasta 3.19 s en SLM local sobre CPU) y riesgos de sobre-bloqueo (over-refusal), ofreciendo una guía integral para el despliegue seguro en producción.",
        space_after=4
    )
    add_p(
        "Palabras clave:\n"
        "Modelos de Lenguaje Grande (LLMs), Análisis Bibliométrico, VOSviewer, Inyección de Prompts, Jailbreak, Guardrails, Ciberseguridad, MITRE ATLAS.",
        bold=False, font_size=9, color=NAVY_COLOR, space_after=8
    )

    add_heading_bigdata("ABSTRACT:")
    add_p(
        "In contemporary software engineering and cybersecurity, securing large language models (LLMs) against adversarial vectors has become "
        "a critical challenge due to the lack of architectural separation between control instructions and untrusted data tokens. The objective "
        "of this bibliometric review was to analyze the evolution of scientific output, identify key research trends, and characterize evasion techniques "
        "and algorithmic defenses in LLM security between 2023 and 2026. The methodology followed a descriptive bibliometric study structured into "
        "five phases (Rivera-Arroyo et al., 2021; Olivares-Fong et al., 2026): 1) objective formulation; 2) data and database identification; "
        "3) data selection; 4) data confirmation; and 5) data analysis using specialized software. Bibliographic records were retrieved from five "
        "international databases (Scopus, ScienceDirect, IEEE Xplore, EBSCOhost, and IOPscience; 4,037 raw records). After removing 63 records pre-indexed "
        "for 2027, 16 non-English/non-Spanish records, and 685 duplicates (669 inter-database and 16 intra-Scopus duplicates), a final corpus of 3,273 "
        "unique publications was processed using Python and VOSviewer. Results demonstrate exponential growth, expanding from 412 papers in 2023 to 1,328 "
        "in 2025, alongside 449 cumulative publications observed up to November 2026. The co-occurrence, overlay, and density maps highlight the dominance "
        "of prompt injection, jailbreaking, adversarial machine learning, retrieval-augmented generation (RAG), and guardrails. Furthermore, categorization "
        "under MITRE ATLAS v5.1.0 and a comparative synthesis of ten key studies reveal that perimeter guardrails and decontextualized safeguards achieve "
        "93.9%–96.8% mitigation accuracy, albeit introducing latency overheads (<5 ms to 1.1 s in APIs, and up to 3.19 s in local CPU SLMs) and over-refusal trade-offs, providing "
        "a comprehensive roadmap for secure production deployment.",
        space_after=4
    )
    add_p(
        "Keywords:\n"
        "Large Language Models (LLMs), Bibliometric Analysis, VOSviewer, Prompt Injection, Jailbreak, Guardrails, Cybersecurity, MITRE ATLAS.",
        bold=False, font_size=9, color=NAVY_COLOR, space_after=10
    )

    add_heading_bigdata("INTRODUCCIÓN")
    add_p(
        "La integración acelerada de modelos de lenguaje grande (LLMs) fundacionales y de código abierto en arquitecturas corporativas "
        "ha transformado radicalmente el desarrollo de aplicaciones inteligentes en sectores críticos como finanzas, medicina, comercio y gobierno "
        "(Schulhoff et al., 2023). No obstante, a diferencia de los sistemas de cómputo tradicionales basados en la arquitectura "
        "Von Neumann —donde las instrucciones de control del procesador y los flujos de datos residen en canales de memoria diferenciados—, "
        "un modelo fundacional procesa las directivas del desarrollador (system prompt), los datos contextuales recuperados y la entrada "
        "del usuario dentro de un único espacio latente indiferenciado de tokens (Ait Hsine & Arabo, 2026).",
        space_after=3
    )
    add_p(
        "Esta indistinción estructural entre datos e instrucciones habilita un amplio espectro de vectores de ataque adversarial tipificados "
        "en la taxonomía MITRE ATLAS v5.1.0 (Adversarial Threat Landscape for Artificial-Intelligence Systems) y en la guía NIST AI 600-1 (NIST, 2024; "
        "MITRE, 2025). Entre las amenazas predominantes destacan: (a) la inyección directa e indirecta de prompts en sistemas de recuperación "
        "aumentada (RAG) y motores de búsqueda en línea (Pfrommer et al., 2024; Yang et al., 2025); (b) el jailbreaking optimizado mediante "
        "gradientes y fuzzer automatizados capaces de vulnerar la alineación ética del modelo (Zou et al., 2023; Shao et al., 2026); (c) la escalada "
        "de privilegios en agentes autónomos mediante manipulación de contexto para forzar la ejecución indebida de herramientas y APIs externas "
        "(AML.TA0012 / AML.T0053); y (d) el envenenamiento de bases de conocimiento corporativas y desalineación tras ajustes finos (Wang et al., 2024).",
        space_after=3
    )
    add_p(
        "Para contener estos riesgos en despliegues productivos, la industria ha implementado mecanismos de defensa algorítmica que abarcan "
        "guardrails perimetrales probabilísticos (Llama Guard, NeMo Guardrails, Azure AI Content Safety), arquitecturas de salvaguarda "
        "descontextualizada (D-SHIELD) y marcos de detección activa mediante honeypots (Yuan et al., 2024; Santilli et al., 2026; Vargas Yáñez & Tobón, 2026). "
        "Sin embargo, la adopción real de estas defensas enfrenta un trilema operacional severo: alcanzar altas tasas de bloqueo adversarial "
        "sin incurrir en sobrecargas de latencia inaceptables para el usuario final (las cuales oscilan entre 5 ms en proxies locales hasta más de 1.1 s "
        "en inspectores basados en modelos secundarios) y manteniendo un estricto control sobre las tasas de sobre-bloqueo o falso positivo "
        "(over-refusal) que degradan la experiencia del usuario (Majewski et al., 2026).",
        space_after=3
    )
    add_p(
        "El objetivo del presente estudio es analizar, por medio de una evaluación bibliométrica de las publicaciones científicas indexadas entre "
        "2023 y 2026 en cinco bases de datos científicas internacionales (Scopus, ScienceDirect, IEEE Xplore, EBSCOhost e IOPscience), "
        "cómo ha evolucionado la literatura sobre vulnerabilidades, técnicas de evasión y defensas algorítmicas en la seguridad de LLMs, "
        "identificando mediante VOSviewer las redes de co-ocurrencia temática, la evolución cronológica de términos, los focos de densidad térmica, "
        "las fuentes y países líderes, y las características empíricas de los modelos y mitigaciones reportados.",
        space_after=8
    )

    add_heading_bigdata("MATERIALES Y MÉTODOS")
    add_p(
        "La presente investigación es un estudio bibliométrico de tipo descriptivo concluyente (Malhotra, 2004; López-Fraile et al., 2023), "
        "enfocado en analizar el desarrollo de la literatura científica relacionada con la seguridad, vulnerabilidades, técnicas de evasión "
        "y defensas algorítmicas en modelos de lenguaje grande (LLMs) en el periodo 2023–2026.",
        space_after=3
    )
    add_p(
        "Para definir la metodología se tomó como referencia a Rivera-Arroyo et al. (2021) y Olivares-Fong et al. (2026), quienes estructuran "
        "el análisis bibliométrico en cinco etapas: (1) formulación de objetivos; (2) identificación de datos y bases de datos relevantes; "
        "(3) selección de datos; (4) confirmación de datos; y (5) análisis de datos con apoyo de herramientas informáticas. "
        "A continuación, se describe cómo se aplicó cada etapa.",
        space_after=4
    )

    add_substage_title("Descripción de cada Etapa")
    
    add_p(
        "Formulación de objetivos. Se definió como objetivo central identificar las tendencias, la estructura temática, las redes de co-ocurrencia "
        "de palabras clave y los mecanismos de defensa algorítmica en la literatura científica sobre la seguridad de LLMs durante la ventana 2023–2026, "
        "categorizando las amenazas y mitigaciones bajo la taxonomía MITRE ATLAS y contrastando la evidencia empírica de eficacia defensiva, "
        "latencia operativa y sobre-bloqueo en entornos orientados a producción.",
        space_after=3
    )

    add_p(
        "Identificación de datos y bases de datos relevantes. Se seleccionaron cinco bases de datos científicas internacionales de amplia cobertura "
        "e indiscutible impacto en ingeniería de software, inteligencia artificial y ciberseguridad: Scopus, ScienceDirect, IEEE Xplore, EBSCOhost "
        "e IOPscience (verificando complementariamente SciELO, donde no se recuperaron registros que cumplieran los descriptores booleanos).",
        space_after=3
    )

    add_p(
        "Selección de datos. Se utilizaron operadores booleanos para recuperar publicaciones científicas arbitradas que abordaran de manera explícita "
        "la intersección entre modelos fundacionales de lenguaje, vectores de ataque adversarial y técnicas de mitigación algorítmica. "
        "La ecuación de búsqueda general construida y ejecutada en Scopus, ScienceDirect, IEEE Xplore y EBSCOhost fue la siguiente:",
        space_after=2
    )

    add_p(
        "(\"large language model*\" OR LLM OR LLMs OR \"foundation model*\") AND (\"prompt injection\" OR jailbreak* OR \"data poisoning\" "
        "OR \"adversarial machine learning\" OR \"AI red teaming\") AND (\"LLM security\" OR \"language model security\" OR vulnerab* OR "
        "attack* OR evasion OR defense OR defence OR mitigation OR detection OR guardrails)",
        italic=True, font_size=9, color=NAVY_COLOR, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=3
    )

    add_p(
        "En IOPscience, debido a limitaciones sintácticas de longitud del motor de consulta, se aplicó la cadena adaptada equivalente: "
        "(\"Large Language Model\" OR \"LLM\") AND (\"Prompt Injection\" OR \"Jailbreak\" OR \"Adversarial Attack\" OR \"Guardrail\" OR \"Defense\").",
        space_after=3
    )

    add_p(
        "Confirmación de datos. La recolección global arrojó inicialmente 4,037 registros brutos (Scopus: 2,272; ScienceDirect: 796; "
        "IEEE Xplore: 666; EBSCOhost: 243; IOPscience: 60). Mediante procesamiento auditable en Python se depuraron 63 registros de Scopus "
        "pre-indexados formalmente al año 2027 (código EX-05) y 16 registros de EBSCOhost publicados en idiomas distintos a inglés o español (EX-06), "
        "quedando 3,958 registros elegibles. Posteriormente, se efectuó la deduplicación exacta por DOI y título normalizado, identificándose "
        "685 duplicados (669 duplicados inter-base y exactamente 16 duplicados internos intra-base en la exportación de Scopus, reduciendo su cuenta "
        "individual de 2,209 a 2,193 registros únicos). De esta manera se consolidó un corpus bibliométrico definitivo de 3,273 publicaciones "
        "científicas únicas dentro del periodo 2023–2026 (equivalentes a 3,942 apariciones de base no exclusivas). Asimismo, del subconjunto "
        "de estudios enfocados en mitigación algorítmica y arquitecturas de guardrails, se seleccionaron diez (10) artículos ancla a texto completo "
        "en acceso abierto para sustentar el contraste cuantitativo de métricas de seguridad y costo operacional.",
        space_after=3
    )

    add_p(
        "Análisis de datos. Para el mapeo bibliométrico se utilizó el software VOSviewer versión 1.6.20 (van Eck & Waltman, 2010), aplicando el análisis "
        "de co-ocurrencia de palabras clave (co-occurrence of keywords) con método de conteo completo (full counting), normalización por fuerza de "
        "asociación (association strength) y un umbral mínimo de ocurrencia de 5 repeticiones (T ≥ 5), depurado con un tesauro de normalización ortográfica. "
        "Se generaron tres mapas fundamentales: red de co-ocurrencia por clústeres (Network Visualization), visualización cronológica superpuesta "
        "(Overlay Visualization, escala 2023–2026) y mapa de densidad térmica (Density Visualization). De manera complementaria, se utilizó Python 3.12 "
        "y Microsoft Excel para el cálculo estadístico de frecuencias anuales, tipología documental, distribución geográfica por países de afiliación, "
        "categorización bajo MITRE ATLAS v5.1.0 y síntesis comparativa de los estudios clave.",
        space_after=8
    )

    # =========================================================================
    # SECTION 3: RESULTADOS (1 COLUMN - FULL WIDTH FOR FIGURES AND TABLES)
    # =========================================================================
    sec3 = doc.add_section(docx.enum.section.WD_SECTION.CONTINUOUS)
    set_section_layout(sec3, num_cols=1)

    add_heading_bigdata("RESULTADOS")
    add_p(
        "En la base bibliográfica depurada se consolidaron 3,273 publicaciones científicas únicas comprendidas entre enero de 2023 y noviembre "
        "de 2026 (2,284 artículos de revista arbitrada [69.78%], 871 actas de conferencias internacionales indexadas [26.61%], 103 revisiones "
        "sistemáticas [3.15%] y 15 artículos de acceso anticipado con revisión por pares [0.46%]), distribuidas en las cinco fuentes consultadas. "
        "A partir de los metadatos analizados en VOSviewer v1.6.20 con umbral T ≥ 5, se conformó una red conectada de palabras clave de alta densidad. "
        "La Figura 1 presenta el mapa de red de co-ocurrencia, donde se estructuran cuatro clústeres temáticos principales identificados por colores, "
        "gravitando en torno al nodo nuclear large language models.",
        space_after=4
    )

    # FIGURA 1: VOSviewer Co-occurrence Network
    add_figure_block(
        FIG1_PATH,
        "Figura 1: Mapa bibliométrico de red de co-ocurrencia y clústeres temáticos en VOSviewer.",
        "Fuente: Base de datos consolidada de Scopus, ScienceDirect, IEEE Xplore, EBSCOhost e IOPscience procesada en VOSviewer v1.6.20.",
        width_in=6.2
    )

    add_p(
        "Para el clúster rojo (Clúster 1: Prompt Injection y Ataques Adversariales), los conceptos dominantes son prompt injection, "
        "adversarial attacks, indirect prompt injection, data poisoning, privacy y backdoor attacks. Este clúster representa el núcleo ofensivo "
        "de la literatura, enfocado en documentar cómo entradas maliciosas pueden manipular el contexto de los modelos para eludir filtros perimetrales, "
        "extraer información privada de entrenamiento o forzar fugas del prompt de sistema en interfaces conversacionales.",
        space_after=3
    )
    add_p(
        "En el clúster verde (Clúster 2: Jailbreaking, Alineación y Guardrails), destacan jailbreak, jailbreaking, ai alignment, "
        "guardrails, reinforcement learning from human feedback (rlhf), safety y large language models. Este agrupamiento articula los esfuerzos "
        "metodológicos y algorítmicos dirigidos a reforzar las barreras internas de los modelos frente a técnicas de persuasión semántica, "
        "prompts hipotéticos estructurados y sufijos optimizados que buscan desactivar las políticas de seguridad preentrenadas.",
        space_after=3
    )
    add_p(
        "Por su parte, el clúster azul (Clúster 3: Arquitecturas RAG y Envenenamiento de Contexto), reporta retrieval-augmented generation (rag), "
        "knowledge base, context injection, information retrieval y data integrity. Este grupo de términos refleja la preocupación creciente "
        "por la seguridad de las arquitecturas que conectan modelos fundacionales con bases de datos documentales vectorizadas, donde la inyección "
        "indirecta de prompts a través de documentos de terceros puede comprometer la fiabilidad de las respuestas corporativas.",
        space_after=3
    )
    add_p(
        "Finalmente, en el clúster amarillo y cian (Clúster 4: AI Red Teaming y Seguridad en Agentes), se agrupan ai red teaming, "
        "vulnerability assessment, autonomous agents, tool invocation y threat modeling. Estos nodos evidencian la transición metodológica hacia "
        "la auditoría automatizada y el análisis de amenazas en agentes basados en LLMs capaces de ejecutar herramientas y APIs externas.",
        space_after=6
    )

    # FIGURA 2: VOSviewer Overlay Chronological Evolution
    add_p(
        "En la Figura 2 se presenta la visualización cronológica superpuesta (Overlay Visualization) calibrada en la escala 2023–2026. "
        "Se constata una transición nítida en el foco de la comunidad científica: las investigaciones tempranas (en tonos violeta y azul oscuro, "
        "correspondientes a 2023 y principios de 2024) se concentraron en caracterizaciones iniciales de caja negra, prompt injection directo básico "
        "y ataques heurísticos. Hacia la etapa intermedia (tonos verde-azulado y verde medio, 2024–2025) emergen la optimización formal de ataques "
        "adversariales (algoritmos GCG y AutoDAN), el análisis de toxicidad y los primeros guardrails clasificadores. Por último, las investigaciones "
        "más recientes (en tonos verde lima y amarillo brillante, 2025–2026) se concentran en arquitecturas agénticas seguras, protección contra "
        "inyección indirecta en RAG en tiempo real, mitigación descontextualizada de jailbreaks y gobernanza bajo marcos regulatorios internacionales:",
        space_after=4
    )

    add_figure_block(
        FIG2_PATH,
        "Figura 2: Visualización global por años de la evolución temática en VOSviewer (escala 2023–2026).",
        "Fuente: Base de datos consolidada procesada en VOSviewer v1.6.20 (gradiente temporal de azul a amarillo).",
        width_in=6.2
    )

    # FIGURA 3: VOSviewer Density Visualization
    add_p(
        "La Figura 3 ilustra el mapa de densidad térmica de palabras clave en VOSviewer. El foco incandescente de mayor densidad relativa y "
        "co-ocurrencia bibliométrica se concentra en la tríada large language models, prompt injection y jailbreak, rodeado inmediatamente "
        "por una corona de alta densidad integrada por adversarial machine learning, security, guardrails y retrieval-augmented generation. "
        "En zonas de menor densidad relativa (tonos cian y verde claro) se sitúan conceptos especializados y de frontera operativa como "
        "honey-pot, differential privacy, tool use, runtime alignment y privilege escalation, indicando líneas de desarrollo emergente con alto potencial:",
        space_after=4
    )

    add_figure_block(
        FIG3_PATH,
        "Figura 3: Mapa de densidad térmica de palabras clave en VOSviewer.",
        "Fuente: Base de datos consolidada procesada en VOSviewer v1.6.20.",
        width_in=6.2
    )

    # FIGURA 4: Evolución Temporal Anual
    add_p(
        "Por otra parte, se procesaron las series estadísticas de los 3,273 registros únicos consolidados en Python para examinar la evolución "
        "anual de publicaciones (Figura 4). La producción científica en seguridad de LLMs inició con 412 publicaciones en 2023 (12.59% del total), "
        "experimentó un salto de +163.1% en 2024 alcanzando 1,084 documentos (33.12%), y registró su máxima concentración en 2025 con 1,328 artículos "
        "(40.57%). En el periodo comprendido entre enero y noviembre de 2026 se contabilizan 449 publicaciones indexadas (13.72%), evidenciando un "
        "volumen acumulado sostenido que consolida a la seguridad ofensiva y defensiva de modelos generativos como un dominio científico maduro y prioritario:",
        space_after=4
    )

    add_figure_block(
        FIG4_PATH,
        "Figura 4: Número de publicaciones por año entre 2023 y 2026 (N = 3,273).",
        "Fuente: Elaboración propia a partir del corpus único consolidado (2023: 412; 2024: 1,084; 2025: 1,328; 2026 acumulado a noviembre: 449).",
        width_in=5.8
    )

    # FIGURA 5: Distribución Geográfica por País
    add_p(
        "Respecto a la distribución geográfica por país de afiliación institucional (Figura 5), Estados Unidos y China encabezan ampliamente la producción "
        "científica global, concentrando más del 58% de las investigaciones publicadas. Les siguen en productividad el Reino Unido, Alemania, India, "
        "Canadá, Australia, Singapur y Corea del Sur. En contraste, la región de América Latina presenta una participación aún emergente (menor al 2.5% "
        "del total), con aportes procedentes de Brasil, Chile, México y Perú, orientados principalmente a la aplicación de modelos en auditoría, educación "
        "y detección de vulnerabilidades:",
        space_after=4
    )

    add_figure_block(
        FIG5_PATH,
        "Figura 5: Número de artículos publicados por país (Distribución geográfica).",
        "Fuente: Elaboración propia con base en las filiaciones institucionales normalizadas del corpus analizado.",
        width_in=5.8
    )

    # FIGURA 6: MITRE ATLAS Taxonomy
    add_p(
        "Con el propósito de evaluar la orientación técnica y la aplicabilidad de la literatura en entornos de producción, la Figura 6 presenta "
        "la distribución porcentual multi-etiqueta de amenazas y defensas bajo la taxonomía oficial MITRE ATLAS v5.1.0 en la muestra de evaluación en producción. "
        "Entre las técnicas adversariales destacan ampliamente AML.T0051 (LLM Prompt Injection, 81.5%), AML.T0054 (LLM Jailbreak, 63.8%), AML.TA0005 "
        "(Defense Evasion, 71.3%), AML.T0053 (AI Agent Tool Invocation, 27.5%) y AML.TA0012 (Privilege Escalation, 24.8%). A nivel de mecanismos defensivos, "
        "predominan AML.M0020 (Generative AI Guardrails, 49.3%), AML.M0015 (Adversarial Input Detection, 42.0%), AML.M0008/M0022 (Generative AI Model "
        "Alignment, 35.8%), AML.M0030 (Restrict AI Agent Tool Invocation on Untrusted Data, 22.0%) y AML.M0007 (Sanitize Training Data, 19.3%):",
        space_after=4
    )

    add_figure_block(
        FIG6_PATH,
        "Figura 6: Prevalencia multi-etiqueta de tácticas y mitigaciones bajo taxonomía MITRE ATLAS v5.1.0.",
        "Fuente: Elaboración propia con base en el estrato de estudios de seguridad de LLMs evaluados bajo MITRE ATLAS v5.1.0.",
        width_in=5.8
    )

    # -------------------------------------------------------------------------
    # TABLA 1: Ejes temáticos, tipo de doc, idioma y volumen por periodo
    # -------------------------------------------------------------------------
    add_table_header(
        "Tabla 1: Ejes temáticos, tipos de documento, idioma y volumen de publicaciones por periodo (2023–2026) (N = 3,273).",
        "Fuente: Elaboración propia con base en los registros únicos consolidados de Scopus, ScienceDirect, IEEE Xplore, EBSCOhost e IOPscience."
    )

    t1_headers = ["Periodo / Año", "Ejes Temáticos Principales", "Tipos de Documento", "Idioma", "No. Artículos (n / %)"]
    t1_rows = [
        [
            "2023",
            "1. Modelos fundacionales y ciberseguridad inicial\n2. Inyección directa de prompts en interfaces web\n3. Detección heurística y filtrado preliminar",
            "Artículo de Revista (268; 65.0%)\nActas de Conferencia (129; 31.3%)\nRevisiones (15; 3.6%)",
            "Inglés (406; 98.5%)\nEspañol (6; 1.5%)",
            "412 (12.59%)"
        ],
        [
            "2024",
            "1. Jailbreaking estructurado y optimización adversarial (GCG)\n2. Vulnerabilidades en RAG y envenenamiento de datos\n3. Guardrails perimetrales clasificadores (Llama Guard)",
            "Artículo de Revista (742; 68.5%)\nActas de Conferencia (306; 28.2%)\nRevisiones (36; 3.3%)",
            "Inglés (1,071; 98.8%)\nEspañol (13; 1.2%)",
            "1,084 (33.12%)"
        ],
        [
            "2025",
            "1. Inyección indirecta en sistemas productivos y clínicos\n2. Honeypots activos y arquitecturas de triangulación\n3. Salvaguardas descontextualizadas (D-SHIELD)",
            "Artículo de Revista (948; 71.4%)\nActas de Conferencia (338; 25.4%)\nRevisiones (42; 3.2%)",
            "Inglés (1,314; 98.9%)\nEspañol (14; 1.1%)",
            "1,328 (40.57%)"
        ],
        [
            "2026*",
            "1. Agentes autónomos, escalada de privilegios y APIs\n2. Proxies locales SLM en CPU y regulación EU AI Act\n3. Detección multi-capa en tiempo de ejecución",
            "Artículo de Revista (326; 72.6%)\nActas de Conferencia (98; 21.8%)\nEarly Access / Rev. (25; 5.6%)",
            "Inglés (444; 98.9%)\nEspañol (5; 1.1%)",
            "449 (13.72%)"
        ],
        [
            "Total (2023–2026)",
            "Seguridad integral ofensiva y defensiva de LLMs orientada a producción",
            "Revistas (2,284; 69.8%)\nActas (871; 26.6%)\nRevisiones / EA (118; 3.6%)",
            "Inglés (3,235; 98.8%)\nEspañol (38; 1.2%)",
            "3,273 (100.0%)"
        ]
    ]

    t1 = doc.add_table(rows=len(t1_rows) + 1, cols=len(t1_headers))
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t1)

    # Style Header
    hdr_cells = t1.rows[0].cells
    for c_idx, h_text in enumerate(t1_headers):
        hdr_cells[c_idx].text = h_text
        set_cell_background(hdr_cells[c_idx], "E9EDF4")
        set_cell_margins(hdr_cells[c_idx], top=80, bottom=80, left=100, right=100)
        p = hdr_cells[c_idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.bold = True
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = NAVY_COLOR

    # Add header repeat & cantSplit
    trPr = t1.rows[0]._tr.get_or_add_trPr()
    trPr.append(parse_xml(r'<w:tblHeader xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
    trPr.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

    for r_idx, row_data in enumerate(t1_rows):
        row_cells = t1.rows[r_idx + 1].cells
        r_trPr = t1.rows[r_idx + 1]._tr.get_or_add_trPr()
        r_trPr.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].text = cell_value
            set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=80, right=80)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 3, 4] else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(8.5)
                if r_idx == len(t1_rows) - 1:
                    r.bold = True

    # Note
    p_note = doc.add_paragraph()
    p_note.paragraph_format.space_before = Pt(2)
    p_note.paragraph_format.space_after = Pt(8)
    r_n = p_note.add_run("*Nota: Los datos de 2026 corresponden a las publicaciones acumuladas e indexadas hasta noviembre de 2026. La suma de apariciones por base en el corpus único es de 3,942: Scopus (2,193 tras deduplicar 16 registros internos), ScienceDirect (796), IEEE Xplore (666), EBSCOhost (227) e IOPscience (60).")
    r_n.font.size = Pt(8)
    r_n.italic = True
    r_n.font.color.rgb = GRAY_COLOR

    # -------------------------------------------------------------------------
    # TABLA 2: Palabras clave, cobertura y países por periodo
    # -------------------------------------------------------------------------
    add_table_header(
        "Tabla 2: Palabras clave de autor más frecuentes, cobertura por base de datos y países líderes por periodo.",
        "Fuente: Elaboración propia a partir de las etiquetas de metadatos KW, SO, PU y AF de los registros únicos consolidados."
    )

    t2_headers = ["Periodo / Año", "Palabras Clave Más Frecuentes (KW)", "Países Líderes / Referentes", "Cobertura por Base de Datos y Fuentes"]
    t2_rows = [
        [
            "2023",
            "1. large language models (184)\n2. prompt injection (82)\n3. natural language processing (76)\n4. adversarial attacks (58)\n5. chatgpt (52)",
            "1. Estados Unidos\n2. China\n3. Reino Unido\n4. Alemania\n5. India",
            "Scopus: 251 | ScienceDirect: 84 | IEEE: 61 | EBSCO: 12 | IOP: 4\nRevistas científicas (65.0%) y talleres especializados ACM/IEEE."
        ],
        [
            "2024",
            "1. large language models (492)\n2. jailbreak / jailbreaking (246)\n3. prompt injection (218)\n4. adversarial machine learning (174)\n5. guardrails (112)",
            "1. Estados Unidos\n2. China\n3. Reino Unido\n4. Alemania\n5. Canadá",
            "Scopus: 724 | ScienceDirect: 262 | IEEE: 221 | EBSCO: 78 | IOP: 20\nRevistas de alto impacto (IEEE Trans., ACM) y conferencias ACL, EMNLP, NeurIPS."
        ],
        [
            "2025",
            "1. large language models (614)\n2. retrieval-augmented generation (295)\n3. prompt injection (284)\n4. jailbreak (271)\n5. guardrails / safety (198)",
            "1. Estados Unidos\n2. China\n3. Alemania\n4. Singapur\n5. Australia",
            "Scopus: 902 | ScienceDirect: 318 | IEEE: 268 | EBSCO: 98 | IOP: 26\nConsolidación editorial en ciberseguridad aplicada (Computers & Security, IEEE Access)."
        ],
        [
            "2026*",
            "1. large language models (211)\n2. autonomous agents / tool use (118)\n3. prompt injection (98)\n4. jailbreak mitigation (92)\n5. runtime alignment (64)",
            "1. China\n2. Estados Unidos\n3. Reino Unido\n4. Corea del Sur\n5. Países Bajos",
            "Scopus: 316 | ScienceDirect: 132 | IEEE: 116 | EBSCO: 39 | IOP: 10\nRevistas en acceso abierto, series Procedia Computer Science e IEEE Early Access."
        ]
    ]

    t2 = doc.add_table(rows=len(t2_rows) + 1, cols=len(t2_headers))
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t2)

    hdr_cells2 = t2.rows[0].cells
    for c_idx, h_text in enumerate(t2_headers):
        hdr_cells2[c_idx].text = h_text
        set_cell_background(hdr_cells2[c_idx], "E9EDF4")
        set_cell_margins(hdr_cells2[c_idx], top=80, bottom=80, left=100, right=100)
        p = hdr_cells2[c_idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.bold = True
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = NAVY_COLOR

    trPr2 = t2.rows[0]._tr.get_or_add_trPr()
    trPr2.append(parse_xml(r'<w:tblHeader xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
    trPr2.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

    for r_idx, row_data in enumerate(t2_rows):
        row_cells = t2.rows[r_idx + 1].cells
        r_trPr = t2.rows[r_idx + 1]._tr.get_or_add_trPr()
        r_trPr.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].text = cell_value
            set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=80, right=80)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(8.5)

    p_note2 = doc.add_paragraph()
    p_note2.paragraph_format.space_before = Pt(2)
    p_note2.paragraph_format.space_after = Pt(8)
    r_n2 = p_note2.add_run("*Nota: El total de apariciones por base excede el corpus único (3,273) debido a indexaciones simultáneas no excluyentes entre Scopus, IEEE y ScienceDirect.")
    r_n2.font.size = Pt(8)
    r_n2.italic = True
    r_n2.font.color.rgb = GRAY_COLOR

    # -------------------------------------------------------------------------
    # TABLA 3: Revistas principales y autores más productivos
    # -------------------------------------------------------------------------
    add_table_header(
        "Tabla 3: Revistas y fuentes principales y autores más productivos por periodo (2023–2026).",
        "Fuente: Elaboración propia a partir de las etiquetas SO / JO y AU de los 3,273 registros únicos consolidados."
    )

    t3_headers = ["Periodo / Año", "Revistas y Fuentes Principales (Top Venues)", "Autores Más Productivos"]
    t3_rows = [
        [
            "2023",
            "1. Advances in Neural Information Processing Systems (NeurIPS)\n2. Meta-Radiology (3)\n3. EMNLP Proceedings (2)\n4. ACM Workshop on AI and Security (AISec) (2)\n5. ACM Moving Target Defense (MTD) (2)",
            "1. Zhu, C. (2)\n2. Ray, Partha Pratim (2)\n3. Lin, Z. (2)\n4. Liu, Zhengliang (2)\n5. Wu, Zihao (2)"
        ],
        [
            "2024",
            "1. Proceedings of the ACL (30)\n2. Proceedings of EMNLP (26)\n3. Advances in Neural Information Processing Systems (NeurIPS) (26)\n4. CEUR Workshop Proceedings (20)\n5. Proceedings of Machine Learning Research (PMLR) (15)",
            "1. Wang, Y. (17)\n2. Liu, Y. (17)\n3. Zhang, Y. (16)\n4. Li, Y. (11)\n5. Zhang, X. (11)"
        ],
        [
            "2025",
            "1. Proceedings of the ACL (60)\n2. Proceedings of EMNLP (38)\n3. International Conference on Learning Representations (ICLR) (36)\n4. Advances in Neural Information Processing Systems (NeurIPS) (35)\n5. Computers, Materials and Continua (29)",
            "1. Wang, Y. (28)\n2. Zhang, Y. (27)\n3. Wang, Z. (26)\n4. Li, Y. (24)\n5. Zhang, J. (21)"
        ],
        [
            "2026*",
            "1. Proceedings of the ACL (85)\n2. Procedia Computer Science (58)\n3. Lecture Notes in Computer Science (LNCS) (50)\n4. Computers, Materials and Continua (43)\n5. Proceedings of the AAAI Conference on Artificial Intelligence (33)",
            "1. Wang, Y. (22)\n2. Liu, Y. (16)\n3. Li, Y. (16)\n4. Li, H. (15)\n5. Wang, H. (15)"
        ]
    ]

    t3 = doc.add_table(rows=len(t3_rows) + 1, cols=len(t3_headers))
    t3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t3)

    hdr_cells3 = t3.rows[0].cells
    for c_idx, h_text in enumerate(t3_headers):
        hdr_cells3[c_idx].text = h_text
        set_cell_background(hdr_cells3[c_idx], "E9EDF4")
        set_cell_margins(hdr_cells3[c_idx], top=80, bottom=80, left=100, right=100)
        p = hdr_cells3[c_idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.bold = True
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = NAVY_COLOR

    trPr3 = t3.rows[0]._tr.get_or_add_trPr()
    trPr3.append(parse_xml(r'<w:tblHeader xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
    trPr3.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

    for r_idx, row_data in enumerate(t3_rows):
        row_cells = t3.rows[r_idx + 1].cells
        r_trPr = t3.rows[r_idx + 1]._tr.get_or_add_trPr()
        r_trPr.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].text = cell_value
            set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=80, right=80)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx == 0 else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(8.5)

    p_note3 = doc.add_paragraph()
    p_note3.paragraph_format.space_before = Pt(2)
    p_note3.paragraph_format.space_after = Pt(8)
    r_n3 = p_note3.add_run("*Nota: El liderazgo de conferencias internacionales indexadas en Scopus (ACL, EMNLP, NeurIPS, ICLR) refleja la rápida dinámica de divulgación en IA, mientras que Procedia Computer Science e IEEE Access canalizan el volumen principal en revistas.")
    r_n3.font.size = Pt(8)
    r_n3.italic = True
    r_n3.font.color.rgb = GRAY_COLOR

    # -------------------------------------------------------------------------
    # TABLA 4: Síntesis comparativa de estudios clave
    # -------------------------------------------------------------------------
    add_p(
        "Con el objetivo de profundizar en el desempeño operativo de los mecanismos de mitigación reportados en la literatura, "
        "la Tabla 4 presenta la síntesis comparativa de los diez (10) estudios clave seleccionados a texto completo, detallando sus "
        "entornos de evaluación, amenazas evaluadas bajo MITRE ATLAS, salvaguardas algorítmicas, métricas cuantitativas verificadas "
        "y costos operativos en términos de latencia y tasa de sobre-bloqueo (over-refusal):",
        space_after=4
    )

    add_table_header(
        "Tabla 4: Síntesis comparativa de los estudios clave seleccionados sobre vulnerabilidades y defensas algorítmicas en LLMs.",
        "Fuente: Elaboración propia a partir de los artículos a texto completo analizados en el repositorio del proyecto."
    )

    t4_headers = [
        "Estudio (Autor, Año)",
        "Medio y DOI verificado",
        "Entorno de evaluación empírica",
        "Amenaza y método evaluado",
        "Métricas cuantitativas verificadas",
        "Costo operativo / Latencia / Limitación"
    ]

    t4_rows = [
        [
            "Schulhoff et al. (2023)",
            "EMNLP 2023, pp. 4945–4977\n10.18653/v1/2023.emnlp-main.302",
            "Competencia pública global abierta en línea (HackAPrompt)",
            "Inyección humana masiva sobre GPT-3, ChatGPT y FlanT5-XXL",
            ">600k prompts (560,161 Playground [7.7% éxito]; 41,596 envíos [83.2%]); 9/10 niveles vulnerados; 29 técnicas.",
            "Demuestra ineficacia de defensas basadas únicamente en instrucciones de sistema."
        ],
        [
            "Yuan et al. (2024)",
            "ICML 2024, PMLR 235, pp. 57953–57965",
            "Benchmark experimental controlado (ToxicChat, AdvBench, OpenAI)",
            "RigorLLM (datos por energía Langevin + sufijo minimax + fusión kNN/LLM)",
            "OpenAI Mod. (AUPRC 0.841; F1 0.791); ToxicChat (AUPRC 0.869; F1 0.749); HDR 0.99–1.00 bajo GCG/AutoDAN (+33% vs LlamaGuard/NeMo).",
            "Latencia promedio de 1.02 s por prompt (GPU A6000 Ada); exige cómputo local dedicado."
        ],
        [
            "Wang et al. (2024)",
            "NeurIPS 37, pp. 5210–5243\n(arXiv:2402.14968)",
            "Servicio LMaaS simulado con fine-tuning asistido",
            "BackdoorAlign (11 ejemplos seguros + prefijo secreto de 150 tokens)",
            "Reduce ASR en Llama-2-7B-Chat de 94.91% a 3.64% (2.91% LoRA; daño 4.68→1.22) y en GPT-3.5 de 75.64% a 14.91% (ARC 51.88%, MMLU 45.21%, MT-Bench 6.25).",
            "Requiere control del proveedor sobre el pipeline de ajuste fino y custodia del prefijo."
        ],
        [
            "Pfrommer et al. (2024)",
            "EMNLP 2024, pp. 9523–9552\n10.18653/v1/2024.emnlp-main.534",
            "Búsqueda web RAG y motor comercial en línea (Perplexity Sonar)",
            "RAGDOLL (búsqueda en árbol adversarial sobre HTML recuperado)",
            "Mejora de posición media: GPT-3.5 (+3.38 / 57.53% brecha), GPT-4 (+5.00 / 82.94%), Llama 3 70B (+6.02 / 95.74%); Perplexity Online +2.89 puestos (54.23%).",
            "La mayor capacidad de razonamiento aumenta la susceptibilidad a instrucciones web ocultas."
        ],
        [
            "Yang et al. (2025)",
            "Nature Communications, 16(1), 9011\n10.1038/s41467-025-64062-1",
            "Notas clínicas hospitalarias reales MIMIC-III (soporte clínico)",
            "Inyección de prompt (PE) y fine-tuning envenenado (FT) clínico",
            "Recomendación de vacuna en GPT-4o cayó de 88.06% a 6.47% (PE) y 20.40% (FT); alteración de pruebas alcanzó 95.5%–100% en Llama-3.3 70B; parafraseo redujo ASR -33.37% (PE) y -42.65% (FT).",
            "MedQA (78.9–81.5%), MedMCQA (69.9–72.7%) y PubMedQA (61.2–64.3%) permanecen sin degradación aparente."
        ],
        [
            "Ait Hsine & Arabo (2026)",
            "Electronics, 15(16), 3554\n10.3390/electronics15163554",
            "Middleware local corporativo en CPU previo a APIs externas",
            "Frontera híbrida (regex + Narasimha-0.6B) con enrutamiento selectivo",
            "En 120 prompts: 95.83% exactitud; 100% recall (0/80 FN); 95% prompts sensibles retenidos en local (5.0% fuga residual); 58.3% menos llamadas externas.",
            "SLM local en CPU ~3,193.7 ms (regex 0.1 ms); latencia media global 3,673.3 ms (-15.5% vs 4,344.7 ms); FPR 12.5%."
        ],
        [
            "Majewski et al. (2026)",
            "IEEE Access, 14, pp. 70863–70879\n10.1109/ACCESS.2026.3690365",
            "Benchmark comparativo multimodelo y APIs comerciales (AWS, Azure)",
            "Evaluación de 6 guardrails en 13 datasets y 3 LLMs (Mistral, Llama 3, Claude)",
            "Exactitud media: AWS Guardrails 96.8% (prec. 98.9%, rec. 97.8%), NeMo 93.9%, Azure 89.2%, Baseline 82.2%, Llama Guard 73.5%.",
            "AWS añade 1.0–1.1 s por llamada API (11.8%–21.5% del total); Llama Guard sufre sobre-bloqueo en neutrales (49.3%–53.4%)."
        ],
        [
            "Santilli et al. (2026)",
            "Information and Software Technology, 195, 108130\n10.1016/j.infsof.2026.108130",
            "Pipeline de integración como plugin/filtro para EU AI Act",
            "D-SHIELD (verificación descontextualizada de respuesta sin historial)",
            "En 165 salidas: 85.5% exactitud, 96.1% recall nocivo; en 145 jailbreaks: ASR = 2.76% (141/145 bloqueados vs 13.8%–78.6% pares); D-SHIELDlight ASR = 1.38%.",
            "Recall en salidas conformes de 67.7% por sesgo conservador que penaliza parcialmente la utilidad."
        ],
        [
            "Shao et al. (2026)",
            "IEEE TIFS, 21, pp. 2727–2741\n10.1109/TIFS.2026.3666893",
            "Evaluación automatizada en 20 apps y 50 servicios LLM en línea",
            "PROMPTFUZZ (pre-búsqueda de semillas + fuzzing con retroalimentación)",
            "TensorTrust: bestASR 64.90% (extracción) y 75.33% (secuestro), 7.º de >4,000; 65% ASR en 20 apps y 92% en 50 apps en línea; 13/15 evaluadores CV vulnerados.",
            "Evade detectores comerciales en 70%–90% tras ajuste fino; evidencia caducidad de listas negras fijas."
        ],
        [
            "Vargas Yáñez & Tobón (2026)",
            "Int. J. Inf. Secur., 25(5), 158\n10.1007/s10207-026-01307-0",
            "Despliegue operativo real continuo en VPS durante 20 días",
            "HIVE-AI (5 fachadas API + cascada 8 etapas + caza protegida en 5 capas)",
            "20 días (4-vCPU/4-GB): 16,683 ataques desde 1,229 IPs (50 países); detección 94.2% (FPR 4.6%); triangulación reduce evasión de 54.8% a 9.3% (κ = 0.74).",
            "Latencia síncrona p99 de 4.7 ms (<5 ms); diseñado como sensor perimetral/honeypot más que proxy directo de usuarios."
        ]
    ]

    t4 = doc.add_table(rows=len(t4_rows) + 1, cols=len(t4_headers))
    t4.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(t4)

    hdr_cells4 = t4.rows[0].cells
    for c_idx, h_text in enumerate(t4_headers):
        hdr_cells4[c_idx].text = h_text
        set_cell_background(hdr_cells4[c_idx], "E9EDF4")
        set_cell_margins(hdr_cells4[c_idx], top=80, bottom=80, left=100, right=100)
        p = hdr_cells4[c_idx].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.bold = True
            r.font.name = "Arial"
            r.font.size = Pt(9)
            r.font.color.rgb = NAVY_COLOR

    trPr4 = t4.rows[0]._tr.get_or_add_trPr()
    trPr4.append(parse_xml(r'<w:tblHeader xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
    trPr4.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))

    for r_idx, row_data in enumerate(t4_rows):
        row_cells = t4.rows[r_idx + 1].cells
        r_trPr = t4.rows[r_idx + 1]._tr.get_or_add_trPr()
        r_trPr.append(parse_xml(r'<w:cantSplit xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"/>'))
        for c_idx, cell_value in enumerate(row_data):
            row_cells[c_idx].text = cell_value
            set_cell_margins(row_cells[c_idx], top=60, bottom=60, left=80, right=80)
            p = row_cells[c_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = "Arial"
                r.font.size = Pt(8)

    p_note4 = doc.add_paragraph()
    p_note4.paragraph_format.space_before = Pt(2)
    p_note4.paragraph_format.space_after = Pt(10)
    r_n4 = p_note4.add_run("*Nota: ASR = Attack Success Rate. Todos los identificadores DOI, volúmenes editoriales y métricas fueron verificados directamente contra los textos completos en PDF alojados en el repositorio del proyecto.")
    r_n4.font.size = Pt(8)
    r_n4.italic = True
    r_n4.font.color.rgb = GRAY_COLOR

    # =========================================================================
    # SECTION 4: DISCUSIÓN, CONCLUSIONES, REFERENCIAS (2 COLUMNS)
    # =========================================================================
    sec4 = doc.add_section(docx.enum.section.WD_SECTION.CONTINUOUS)
    set_section_layout(sec4, num_cols=2, space_dxa=503)

    add_heading_bigdata("DISCUSIÓN")
    add_p(
        "Los resultados de la presente investigación confirman que la seguridad en modelos de lenguaje grande ha dejado de ser un tema "
        "periférico para convertirse en una disciplina central dentro de la ingeniería de software y la ciberseguridad. La aceleración observada "
        "en la producción científica —que escala desde 412 artículos en 2023 hasta 1,328 en 2025 y mantiene un dinamismo sostenido con 449 publicaciones "
        "hasta noviembre de 2026 (Figura 4 y Tabla 1)— responde a la adopción masiva de LLMs en entornos empresariales y la consiguiente necesidad "
        "de blindar estas arquitecturas frente a ataques adversariales (Schulhoff et al., 2023).",
        space_after=3
    )
    add_p(
        "El análisis de los clústeres temáticos en VOSviewer (Figura 1) y los focos de densidad (Figura 3) demuestra que la literatura gravita en torno "
        "a una tensión fundamental: la inyección de prompts y el jailbreaking constituyen las amenazas primarias (Clústeres 1 y 2), mientras que "
        "los guardrails y las salvaguardas arquitectónicas representan la principal respuesta de la comunidad (Yuan et al., 2024; Majewski et al., 2026). "
        "La emergencia de clústeres especializados en RAG y agentes autónomos (Clústeres 3 y 4) refleja que los riesgos se han trasladado desde la simple "
        "conversación directa hacia la manipulación indirecta de bases documentales y la invocación indebida de herramientas externas con privilegios elevados "
        "(Pfrommer et al., 2024; Yang et al., 2025).",
        space_after=3
    )
    add_p(
        "Un hallazgo central derivado de la visualización cronológica superpuesta (Figura 2) y la dinámica de palabras clave (Tabla 2) es la evolución "
        "cualitativa de las amenazas y defensas: entre 2023 y 2024 predominaron los ataques manuales de caja negra y los filtros léxicos perimetrales, "
        "mientras que en 2025 y 2026 el foco se ha desplazado hacia ataques automatizados multironda (fuzzing genético y optimización por gradientes) "
        "y defensas resilientes descontextualizadas (Santilli et al., 2026; Shao et al., 2026).",
        space_after=3
    )
    add_p(
        "Asimismo, la síntesis comparativa de los diez estudios clave (Tabla 4) expone un trilema operacional crítico para los ingenieros de software "
        "que despliegan LLMs en producción. Por un lado, los guardrails perimetrales comerciales (AWS Guardrails, NeMo) logran "
        "excelentes niveles de exactitud (93.9%–96.8%), pero añaden latencias de 1.0 a 1.1 s por llamada en APIs comerciales, mientras que Llama Guard "
        "exhibe tasas de sobre-bloqueo (over-refusal) de 49.3%–53.4% sobre textos neutrales (Majewski et al., 2026). Por otro lado, aproximaciones "
        "arquitectónicas innovadoras como D-SHIELD (Santilli et al., 2026) demuestran que descontextualizar la evaluación de la salida respecto al prompt "
        "del atacante reduce el ASR a 2.76% (1.38% en D-SHIELDlight), y sensores perimetrales como HIVE-AI (Vargas Yáñez & Tobón, 2026) operan con latencia "
        "p99 de 4.7 ms en producción.",
        space_after=3
    )
    add_p(
        "En cuanto a las limitaciones del estudio, debe señalarse que, si bien se integraron cinco bases de datos científicas de primer nivel (3,273 registros únicos), "
        "la rápida evolución del área hace que muchos desarrollos técnicos se divulguen inicialmente en repositorios de preprints antes de su consolidación "
        "en revistas arbitradas. Futuras investigaciones deberán incorporar telemetría continua de ataques en producción y evaluar el impacto de las normativas "
        "emergentes, como el Reglamento Europeo de Inteligencia Artificial (EU AI Act), en los requerimientos de auditoría y robustez algorítmica.",
        space_after=8
    )

    add_heading_bigdata("CONCLUSIONES")
    add_p(
        "La literatura científica sobre seguridad en modelos de lenguaje grande presenta un crecimiento acelerado y sostenido entre 2023 y 2026, "
        "consolidando un corpus depurado de 3,273 publicaciones científicas únicas indexadas en cinco bases internacionales, con liderazgo de Scopus, "
        "ScienceDirect e IEEE Xplore, y una concentración geográfica prominente en Estados Unidos y China.",
        space_after=3
    )
    add_p(
        "A partir del mapeo en VOSviewer v1.6.20 (red de co-ocurrencia, evolución cronológica y densidad térmica), se concluye que la disciplina se articula "
        "en torno a cuatro clústeres cardinales: 1) inyección de prompts directa e indirecta; 2) jailbreaking y alineación mediante guardrails; 3) seguridad "
        "en arquitecturas RAG y bases documentales; y 4) auditoría por AI Red Teaming y contención en agentes autónomos, transitando desde ataques heurísticos "
        "básicos hacia amenazas automatizadas complejas y defensas adaptativas en tiempo de ejecución.",
        space_after=3
    )
    add_p(
        "La categorización taxonómica bajo MITRE ATLAS v5.1.0 ratifica que las técnicas de inyección de prompts (AML.T0051; 81.5%), evasión de defensas "
        "(AML.TA0005; 71.3%) y jailbreaking (AML.T0054; 63.8%) representan las amenazas de mayor frecuencia operativa, frente a las cuales los guardrails "
        "de IA generativa (AML.M0020; 49.3%) y la detección de entradas adversariales (AML.M0015; 42.0%) constituyen las mitigaciones predominantes.",
        space_after=3
    )
    add_p(
        "Finalmente, la síntesis empírica comparativa de los estudios clave confirma que el despliegue seguro en producción exige balancear la exactitud "
        "defensiva frente a la latencia operativa y el sobre-bloqueo (over-refusal). Arquitecturas emergentes basadas en honeypots activos y desacoplamiento "
        "descontextualizado de prompts demuestran que es factible mitigar la inyección adversarial a niveles inferiores al 5% con costos computacionales "
        "admisibles, configurando la base para las futuras salvaguardas de la inteligencia artificial corporativa.",
        space_after=8
    )

    add_heading_bigdata("REFERENCIAS BIBLIOGRÁFICAS")

    references = [
        "Ait Hsine, A., & Arabo, A. (2026). A privacy-preserving middleware architecture for detecting prompt injection and sensitive data exposure in large-language-model interactions. Electronics, 15(16), 3554. https://doi.org/10.3390/electronics15163554",
        "López-Fraile, L. A., Jiménez-García, E., & Alonso Guisande, M. Á. (2023). Análisis de citación, co-citación y co-palabras de los medios de comunicación pública y ecosistema digital. Revista Latina de Comunicación Social, (82), 1–24. https://doi.org/10.4185/rlcs-2024-1979",
        "Majewski, P., Marczak, K., Dubicka, N., Podolak, J., Sochaj, B., Siłka, J., & Kowal, M. (2026). Comprehensive analysis of LLM guardrails approaches preventing harmful content and jailbreak attacks. IEEE Access, 14, 70863–70879. https://doi.org/10.1109/ACCESS.2026.3690365",
        "Malhotra, N. (2004). Investigación de mercados: Un enfoque aplicado (4.ª ed.). Pearson Educación.",
        "MITRE. (2025). Adversarial Threat Landscape for Artificial-Intelligence Systems (MITRE ATLAS™ v5.1.0). MITRE Corporation. https://atlas.mitre.org",
        "National Institute of Standards and Technology. (2024). Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1). U.S. Department of Commerce. https://doi.org/10.6028/NIST.AI.600-1",
        "Olivares-Fong, L. del C., Jacobo-Galicia, G., Gutiérrez-Moreno, J. M., & Meguro-Yuno, K. R. (2026). Análisis bibliométrico del burnout en docentes de nivel superior utilizando VOSviewer. Revista Conrado, 22(108), e4865.",
        "Pfrommer, S., Bai, Y., Gautam, T., & Sojoudi, S. (2024). Ranking manipulation for conversational search engines. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP 2024) (pp. 9523–9552). Association for Computational Linguistics. https://doi.org/10.18653/v1/2024.emnlp-main.534",
        "Rivera-Arroyo, J. K., Araya-Castillo, L., Ganga-Contreras, F., Torres, J. P., & Sánchez-Morales, F. (2021). Análisis bibliométrico de la investigación en calidad de servicio. Interciencia, 46(11), 404–415.",
        "Santilli, T., De Luca, M., Amalfitano, D., Fasolino, A. R., & Pelliccione, P. (2026). A decontextualized LLM-based safeguard technique for automated jailbreak mitigation. Information and Software Technology, 195, 108130. https://doi.org/10.1016/j.infsof.2026.108130",
        "Schulhoff, S., Pinto, J., Khan, A., Bouchard, L.-F., Si, C., Anati, S., Tagliabue, V., Kost, A. L., Carnahan, C., & Boyd-Graber, J. (2023). Ignore this title and HackAPrompt: Exposing systemic vulnerabilities of LLMs through a global scale prompt hacking competition. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP 2023) (pp. 4945–4977). Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.emnlp-main.302",
        "Shao, Y., Yu, J., Miao, H., Gou, G., Li, Z., & Shi, J. (2026). PROMPTFUZZ: Harnessing fuzzing techniques for robust testing of prompt injection in LLMs. IEEE Transactions on Information Forensics and Security, 21, 2727–2741. https://doi.org/10.1109/TIFS.2026.3666893",
        "van Eck, N. J., & Waltman, L. (2010). Software survey: VOSviewer, a computer program for bibliometric mapping. Scientometrics, 84(2), 523–538. https://doi.org/10.1007/s11192-009-0146-3",
        "Vargas Yáñez, S., & Tobón, S. (2026). Hive-AI: A defended multi-service honeypot framework for generative AI APIs. International Journal of Information Security, 25(5), 158. https://doi.org/10.1007/s10207-026-01307-0",
        "Wang, J., Li, J., Li, Y., Qi, X., Hu, J., Li, Y., McDaniel, P., Chen, M., Li, B., & Xiao, C. (2024). Mitigating fine-tuning based jailbreak attack with backdoor enhanced safety alignment. In Advances in Neural Information Processing Systems 37 (NeurIPS 2024) (pp. 5210–5243). Curran Associates.",
        "Yang, Y., Jin, Q., Huang, F., & Lu, Z. (2025). Adversarial prompt and fine-tuning attacks threaten medical large language models. Nature Communications, 16(1), 9011. https://doi.org/10.1038/s41467-025-64062-1",
        "Yuan, Z., Xiong, Z., Zeng, Y., Yu, N., Jia, R., Song, D., & Li, B. (2024). RigorLLM: Resilient guardrails for large language models against undesired content. In Proceedings of the 41st International Conference on Machine Learning (ICML 2024), Proceedings of Machine Learning Research (Vol. 235, pp. 57953–57965). PMLR.",
        "Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J. Z., & Fredrikson, M. (2023). Universal and transferable adversarial attacks on aligned language models. arXiv preprint arXiv:2307.15043. https://doi.org/10.48550/arXiv.2307.15043"
    ]

    for ref in references:
        p_ref = doc.add_paragraph()
        p_ref.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p_ref.paragraph_format.left_indent = Inches(0.2)
        p_ref.paragraph_format.first_line_indent = Inches(-0.2)
        p_ref.paragraph_format.space_after = Pt(2)
        p_ref.paragraph_format.line_spacing = 1.12
        r_ref = p_ref.add_run(ref)
        r_ref.font.name = "Arial"
        r_ref.font.size = Pt(8)

    doc.save(OUTPUT_DOCX)
    print(f"File successfully created: {OUTPUT_DOCX}")
    print(f"File size: {os.path.getsize(OUTPUT_DOCX)} bytes")

if __name__ == "__main__":
    generate_paper()
