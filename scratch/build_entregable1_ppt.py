"""Build Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx matching MATRIZ_DELI design."""
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls

BASE_PPTX = Path("MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx")
OUT_PPTX = Path("Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx")

# Theme palette (from Delimitacion LLM Seguridad)
C_DARK = RGBColor(0x0F, 0x1B, 0x1E)
C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
C_TEAL_DARK = RGBColor(0x1B, 0x3A, 0x3A)
C_MIST = RGBColor(0xED, 0xF2, 0xF1)
C_CORAL = RGBColor(0xD6, 0x47, 0x1F)
C_EMERALD = RGBColor(0x17, 0x8A, 0x7B)
C_AMBER = RGBColor(0xF2, 0xB1, 0x34)
C_SLATE = RGBColor(0x5C, 0x6B, 0x73)
C_MINT = RGBColor(0x9A, 0xDB, 0xD0)
C_PEACH = RGBColor(0xF6, 0xB8, 0xA8)

FONT_TITLE = "Cambria"
FONT_BODY = "Calibri"


def clear_existing_slides(prs: Presentation) -> None:
    """Remove all existing slides from the template presentation."""
    sldIdLst = prs.slides._sldIdLst
    for sldId in list(sldIdLst):
        rId = sldId.rId
        prs.part.drop_rel(rId)
        sldIdLst.remove(sldId)


def update_layout_footers(prs: Presentation, footer_text: str) -> None:
    """Update the footer text in layouts OSCURO (2), CLARO (3), CLARO_GRIS (4)."""
    for idx in (2, 3, 4):
        lay = prs.slide_layouts[idx]
        for sh in lay.shapes:
            if sh.has_text_frame and "Matriz de delimitación" in sh.text_frame.text:
                for p in sh.text_frame.paragraphs:
                    for r in p.runs:
                        r.text = footer_text


def add_shadow(shape) -> None:
    """Add a subtle drop shadow matching the reference cards."""
    spPr = shape._element.spPr
    effectLst = parse_xml(
        f'<a:effectLst {nsdecls("a")}>'
        '  <a:outerShdw blurRad="101600" dist="38100" dir="5400000" algn="ctr" rotWithShape="0">'
        '    <a:srgbClr val="0F1B1E"><a:alpha val="14000"/></a:srgbClr>'
        '  </a:outerShdw>'
        '</a:effectLst>'
    )
    spPr.append(effectLst)


def add_card(slide, left, top, width, height, fill_color, radius=0.04, shadow=True):
    """Add a rounded rectangle card with no border and optional subtle shadow."""
    sh = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE,
        Inches(left), Inches(top), Inches(width), Inches(height)
    )
    sh.adjustments[0] = radius
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill_color
    sh.line.fill.background()
    if shadow:
        add_shadow(sh)
    return sh


def add_badge(slide, left, top, size, text, fill_color, text_color=C_WHITE, font_size=14):
    """Add a circular numbered/icon badge."""
    sh = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        Inches(left), Inches(top), Inches(size), Inches(size)
    )
    sh.fill.solid()
    sh.fill.fore_color.rgb = fill_color
    sh.line.fill.background()
    tf = sh.text_frame
    tf.word_wrap = False
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = text
    r.font.name = FONT_BODY
    r.font.size = Pt(font_size)
    r.font.bold = True
    r.font.color.rgb = text_color
    return sh


def add_textbox(slide, left, top, width, height, text="", font_name=FONT_BODY,
                font_size=15, bold=False, italic=False, color=C_DARK,
                align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, line_spacing=1.18):
    """Add a clean textbox with zero internal margins."""
    tb = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    if text:
        p = tf.paragraphs[0]
        p.alignment = align
        p.line_spacing = line_spacing
        r = p.add_run()
        r.text = text
        r.font.name = font_name
        r.font.size = Pt(font_size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
    return tb


def add_rich_paragraph(tf, segments, first=False, space_after=6, line_spacing=1.18, align=PP_ALIGN.LEFT):
    """Add a paragraph with multiple styled runs: [(text, bold, color, size, font_name), ...]."""
    p = tf.paragraphs[0] if first else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    p.line_spacing = line_spacing
    for seg in segments:
        txt = seg[0]
        bold = seg[1] if len(seg) > 1 else False
        color = seg[2] if len(seg) > 2 else C_DARK
        size = seg[3] if len(seg) > 3 else 15
        fname = seg[4] if len(seg) > 4 else FONT_BODY
        italic = seg[5] if len(seg) > 5 else False
        r = p.add_run()
        r.text = txt
        r.font.name = fname
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.italic = italic
        r.font.color.rgb = color
    return p


def set_header(slide, kicker, title, slide_num, dark=False):
    """Set the standard kicker, title placeholder, and slide number on a slide."""
    kicker_color = C_MINT if dark else C_SLATE
    add_textbox(
        slide, 0.60, 0.42, 11.50, 0.40,
        text=kicker.upper(), font_name=FONT_BODY, font_size=12,
        bold=True, color=kicker_color
    )
    title_ph = slide.placeholders[100]
    title_ph.text = title
    for p in title_ph.text_frame.paragraphs:
        for r in p.runs:
            r.font.name = FONT_TITLE
            r.font.size = Pt(34)
            r.font.bold = True
            r.font.color.rgb = C_WHITE if dark else C_DARK
    add_textbox(
        slide, 12.13, 7.03, 0.60, 0.30,
        text=str(slide_num), font_name=FONT_BODY, font_size=11,
        bold=False, color=C_MINT if dark else C_SLATE, align=PP_ALIGN.RIGHT
    )


def build_slide_1(prs: Presentation) -> None:
    """Slide 1: Portada (OSCURO)."""
    slide = prs.slides.add_slide(prs.slide_layouts[2])
    set_header(
        slide,
        "ENTREGABLE 1 · TRABAJO DE INVESTIGACIÓN (ESTDI37) · CIBERSEGURIDAD",
        "Título de la investigación",
        slide_num=1,
        dark=True,
    )

    tb = add_textbox(slide, 0.60, 2.02, 12.13, 2.30)
    add_rich_paragraph(
        tb.text_frame,
        [
            ("Vulnerabilidades adversariales, técnicas de evasión y defensas algorítmicas ", True, C_PEACH, 27, FONT_TITLE),
            ("en ", False, C_WHITE, 27, FONT_TITLE),
            ("Modelos de Lenguaje Grande (LLMs) desplegados en producción: ", True, C_MINT, 27, FONT_TITLE),
            ("una revisión sistemática exploratoria (2023–2026)", True, C_AMBER, 27, FONT_TITLE),
        ],
        first=True, space_after=0, line_spacing=1.18
    )

    cards = [
        ("TEMA", C_PEACH, "Ciberseguridad adversarial y guardrails en LLMs"),
        ("OBJETO", C_MINT, "LLMs fundacionales en producción"),
        ("DISEÑO", C_AMBER, "Revisión sistemática exploratoria (PRISMA-ScR)"),
        ("PERIODO", C_WHITE, "2023–2026 · Semestre 2026-II"),
    ]
    for i, (label, lcolor, body) in enumerate(cards):
        x = 0.60 + i * 3.08
        add_card(slide, x, 4.60, 2.88, 1.45, C_TEAL_DARK, radius=0.08, shadow=False)
        add_textbox(slide, x + 0.25, 4.78, 2.38, 0.28, label, FONT_BODY, 11, True, color=lcolor)
        add_textbox(slide, x + 0.25, 5.10, 2.38, 0.85, body, FONT_BODY, 15, True, color=C_WHITE)

    add_textbox(
        slide, 0.60, 6.40, 12.13, 0.35,
        "Pedro Giovanni Ricra Figueroa – EPIS · Universidad Nacional de Ucayali   |   Docente: Dr. Jorge Luis Hilario Rivas",
        FONT_BODY, 13.5, True, color=C_AMBER
    )


def build_slide_2(prs: Presentation) -> None:
    """Slide 2: Problema, evidencia y vacío (CLARO_GRIS)."""
    slide = prs.slides.add_slide(prs.slide_layouts[4])
    set_header(slide, "PLANTEAMIENTO DEL PROBLEMA", "Problema, evidencia y vacío de conocimiento", slide_num=2, dark=False)

    # Card 1: El problema
    add_card(slide, 0.60, 2.10, 3.88, 4.65, C_WHITE)
    add_textbox(slide, 0.90, 2.35, 3.28, 0.30, "1 · EL PROBLEMA", FONT_BODY, 12, True, color=C_CORAL)
    tb1 = add_textbox(slide, 0.90, 2.82, 3.28, 3.70)
    add_rich_paragraph(tb1.text_frame, [
        ("Los LLMs procesan instrucciones del sistema y entradas no confiables en un ", False, C_DARK, 16.5),
        ("mismo canal semántico", True, C_DARK, 16.5),
        (", eludiendo controles perimetrales (WAF, IDS).", False, C_DARK, 16.5),
    ], first=True, space_after=12)
    add_rich_paragraph(tb1.text_frame, [
        ("Vectores críticos: ", True, C_CORAL, 15.5),
        ("Prompt Injection (directo e indirecto), Jailbreaking y Data Poisoning en RAG, APIs y agentes.", False, C_DARK, 15.5),
    ], space_after=0)

    # Card 2: La evidencia (dark highlight)
    add_card(slide, 4.73, 2.10, 3.88, 4.65, C_TEAL_DARK)
    add_textbox(slide, 5.03, 2.35, 3.28, 0.30, "2 · LA EVIDENCIA", FONT_BODY, 12, True, color=C_AMBER)
    add_textbox(slide, 5.03, 2.74, 3.28, 0.72, "83.2% / 54.8%", FONT_TITLE, 32, True, color=C_WHITE)
    add_textbox(
        slide, 5.03, 3.48, 3.28, 0.62,
        "éxito en HackAPrompt (600k+ prompts) y evasión media en HIVE-AI (16,683 ataques reales)",
        FONT_BODY, 13.5, False, color=C_MINT
    )
    tb2 = add_textbox(slide, 5.03, 4.28, 3.28, 2.25)
    add_rich_paragraph(tb2.text_frame, [
        ("• Yang et al. (2025): ", True, C_AMBER, 14),
        ("inyección y fine-tuning envenenado alteran LLMs médicos sin degradar benchmarks.", False, C_WHITE, 14),
    ], first=True, space_after=10)
    add_rich_paragraph(tb2.text_frame, [
        ("• Majewski & Santilli (2026): ", True, C_AMBER, 14),
        ("guardrails sufren sobrecarga de latencia, over-refusal y contaminación contextual.", False, C_WHITE, 14),
    ], space_after=0)

    # Card 3: El vacío
    add_card(slide, 8.85, 2.10, 3.88, 4.65, C_WHITE)
    add_textbox(slide, 9.15, 2.35, 3.28, 0.30, "3 · EL VACÍO", FONT_BODY, 12, True, color=C_CORAL)
    tb3 = add_textbox(slide, 9.15, 2.80, 3.28, 3.65)
    add_rich_paragraph(tb3.text_frame, [
        ("Dispersión metodológica y falta de síntesis estandarizada bajo ", False, C_DARK, 15),
        ("MITRE ATLAS", True, C_DARK, 15),
        (" que contraste el trilema operativo:", False, C_DARK, 15),
    ], first=True, space_after=8, line_spacing=1.15)
    add_rich_paragraph(tb3.text_frame, [
        ("• Eficacia defensiva (ASR, exactitud)\n• Latencia de inferencia\n• Sobre-bloqueo (over-refusal)", True, C_TEAL_DARK, 14.5),
    ], space_after=10, line_spacing=1.22)
    add_rich_paragraph(tb3.text_frame, [
        ("Falta una scoping review multibases que integre ataques y defensas en producción.", True, C_CORAL, 14.5),
    ], space_after=0, line_spacing=1.15)


def build_slide_3(prs: Presentation) -> None:
    """Slide 3: Marco PICOD (CLARO)."""
    slide = prs.slides.add_slide(prs.slide_layouts[3])
    set_header(slide, "ESTRUCTURACIÓN METODOLÓGICA", "Marco PICOD de la investigación", slide_num=3, dark=False)

    rows = [
        ("P", "Población / Objeto", C_TEAL_DARK,
         "LLMs fundacionales (propietarios y código abierto) desplegados en producción: APIs, asistentes, sistemas RAG y agentes."),
        ("I", "Intervención / Tecnología", C_TEAL_DARK,
         "Exposición a vectores adversariales (Prompt Injection, Jailbreaking, Data Poisoning) y defensas algorítmicas / guardrails."),
        ("C", "Comparación / Control", C_CORAL,
         "No aplica como comparador único (scoping review exploratoria; se documentan líneas base reportadas en estudios primarios)."),
        ("O", "Outcome / Resultado", C_EMERALD,
         "Taxonomía bajo MITRE ATLAS, eficacia defensiva (ASR, exactitud, F1) y compromisos operacionales (latencia y over-refusal)."),
        ("D", "Diseño de estudio", C_TEAL_DARK,
         "Estudios empíricos y experimentales arbitrados por pares (2023–2026): benchmarking, red teaming y telemetría en producción."),
    ]
    for i, (letter, label, badge_col, desc) in enumerate(rows):
        y = 2.08 + i * 0.96
        add_card(slide, 0.60, y, 12.13, 0.82, C_MIST, radius=0.06, shadow=False)
        add_badge(slide, 0.82, y + 0.16, 0.50, letter, badge_col, C_WHITE, font_size=16)
        add_textbox(slide, 1.50, y + 0.10, 2.75, 0.62, label, FONT_BODY, 15.5, True, color=C_DARK, anchor=MSO_ANCHOR.MIDDLE)
        add_textbox(slide, 4.35, y + 0.08, 8.15, 0.66, desc, FONT_BODY, 14.5, False, color=C_DARK, anchor=MSO_ANCHOR.MIDDLE)


def build_slide_4(prs: Presentation) -> None:
    """Slide 4: Pregunta principal, objetivo general 1:1 y secundarias (CLARO_GRIS)."""
    slide = prs.slides.add_slide(prs.slide_layouts[4])
    set_header(slide, "PREGUNTA Y OBJETIVO · CORRESPONDENCIA 1:1", "Pregunta principal y objetivo general", slide_num=4, dark=False)

    # Top card: Pregunta principal
    add_card(slide, 0.60, 2.05, 5.90, 2.45, C_WHITE)
    add_textbox(slide, 0.90, 2.25, 5.30, 0.28, "PREGUNTA PRINCIPAL DE REVISIÓN", FONT_BODY, 11.5, True, color=C_CORAL)
    tb_q = add_textbox(slide, 0.90, 2.60, 5.30, 1.75)
    add_rich_paragraph(tb_q.text_frame, [
        ("¿Cuáles son los ", False, C_DARK, 15.5),
        ("vectores de ataque y evasión (MITRE ATLAS)", True, C_DARK, 15.5),
        (", así como la ", False, C_DARK, 15.5),
        ("eficacia defensiva y compromisos operacionales", True, C_DARK, 15.5),
        (" (latencia y sobre-bloqueo) de los guardrails en LLMs en producción (2023–2026)?", False, C_DARK, 15.5),
    ], first=True, space_after=0)

    # Right card: Objetivo general
    add_card(slide, 6.83, 2.05, 5.90, 2.45, C_TEAL_DARK)
    add_textbox(slide, 7.13, 2.25, 5.30, 0.28, "OBJETIVO GENERAL (CORRESPONDENCIA 1:1)", FONT_BODY, 11.5, True, color=C_AMBER)
    tb_o = add_textbox(slide, 7.13, 2.60, 5.30, 1.75)
    add_rich_paragraph(tb_o.text_frame, [
        ("Sintetizar ", True, C_AMBER, 15.5),
        ("los vectores de ataque y evasión (MITRE ATLAS), la eficacia defensiva y los compromisos operacionales (latencia y sobre-bloqueo) de los guardrails en LLMs en producción, mediante una ", False, C_WHITE, 15.5),
        ("scoping review (2023–2026).", True, C_MINT, 15.5),
    ], first=True, space_after=0)

    # Secondary questions
    add_textbox(slide, 0.60, 4.72, 6.00, 0.28, "PREGUNTAS SECUNDARIAS", FONT_BODY, 11.5, True, color=C_SLATE)
    secs = [
        ("1", "Taxonomía de ataques", "Vectores de ataque y técnicas de evasión reportados bajo el marco MITRE ATLAS."),
        ("2", "Eficacia defensiva", "Desempeño empírico (ASR, exactitud, precisión y recall) de guardrails en producción."),
        ("3", "Compromisos operativos", "Impacto de la sobrecarga de latencia de inferencia y tasa de sobre-bloqueo (over-refusal)."),
    ]
    for i, (num, stitle, sbody) in enumerate(secs):
        x = 0.60 + i * 4.13
        add_card(slide, x, 5.08, 3.88, 1.72, C_WHITE)
        add_badge(slide, x + 0.25, 5.26, 0.42, num, C_CORAL, C_WHITE, font_size=14)
        add_textbox(slide, x + 0.80, 5.26, 2.85, 0.42, stitle, FONT_BODY, 15.5, True, color=C_DARK, anchor=MSO_ANCHOR.MIDDLE)
        add_textbox(slide, x + 0.25, 5.80, 3.38, 0.85, sbody, FONT_BODY, 13.5, False, color=C_DARK)


def build_slide_5(prs: Presentation) -> None:
    """Slide 5: Diseño metodológico y criterios (CLARO)."""
    slide = prs.slides.add_slide(prs.slide_layouts[3])
    set_header(slide, "DISEÑO Y ALCANCE METODOLÓGICO", "Scoping Review bajo protocolo PRISMA-ScR", slide_num=5, dark=False)

    # Left dark card: Diseño y fuentes
    add_card(slide, 0.60, 2.10, 4.80, 4.65, C_TEAL_DARK)
    add_textbox(slide, 0.90, 2.32, 4.20, 0.28, "ESTRATEGIA DE REVISIÓN", FONT_BODY, 12, True, color=C_AMBER)
    tb_l = add_textbox(slide, 0.90, 2.72, 4.20, 3.85)
    items = [
        ("Tipo de revisión", "Revisión sistemática exploratoria (PRISMA-ScR; Tricco et al., 2018)."),
        ("Fuentes (5 bases)", "Scopus, IEEE Xplore, ScienceDirect, EBSCOhost e IOPscience."),
        ("Periodo e idiomas", "2023–2026 (despliegue masivo de LLMs) · Inglés y español."),
        ("Diseños primarios", "Benchmarking adversarial, red teaming y telemetría en producción."),
    ]
    for idx, (k, v) in enumerate(items):
        add_rich_paragraph(tb_l.text_frame, [
            (f"{k}: ", True, C_MINT, 13.5),
            (v, False, C_WHITE, 13.5),
        ], first=(idx == 0), space_after=10, line_spacing=1.15)

    # Right top card: Inclusión
    add_card(slide, 5.70, 2.10, 7.03, 2.22, C_MIST, shadow=False)
    add_badge(slide, 6.00, 2.28, 0.44, "✓", C_EMERALD, C_WHITE, font_size=16)
    add_textbox(slide, 6.58, 2.28, 4.00, 0.44, "Criterios de inclusión", FONT_BODY, 19, True, color=C_DARK, anchor=MSO_ANCHOR.MIDDLE)
    tb_in = add_textbox(slide, 6.00, 2.85, 6.45, 1.35)
    add_rich_paragraph(tb_in.text_frame, [
        ("1. Estudios primarios empíricos/experimentales arbitrados por pares (2023–2026).\n", False, C_DARK, 14.5),
        ("2. Evalúan LLMs en producción frente a ataques adversariales o guardrails.\n", False, C_DARK, 14.5),
        ("3. Reportan métricas verificables (ASR, exactitud, latencia u over-refusal).", False, C_DARK, 14.5),
    ], first=True, space_after=0, line_spacing=1.25)

    # Right bottom card: Exclusión
    add_card(slide, 5.70, 4.53, 7.03, 2.22, C_MIST, shadow=False)
    add_badge(slide, 6.00, 4.71, 0.44, "✕", C_CORAL, C_WHITE, font_size=15)
    add_textbox(slide, 6.58, 4.71, 4.00, 0.44, "Criterios de exclusión", FONT_BODY, 19, True, color=C_DARK, anchor=MSO_ANCHOR.MIDDLE)
    tb_ex = add_textbox(slide, 6.00, 5.28, 6.45, 1.35)
    add_rich_paragraph(tb_ex.text_frame, [
        ("1. Publicaciones anteriores a 2023 o duplicados entre bases de datos.\n", False, C_DARK, 14.5),
        ("2. Preprints no arbitrados, ensayos opinativos o literatura gris sin validación.\n", False, C_DARK, 14.5),
        ("3. Estudios de ML convencional o seguridad de red tradicional sin LLMs.", False, C_DARK, 14.5),
    ], first=True, space_after=0, line_spacing=1.25)


def build_slide_6(prs: Presentation) -> None:
    """Slide 6: Evidencia científica preliminar (CLARO_GRIS)."""
    slide = prs.slides.add_slide(prs.slide_layouts[4])
    set_header(slide, "BASE CIENTÍFICA PRELIMINAR", "4 estudios clave que sustentan la brecha", slide_num=6, dark=False)

    studies = [
        ("1", "Schulhoff et al. (2023) · HackAPrompt",
         "600,000+ prompts; 9/10 desafíos vulnerados (83.2% éxito en envíos optimizados).",
         "Vacío: solo inyección directa en 3 modelos; sin RAG/agentes ni guardrails externos."),
        ("2", "Majewski et al. (2026) · IEEE Access",
         "AWS Guardrails (96.8%) y NeMo (93.9%) lideran, pero presentan severo over-refusal.",
         "Vacío: en soluciones cloud solo evaluó filtrado de entrada, omitiendo salida."),
        ("3", "Santilli et al. (2026) · D-SHIELD",
         "Evidencia contaminación contextual multiturno; arquitectura desacoplada reduce ASR.",
         "Vacío: validado en un solo modelo (GPT-4o) en prototipo sin alta concurrencia."),
        ("4", "Vargas Yáñez & Tobón (2026) · HIVE-AI",
         "16,683 ataques reales (1,229 IPs, 50 países); 54.8% evasión sin defensa activa.",
         "Vacío: telemetría de un único nodo VPS en 20 días; sin ablación de guardrails."),
    ]
    for i, (num, title, finding, gap) in enumerate(studies):
        col = i % 2
        row = i // 2
        x = 0.60 + col * 6.21
        y = 2.08 + row * 2.40
        add_card(slide, x, y, 5.92, 2.20, C_WHITE)
        add_badge(slide, x + 0.25, y + 0.22, 0.42, num, C_CORAL, C_WHITE, font_size=14)
        add_textbox(slide, x + 0.80, y + 0.22, 4.90, 0.42, title, FONT_BODY, 15.5, True, color=C_DARK, anchor=MSO_ANCHOR.MIDDLE)
        tb = add_textbox(slide, x + 0.25, y + 0.78, 5.42, 1.30)
        add_rich_paragraph(tb.text_frame, [
            ("Aporte: ", True, C_EMERALD, 14),
            (finding, False, C_DARK, 14),
        ], first=True, space_after=8)
        add_rich_paragraph(tb.text_frame, [
            (gap, True, C_CORAL, 13.5),
        ], space_after=0)


def build_slide_7(prs: Presentation) -> None:
    """Slide 7: Aporte esperado y cierre (OSCURO)."""
    slide = prs.slides.add_slide(prs.slide_layouts[2])
    set_header(slide, "CIERRE · IMPACTO DE LA INVESTIGACIÓN", "Aporte científico, tecnológico y práctico", slide_num=7, dark=True)

    impacts = [
        ("CIENTÍFICO", C_PEACH, "Unificación taxonómica",
         "Estructurar bajo MITRE ATLAS y PRISMA-ScR la evidencia empírica 2023–2026 hoy fragmentada."),
        ("TECNOLÓGICO", C_MINT, "Trilema operativo",
         "Caracterizar el equilibrio entre resiliencia (ASR), latencia de inferencia y sobre-bloqueo (over-refusal)."),
        ("PRÁCTICO", C_AMBER, "Criterios de diseño",
         "Guiar a ingenieros y equipos de ciberseguridad para seleccionar y auditar guardrails en producción."),
    ]
    for i, (kicker, kcol, ititle, ibody) in enumerate(impacts):
        x = 0.60 + i * 4.13
        add_card(slide, x, 2.25, 3.88, 3.30, C_TEAL_DARK, radius=0.06, shadow=False)
        add_textbox(slide, x + 0.30, 2.52, 3.28, 0.28, kicker, FONT_BODY, 11.5, True, color=kcol)
        add_textbox(slide, x + 0.30, 2.90, 3.28, 0.45, ititle, FONT_TITLE, 21, True, color=C_WHITE)
        add_textbox(slide, x + 0.30, 3.52, 3.28, 1.80, ibody, FONT_BODY, 15.5, False, color=C_MIST, line_spacing=1.25)

    add_textbox(
        slide, 0.60, 6.05, 12.13, 0.45,
        "¡Muchas gracias!   ·   Pedro Giovanni Ricra Figueroa   ·   EPIS – Universidad Nacional de Ucayali (2026-II)",
        FONT_BODY, 15, True, color=C_AMBER, align=PP_ALIGN.CENTER
    )


def main() -> None:
    prs = Presentation(str(BASE_PPTX))
    clear_existing_slides(prs)
    update_layout_footers(prs, "Ricra Figueroa · Entregable 1 · Ciberseguridad")

    build_slide_1(prs)
    build_slide_2(prs)
    build_slide_3(prs)
    build_slide_4(prs)
    build_slide_5(prs)
    build_slide_6(prs)
    build_slide_7(prs)

    prs.save(str(OUT_PPTX))
    print(f"Saved {OUT_PPTX} with {len(prs.slides)} slides.")


if __name__ == "__main__":
    main()
