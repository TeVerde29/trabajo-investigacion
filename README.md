# trabajo-investigacion — Revisión Sistemática de Ataques y Defensas en LLMs en Producción bajo MITRE ATLAS (2023–2026)

> Repositorio académico y metodológico para el desarrollo del mapeo sistemático (scoping review) sobre vectores de evasión (Prompt Injection, Jailbreaking, Data Poisoning) y defensas algorítmicas en Modelos de Lenguaje Grande desplegados en producción.

[![Estado](https://img.shields.io/badge/Estado-Activo-success?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Tipo](https://img.shields.io/badge/Tipo-Scoping_Review-blue?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Línea](https://img.shields.io/badge/Línea-Ciberseguridad-red?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Institución](https://img.shields.io/badge/Institución-EPIS--UNU-003366?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Ciclo](https://img.shields.io/badge/Ciclo-X_(2026--II)-orange?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Muestra Inicial](https://img.shields.io/badge/Muestra_Inicial-484_registros-informational?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Muestra Final](https://img.shields.io/badge/Muestra_Final-56_conservados-brightgreen?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)

El tesista formula la delimitación temática cuatridimensional, ejecuta las ecuaciones booleanas en bases de datos indexadas, audita el cribado metodológico y clasifica la muestra documental bajo el estándar MITRE ATLAS; los docentes y revisores de la EPIS-UNU evalúan la pertinencia temática en ciberseguridad, la reproducibilidad del protocolo de filtrado y el sustento bibliográfico del proyecto.

## Tabla de contenidos

- [Descripción](#descripción)
- [Repositorio y recursos](#repositorio-y-recursos)
- [Características principales](#características-principales)
- [Stack tecnológico y herramientas](#stack-tecnológico-y-herramientas)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Instalación y flujo de trabajo](#instalación-y-flujo-de-trabajo)
- [Requisitos del sistema](#requisitos-del-sistema)
- [Pregunta y objetivos de investigación](#pregunta-y-objetivos-de-investigación)
- [Estrategia de búsqueda y ecuación construida](#estrategia-de-búsqueda-y-ecuación-construida)
- [Métricas de recuperación y depuración de datos](#métricas-de-recuperación-y-depuración-de-datos)
- [Embudo de cribado metodológico (Filtros F0 a F12)](#embudo-de-cribado-metodológico-filtros-f0-a-f12)
- [Muestra final de registros conservados (N=56)](#muestra-final-de-registros-conservados-n56)
- [Fuentes científicas de soporte](#fuentes-científicas-de-soporte)
- [Taxonomía de vectores y defensas MITRE ATLAS](#taxonomía-de-vectores-y-defensas-mitre-atlas)
- [Cronograma de trabajo](#cronograma-de-trabajo)
- [Autor](#autor)

## Descripción

La integración de modelos de lenguaje grande (LLMs) y arquitecturas de agentes autónomos en entornos productivos introduce riesgos de seguridad críticos que la ciberseguridad perimetral tradicional no puede mitigar. A diferencia del software convencional, estos modelos procesan directivas de control del sistema y entradas no confiables de usuarios a través del mismo canal en lenguaje natural, facilitando manipulaciones como la inyección de prompts (*prompt injection* directo e indirecto), la evasión de filtros de seguridad (*jailbreaking*) y el envenenamiento de datos o contextos de recuperación (*data poisoning* / RAG poisoning).

Este repositorio centraliza los artefactos de delimitación, la base de datos documental y los pipelines de cribado sistemático del proyecto de fin de carrera en la asignatura Trabajo de Investigación (Ciclo X) de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Nacional de Ucayali (EPIS-UNU). El trabajo formaliza la matriz cuatridimensional institucional en `MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx`, los parámetros conceptuales en `tema.md`, la base general de 484 registros en `Base de Datos.xlsx` y la muestra depurada en `Registros_Conservados_56_LLM.xlsx`.

Las decisiones clave del diseño metodológico comprenden:
1. Adopción del estándar **MITRE ATLAS** (*Adversarial Threat Landscape for Artificial-Intelligence Systems*) como marco taxonómico para estructurar ataques y defensas.
2. Formulación de una ecuación booleana triaxial común probada y ejecutada en tres bases de datos indexadas: Scopus, IEEE Xplore y EBSCO Host.
3. Ventana temporal acotada a publicaciones comprendidas entre 2023 y 2026, capturando el despliegue empírico de modelos fundacionales en producción.
4. Protocolo estricto de cribado auditable paso a paso (F0 a F12), con verificación directa de acceso web, evaluación empírica de mitigaciones y aislamiento de modelos comerciales (APIs GPT-4, Claude, Gemini, ChatGPT).

## Repositorio y recursos

| Componente | Recurso | Detalle |
| :--- | :--- | :--- |
| Control de versiones | GitHub | [TeVerde29/trabajo-investigacion](https://github.com/TeVerde29/trabajo-investigacion) |
| Rama principal | `main` | Seguimiento de matrices, scripts de cribado, datos tabulares y reportes |
| Protocolo de clonación | HTTPS / SSH | `https://github.com/TeVerde29/trabajo-investigacion.git` |

## Características principales

- **Delimitación formal completa:** Secciones I a V desarrolladas íntegramente en la matriz institucional, con delimitación espacial en la UNU (Pucallpa) y temporal en el semestre 2026-II.
- **Universo bibliográfico de 484 registros únicos:** Dataset depurado a partir de 567 registros iniciales de Scopus (470), IEEE Xplore (29) y EBSCO Host (68), tras remover 82 duplicados inter-base y 1 registro en ucraniano.
- **Cribado metodológico auditable (F0–F12):** Pipeline automatizado y reproducible en Python (`scripts_cribado/`) con registro de estado HTTP para cada DOI y extracción de citas textuales de respaldo (≤ 15 palabras).
- **Muestra final conservada de 56 publicaciones:** 56 artículos y actas indexadas en Scopus que superan simultáneamente los criterios de acceso abierto, modalidad de texto, vector central, co-ocurrencia de ataque/defensa y contexto productivo/comercial.
- **Identificación de casos para revisión manual:** 2 registros aislados bajo la Regla G (Scopus ID 128 sobre robótica física vs. simulación; IEEE Xplore ID 4 sobre disparidad demográfica y equidad) para dictamen cualitativo.
- **Libro de trabajo formateado bajo Design Ricra:** Hoja de cálculo `Registros_Conservados_56_LLM.xlsx` con paleta institucional *Tea Green*, filtros automáticos, hipervínculos DOI y resúmenes completos.

## Stack tecnológico y herramientas

| Capa | Herramienta / Estándar | Función |
| :--- | :--- | :--- |
| Formulación conceptual | Markdown (`.md`) | Documentación de descriptores, pregunta PICO y parámetros en `tema.md` |
| Matriz institucional | Microsoft Word OpenXML (`.docx`) | Documento oficial con Secciones I a V completas para revisión académica UNU |
| Base de datos general | Microsoft Excel (`.xlsx`) | Archivo `Base de Datos.xlsx` con 484 registros en 3 hojas: Scopus, IEEE y EBSCO HOST |
| Base de datos conservada | Microsoft Excel (`.xlsx`) | Archivo `Registros_Conservados_56_LLM.xlsx` con 56 publicaciones seleccionadas y métricas |
| Pipeline de cribado | Python 3.11 (`openpyxl`, `requests`) | Scripts reproducibles en `scripts_cribado/` para auditoría HTTP y filtrado sistemático |
| Marco de ciberseguridad | MITRE ATLAS | Taxonomía estándar para clasificación de amenazas y vectores de ataque en IA |
| Fuentes científicas | Scopus, IEEE Xplore, EBSCO Host | Plataformas de recuperación de literatura científica indexada |
| Control de versiones | Git / GitHub | Trazabilidad del repositorio y preservación de cambios |

## Estructura del repositorio

```text
trabajo-investigacion/
├── .git/                                                                 # Metadatos del repositorio Git local
├── Base de Datos.xlsx                                                    # Dataset original con 484 registros (Scopus, IEEE, EBSCO)
├── Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf               # Respaldo institucional de cuenta en bases acreditadas
├── MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx                        # Matriz oficial completada (Secciones I a V)
├── Matriz_delimitacion_tematica_redactada - ejemplo.docx                 # Documento de referencia metodológica del curso
├── README.md                                                             # Documentación técnica, metodológica y operativa del repositorio
├── Registros_Conservados_56_LLM.xlsx                                     # Dataset final depurado con los 56 registros conservados
├── scripts_cribado/                                                      # Pipeline reproducible y logs de auditoría sistemática
│   ├── access_log.json                                                   # Registro de estados HTTP de acceso a los 484 enlaces/DOIs
│   ├── candidates_f4.json                                                # 225 registros preseleccionados que alcanzaron el filtro F4
│   ├── classify_deep.py                                                  # Motor de clasificación según vectores, defensas y producción
│   ├── cribado_sistematico_completo.md                                   # Informe de auditoría exhaustiva con log de 484 registros
│   ├── final_conserved.json                                              # Datos estructurados de las 56 publicaciones conservadas
│   ├── full_audit_log.json                                               # Log completo registro por registro (decisiones y citas)
│   ├── generate_excel.py                                                 # Generador del libro Excel con estilo visual Tea Green
│   └── run_access_check_all.py                                           # Script concurrente de auditoría de enlaces y verificación HTTP
└── tema.md                                                               # Esquema base: eje temático, pregunta PICO y objetivos
```

Decisiones sobre la estructura:
- `Base de Datos.xlsx` preserva la base original sin alterar identificadores ni metadatos originales de descarga.
- `Registros_Conservados_56_LLM.xlsx` centraliza la muestra documental final con campos normalizados para el análisis cienciométrico.
- `scripts_cribado/` aísla los scripts y artefactos de cómputo para mantener la raíz del repositorio limpia y enfocada en los entregables académicos.
- `tema.md` actúa como archivo de configuración conceptual de rápida lectura para alinear la pregunta PICO y los objetivos.

## Instalación y flujo de trabajo

### Prerrequisitos

- Git instalado en el sistema (`git --version` >= 2.30).
- Python 3.10 o superior (para ejecutar los scripts de auditoría y análisis en `scripts_cribado/`).
- Dependencias de Python: `openpyxl`, `requests`, `beautifulsoup4`.
- Suite ofimática compatible con `.docx` y `.xlsx` (Microsoft Office 2016+, LibreOffice 7.0+ o Google Docs/Sheets).
- Lector de documentos PDF.

### Obtención del repositorio

```bash
git clone https://github.com/TeVerde29/trabajo-investigacion.git
cd trabajo-investigacion
```

### Ejecución de los scripts de cribado (opcional)

Para reproducir la auditoría de accesos HTTP y la generación de la hoja de cálculo de registros conservados:

```bash
# Instalar dependencias requeridas
pip install openpyxl requests beautifulsoup4

# Ejecutar el generador del Excel de registros conservados
cd scripts_cribado
python generate_excel.py
```

### Flujo metodológico de investigación

1. **Revisar la matriz temática:** Abrir [MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx) para verificar la coherencia entre las Secciones I a V.
2. **Consultar la base general:** Abrir [Base de Datos.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Base%20de%20Datos.xlsx) para examinar los 484 registros en las hojas `Scopus`, `IEEE` y `EBSCO HOST`.
3. **Auditar el cribado sistemático:** Consultar [cribado_sistematico_completo.md](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/scripts_cribado/cribado_sistematico_completo.md) para verificar el log de decisiones por registro.
4. **Examinar la muestra conservada:** Abrir [Registros_Conservados_56_LLM.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Registros_Conservados_56_LLM.xlsx) con los 56 artículos categorizados bajo MITRE ATLAS.
5. **Síntesis y redacción:** Consolidar los resultados en el informe formal de revisión sistemática para la cátedra EPIS-UNU.

## Requisitos del sistema

| Componente | Requisito mínimo | Propósito |
| :--- | :--- | :--- |
| Sistema operativo | Windows 10/11, macOS 12+ o Linux x86_64 | Entorno local de edición, análisis y ejecución de scripts |
| Cliente Git | Git 2.30 o superior | Control de versiones y sincronización con GitHub |
| Intérprete Python | Python 3.10+ | Ejecución de pipelines de auditoría y análisis documental |
| Procesador de texto | Word 2016 o LibreOffice Writer | Edición de la matriz oficial `.docx` |
| Hoja de cálculo | Excel 2016 o LibreOffice Calc | Procesamiento de metadatos en `.xlsx` |
| Conexión a red | Acceso a internet | Verificación de enlaces persistentes, DOIs y catálogos MITRE ATLAS |

## Pregunta y objetivos de investigación

### Pregunta orientadora (Formulación PICO / CIMO)

> ¿Cuáles son las principales vulnerabilidades y técnicas de evasión de seguridad en Modelos de Lenguaje Grande (LLMs) desplegados en producción?

- **Población / Objeto (P):** Modelos de lenguaje grande desplegados en sistemas comerciales, APIs y agentes autónomos.
- **Intervención / Fenómeno (I):** Vulnerabilidades y vectores de ataque (Prompt Injection, Jailbreaking, Data Poisoning).
- **Comparación / Contexto (C):** Entornos de producción y APIs comerciales frente a evaluaciones teóricas de laboratorio.
- **Resultado (*Outcome*) (O):** Clasificación taxonómica bajo MITRE ATLAS y evaluación de la efectividad de las defensas algorítmicas.

### Objetivo general

Identificar y categorizar los vectores de ataque contra LLMs (Prompt Injection, Data Poisoning, Jailbreaking) y las defensas algorítmicas actuales documentadas en la literatura científica publicada entre 2023 y 2026.

## Estrategia de búsqueda y ecuación construida

La recuperación de literatura se estructura en tres bloques combinados con el operador lógico `AND`:

```text
("large language model*" OR "LLM*" OR "foundation model*") 
AND 
("prompt injection" OR "jailbreak*" OR "data poisoning" OR "adversarial attack*") 
AND 
("LLM security" OR "guardrail*" OR "safety alignment" OR "MITRE ATLAS")
```

### Descriptores especializados consignados en la matriz

* **Español:** Ciberseguridad; modelos de lenguaje grande; modelos fundacionales; inyección de prompts; evasión de restricciones (jailbreak); envenenamiento de datos; aprendizaje automático adversario; defensas algorítmicas; alineamiento de seguridad; MITRE ATLAS.
* **Inglés (IEEE / UNESCO):** Cybersecurity; large language models; foundation models; prompt injection; jailbreak; data poisoning; adversarial machine learning; algorithmic defenses; safety alignment; AI red teaming; guardrails; MITRE ATLAS.
* **Operadores utilizados:** `AND` para intersección de conceptos, `OR` para sinónimos y variantes, asterisco (`*`) para capturar derivaciones morfológicas.

## Métricas de recuperación y depuración de datos

El proceso de extracción documental inicial arrojó las siguientes métricas de depuración entre bases:

```text
  [ Registros brutos descargados: 567 ]
  ├── Scopus: 470
  ├── EBSCO HOST: 68
  └── IEEE Xplore: 29
               │
               ▼
  [ Filtrado por idioma ] ──> Exclusión de 1 registro en ucraniano (EBSCO HOST, fila 68)
               │
               ▼
  [ Registros en inglés/español: 566 ]
               │
               ▼
  [ Control de duplicados ] ──> Remoción de 82 duplicados
  ├── IEEE duplicados con Scopus: 25
  ├── EBSCO duplicados con Scopus: 40
  └── EBSCO duplicados internos: 17
               │
               ▼
  [ Muestra consolidada para cribado: 484 ]
  ├── Provenientes de Scopus: 470
  ├── Aportes únicos de EBSCO HOST: 10
  └── Aportes únicos de IEEE Xplore: 4
```

## Embudo de cribado metodológico (Filtros F0 a F12)

La evaluación sistemática de los 484 registros sobre los criterios de elegibilidad y delimitación temática arrojó las siguientes transiciones de inclusión y exclusión:

| Filtro | Etapa Metodológica | Entran | Salen | Excluidos | Razón Principal de Exclusión |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **F0** | Base de partida inicial | 484 | 484 | 0 | Verificación inicial de universo completo (Scopus: 470, IEEE: 4, EBSCO: 10). |
| **F1** | Duplicados inter-base | 484 | 484 | 0 | Control por DOI y título normalizado (0 duplicados encontrados). |
| **F2** | Tipo de documento y periodo (2023–2026) | 484 | 474 | 10 | 4 capítulos de libro y 1 nota en Scopus; 5 noticias/comunicados en EBSCO HOST. |
| **F3** | Libre acceso (Open Access / CC BY) | 474 | 225 | 249 | 247 registros Scopus sin Open Access; 2 registros IEEE con licencia cerrada no-CCBY. |
| **F4** | Alcance temático general | 225 | 222 | 3 | Trabajos pedagógicos/educativos o encuestas generales de IA no centradas en LLMs. |
| **F5** | Objeto de estudio LLM | 222 | 184 | 38 | El LLM actúa como herramienta secundaria y no como activo atacado/defendido. |
| **F6** | Vector central (Injection/Jailbreak/Poisoning) | 184 | 163 | 21 | Vectores no prioritarios (fuga pasiva, sesgo sin ataque, perturbaciones léxicas). |
| **F7** | Modalidad exclusiva de texto | 163 | 146 | 17 | Modelos multimodales (VLM, MLLM, audio, imagen, visión-lenguaje). |
| **F8** | LLM como objeto de estudio (re-verificación) | 146 | 146 | 0 | Confirmación explícita de objeto LLM / agente / RAG bajo ataque. |
| **F9** | Co-ocurrencia de ataque y defensa | 146 | 134 | 12 | Estudios que describen ataques sin mitigación o defensas sin ataque sobre LLM. |
| **F10** | Contexto de producción | 134 | 58 | 76 | Evaluación exclusiva en modelos base locales de laboratorio sin APIs comerciales. |
| **F11** | Evaluación empírica de defensa | 58 | 56 | 2* | 29 con medición empírica ('Sí'), 27 cualitativos ('No / parcial'); *2 pasan a Revisión Manual. |
| **F12** | Mapeo taxonómico MITRE ATLAS | 56 | 56 | 0 | Clasificación en técnicas oficiales AML.T0051, AML.T0054, AML.T0020 y AML.T0099. |

### Registros derivados a Revisión Manual (Regla G)

- **Scopus ID 128:** *Jailbreaking LLM-Controlled Robots* — Evalúa vectores de jailbreak en robots gobernados por LLMs; requiere dictamen sobre si el entorno corresponde a un despliegue productivo físico o simulador de laboratorio.
- **IEEE Xplore ID 4:** *Are Large Language Models Trained Fairly Across Demographic Categories?* — Evalúa empíricamente jailbreaks (*translation-distraction*) contra modelos comerciales (Claude Haiku) y propone políticas de sistema, pero su encuadre central aborda equidad y disparidad demográfica.

## Muestra final de registros conservados (N=56)

Los 56 artículos conservados se encuentran consolidados con metadatos completos, resúmenes y citas en [Registros_Conservados_56_LLM.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Registros_Conservados_56_LLM.xlsx). La distribución analítica de la muestra es la siguiente:

### Distribución por vector de ataque
- **Jailbreaking:** 33 publicaciones (58.9%) — Foco en evasión de alineamiento (*safety alignment bypass*), ofuscación semántica y manipulación de roles.
- **Prompt Injection:** 19 publicaciones (33.9%) — Inyecciones directas a nivel de prompt e indirectas a través de fuentes externas en agentes y RAG.
- **Vectores híbridos (Prompt Injection / Jailbreaking):** 1 publicación (1.8%).
- **Vectores híbridos (Prompt Injection / Data Poisoning):** 2 publicaciones (3.6%).
- **Data Poisoning (PoisonedRAG):** 1 publicación (1.8%) — Envenenamiento de bases de conocimiento recuperadas en tiempo de inferencia.

### Distribución por técnicas MITRE ATLAS
- **`AML.T0054` (LLM Jailbreak Injection):** 34 publicaciones.
- **`AML.T0051.000` (LLM Prompt Injection: Direct):** 11 publicaciones.
- **`AML.T0051.001` (LLM Prompt Injection: Indirect):** 8 publicaciones.
- **`AML.T0099` (AI Agent / Context Data Poisoning):** 3 publicaciones.

## Fuentes científicas de soporte

Artículos clave indexados (2026) incorporados en la Sección IV de la matriz de delimitación e integrados en la muestra conservada final:

| N° | Cita Bibliográfica (Estilo APA 7ma ed.) | Base de Datos | Aporte Principal al Tema Delimitado |
| :---: | :--- | :---: | :--- |
| 1 | Cao, X., & Bao, Y. (2026). A systematic survey of prompt injection attacks and defenses in LLM-integrated applications and agentic systems. *Proceedings of the 2026 International Conference on Big Data and Information Analytics (BigDIA)*, 11684636. https://doi.org/10.1109/BigDIA71496.2026.11684636 | Scopus *(Fila 184)* | Revisión sistemática sobre inyección de prompts en agentes conectados; formaliza cómo los datos se convierten en instrucciones de ejecución y clasifica defensas en tiempo de inferencia. |
| 2 | Majewski, P., Marczak, K., Dubicka, N., Podolak, J., & Szczuko, P. (2026). Comprehensive analysis of LLM guardrails approaches preventing harmful content and jailbreak attacks. *IEEE Access*, 14, 105214–105230. https://doi.org/10.1109/ACCESS.2026.3690365 | Scopus / IEEE Access *(Fila 248)* | Análisis comparativo y empírico de las principales arquitecturas de *guardrails* (como NeMo y Llama Guard) para la mitigación activa de ataques de *jailbreak*. |
| 3 | Knowlton, B., Campa, J., Gallo, D. S., Dajani, K., & Alzahrani, A. (2026). Prompt-based jailbreaking of leading LLM chatbots: A survey of attacks and defenses. *IEEE Transactions on Artificial Intelligence*, 7(1), 112–129. https://doi.org/10.1109/TAI.2026.3665656 | Scopus *(Fila 34)* | Analiza y categoriza las técnicas de persuasión y ofuscación semántica utilizadas para evadir el alineamiento (*safety alignment*) en modelos comerciales desplegados. |

## Taxonomía de vectores y defensas MITRE ATLAS

```text
+-----------------------------------------------------------------------------------+
|                        SEGURIDAD EN LLMS EN PRODUCCIÓN                           |
+-----------------------------------------+-----------------------------------------+
|           Vectores de Ataque            |          Defensas Algorítmicas          |
|              (MITRE ATLAS)              |             y Mitigaciones              |
+-----------------------------------------+-----------------------------------------+
| - AML.T0051.000: Prompt Injection Direct | - Sanitización y filtrado de prompts    |
| - AML.T0051.001: Prompt Injection Indir. | - Optimización de preferencias (DPO)    |
| - AML.T0054: LLM Jailbreak Injection    | - Guardrails semánticos en tiempo real  |
| - AML.T0099: AI Agent / Context Poison. | - Aislamiento de privilegios en agentes |
| - AML.T0020: Training Data Poisoning    | - Verificación formal de robustez       |
| - Evasión por ofuscación sintáctica     | - Detección por divergencia latente     |
+-----------------------------------------+-----------------------------------------+
```

## Cronograma de trabajo

| Fase | Hito metodológico | Entregable |
| :---: | :--- | :--- |
| 1 | Delimitación temática cuatridimensional y evidencia de acceso | `MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx` y PDF de cuenta |
| 2 | Búsqueda booleana, depuración lingüística y deduplicación | Base consolidada en `Base de Datos.xlsx` (484 registros) |
| 3 | Cribado sistemático estricto y auditoría HTTP | Muestra conservada en `Registros_Conservados_56_LLM.xlsx` (56 registros) |
| 4 | Mapeo taxonómico MITRE ATLAS y síntesis de defensas | Tabla comparativa de vectores (`AML.T0051`, `AML.T0054`, etc.) |
| 5 | Redacción de resultados, discusión y conclusiones | Informe final de Trabajo de Investigación |

---

**Pedro Giovanni Ricra Figueroa** — Estudiante de Ingeniería de Sistemas (EPIS-UNU)

- **GitHub:** [@TeVerde29](https://github.com/TeVerde29)
- **Correo electrónico:** hikih020@gmail.com

---

Si este proyecto te resultó útil, considera darle una estrella en GitHub.
