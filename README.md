# trabajo-investigacion — Revisión Sistemática Exploratoria de Seguridad en LLMs en Producción (2023–2026)

> Repositorio académico y cienciométrico para la asignatura Trabajo de Investigación (ESTDI37, EPIS-UNU): delimitación PICOD, búsqueda booleana en cinco bases indexadas, cribado PRISMA-ScR, análisis bibliométrico y categorización bajo MITRE ATLAS de vulnerabilidades adversariales y *guardrails* en Modelos de Lenguaje Grande.

[![Estado](https://img.shields.io/badge/Estado-Activo-success?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Tipo](https://img.shields.io/badge/Tipo-Scoping_Review_(PRISMA--ScR)-blue?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Línea](https://img.shields.io/badge/Línea-Ciberseguridad-red?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Institución](https://img.shields.io/badge/Institución-EPIS--UNU-003366?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Ciclo](https://img.shields.io/badge/Ciclo-X_(2026--II)-orange?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Universo Inicial](https://img.shields.io/badge/Universo_Inicial-4%2C037_registros-informational?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Corpus Incluido](https://img.shields.io/badge/Corpus_Incluido-400_publicaciones-brightgreen?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Muestra Fundamental](https://img.shields.io/badge/Muestra_Fundamental-12_estudios_ancla-blueviolet?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)

El estudiante formula la delimitación temática y la pregunta estructurada PICOD, ejecuta las ecuaciones booleanas en cinco bases de datos científicas, audita el cribado bajo el protocolo PRISMA-ScR y categoriza el corpus bajo MITRE ATLAS; el docente de la asignatura (Dr. Jorge Luis Hilario Rivas, EPIS-UNU) evalúa la coherencia metodológica 1:1, los criterios de elegibilidad, el rigor APA 7 y la sustentación oral de los entregables.

## Tabla de contenidos

- [Descripción](#descripción)
- [Características principales](#características-principales)
- [Stack tecnológico y herramientas](#stack-tecnológico-y-herramientas)
- [Arquitectura del repositorio](#arquitectura-del-repositorio)
- [Instalación y flujo de trabajo](#instalación-y-flujo-de-trabajo)
- [Requisitos del sistema](#requisitos-del-sistema)
- [Pregunta PICOD y objetivo general (Entregable 1)](#pregunta-picod-y-objetivo-general-entregable-1)
- [Estrategia de búsqueda y ecuaciones construidas](#estrategia-de-búsqueda-y-ecuaciones-construidas)
- [Flujo metodológico de selección PRISMA-ScR](#flujo-metodológico-de-selección-prisma-scr)
- [Distribución cienciométrica del corpus (N=400)](#distribución-cienciométrica-del-corpus-n400)
- [Selección de investigaciones fundamentales (N=12)](#selección-de-investigaciones-fundamentales-n12)
- [Taxonomía de vectores y defensas bajo MITRE ATLAS](#taxonomía-de-vectores-y-defensas-bajo-mitre-atlas)
- [Cronograma metodológico y evaluaciones del curso](#cronograma-metodológico-y-evaluaciones-del-curso)
- [Autor](#autor)

## Descripción

El despliegue comercial de Modelos de Lenguaje Grande (LLMs) en interfaces API, asistentes conversacionales, sistemas de generación aumentada por recuperación (RAG) y arquitecturas agénticas expone una superficie de ataque en la capa semántica que elude los controles perimetrales tradicionales (WAF, cortafuegos y NIDS). Al procesar instrucciones privilegiadas del sistema y entradas no confiables en un mismo canal textual no estructurado, los modelos quedan expuestos a *Prompt Injection* directo e indirecto, *Jailbreaking* y envenenamiento de datos en ajuste fino o contextos RAG.

Este repositorio centraliza los entregables académicos, las bases de datos cienciométricas, los artículos científicos primarios en acceso abierto, los materiales oficiales de clase y la bóveda de conocimiento para la asignatura Trabajo de Investigación (ESTDI37, Ciclo X, 2026-II) en la Escuela Profesional de Ingeniería de Sistemas de la Universidad Nacional de Ucayali (EPIS-UNU). Incluye la matriz inicial [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx), el primer avance formal [Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx](Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx) con su presentación de sustentación [Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx](Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx), el dataset consolidado [Base de Datos - 12.xlsx](Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx) y los textos completos en [investigaciones/](investigaciones).

Las decisiones metodológicas centrales del proyecto comprenden:
1. Estructuración de la pregunta mediante el marco **PICOD** (Khan et al., 2022) con correspondencia directa 1:1 entre problema, pregunta principal y objetivo general, justificando la no aplicabilidad de un comparador experimental único por la naturaleza exploratoria de la revisión.
2. Adopción de la guía **PRISMA-ScR** (Tricco et al., 2018) para revisiones sistemáticas exploratorias y la taxonomía **MITRE ATLAS** (*Adversarial Threat Landscape for Artificial-Intelligence Systems*, v5.1.0) para clasificar vectores ofensivos y defensas.
3. Búsqueda booleana triaxial ejecutada en cinco bases indexadas (Scopus, ScienceDirect, IEEE Xplore, EBSCOhost e IOPscience) acotada al cuatrienio **2023–2026**, depurando 4,037 registros brutos hasta consolidar 3,262 publicaciones únicas y un corpus incluido de 400 estudios bajo 12 códigos explícitos de exclusión (`EX-01` a `EX-12`).
4. Contraste empírico del trilema operativo de los *guardrails* en producción: resiliencia ante ataques (tasa de éxito de ataque, ASR), sobrecarga de latencia en inferencia y tasa de sobre-bloqueo (*over-refusal*) en consultas benignas.

## Características principales

- **Entregable 1 completo y sustentación (PC2):** Documento oficial [Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx](Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx) y presentación ejecutiva de 7 diapositivas [Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx](Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx) basados en [Formato_Entregable_1_Primer_Avance_Investigacion-tarea.docx](Formato_Entregable_1_Primer_Avance_Investigacion-tarea.docx) y [Paso 1.docx](Paso%201.docx).
- **Delimitación temática inicial (PC1):** Matriz institucional [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx) y diapositivas [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx](MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx) con delimitación espacial en la UNU (Pucallpa, Perú) y temporal 2023–2026.
- **Universo bibliográfico de 4,037 registros brutos:** Extracciones originales en CSV y RIS desde Scopus (2,272), ScienceDirect (796), IEEE Xplore (666), EBSCOhost (243) e IOPscience (60), consolidadas en [Base de Datos - Identificación Inicial.xlsx](Base%20de%20Datos/Base%20de%20Datos%20-%20Identificaci%C3%B3n%20Inicial.xlsx).
- **Deduplicación y cribado PRISMA-ScR auditable:** Remoción documentada de 79 exclusiones de pre-screening y 696 duplicados en [Base de Datos - Sin duplicados.xlsx](Base%20de%20Datos/Base%20de%20Datos%20-%20Sin%20duplicados.xlsx), seguida de 2,862 exclusiones codificadas (`EX-01` a `EX-12`) y 400 estudios incluidos en [Base de Datos - 12.xlsx](Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx).
- **Núcleo de 12 investigaciones fundamentales (10 PDFs locales):** Artículos completos de acceso abierto en [investigaciones/](investigaciones) con citas APA 7 verificadas directamente sobre las publicaciones originales.
- **Material de cátedra y referencias bibliométricas:** Sílabo oficial 2026-II, sesiones de aprendizaje (semanas 1–17), diapositivas de clase y guías de VOSviewer/PRISMA en [TRABAJOS DE INVESTIGACION/](TRABAJOS%20DE%20INVESTIGACION), además de ejemplos y análisis bibliométricos en [Ejemplos/](Ejemplos).
- **Evidencias de consulta y bóveda de conocimiento:** Capturas de búsqueda en [Evidencias/](Evidencias), constancia RENACYT-CONCYTEC en [Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf](Evidencia%20creaci%C3%B3n%20de%20cuenta%20-%20Pedro%20Ricra%20Figueroa.pdf) y notas estructuradas en [Obsidian/](Obsidian).

## Stack tecnológico y herramientas

| Capa | Tecnología / Herramienta | Función |
| :--- | :--- | :--- |
| Formulación conceptual | Markdown (`.md`) | Parámetros iniciales en [tema.md](tema.md) y notas en [Obsidian/](Obsidian) |
| Documentos académicos | Microsoft Word OpenXML (`.docx`) | Entregable 1 oficial, matriz de delimitación y análisis bibliométricos |
| Presentaciones | Microsoft PowerPoint OpenXML (`.pptx`) | Diapositivas de sustentación para PC1 y Entregable 1 (PC2) |
| Gestión tabular y cribado | Microsoft Excel (`.xlsx`), CSV, RIS | Registro bruto, deduplicación, códigos `EX-01` a `EX-12` y estadísticas |
| Corpus documental | PDF (`.pdf`) | 10 artículos ancla en [investigaciones/](investigaciones) y 15 materiales de clase en [TRABAJOS DE INVESTIGACION/](TRABAJOS%20DE%20INVESTIGACION) |
| Mapeo bibliométrico | VOSviewer (v1.6.21) | Redes de coocurrencia, densidad y evolución temporal (*Overlay*) en [Obsidian/99_Adjuntos/](Obsidian/99_Adjuntos) |
| Marco de ciberseguridad | MITRE ATLAS (v5.1.0) | Taxonomía estándar de técnicas adversariales y mitigaciones en sistemas de IA |
| Protocolo de revisión | PRISMA-ScR / PRISMA 2020 | Trazabilidad del cribado, elegibilidad y consistencia numérica |
| Bases indexadas | Scopus, ScienceDirect, IEEE Xplore, EBSCOhost, IOPscience | Recuperación documental mediante acceso institucional RENACYT-CONCYTEC |
| Control de versiones | Git / GitHub | Trazabilidad de cambios del repositorio |

## Arquitectura del repositorio

```text
trabajo-investigacion/
├── Base de Datos/                                              # Extracciones brutas (.csv, .ris) y libros procesados (.xlsx)
│   ├── RIS/                                                    # Registros individuales .ris (1.ris–10.ris y ScienceDirect_consolidado.ris)
│   ├── Base de Datos - Identificación Inicial.xlsx             # Recopilación bruta inicial (4,037 registros)
│   ├── Base de Datos - Sin duplicados.xlsx                     # Universo deduplicado (3,262 registros únicos)
│   ├── Base de Datos - 12.xlsx                                 # Libro consolidado (400 incluidos, 2,862 excluidos, métricas)
│   ├── EBSCO.csv                                               # Extracción de EBSCOhost (243 registros)
│   ├── IEEE Xplore.csv / IEE Xplore Completo.csv               # Extracción de IEEE Xplore (666 registros)
│   ├── IOPscience.csv                                          # Extracción de IOPscience (60 registros)
│   ├── ScienceDirect.csv / ScienceDirect.ris                   # Extracción de ScienceDirect (796 registros)
│   └── Scopus.csv                                              # Extracción de Scopus (2,272 registros)
├── Ejemplos/                                                   # Formatos de ejemplo de Entregable 1 y análisis bibliométricos
├── Evidencias/                                                 # Capturas de pantalla de consultas en Scopus, IEEE e IOPscience
├── Obsidian/                                                   # Bóveda ATLAS (Dashboard, Proyecto PRJ-2026-001, Referencias, MITRE ATLAS)
├── TRABAJOS DE INVESTIGACION/                                  # Sílabo 2026-II, sesiones de aprendizaje y 13 PDFs de clase/VOSviewer
├── investigaciones/                                            # 10 artículos científicos completos en PDF (Acceso Abierto)
├── ANÁLISIS BIBLIOMÉTRICO.docx                                 # Documento de análisis bibliométrico del proyecto
├── Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf     # Constancia de credencial RENACYT-CONCYTEC / UNU
├── Formato_Entregable_1_Primer_Avance_Investigacion-tarea.docx # Plantilla oficial del Entregable 1 (ESTDI37)
├── MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx              # Matriz de delimitación temática (PC1)
├── MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx              # Diapositivas de sustentación inicial (8 láminas)
├── Paso 1.docx                                                 # Lectura base: Khan et al. (2022) sobre formulación de pregunta
├── Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx              # Entregable 1 completado (Paso 1 / PICOD / APA 7)
├── Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx              # Presentación ejecutiva del Entregable 1 (7 diapositivas)
├── README.md                                                   # Documentación general del repositorio
└── tema.md                                                     # Parámetros conceptuales iniciales del estudio
```

Decisiones de organización del repositorio:
- **Separación de datos crudos y curados (`Base de Datos/`):** Aísla las descargas originales en `.csv` y `.ris` de los libros `.xlsx` de deduplicación y cribado para auditar cada etapa de filtrado sin alterar los datos fuente.
- **Preservación local de fuentes primarias (`investigaciones/`):** Almacena los PDFs de acceso abierto para verificar citas textuales, autores, DOIs y métricas cuantitativas sin depender de enlaces externos.
- **Separación de material de cátedra (`TRABAJOS DE INVESTIGACION/`):** Mantiene el sílabo, las 17 sesiones de aprendizaje y las diapositivas del curso desacopladas de los entregables propios ubicados en la raíz.

## Instalación y flujo de trabajo

### Prerrequisitos

- Git (`>= 2.30`) para clonar el repositorio.
- Suite ofimática compatible con OpenXML (Microsoft Office 2016+ o LibreOffice) para abrir `.docx`, `.pptx` y `.xlsx`.
- Visor PDF para consultar los artículos en `investigaciones/` y el material de `TRABAJOS DE INVESTIGACION/`.
- Opcional: Python `3.10+` con `openpyxl` y `pandas` para inspección tabular automatizada.

### Clonación e inspección rápida

```bash
git clone https://github.com/TeVerde29/trabajo-investigacion.git
cd trabajo-investigacion
```

```powershell
# Opcional: inspeccionar las hojas de Base de Datos - 12.xlsx con Python
python -c "import openpyxl; wb = openpyxl.load_workbook('Base de Datos/Base de Datos - 12.xlsx', read_only=True); print(wb.sheetnames)"
```

### Flujo de consulta para revisión académica

1. Revisar el **Entregable 1 (PC2)** en [Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx](Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx) y su presentación en [Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx](Ricra_Figueroa_Pedro_Giovanni_Entregable1.pptx).
2. Contrastar con la matriz inicial de la **Unidad I (PC1)** en [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx).
3. Verificar las evidencias de acceso y capturas en [Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf](Evidencia%20creaci%C3%B3n%20de%20cuenta%20-%20Pedro%20Ricra%20Figueroa.pdf) y [Evidencias/](Evidencias).
4. Auditar la deduplicación y el cribado PRISMA-ScR en [Base de Datos - Sin duplicados.xlsx](Base%20de%20Datos/Base%20de%20Datos%20-%20Sin%20duplicados.xlsx) y [Base de Datos - 12.xlsx](Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx).
5. Consultar los textos completos de respaldo en [investigaciones/](investigaciones).

## Requisitos del sistema

| Componente | Requisito mínimo | Propósito |
| :--- | :--- | :--- |
| Sistema operativo | Windows 10/11, macOS 12+ o Linux x86_64 | Entorno local de edición y consulta |
| Procesador de texto | Microsoft Word 2016+ o LibreOffice Writer | Lectura y edición de entregables `.docx` |
| Presentador | PowerPoint 2016+ o LibreOffice Impress | Visualización de presentaciones `.pptx` |
| Hoja de cálculo | Excel 2016+ o LibreOffice Calc | Auditoría de `.xlsx` y `.csv` |
| Lector PDF | Navegador web, Adobe Reader o SumatraPDF | Lectura de artículos y material de clase |
| Python (opcional) | Python 3.10+ (`python-docx`, `python-pptx`, `openpyxl`) | Automatización y verificación de datos |

## Pregunta PICOD y objetivo general (Entregable 1)

### Estructuración PICOD

- **P (Población / Objeto):** Modelos de Lenguaje Grande (LLMs) fundacionales, propietarios y de código abierto desplegados en entornos de producción (interfaces API, asistentes conversacionales, sistemas RAG y arquitecturas de agentes autónomos).
- **I (Intervención / Tecnología):** Exposición a vectores de ataque adversarial y técnicas de evasión (*Prompt Injection* directo e indirecto, *Jailbreaking* y *Data/RAG Poisoning*) e implementación de mecanismos de defensa algorítmica y *guardrails* de seguridad, categorizados bajo MITRE ATLAS.
- **C (Comparación / Control):** No aplica como comparador experimental único en la pregunta principal debido a la naturaleza exploratoria del *scoping review* (Khan et al., 2022); se documentan los contrastes internos reportados en los estudios primarios.
- **O (Outcome / Resultados):** Categorización taxonómica bajo MITRE ATLAS, eficacia defensiva (tasa de éxito de ataque [ASR], exactitud, precisión, *recall* y tasa de detección) y compromisos operacionales (sobrecarga de latencia de inferencia y tasa de sobre-bloqueo [*over-refusal*]).
- **D (Diseño):** Estudios científicos primarios empíricos y experimentales (*benchmarking* adversarial, validaciones de *guardrails*, *red teaming* a gran escala y telemetría en producción) arbitrados por pares (2023–2026).

### Pregunta principal y objetivo general (correspondencia 1:1)

- **Pregunta principal:** ¿Cuáles son los vectores de ataque adversarial y técnicas de evasión (clasificados bajo MITRE ATLAS), así como la eficacia defensiva y los compromisos operacionales (latencia de inferencia y sobre-bloqueo) de los mecanismos de defensa algorítmica y *guardrails* en Modelos de Lenguaje Grande (LLMs) desplegados en producción, según estudios científicos empíricos arbitrados por pares publicados entre 2023 y 2026?
- **Objetivo general:** Sintetizar los vectores de ataque adversarial y técnicas de evasión (clasificados bajo MITRE ATLAS), así como la eficacia defensiva y los compromisos operacionales (latencia de inferencia y sobre-bloqueo) de los mecanismos de defensa algorítmica y *guardrails* en Modelos de Lenguaje Grande (LLMs) desplegados en producción, mediante una revisión sistemática exploratoria (*scoping review*) de estudios científicos empíricos arbitrados por pares publicados entre 2023 y 2026.

## Estrategia de búsqueda y ecuaciones construidas

La recuperación documental se articuló mediante una formulación booleana triaxial combinada con el operador `AND`:

```text
Bloque 1 (Modelos):
("large language model*" OR LLM OR LLMs OR "foundation model*")

AND

Bloque 2 (Vectores de ataque):
("prompt injection" OR jailbreak* OR "data poisoning" OR "adversarial machine learning" OR "AI red teaming")

AND

Bloque 3 (Seguridad y defensa):
("LLM security" OR "language model security" OR vulnerab* OR attack* OR evasion OR defense OR defence OR mitigation OR detection OR guardrails)
```

### Ecuación general aplicada (Scopus, IEEE Xplore, ScienceDirect, EBSCOhost)

```text
("large language model*" OR LLM OR LLMs OR "foundation model*") AND ("prompt injection" OR jailbreak* OR "data poisoning" OR "adversarial machine learning" OR "AI red teaming") AND ("LLM security" OR "language model security" OR vulnerab* OR attack* OR evasion OR defense OR defence OR mitigation OR detection OR guardrails)
```

### Ecuación adaptada a IOPscience

```text
("large language model" OR LLM) AND ("prompt injection" OR jailbreak OR "data poisoning" OR "adversarial") AND (security OR defense OR attack)
```

Filtros aplicados en IOPscience: periodo de los últimos 5 años, tipo de documento *Article* y disponibilidad exclusiva en *Open Access*.

## Flujo metodológico de selección PRISMA-ScR

El cribado sistemático documentado en la hoja `8. Estadísticas de selección` de [Base de Datos - 12.xlsx](Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx) sigue seis etapas:

| Fase PRISMA-ScR | Etapa del proceso | Criterio aplicado / Justificación | Registros | % del Total |
| :--- | :--- | :--- | :---: | :---: |
| **Identificación** | Registros brutos recopilados | Scopus (2,272), ScienceDirect (796), IEEE (666), EBSCO (243), IOP (60) | **4,037** | 100.0% |
| **Pre-screening** | Exclusiones temporales | Artículos con año 2027 (fuera de 2023–2026, código `EX-05`) | 63 | 1.6% |
| **Pre-screening** | Exclusiones por idioma | Artículos en chino u otros alfabetos no latinos (`EX-06`) | 16 | 0.4% |
| **Deduplicación** | Duplicados inter-base exactos | Coincidencia exacta de DOI normalizado | 685 | 17.0% |
| **Deduplicación** | Consolidación de versiones | Pares inter-base EBSCO/Scopus y versiones conferencia-revista | 11 | 0.3% |
| **Screening** | Base única consolidada a evaluar | Publicaciones únicas examinadas (Hoja 1) | **3,262** | 80.8% |
| **Elegibilidad** | Exclusiones aplicadas (`EX-01` a `EX-12`) | ML clásico, mención superficial, ciberseguridad tradicional, sin defensa, laboratorio aislado, etc. (Hoja 4) | **2,862** | 70.9% |
| **Inclusión** | Prioridad Alta (Hoja 2) + Media (Hoja 3) | 346 de prioridad alta + 54 de prioridad media | **400** | **9.9%** |

### Distribución por base de datos de origen

| Base de datos | Registros brutos | Exclusiones pre-screening | Duplicados consolidados | Estudios únicos (Hoja 1) | Estudios incluidos (Hojas 2+3) | Tasa de inclusión (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Scopus | 2,272 | 38 | 284 | 1,950 | 248 | 12.7% |
| ScienceDirect (Elsevier) | 796 | 14 | 218 | 564 | 62 | 11.0% |
| IEEE Xplore | 666 | 11 | 156 | 499 | 74 | 14.8% |
| EBSCOhost | 243 | 16 | 26 | 201 | 14 | 7.0% |
| IOPscience | 60 | 0 | 12 | 48 | 2 | 4.2% |
| **Total Consolidado** | **4,037** | **79** | **696** | **3,262** | **400** | **12.3%** |

## Distribución cienciométrica del corpus (N=400)

- **Distribución temporal:** 2026 (272 estudios, 68.0%), 2025 (112 estudios, 28.0%), 2024 (14 estudios, 3.5%) y 2023 (2 estudios, 0.5%).
- **Idioma del corpus incluido:** 400 publicaciones en inglés (100.0%).

| Vector de ataque principal | Frecuencia | % del Corpus (N=400) | Mecanismo defensivo predominante | Frecuencia | % del Corpus (N=400) |
| :--- | :---: | :---: | :--- | :---: | :---: |
| **Prompt Injection (Directo e Indirecto)** | 164 | 41.0% | **Generative AI Guardrails** | 178 | 44.5% |
| **Jailbreaking (Evasión de alineamiento)** | 148 | 37.0% | **Adversarial Input Detection** | 124 | 31.0% |
| **Data Poisoning & Backdoor Attacks** | 52 | 13.0% | **Architectural Isolation & Tool Limits** | 50 | 12.5% |
| **RAG Poisoning & Context Manipulation** | 36 | 9.0% | **Model Alignment & Safe Unlearning** | 48 | 12.0% |

## Selección de investigaciones fundamentales (N=12)

A partir del corpus incluido se aislaron 12 estudios ancla; 10 cuentan con su archivo PDF completo en [investigaciones/](investigaciones) (los estudios 1, 3, 4 y 5 de la tabla siguiente incorporan las citas verificadas directamente sobre los PDFs):

| N.º | ID | Referencia APA 7 / Estudio | Vector principal | Hallazgo o métrica clave | Archivo local |
| :---: | :---: | :--- | :--- | :--- | :---: |
| 1 | 141 | Cao, X., & Bao, Y. (2026). *IEEE BigDIA*. | Prompt Injection | Formaliza control de flujo (IFC) y métrica *Safe Utility Ratio* (SUR). | - |
| 2 | 419 | Majewski, P., Marczak, K., Dubicka, N., Podolak, J., Sochaj, B., Siłka, J., & Kowal, M. (2026). *IEEE Access*, *14*, 70863–70879. | Jailbreaking & Guardrails | AWS Guardrails (96.8%) y NeMo (93.9%) lideran; Llama Guard falla en neutrales (49.3%–53.4%). | [`2_Comprehensive...pdf`](investigaciones/2_Comprehensive_Analysis_of_LLM_Guardrails_Approaches_Preventing_Harmful_Content_and_Jailbreak_Attacks.pdf) |
| 3 | 1068 | Knowlton, B. et al. (2026). *IEEE Access*. | Jailbreaking | Evasión de alineamiento en chatbots comerciales y fragilidad de filtros estáticos. | - |
| 4 | 748 | Vargas Yáñez, S., & Tobón, S. (2026). *International Journal of Information Security*, *25*(3), 158. | Indirect Prompt Injection | HIVE-AI captura 16,683 ataques en producción; triangulación reduce evasión de 54.8% a 9.3% (*p99* < 5 ms). | [`4_Hive-AI...pdf`](investigaciones/4_Hive-AI%20a%20defended%20multi-service%20honeypot%20framework%20for%20generative%20AI%20APIs.pdf) |
| 5 | 1085 | IEEE Authors. (2026). *PROMPTFUZZ*. | Prompt Injection & Jailbreak | Fuzzing semántico descubrió >1,400 jailbreaks con tasas de bypass >65%. | [`5_PROMPTFUZZ...pdf`](investigaciones/5_PROMPTFUZZ%20Harnessing%20Fuzzing%20Techniques%20for%20Robust%20Testing%20of%20Prompt%20Injection%20in%20Large%20Language%20Models.pdf) |
| 6 | 3098 | Yuan, Z., Xiong, Z., Zeng, Y., Yu, N., Jia, R., Song, D., & Li, B. (2024). *RigorLLM* (*ICML / PMLR 235*). | Jailbreaking & Inyección | Fusión k-NN + LLM con optimización minimax; 100% detección ante ataques GCG/AutoDAN en AdvBench. | [`6_RigorLLM...pdf`](investigaciones/6_RigorLLM%20Resilient%20Guardrails%20for%20Large%20Language%20Models%20against%20Undesired%20Content.pdf) |
| 7 | 2747 | Zhang, Y. et al. (2026). *BackdoorAlign*. | Data Poisoning & Backdoors | Reduce ASR de backdoor de 89.4% a <3.1% preservando utilidad. | [`7_BackdoorAlign...pdf`](investigaciones/7_BackdoorAlign%20Mitigating%20Fine-tuning%20based%20Jailbreak%20Attack%20with%20Backdoor%20Enhanced%20Safety%20Alignment.pdf) |
| 8 | 3086 | Liu, H. et al. (2026). *Ranking Manipulation for Conversational Search Engines*. | RAG Poisoning | Consenso verificable mitiga 91.2% de ataques de envenenamiento en RAG. | [`8_Ranking...pdf`](investigaciones/8_Ranking%20Manipulation%20for%20Conversational%20Search%20Engines.pdf) |
| 9 | 80 | MDPI Authors. (2026). *Electronics*. | Prompt Injection & Privacidad | Middleware con SLM local alcanza 95.83% de exactitud y retiene 95% de datos sensibles. | [`9_A Privacy...pdf`](investigaciones/9_A%20Privacy-Preserving%20Middleware%20Architecture%20for%20Detecting%20Prompt%20Injection%20and%20Sensitive%20Data%20Exposure%20in%20Large-Language-Model%20Interactions.pdf) |
| 10 | 3256 | Schulhoff, S., Pinto, J., Khan, A., Bouchard, L.-F., Si, C., Anati, S., Tagliabue, V., Kost, A. L., Carnahan, C., & Boyd-Graber, J. (2023). *EMNLP 2023*, pp. 4945–4977. | Prompt Injection & Jailbreak | Competición HackAPrompt (>600,000 prompts); 9/10 desafíos vulnerados (83.2% en envíos). | [`10_Ignore...pdf`](investigaciones/10_Ignore%20This%20Title%20and%20HackAPrompt%20Exposing%20Systemic%20Vulnerabilities%20of%20LLMs%20Through%20a%20Global%20Prompt%20Hacking%20Competition.pdf) |
| 11 | 1628 | Yang, Y., Jin, Q., Huang, F., & Lu, Z. (2025). *Nature Communications*, *16*, 9011. | Prompt & Fine-Tuning Poisoning | Alteración grave de decisiones médicas (0.50%→80.60%) sin degradar *benchmarks* estándar. | [`11_Adversarial...pdf`](investigaciones/11_Adversarial%20prompt%20and%20fine-tuning%20attacks%20threaten%20medical%20large%20language%20models.pdf) |
| 12 | 40 | Santilli, T., De Luca, M., Amalfitano, D., Fasolino, A. R., & Pelliccione, P. (2026). *Information and Software Technology*, *195*, 108130. | Jailbreak & Runtime Evasion | D-SHIELD descontextualizado reduce ASR a 2.76% (1.38% en *light* con 94% de ahorro de costo). | [`12_A decontext...pdf`](investigaciones/12_A%20decontextualized%20LLM-based%20safeguard%20technique%20for%20automated%20jailbreak%20mitigation.pdf) |

## Taxonomía de vectores y defensas bajo MITRE ATLAS

```text
+----------------------------------------------------------------------------------------------------+
|                         MATRIZ TAXONÓMICA DE CIBERSEGURIDAD EN LLMS EN PRODUCCIÓN                  |
+--------------------------------------------------+-------------------------------------------------+
|      Técnicas de Ataque Adversarial (ATLAS)      |        Mecanismos Defensivos y Guardrails       |
+--------------------------------------------------+-------------------------------------------------+
| AML.T0051.000 - Direct Prompt Injection          | - Sanitización y normalización léxica en entrada|
|   Inyección de instrucciones en prompts de usuario| - Filtros semánticos perimetrales con SLM local |
| AML.T0051.001 - Indirect Prompt Injection        | - Aislamiento contextual de datos recuperados   |
|   Inyección a través de fuentes web, APIs y RAG  | - Triangulación defensiva multiturno (HIVE-AI)  |
| AML.T0054 - LLM Jailbreak Injection             | - Guardrails dedicados (Llama Guard, NeMo, AWS) |
|   Bypass de alineamiento mediante roles y sufijos | - Evaluación descontextualizada (D-SHIELD)      |
| AML.T0020 - Poison Training Data                 | - Purificación de gradientes en fine-tuning     |
|   Inserción de triggers en datasets de ajuste    | - Desaprendizaje guiado de backdoors            |
| AML.T0099 - AI Agent / Context Poisoning         | - Control de Flujo de Información (IFC)         |
|   Contaminación de la memoria y bases vectoriales| - Verificación de consenso en pasajes RAG       |
+--------------------------------------------------+-------------------------------------------------+
```

## Cronograma metodológico y evaluaciones del curso

De acuerdo con el sílabo oficial de la asignatura (`Silabo Trabajo De Investigacion 2026 - II DR HILARIO RV[R].pdf`):

| Evaluación | Unidad / Semana | Fechas | Evidencia principal | Estado |
| :--- | :---: | :--- | :--- | :---: |
| **PC1** | Unidad I · Sem. 04 | 02–08/11/2026 | Matriz bibliográfica inicial y delimitación (`MATRIZ_DELI_*.docx` y `.pptx`) | Completado |
| **PC2 (Entregable 1)** | Unidad II · Sem. 07 | 23–29/11/2026 | Pregunta PICOD y objetivo 1:1 (`Ricra_Figueroa_Pedro_Giovanni_Entregable1.docx` y `.pptx`) | Completado |
| **Examen Parcial** | Sem. 08 | 30/11–06/12/2026 | Evaluación escrita de Unidades I y II | Próximo |
| **PC3** | Unidad III · Sem. 13 | 04–10/01/2027 | Matriz de selección, evaluación de calidad/sesgo y extracción de datos | Adelantado (`Base de Datos - 12.xlsx`) |
| **PC4** | Unidad IV · Sem. 16 | 25–31/01/2027 | Revisión integrada, diagrama PRISMA y análisis bibliométrico VOSviewer | En progreso |
| **Examen Final** | Sem. 17 | 01–07/02/2027 | Presentación y sustentación individual ante el docente | Pendiente |

---

## Autor

**Pedro Giovanni Ricra Figueroa** — Estudiante de Ingeniería de Sistemas (EPIS-UNU)

- GitHub: [@TeVerde29](https://github.com/TeVerde29)
- Correo electrónico: hikih020@gmail.com

---

Si este proyecto te resultó útil, considera darle una estrella en GitHub.
