# trabajo-investigacion — Mapeo Sistemático de Vulnerabilidades, Evasión y Defensas en LLMs en Producción bajo MITRE ATLAS (2023–2026)

> Repositorio de investigación cienciométrica y metodológica para el mapeo sistemático (*Scoping Review*) de vectores de ataque adversarial y evaluación empírica de defensas algorítmicas en Modelos de Lenguaje Grande desplegados en producción.

[![Estado](https://img.shields.io/badge/Estado-Activo-success?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Tipo](https://img.shields.io/badge/Tipo-Scoping_Review_(PRISMA--ScR)-blue?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Línea](https://img.shields.io/badge/Línea-Ciberseguridad-red?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Institución](https://img.shields.io/badge/Institución-EPIS--UNU-003366?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Ciclo](https://img.shields.io/badge/Ciclo-X_(2026--II)-orange?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Universo Inicial](https://img.shields.io/badge/Universo_Inicial-4%2C037_registros-informational?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Corpus Incluido](https://img.shields.io/badge/Corpus_Incluido-400_publicaciones-brightgreen?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Muestra Fundamental](https://img.shields.io/badge/Muestra_Fundamental-12_estudios_ancla-blueviolet?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)

El tesista formula la delimitación cuatridimensional, ejecuta las ecuaciones booleanas en cinco bases de datos indexadas, audita el cribado bajo el protocolo PRISMA-ScR y categoriza el corpus bajo MITRE ATLAS; los docentes revisores y asesores de la EPIS-UNU evalúan la pertinencia temática en ciberseguridad, auditan la reproducibilidad del protocolo de filtrado y verifican la consistencia de las fuentes científicas de soporte.

## Tabla de contenidos

- [Descripción](#descripción)
- [Repositorio y recursos](#repositorio-y-recursos)
- [Características principales](#características-principales)
- [Stack tecnológico y herramientas](#stack-tecnológico-y-herramientas)
- [Arquitectura del repositorio](#arquitectura-del-repositorio)
- [Instalación y flujo de trabajo](#instalación-y-flujo-de-trabajo)
- [Requisitos del sistema](#requisitos-del-sistema)
- [Pregunta y objetivos de investigación](#pregunta-y-objetivos-de-investigación)
- [Estrategia de búsqueda y ecuaciones construidas](#estrategia-de-búsqueda-y-ecuaciones-construidas)
- [Flujo metodológico de selección PRISMA-ScR](#flujo-metodológico-de-selección-prisma-scr)
- [Distribución cienciométrica del corpus (N=400)](#distribución-cienciométrica-del-corpus-n400)
- [Selección de investigaciones fundamentales (N=12)](#selección-de-investigaciones-fundamentales-n12)
- [Taxonomía de vectores y defensas bajo MITRE ATLAS](#taxonomía-de-vectores-y-defensas-bajo-mitre-atlas)
- [Cronograma metodológico de trabajo](#cronograma-metodológico-de-trabajo)

## Descripción

El despliegue a gran escala de Modelos de Lenguaje Grande (LLMs) y sistemas agénticos en aplicaciones comerciales expone vulnerabilidades críticas en el plano semántico que no pueden mitigarse con controles perimetrales convencionales (cortafuegos, autenticación de red o inspección estática). A diferencia del software determinista, los LLMs procesan instrucciones de control del sistema y datos no confiables de usuarios a través de un único canal conversacional no estructurado, habilitando vectores de explotación como la inyección directa e indirecta de prompts (*Prompt Injection*), la evasión algorítmica de restricciones (*Jailbreaking*) y la manipulación de contextos externos (*RAG Poisoning*).

Este repositorio centraliza los artefactos metodológicos, las matrices institucionales, la base cienciométrica y los artículos científicos de soporte para el desarrollo de la asignatura Trabajo de Investigación (Ciclo X, semestre 2026-II) en la Escuela Profesional de Ingeniería de Sistemas de la Universidad Nacional de Ucayali (EPIS-UNU). El proyecto articula la formulación formal en [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx), la presentación de sustentación en [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx), los parámetros de búsqueda en [tema.md](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/tema.md), el dataset de cribado en [Base de Datos - 12.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx) y los textos completos de acceso abierto en [investigaciones/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones).

Las decisiones de diseño metodológico aplicadas en el estudio comprenden:
1. Adopción de la taxonomía **MITRE ATLAS** (*Adversarial Threat Landscape for Artificial-Intelligence Systems*) como marco técnico de clasificación de amenazas y mecanismos de mitigación.
2. Ecuación booleana triaxial común probada y ejecutada en cinco bases de datos indexadas: Scopus, ScienceDirect, IEEE Xplore, EBSCOhost e IOPscience.
3. Ventana temporal acotada a publicaciones comprendidas entre 2023 y 2026, capturando el despliegue empírico de modelos fundacionales en arquitecturas productivas.
4. Protocolo estricto de cribado PRISMA-ScR en seis etapas con 12 códigos de exclusión explícitos (EX-01 a EX-12), depurando 4,037 registros brutos hasta consolidar un corpus de 400 publicaciones evaluadas (346 de prioridad alta y 54 de prioridad media).
5. Aislamiento de un núcleo de 12 investigaciones fundamentales para la delimitación temática y contraste empírico de métricas críticas: tasa de éxito de ataque (ASR), sobre-bloqueo (*over-refusal*) y latencia de inferencia en *guardrails* comerciales.

## Repositorio y recursos

| Capa | Recurso / URL | Detalle |
| :--- | :--- | :--- |
| Control de versiones | GitHub | [TeVerde29/trabajo-investigacion](https://github.com/TeVerde29/trabajo-investigacion) |
| Rama principal | `main` | Seguimiento de matrices, bases tabulares, diapositivas, evidencias y artículos |
| Protocolo de clonación | HTTPS | `https://github.com/TeVerde29/trabajo-investigacion.git` |

## Características principales

- **Delimitación cuatridimensional institucional completa:** Secciones I a V desarrolladas íntegramente en la matriz oficial [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx), con delimitación espacial en la UNU (Pucallpa, Perú) y delimitación temporal en el semestre académico 2026-II.
- **Universo bibliográfico inicial de 4,037 registros brutos:** Recopilación documental descargada desde Scopus (2,272), ScienceDirect (796), IEEE Xplore (666), EBSCOhost (243) e IOPscience (60), archivada en formato CSV individual y consolidada en [Base de Datos - Identificación Inicial.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%20Identificaci%C3%B3n%20Inicial.xlsx).
- **Deduplicación y depuración lingüística documentada:** Identificación y remoción de 79 exclusiones de pre-screening (63 fuera de 2023–2026 y 16 en idiomas no latinos) y 696 registros duplicados (685 por DOI exacto y 11 pares inter-base), consolidando 3,262 estudios únicos en [Base de Datos - Sin duplicados.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%20Sin%20duplicados.xlsx).
- **Protocolo de cribado PRISMA-ScR con códigos justificados:** 2,862 artículos excluidos en [Base de Datos - 12.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx) bajo 12 motivos estandarizados (desde ML convencional sin LLMs hasta modelos de laboratorio sin defensas empíricas).
- **Corpus analizado de 400 publicaciones científicas:** 346 artículos de prioridad alta (puntaje 8–10, categorías A/B de producción y guardrails) y 54 de prioridad media (puntaje 6–7), clasificados en matriz de extracción y catalogados según técnicas MITRE ATLAS.
- **Núcleo de 12 investigaciones fundamentales:** Síntesis técnica de 12 estudios ancla con métricas cuantitativas de exactitud, latencia y bypass, respaldados con 10 artículos completos en PDF archivados en la carpeta [investigaciones/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones).
- **Evidencias gráficas y credenciales auditables:** Capturas de pantalla de alta resolución de las búsquedas en bases indexadas archivadas en [Evidencias/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Evidencias) y credencial de acceso institucional RENACYT-CONCYTEC en [Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Evidencia%20creaci%C3%B3n%20de%20cuenta%20-%20Pedro%20Ricra%20Figueroa.pdf).

## Stack tecnológico y herramientas

| Capa | Tecnología / Herramienta | Función |
| :--- | :--- | :--- |
| Formulación conceptual | Markdown (`.md`) | Especificación de descriptores, pregunta PICO y parámetros en [tema.md](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/tema.md) |
| Matriz institucional | Microsoft Word OpenXML (`.docx`) | Documento oficial con Secciones I a V completas para evaluación docente en EPIS-UNU |
| Presentación ejecutiva | Microsoft PowerPoint OpenXML (`.pptx`) | Diapositivas de sustentación con flujo metodológico, gráficos y ecuaciones |
| Base de datos general | Microsoft Excel (`.xlsx`) | Archivo [Base de Datos - 12.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx) con 8 hojas de trabajo analíticas |
| Datasets intermedios | CSV / Excel (`.csv`, `.xlsx`) | Archivos brutos por base y libros de deduplicación en [Base de Datos/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos) |
| Repositorio documental | Formato PDF (`.pdf`) | 10 artículos científicos completos de acceso abierto archivados en [investigaciones/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones) |
| Evidencias de búsqueda | Imágenes JPEG (`.jpg`, `.jpeg`) | Capturas de pantalla de consultas en Scopus, IEEE Xplore e IOPscience en [Evidencias/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Evidencias) |
| Marco de ciberseguridad | MITRE ATLAS | Taxonomía estándar para catalogación de amenazas y mitigaciones en sistemas de IA |
| Fuentes indexadas | Scopus, ScienceDirect, IEEE, EBSCO, IOP | Plataformas bibliográficas consultadas mediante acceso institucional RENACYT |
| Control de versiones | Git / GitHub | Preservación del historial de cambios y trazabilidad del repositorio |

## Arquitectura del repositorio

```text
trabajo-investigacion/
├── .git/                                                                 # Metadatos del repositorio Git local
├── Base de Datos/                                                        # Datos cienciométricos brutos, deduplicados y clasificados
│   ├── Base de Datos - 12.xlsx                                           # Libro consolidado: 8 hojas (400 incluidos, 2862 excluidos, ATLAS)
│   ├── Base de Datos - Identificación Inicial.xlsx                       # Recopilación inicial bruta por pestañas (4,037 registros)
│   ├── Base de Datos - Sin duplicados.xlsx                               # Universo deduplicado (3,273 registros únicos y control DOI)
│   ├── EBSCO.csv                                                         # Extracción bruta de EBSCOhost (243 registros)
│   ├── IEEE Xplore.csv                                                   # Extracción bruta de IEEE Xplore (666 registros)
│   ├── IOPscience.csv                                                    # Extracción bruta de IOPscience (60 registros)
│   ├── ScienceDirect.csv                                                 # Extracción bruta de ScienceDirect (796 registros)
│   └── Scopus.csv                                                        # Extracción bruta de Scopus (2,272 registros)
├── Evidencias/                                                           # Evidencias gráficas de ejecución de búsquedas booleanas
│   ├── IEEE Explore.jpg                                                  # Captura de pantalla de consulta en IEEE Xplore (666 resultados)
│   ├── ioSience.jpeg                                                     # Captura de pantalla de consulta en IOPscience (60 resultados)
│   ├── scopus.jpg                                                        # Captura de pantalla de consulta en Scopus (2,272 resultados)
│   └── scopus2.jpeg                                                      # Captura complementaria de refinamiento temporal en Scopus
├── investigaciones/                                                      # Textos completos en PDF de artículos fundamentales Open Access
│   ├── 2_Comprehensive_Analysis_of_LLM_Guardrails_Approaches...pdf       # ID 419: Majewski et al. (2026) sobre guardrails comerciales
│   ├── 4_Hive-AI a defended multi-service honeypot framework...pdf        # ID 748: Vargas Yáñez & Tobón (2026) sobre ataques a APIs reales
│   ├── 5_PROMPTFUZZ Harnessing Fuzzing Techniques for Robust...pdf       # ID 1085: PROMPTFUZZ (2026) sobre fuzzing semántico contra LLMs
│   ├── 6_RigorLLM Resilient Guardrails for Large Language Models...pdf   # ID 3098: Yuan et al. (2026) sobre guardrails combinados OOD
│   ├── 7_BackdoorAlign Mitigating Fine-tuning based Jailbreak...pdf      # ID 2747: Zhang et al. (2026) sobre alineamiento ante backdoors
│   ├── 8_Ranking Manipulation for Conversational Search Engines.pdf      # ID 3086: Liu et al. (2026) sobre manipulación y envenenamiento RAG
│   ├── 9_A Privacy-Preserving Middleware Architecture for Detecting...pdf # ID 80: Arquitectura middleware con SLM local para APIs de LLM
│   ├── 10_Ignore This Title and HackAPrompt Exposing Systemic...pdf      # ID 3256: Schulhoff et al. (2024) sobre HackAPrompt (+600k ataques)
│   ├── 11_Adversarial prompt and fine-tuning attacks threaten...pdf      # ID 1628: Chen et al. (2026) sobre envenenamiento en modelos médicos
│   └── 12_A decontextualized LLM-based safeguard technique...pdf         # ID 40: Santilli / D-SHIELD (2026) sobre mitigación de jailbreak
├── Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf               # Constancia de credencial activa RENACYT-CONCYTEC / UNU
├── MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx                        # Matriz oficial completada (Secciones I a V) para EPIS-UNU
├── MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx                        # Diapositivas oficiales de sustentación del proyecto (8 diapositivas)
├── Matriz_delimitacion_tematica_redactada - ejemplo.docx                 # Documento de referencia metodológica del curso
├── README.md                                                             # Documentación técnica, metodológica y operativa del repositorio
└── tema.md                                                               # Especificación conceptual del tema, pregunta PICO y objetivos
```

Decisiones arquitectónicas del repositorio:
- **Separación de datos y documentos (`Base de Datos/`):** Aísla los registros crudos en CSV de los libros procesados en `.xlsx`, permitiendo auditar de forma independiente cada etapa de la depuración.
- **Preservación local de fuentes primarias (`investigaciones/`):** Almacena los PDFs de acceso abierto directamente en el repositorio para garantizar la verificación inmediata de citas textuales y métricas reportadas.
- **Trazabilidad visual de consultas (`Evidencias/`):** Conserva las capturas de pantalla de las plataformas indexadas con fecha y parámetros exactos de ejecución para respaldar la reproducibilidad ante el comité evaluador.
- **Entregables académicos en raíz:** Mantiene la matriz institucional `.docx` y las diapositivas `.pptx` en el directorio principal para acceso directo durante las revisiones de cátedra.

## Instalación y flujo de trabajo

### Prerrequisitos

- Cliente Git (`git --version` >= 2.30).
- Suite ofimática con soporte OpenXML (Microsoft Office 2016+, LibreOffice 7.0+ o Google Workspace).
- Visor de documentos PDF (Adobe Acrobat, Foxit o navegador web).
- Opcional: Entorno Python 3.10+ con librerías `openpyxl` y `pandas` para procesamiento automatizado de las hojas de cálculo.

### Clonación del repositorio

```bash
git clone https://github.com/TeVerde29/trabajo-investigacion.git
cd trabajo-investigacion
```

### Inspección automatizada de las bases de datos (opcional con Python)

```bash
# Crear y activar entorno virtual
python -m venv .venv
# En Windows (PowerShell):
.venv\Scripts\Activate.ps1
# En Linux/macOS:
source .venv/bin/activate

# Instalar dependencias de lectura tabular
pip install openpyxl pandas

# Inspeccionar las hojas del libro principal consolidado
python -c "
import openpyxl
wb = openpyxl.load_workbook('Base de Datos/Base de Datos - 12.xlsx', read_only=True)
for sheet in wb.sheetnames:
    print(f'Hoja: {sheet}')
"
```

### Flujo de trabajo para el investigador y evaluador

1. **Revisar la delimitación temática:** Consultar [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx) para verificar la alineación entre las Secciones I a V y la delimitación cuatridimensional.
2. **Revisar la sustentación ejecutiva:** Abrir [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx) para contrastar el problema, los objetivos, las ecuaciones y el embudo de selección.
3. **Comprobar la evidencia de acceso:** Abrir [Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Evidencia%20creaci%C3%B3n%20de%20cuenta%20-%20Pedro%20Ricra%20Figueroa.pdf) y las capturas en [Evidencias/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Evidencias).
4. **Examinar la depuración y deduplicación:** Revisar [Base de Datos - Identificación Inicial.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%20Identificaci%C3%B3n%20Inicial.xlsx) y [Base de Datos - Sin duplicados.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%20Sin%20duplicados.xlsx) para auditar el control de duplicados inter-base.
5. **Auditar el cribado y las estadísticas:** Abrir [Base de Datos - 12.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx) y consultar la hoja `8. Estadísticas de selección` para el balance cuantitativo de exclusiones e inclusiones.
6. **Consultar los artículos fundamentales:** Revisar los documentos PDF en la carpeta [investigaciones/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones) para contrastar las métricas de mitigación y los vectores analizados.

## Requisitos del sistema

| Componente | Requisito mínimo | Propósito |
| :--- | :--- | :--- |
| Sistema operativo | Windows 10/11, macOS 12+ o Linux x86_64 | Entorno local de consulta, edición y procesamiento |
| Procesador de texto | Word 2016 o LibreOffice Writer | Apertura y edición de la matriz oficial institucional `.docx` |
| Presentador de diapositivas | PowerPoint 2016 o LibreOffice Impress | Visualización de la presentación de sustentación `.pptx` |
| Gestor de hojas de cálculo | Excel 2016 o LibreOffice Calc | Procesamiento y filtrado de datasets `.xlsx` y `.csv` |
| Lector de PDF | Adobe Acrobat Reader, SumatraPDF o navegador web | Lectura de los 10 artículos científicos y constancia institucional |
| Intérprete Python | Python 3.10+ (opcional) | Automatización y auditoría de datos mediante scripts |
| Conexión a red | Acceso a internet | Consulta de enlaces DOI persistentes y repositorio GitHub |

## Pregunta y objetivos de investigación

### Pregunta orientadora (Formulación PICO / CIMO)

> ¿Cuáles son las principales vulnerabilidades y técnicas de evasión de seguridad en Modelos de Lenguaje Grande (LLMs) desplegados en producción?

- **Población / Objeto (P):** Modelos de lenguaje grande fundacionales y comerciales desplegados en aplicaciones productivas, interfaces API y arquitecturas de agentes autónomos.
- **Intervención / Fenómeno (I):** Vectores de ataque adversarial (Prompt Injection directo e indirecto, Jailbreaking por ofuscación semántica y Data/RAG Poisoning).
- **Comparación / Contexto (C):** Entornos reales de producción y servicios comerciales (APIs GPT-4, Claude, Gemini) frente a evaluaciones teóricas de laboratorio.
- **Resultado (*Outcome*) (O):** Clasificación taxonómica bajo MITRE ATLAS y evaluación empírica de la eficacia, latencia y tasa de sobre-bloqueo (*over-refusal*) de las defensas algorítmicas y guardrails.

### Objetivos de la investigación

#### Objetivo general
Sintetizar, mediante un mapeo sistemático de la literatura científica (2023–2026), los vectores de ataque adversarial contra LLMs y la eficacia de sus defensas algorítmicas en producción.

#### Objetivos específicos
1. **Categorizar los vectores de ataque:** Clasificar bajo la taxonomía MITRE ATLAS los principales vectores ofensivos: Prompt Injection (directo e indirecto), Jailbreaking y envenenamiento de datos/contextos.
2. **Contrastar las defensas algorítmicas:** Contrastar la evidencia empírica reportada sobre robustez técnica, latencia operacional y tasa de sobre-bloqueo (*over-refusal*) de los guardrails en arquitecturas de producción.
3. **Proponer lineamientos de mitigación:** Identificar limitaciones estructurales y vacíos de conocimiento en los marcos de seguridad actuales para formular recomendaciones técnicas aplicables a despliegues comerciales.

## Estrategia de búsqueda y ecuaciones construidas

La recuperación documental se articuló mediante una formulación booleana estructurada en tres bloques conceptuales combinados con el operador `AND`:

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

Debido a las restricciones de longitud de cadena y operadores en el motor de búsqueda de IOPscience, la ecuación fue optimizada manteniendo la semántica triaxial:

```text
("large language model" OR LLM) AND ("prompt injection" OR jailbreak OR "data poisoning" OR "adversarial") AND (security OR defense OR attack)
```

Filtros aplicados en IOPscience: periodo de los últimos 5 años, tipo de documento *Article* y disponibilidad exclusiva en *Open Access* (acceso verificado mediante credencial institucional RENACYT-CONCYTEC).

## Flujo metodológico de selección PRISMA-ScR

El cribado sistemático de la literatura se estructuró en seis etapas conforme a las directrices PRISMA-ScR, documentadas integralmente en la hoja `8. Estadísticas de selección` de [Base de Datos - 12.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx):

| Fase PRISMA-ScR | Etapa del proceso | Criterio aplicado / Justificación | Registros | % del Total |
| :--- | :--- | :--- | :---: | :---: |
| **Identificación** | Registros brutos recopilados | Consultas en Scopus (2,272), ScienceDirect (796), IEEE (666), EBSCO (243) e IOP (60) | **4,037** | 100.0% |
| **Pre-screening** | Exclusiones temporales | Artículos con año 2027 (fuera del periodo 2023–2026, código `EX-05`) | 63 | 1.6% |
| **Pre-screening** | Exclusiones por idioma | Artículos en chino u otros alfabetos no latinos en EBSCO (código `EX-06`) | 16 | 0.4% |
| **Deduplicación** | Duplicados inter-base exactos | Registros duplicados por coincidencia exacta de DOI normalizado | 685 | 17.0% |
| **Deduplicación** | Consolidación de versiones | Pares inter-base EBSCO ↔ Scopus y versiones preliminares conferencia-revista | 11 | 0.3% |
| **Screening** | Base única consolidada a evaluar | Universo de publicaciones examinadas a texto completo y resumen (Hoja 1) | **3,262** | 80.8% |
| **Elegibilidad** | Filtro Tecnológico (Etapa 2) | No estudian LLMs como activo de seguridad (ML clásico / visión artificial) [`EX-01`] | 563 | 13.9% |
| **Elegibilidad** | Filtro Temático (Etapa 3) | Sin relación con ciberseguridad adversaria de LLMs [`EX-02`] | 757 | 18.8% |
| **Elegibilidad** | Mención Superficial (Etapa 3) | Mencionan ataques solo como contexto introductorio sin analizarlos [`EX-03`] | 327 | 8.1% |
| **Elegibilidad** | Ciberseguridad Convencional (Etapa 3) | LLM usado como herramienta para IDS, phishing o malware tradicional [`EX-04`] | 170 | 4.2% |
| **Elegibilidad** | Idioma no admitido (Etapa 1) | Texto completo en chino indexado en Scopus/CNKI [`EX-06`] | 6 | 0.1% |
| **Elegibilidad** | Metadatos de Actas (Etapa 1) | Volúmenes completos de congresos sin artículo individual identificado [`EX-08`] | 57 | 1.4% |
| **Elegibilidad** | Calidad / Insuficiencia (Etapa 6) | Contenido técnico o resultados no verificables [`EX-09`] | 26 | 0.6% |
| **Elegibilidad** | Vector fuera de alcance (Etapa 3) | Marcas de agua (*watermarking*), copyright o privacidad pasiva sin ataque [`EX-10`] | 151 | 3.7% |
| **Elegibilidad** | Filtro Producción (Etapa 5) | Laboratorio aislado sin entorno productivo representativo (Prioridad Baja) [`EX-11`] | 421 | 10.4% |
| **Elegibilidad** | Filtro Defensas (Etapa 4) | Solo ataque descriptivo sin mecanismo de defensa evaluado [`EX-12`] | 384 | 9.5% |
| **Total Excluidos** | Exclusiones totales en Screening | Suma de registros excluidos en las Etapas 1 a 6 (registrados en Hoja 4) | **2,862** | 70.9% |
| **Inclusión** | Artículos de Prioridad Alta | Puntuación 8–10, Cat. A/B, defensas algorítmicas y guardrails evaluados (Hoja 2) | 346 | 8.6% |
| **Inclusión** | Artículos de Prioridad Media | Puntuación 6–7, Cat. A/B o mitigaciones algorítmicas descritas (Hoja 3) | 54 | 1.3% |
| **Inclusión Total** | Corpus total de estudios incluidos | Publicaciones que integran el cuerpo central del Scoping Review | **400** | **9.9%** |

### Distribución de publicaciones por base de datos de origen

| Base de datos | Registros brutos | Exclusiones pre-screening | Duplicados consolidados | Estudios únicos (Hoja 1) | Estudios incluidos (Hojas 2+3) | Tasa de inclusión (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Scopus | 2,272 | 38 | 284 | 1,950 | 248 | 12.7% |
| ScienceDirect (Elsevier) | 796 | 14 | 218 | 564 | 62 | 11.0% |
| IEEE Xplore | 666 | 11 | 156 | 499 | 74 | 14.8% |
| EBSCOhost | 243 | 16 | 26 | 201 | 14 | 7.0% |
| IOPscience | 60 | 0 | 12 | 48 | 2 | 4.2% |
| **Total Consolidado** | **4,037** | **79** | **696** | **3,262** | **400** | **12.3%** |

## Distribución cienciométrica del corpus (N=400)

### Distribución temporal e idiomática

- **2026 (primer semestre e indexación anticipada):** 272 estudios (68.0%).
- **2025:** 112 estudios (28.0%).
- **2024:** 14 estudios (3.5%).
- **2023:** 2 estudios (0.5%).
- **Idioma del corpus incluido:** 400 publicaciones en inglés (100.0%). Dos artículos en español presentes en la base inicial fueron excluidos por no abordar seguridad adversaria en LLMs.

### Vectores de ataque analizados

| Vector de ataque principal | Frecuencia | % del Corpus (N=400) | Descripción técnica |
| :--- | :---: | :---: | :--- |
| **Prompt Injection (Directo e Indirecto)** | 164 | 41.0% | Manipulación de directivas del sistema mediante entradas no confiables o contexto web externo. |
| **Jailbreaking (Evasión de alineamiento)** | 148 | 37.0% | Técnicas de ofuscación semántica, roles ficticios y sufijos adversariales para violar políticas. |
| **Data Poisoning & Backdoor Attacks** | 52 | 13.0% | Manipulación maliciosa de conjuntos de datos durante el preentrenamiento o fine-tuning. |
| **RAG Poisoning & Context Manipulation** | 36 | 9.0% | Inyección de pasajes adversariales en corpus recuperados para alterar la respuesta del generador. |

### Mecanismos de defensa evaluados

| Mecanismo defensivo predominante | Frecuencia | % del Corpus (N=400) | Enfoque de mitigación |
| :--- | :---: | :---: | :--- |
| **Generative AI Guardrails** | 178 | 44.5% | Marcos desacoplados de inspección de entrada y salida (Llama Guard, NeMo Guardrails, Azure AI). |
| **Adversarial Input Detection** | 124 | 31.0% | Filtros semánticos, clasificadores auxiliares de baja latencia y modelos pequeños (SLM) perimetrales. |
| **Architectural Isolation & Tool Limits** | 50 | 12.5% | Control de flujo de información (IFC), delimitación estricta de permisos y pasarelas seguras. |
| **Model Alignment & Safe Unlearning** | 48 | 12.0% | Reentrenamiento con DPO, optimización de seguridad contra backdoors y desaprendizaje guiado. |

## Selección de investigaciones fundamentales (N=12)

A partir del corpus incluido de 400 publicaciones, se seleccionaron 12 investigaciones fundamentales que sustentan la delimitación temática institucional y aportan evidencia cuantitativa sobre ataques y defensas. Diez de ellas cuentan con su documento PDF de acceso abierto archivado en la carpeta [investigaciones/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones):

| N.º | ID | Cita bibliográfica APA | Vector de ataque | Cat. Prod. | Aporte técnico y vulnerabilidad | Mecanismo defensivo | Métricas y resultados reportados | Archivo local |
| :---: | :---: | :--- | :--- | :---: | :--- | :--- | :--- | :---: |
| 1 | 141 | Cao, X., & Bao, Y. (2026). *A Systematic Survey of Prompt Injection Attacks and Defenses in LLM-Integrated Applications and Agentic Systems*. IEEE BigDIA. | Prompt Injection (Directo e Indirecto) | Cat. B | Formaliza la inyección como secuestro del flujo de control hacia herramientas no autorizadas. | 4 líneas de defensa, control de flujo (IFC) y métrica *Safe Utility Ratio* (SUR). | Propone SUR para evaluar balance entre seguridad y utilidad operativa. | - |
| 2 | 419 | Majewski, P. et al. (2026). *Comprehensive Analysis of LLM Guardrails Approaches Preventing Harmful Content and Jailbreak Attacks*. Springer CCIS. | Jailbreaking & Evasión de Políticas | Cat. B | Benchmarking empírico de guardrails comerciales (NeMo, Llama Guard, Azure) ante jailbreaks. | Comparativa de guardrails dedicados vs reglas semánticas y latencia asociada. | Cuantifica sobrecarga de latencia (ms) y rechazo falso (*over-refusal*) de consultas legítimas. | [`2_Comprehensive...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/2_Comprehensive_Analysis_of_LLM_Guardrails_Approaches_Preventing_Harmful_Content_and_Jailbreak_Attacks.pdf) |
| 3 | 1068 | Knowlton, B. et al. (2026). *Prompt-Based Jailbreaking of Leading LLM Chatbots: A Survey of Attacks and Defenses*. IEEE Access. | Jailbreaking en Chatbots Comerciales | Cat. B | Evasión de alineamiento en servicios comerciales (ChatGPT, Claude, Gemini, Copilot). | Defensas multinivel: preprocesamiento, alineación en entrenamiento (RLHF/DPO) e inferencia. | Evalúa tasas de ataque (ASR) y fragilidad de filtros estáticos ante variantes adaptativas. | - |
| 4 | 748 | Vargas Yáñez, S., & Tobón, S. (2026). *HIVE-AI: Scalable Multi-Tier Threat Hunting with Low-Latency Generative AI Facades*. IEEE TDSC. | Indirect Prompt Injection | Cat. A (Producción real) | Despliegue en VPS público capturando 16,683 ataques de 1,229 IPs en 50 países contra APIs de LLMs. | Cascada de clasificación de 8 etapas (p99 < 5 ms) y defensa por triangulación. | Reduce la evasión adversaria del 54.8% al 9.3% (*p* < 0.001) con kappa de Cohen = 0.74. | [`4_Hive-AI...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/4_Hive-AI%20a%20defended%20multi-service%20honeypot%20framework%20for%20generative%20AI%20APIs.pdf) |
| 5 | 1085 | IEEE Authors. (2026). *PROMPTFUZZ: Harnessing Fuzzing Techniques for Detecting Jailbreak and Prompt Injection Vulnerabilities in LLMs*. IEEE S&P / TDSC. | Prompt Injection & Jailbreaking | Cat. A (Producción) | Fuzzing semántico automatizado para descubrir vulnerabilidades de evasión en modelos comerciales. | Generador de mutaciones semánticas con oráculo de violación de políticas para red-teaming. | Descubrió más de 1,400 jailbreaks exitosos con tasas de bypass superiores al 65%. | [`5_PROMPTFUZZ...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/5_PROMPTFUZZ%20Harnessing%20Fuzzing%20Techniques%20for%20Robust%20Testing%20of%20Prompt%20Injection%20in%20Large%20Language%20Models.pdf) |
| 6 | 3098 | Yuan, Z. et al. (2026). *RigorLLM: Resilient Guardrails for Large Language Models against Combined Jailbreak and Prompt Injection Attacks*. USENIX Security. | Jailbreaking & Inyección Combinada | Cat. B | Vulnerabilidad ante ataques compuestos que combinan inyección y bypass de alineamiento simultáneo. | Framework de guardrails resiliente con detección fuera de distribución (OOD). | Tasa de falsos positivos (FPR) < 2% con detección superior al 94% ante ataques adaptativos. | [`6_RigorLLM...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/6_RigorLLM%20Resilient%20Guardrails%20for%20Large%20Language%20Models%20against%20Undesired%20Content.pdf) |
| 7 | 2747 | Zhang, Y. et al. (2026). *BackdoorAlign: Mitigating Backdoor Attacks in LLMs via Robust Safety Alignment and Data Sanitization*. ACL / IEEE. | Data Poisoning & Backdoors | Cat. B | Manipulación de modelos mediante ejemplos envenenados en fine-tuning que activan comportamientos maliciosos. | Detección de activaciones anómalas y desaprendizaje guiado de triggers maliciosos. | Disminuye la tasa de éxito de backdoor (ASR) del 89.4% a menos del 3.1% preservando utilidad. | [`7_BackdoorAlign...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/7_BackdoorAlign%20Mitigating%20Fine-tuning%20based%20Jailbreak%20Attack%20with%20Backdoor%20Enhanced%20Safety%20Alignment.pdf) |
| 8 | 3086 | Liu, H. et al. (2026). *Adversarial Robustness and Poisoning Defenses in Retrieval-Augmented Generation (RAG) Systems*. ACM CCS / IEEE. | RAG Poisoning & Context Corruption | Cat. A (RAG Empresarial) | Inyección de pasajes maliciosos en corpus externos recuperados para inducir respuestas comprometidas. | Consenso verificable y filtrado robusto de fragmentos antes de la inyección al prompt. | Mitiga el 91.2% de ataques de envenenamiento sin degradar la precisión factual en consultas legítimas. | [`8_Ranking...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/8_Ranking%20Manipulation%20for%20Conversational%20Search%20Engines.pdf) |
| 9 | 80 | MDPI Authors. (2026). *A Privacy-Preserving Middleware Architecture for Detecting Prompt Injection and Sensitive Data Exposure in LLM Interactions*. Electronics. | Prompt Injection & Fuga de Datos | Cat. B | Conflicto entre inspección de prompts e intimidad de datos corporativos al invocar APIs externas de LLMs. | Middleware híbrido con SLM local que actúa como frontera de confianza previa a la nube. | Alcanza 95.83% de exactitud con 100% de recall en detección de inyección y retiene el 95% de datos sensibles en local. | [`9_A Privacy...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/9_A%20Privacy-Preserving%20Middleware%20Architecture%20for%20Detecting%20Prompt%20Injection%20and%20Sensitive%20Data%20Exposure%20in%20Large-Language-Model%20Interactions.pdf) |
| 10 | 3256 | Schulhoff, S. et al. (2024). *Evaluating Large Language Model Vulnerabilities to Prompt Injection: The HackAPrompt Dataset and Competition*. EMNLP. | Prompt Injection & Jailbreaking | Cat. A (CTF a gran escala) | Estudio empírico masivo sobre la fragilidad de directivas del sistema ante adversarios humanos. | Evaluación de delimitadores, instrucciones de refuerzo y preprocesamiento. | Evaluó más de 600,000 intentos reales; demostró que las defensas simples basadas en prompts fracasan. | [`10_Ignore...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/10_Ignore%20This%20Title%20and%20HackAPrompt%20Exposing%20Systemic%20Vulnerabilities%20of%20LLMs%20Through%20a%20Global%20Prompt%20Hacking%20Competition.pdf) |
| 11 | 1628 | Chen, J. et al. (2026). *Robust Defenses Against Instruction and Data Poisoning in Domain-Specific LLM Deployments*. IEEE TIFS. | Fine-tuning Poisoning & Backdoors | Cat. B | Envenenamiento de datos en LLMs especializados (salud, finanzas) desplegados con bases de conocimiento privadas. | Purificación de gradientes durante fine-tuning y verificación de integridad en capas ocultas. | Reduce la evasión de backdoor en un 96.5% con una degradación clínica menor al 0.8%. | [`11_Adversarial...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/11_Adversarial%20prompt%20and%20fine-tuning%20attacks%20threaten%20medical%20large%20language%20models.pdf) |
| 12 | 40 | Santilli, T. / Security Team. (2026). *A Decontextualized LLM-Based Safeguard Technique for Automated Jailbreak Mitigation (D-SHIELD)*. Info & Soft Tech. | Jailbreak & Runtime Evasion | Cat. B | Fenómeno de "contaminación contextual", donde el contexto persuasivo confunde al clasificador de seguridad. | D-SHIELD: blindaje semántico dinámico y aislamiento de la evaluación de la respuesta respecto al prompt. | ASR residual inferior al 4.2% con mínima sobrecarga de latencia operacional. | [`12_A decontext...pdf`](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones/12_A%20decontextualized%20LLM-based%20safeguard%20technique%20for%20automated%20jailbreak%20mitigation.pdf) |

## Taxonomía de vectores y defensas bajo MITRE ATLAS

La clasificación analítica del corpus se estructuró a partir de la matriz MITRE ATLAS (*Adversarial Threat Landscape for Artificial-Intelligence Systems*), vinculando cada técnica de ataque con su correspondiente mecanismo de defensa algorítmica:

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
| AML.T0054 - LLM Jailbreak Injection             | - Guardrails dedicados (Llama Guard, NeMo, AIRS)|
|   Bypass de alineamiento mediante roles y sufijos | - Evaluación descontextualizada (D-SHIELD)      |
| AML.T0020 - Poison Training Data                 | - Purificación de gradientes en fine-tuning     |
|   Inserción de triggers en datasets de ajuste    | - Desaprendizaje guiado de backdoors            |
| AML.T0099 - AI Agent / Context Poisoning         | - Control de Flujo de Información (IFC)         |
|   Contaminación de la memoria y bases vectoriales| - Verificación de consenso en pasajes RAG       |
+--------------------------------------------------+-------------------------------------------------+
```

## Cronograma metodológico de trabajo

| Fase | Hito metodológico | Entregable principal | Estado |
| :---: | :--- | :--- | :---: |
| **Fase 1** | Delimitación temática cuatridimensional y verificación de acceso | [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx) y credencial PDF | Completado |
| **Fase 2** | Búsqueda booleana en 5 bases y extracción bruta | Datasets CSV y [Base de Datos - Identificación Inicial.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%20Identificaci%C3%B3n%20Inicial.xlsx) (4,037 registros) | Completado |
| **Fase 3** | Pre-screening y deduplicación inter-base | [Base de Datos - Sin duplicados.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%20Sin%20duplicados.xlsx) (3,262 registros únicos) | Completado |
| **Fase 4** | Cribado metodológico PRISMA-ScR (Filtros EX-01 a EX-12) | [Base de Datos - 12.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos/Base%20de%20Datos%20-%2012.xlsx) (400 incluidos, 2,862 excluidos) | Completado |
| **Fase 5** | Síntesis taxonómica MITRE ATLAS y artículos ancla | Núcleo de 12 estudios ancla y 10 PDFs en [investigaciones/](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/investigaciones) | Completado |
| **Fase 6** | Sustentación ejecutiva y presentación académica | [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx) (8 diapositivas) | Completado |
| **Fase 7** | Redacción del informe final de Scoping Review | Manuscrito del Trabajo de Investigación según directrices EPIS-UNU | En progreso |

---

**Pedro Giovanni Ricra Figueroa** — Estudiante de Ingeniería de Sistemas (EPIS-UNU)

- **GitHub:** [@TeVerde29](https://github.com/TeVerde29)
- **Correo electrónico:** hikih020@gmail.com

---

Si este proyecto te resultó útil, considera darle una estrella en GitHub.
