---
tipo: dashboard
creado: 2026-08-15
tags:
  - moc
  - dashboard
  - tesis
  - ciberseguridad
  - llm
  - epis-unu
aliases:
  - "Dashboard"
  - "Dashboard General"
  - "MOC Trabajo de Investigacion"
  - "Centro de Control"
  - "Dashboard Trabajo de Investigación"
  - "Dashboard General — Universal Project System (EPIS-UNU)"
  - "Home"
---

# 🛡️ Centro de Control: Sistema ATLAS — Trabajo de Investigación (EPIS-UNU)

> [!abstract] Ficha Institucional y Académica
> - **Tesista:** Pedro Giovanni Ricra Figueroa
> - **Asignatura:** Trabajo de Investigación | **Ciclo:** X (Semestre 2026-II)
> - **Línea de Investigación:** Ciberseguridad
> - **Institución:** Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)
> - **Protocolo:** PRISMA-ScR (*Preferred Reporting Items for Systematic reviews and Meta-Analyses extension for Scoping Reviews*)
> - **Marco Taxonómico:** MITRE ATLAS (*Adversarial Threat Landscape for Artificial-Intelligence Systems*)
> - **Proyecto Activo:** [[PRJ-2026-001_Mapeo-Sistematico-LLMs|PRJ-2026-001: Mapeo Sistemático de Seguridad en LLMs]]
> - **Propuesta de Tesis Derivada:** [[IDEA-001_Tesis-AAM-Guard|AAM-Guard — Desacoplamiento de Atención Asimétrica contra Contaminación Contextual Multi-Turno]] (Puntaje: 94/100)

---

## ⚡ Estado Operativo y Próximos Pasos

> [!tip] Próximas Acciones Prioritarias
> - [x] **Delimitación Temática y Matriz Institucional:** Culminada y aprobada (Secciones I a V en Word) $\rightarrow$ [[PRJ-2026-DELI_Delimitacion-Tematica|Ver archivo histórico]].
> - [x] **Búsqueda Booleana en 5 Bases Indexadas:** 4,037 registros recuperados y deduplicados a 3,262 únicos.
> - [x] **Cribado Sistemático y Auditoría HTTP:** Pipeline de 12 filtros (F0 a F12) con 56 registros conservados y 10 artículos ancla a texto completo.
> - [x] **Análisis Exhaustivo de Vacíos Científicos:** 10 fases culminadas (mapa del estado del arte, contradicciones, ranking multicriterio y selección de tesis).
> - [ ] **Próximo Paso Inmediato:** Redactar la sección de discusión técnica vinculando el trilema de guardrails con las brechas detectadas.
> - [ ] **Hito Semanal:** Ensayar el guion de sustentación oral (3:00 min) con diapositivas PPTX ante asesores EPIS-UNU $\rightarrow$ [[PRJ-2026-001_Sustentacion-Oral|Ver Guion]].

---

## 🧭 Mapa de Navegación ATLAS (Arquitectura del Vault)

`	ext
Atlas/
├── 📂 00_Inbox/
│   └── [[Inbox|Inbox y Triaje de Literatura]]
│
├── 📂 01_Dashboard/
│   ├── [[Home|Home (Centro de Control Principal)]]
│   └── [[Mapa Conceptual Trabajo de Investigación.canvas|Mapa Conceptual Visual Interactivo]]
│
├── 📂 02_Proyectos/
│   └── 📁 PRJ-2026-001_Mapeo-Sistematico-LLMs/ (Proyecto Activo)
│       ├── [[PRJ-2026-001_Mapeo-Sistematico-LLMs|Hub del Proyecto]]
│       ├── 📁 01_Gestion/
│       │   ├── [[PRJ-2026-001_Planificacion|Planificación, Fases y Cronograma]]
│       │   ├── [[PRJ-2026-001_Tareas|Tareas y Checklists]]
│       │   ├── [[PRJ-2026-001_Sustentacion-Oral|Guion de Sustentación Oral (3 min)]]
│       │   └── 📁 Decisiones/ [[DEC-001_Criterios-Inclusion-PRISMA|DEC-001 Criterios PRISMA]]
│       ├── 📁 02_Conocimiento/
│       │   ├── 📁 Investigacion/
│       │   │   ├── [[Matriz Comparativa de Guardrails Comerciales y de Código Abierto]]
│       │   │   ├── [[Evaluación de Trade-offs Seguridad vs Latencia vs Over-Refusal]]
│       │   │   ├── [[Mapa del Estado del Arte y Taxonomía de Evidencia (2023–2026)]]
│       │   │   ├── [[Contradicciones Científicas y Debates Abiertos]]
│       │   │   └── [[Portafolio de Oportunidades y Ranking Multicriterio]]
│       │   └── 📁 Ideas/
│       │       └── [[IDEA-001_Tesis-AAM-Guard|Propuesta de Tesis AAM-Guard]]
│       ├── 📁 03_Trabajo/
│       │   ├── 📁 Protocolos/ [[Protocolo PRISMA-ScR y Códigos de Exclusión]] · [[Ecuaciones de Búsqueda y Filtros por Base de Datos]]
│       │   ├── 📁 Datos/ [[Registro de Datasets y Verificación HTTP]]
│       │   └── 📁 Manuscrito/ [[Esquema-Manuscrito-Scoping-Review]]
│       └── 📁 04_Entregables/
│           ├── [[ENT-001_Matriz-Delimitacion-Oficial|ENT-001 Matriz Word DOCX]]
│           ├── [[ENT-002_Diapositivas-Sustentacion|ENT-002 Diapositivas PPTX]]
│           └── [[ENT-003_Dataset-Consolidado|ENT-003 Dataset 12 XLSX]]
│
├── 📂 03_Conocimiento/ (Biblioteca Reutilizable)
│   ├── 📁 Referencias/ (10 Artículos Clave)
│   │   ├── [[@majewski2026_guardrails|@majewski2026 (Majewski et al.)]]
│   │   ├── [[@santilli2026_dshield|@santilli2026 (Santilli D-SHIELD)]]
│   │   ├── [[@vargasyanez2026_hiveai|@vargasyanez2026 (Vargas Yáñez & Tobón HIVE-AI)]]
│   │   ├── [[@ieee2026_promptfuzz|@ieee2026 (PROMPTFUZZ Fuzzing)]]
│   │   ├── [[@yuan2026_rigorllm|@yuan2026 (Yuan et al. RigorLLM)]]
│   │   ├── [[@zhang2026_backdooralign|@zhang2026 (Zhang et al. BackdoorAlign)]]
│   │   ├── [[@liu2026_rag|@liu2026 (Liu et al. RAG Poisoning)]]
│   │   ├── [[@mdpi2026_middleware|@mdpi2026 (Middleware SLM Local)]]
│   │   ├── [[@schulhoff2024_hackaprompt|@schulhoff2024 (HackAPrompt Global)]]
│   │   └── [[@chen2026_medical|@chen2026 (Chen et al. LLMs Médicos)]]
│   ├── 📁 Conceptos/
│   │   ├── [[Mapa General MITRE ATLAS para LLMs]]
│   │   ├── [[AML.T0051 - Prompt Injection (Directo e Indirecto)]]
│   │   ├── [[AML.T0054 - Jailbreaking y Evasión Adversarial]]
│   │   ├── [[AML.T0018-T0020-T0099 - Data Poisoning y RAG Poisoning]]
│   │   ├── [[AML.M0000 - Guardrails y Mecanismos de Mitigación]]
│   │   ├── [[Linea-Investigacion-Ciberseguridad|Línea de Investigación en Ciberseguridad]]
│   │   └── [[Diccionario de Términos Técnicos y Glosario de Sustentación]]
│   └── 📁 Procedimientos/
│       └── [[Procedimiento-Cribado-PRISMA-ScR]]
│
├── 📂 05_Archivo/
│   ├── 📁 Proyectos/2026/
│   │   └── [[PRJ-2026-DELI_Delimitacion-Tematica|PRJ-2026-DELI: Delimitación Temática]]
│   └── 📁 Historico/
│       ├── [[Archivo - Hitos Culminados Fases 1 a 3]]
│       └── [[Archivo - Log de Búsqueda Booleana Inicial (4037 Registros)]]
│
└── 📂 90_Sistema/
    ├── 📁 Plantillas/ (Catálogo ATLAS)
    └── 📁 Bases/ (Consultas .base)
`

---

## 📊 Embudo PRISMA-ScR y Conciliación Muestral

`mermaid
flowchart TD
    A["<b>1. Búsqueda Global en 5 Bases</b><br>N = 4,037 registros brutos<br>(Scopus: 2,272 | ScienceDirect: 796 | IEEE: 666 | EBSCO: 243 | IOP: 60)"] --> B["<b>2. Pre-screening Técnico</b><br>Filtro temporal (EX-05: 63) e idioma (EX-06: 16)<br>N = 3,958 registros"]
    B --> C["<b>3. Deduplicación Inter-base</b><br>685 duplicados DOI + 11 versiones previas<br>N = 3,262 registros únicos"]
    C --> D["<b>4. Screening Temático y Elegibilidad</b><br>Exclusión ML clásico (EX-01) y sin ciberseguridad (EX-02)<br>N = 400 publicaciones (346 Alta Prioridad + 54 Media)"]
    D --> E["<b>5. Cribado Estricto de Producción (F0–F12)</b><br>N = 56 publicaciones empíricas indexadas<br>(Registros_Conservados_56_LLM.xlsx)"]
    E --> F["⭐ <b>Muestra Ancla a Texto Completo (N=10)</b><br>10 PDFs Open Access archivados en local<br>Evaluación experimental de guardrails y ataques"]
    F --> G["🎓 <b>Análisis de Vacíos y Tesis Formulada</b><br>P-INV-01: AAM-Guard (94 pts)<br>Atención asimétrica contra jailbreaks multi-turno"]

    style A fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    style C fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    style E fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;
    style G fill:#ede7f6,stroke:#512da8,stroke-width:2px;
`

---

## 🔗 Recursos Locales y Enlaces Verificados

- 📑 **Matriz Oficial Word (Secciones I a V):** [[MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx|Abrir Matriz Oficial Word (DOCX)]]
- 📊 **Presentación Oficial de Sustentación:** [[MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx|Abrir Presentación Oficial PPTX (8 Diapositivas)]]
- 📈 **Base Maestra Consolidada (8 Hojas):** [[Base de Datos - 12.xlsx|Abrir Base Maestra Consolidada (XLSX)]]
- 📊 **Base Original 5 Fuentes (Identificación Inicial):** [[Base de Datos - Identificación Inicial.xlsx|Abrir Base Original 5 Fuentes (XLSX)]]
- 📚 **Textos Completos en PDF (10 Investigaciones Ancla):** carpeta investigaciones/
- 🔬 **Entregables de Vacíos Científicos:** [[Mapa del Estado del Arte y Taxonomía de Evidencia (2023–2026)|Abrir Análisis de Vacíos Científicos]]
- 🗺️ **Canvas Interactivo del Proyecto:** [[Mapa Conceptual Trabajo de Investigación.canvas|Abrir Mapa Visual del Proyecto]]