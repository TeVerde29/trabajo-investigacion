# trabajo-investigacion — Mapeo Sistemático de Vulnerabilidades y Defensas en LLMs en Producción

> Repositorio de trabajo de investigación para el mapeo sistemático y categorización taxonómica bajo MITRE ATLAS de vectores de ataque y defensas algorítmicas en Modelos de Lenguaje Grande (LLMs) desplegados en entornos de producción.

[![Estado](https://img.shields.io/badge/Estado-Activo-success?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Tipo](https://img.shields.io/badge/Tipo-Scoping_Review-blue?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Línea](https://img.shields.io/badge/Línea-Ciberseguridad-red?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Institución](https://img.shields.io/badge/Institución-EPIS--UNU-003366?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Ciclo](https://img.shields.io/badge/Ciclo-X_(2026--II)-orange?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Periodo](https://img.shields.io/badge/Periodo-2023--2026-informational?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)

El tesista formula la delimitación temática, diseña las cadenas de búsqueda booleana y estructura la matriz de análisis documental; los docentes y revisores de la EPIS-UNU evalúan la pertinencia temática, el sustento en literatura científica indexada y la viabilidad metodológica del proyecto.

## Tabla de contenidos

- [Descripción](#descripción)
- [Repositorio y recursos](#repositorio-y-recursos)
- [Características principales](#características-principales)
- [Stack tecnológico y herramientas](#stack-tecnológico-y-herramientas)
- [Estructura del repositorio](#estructura-del-repositorio)
- [Instalación y flujo de trabajo](#instalación-y-flujo-de-trabajo)
- [Requisitos del sistema](#requisitos-del-sistema)
- [Pregunta y objetivos de investigación](#pregunta-y-objetivos-de-investigación)
- [Estrategia de búsqueda bibliográfica](#estrategia-de-búsqueda-bibliográfica)
- [Criterios de elegibilidad](#criterios-de-elegibilidad)
- [Taxonomía de vectores y defensas](#taxonomía-de-vectores-y-defensas)
- [Cronograma de trabajo](#cronograma-de-trabajo)
- [Autor](#autor)

## Descripción

La integración de modelos fundacionales y modelos de lenguaje grande (LLMs) en sistemas productivos introduce superficies de ataque no contempladas en las arquitecturas de software tradicionales. Incidentes como inyecciones de instrucciones (*prompt injection*), evasión de políticas de alineamiento (*jailbreaking*), envenenamiento de conjuntos de ajuste fino (*data poisoning*) y extracción de pesos o datos de entrenamiento comprometen la confidencialidad, integridad y disponibilidad de las aplicaciones conectadas a agentes o bases de datos vectoriales.

Este proyecto articula la etapa inicial y de delimitación formal para un mapeo sistemático de literatura (*Scoping Review*), enmarcado en el curso de Trabajo de Investigación del Ciclo X de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Nacional de Ucayali (EPIS-UNU). El trabajo centraliza los descriptores temáticos, las matrices cuatridimensionales de delimitación y las formulaciones booleanas para bases de datos indexadas.

Las decisiones de diseño metodológico contemplan:
1. Uso del marco de amenazas adversarias **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems) como estándar taxonómico para la clasificación de ataques.
2. Formulación de preguntas de investigación estructuradas bajo el esquema PICO/CIMO.
3. Ventana temporal acotada a publicaciones entre 2023 y 2026 para capturar avances post-despliegue masivo de arquitecturas basadas en Transformers.
4. Trazabilidad completa de la evidencia mediante matrices estandarizadas en documentos `.docx` y registros de búsqueda en texto plano estructurado en `tema.md`.

## Repositorio y recursos

| Componente | Recurso | Detalle |
| :--- | :--- | :--- |
| Control de versiones | GitHub | [TeVerde29/trabajo-investigacion](https://github.com/TeVerde29/trabajo-investigacion) |
| Rama principal | `main` | Rama de seguimiento de documentación y artefactos |
| Protocolo de clonación | HTTPS / SSH | `https://github.com/TeVerde29/trabajo-investigacion.git` |

## Características principales

- **Delimitación cuatridimensional validada:** Definición explícita de ejes temático-tecnológico, espacial, temporal (semestre 2026-II) y unidad de análisis en `MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - PEDRO GIOVANNI RICRA FIGUEROA.docx`.
- **Ecuación booleana triaxial para Scopus e IEEE:** Segmentación de términos en tres dimensiones lógicas: objeto de estudio (modelos generativos), superficie ofensiva (ataques/vulnerabilidades) y contramedidas (defensas/alineamiento).
- **Taxonomía orientada a MITRE ATLAS:** Mapeo de vectores de evasión y compromiso frente a defensas algorítmicas, guardrails de entrada/salida y técnicas de *safety alignment*.
- **Criterios de elegibilidad estandarizados:** Filtros de inclusión para artículos arbitrados por pares y revisiones empíricas en Scopus, IEEE Xplore, ScienceDirect, SciELO y EBSCO.
- **Trazabilidad de acreditación institucional:** Respaldo de acceso a bases de datos científicas registrado en `Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf`.

## Stack tecnológico y herramientas

| Capa | Herramienta / Estándar | Función |
| :--- | :--- | :--- |
| Especificación metodológica | Markdown (`.md`) | Redacción de palabras clave, operadores booleanos y diseño de scoping review en `tema.md` |
| Matriz institucional | Microsoft Word OpenXML (`.docx`) | Documentación formal de delimitación según plantilla oficial EPIS-UNU |
| Evidencia documental | Formato PDF | Comprobante institucional de cuenta y acceso a fuentes bibliográficas |
| Marco de ciberseguridad | MITRE ATLAS | Taxonomía para categorización de tácticas, técnicas y procedimientos (TTP) en IA |
| Bases de datos bibliográficas | Scopus, IEEE Xplore, SciELO, ScienceDirect, EBSCO | Fuentes de extracción de literatura científica arbitrada |
| Control de versiones | Git / GitHub | Historial de versiones y distribución del trabajo académico |

## Estructura del repositorio

```text
trabajo-investigacion/
├── .git/                                                                 # Metadatos del repositorio Git
├── Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf               # Respaldo de registro en base de datos científica
├── MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - original.docx     # Plantilla en blanco provista por la asignatura
├── MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - PEDRO GIOVANNI RICRA FIGUEROA.docx # Matriz de delimitación completada
├── Matriz_delimitacion_tematica_redactada - ejemplo.docx                 # Documento de referencia y formato muestra
├── README.md                                                             # Documentación técnica y metodológica principal
└── tema.md                                                               # Especificación técnica: PICO, keywords y Scopus
```

Decisiones sobre la estructura:
- Separación de la plantilla base (`... - original.docx`) y el documento de trabajo del estudiante (`... - PEDRO GIOVANNI RICRA FIGUEROA.docx`) para preservar el formato institucional.
- Archivo `tema.md` como fuente de verdad en texto plano editable para la construcción incremental de ecuaciones booleanas sin depender de procesadores de texto binarios.
- Archivo de evidencia en formato PDF para garantizar la inmutabilidad de las credenciales y registros requeridos por la cátedra.

## Instalación y flujo de trabajo

### Prerrequisitos

- Git instalado en el sistema (`git --version` >= 2.30).
- Procesador de texto compatible con formato `.docx` (Microsoft Word, LibreOffice Writer o Google Docs).
- Lector de archivos PDF.
- Editor de texto con soporte para Markdown (VS Code, Obsidian o Neovim).

### Obtención del repositorio

```bash
git clone https://github.com/TeVerde29/trabajo-investigacion.git
cd trabajo-investigacion
```

### Flujo metodológico de investigación

1. **Revisar la formulación inicial:** Consultar [tema.md](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/tema.md) para verificar la alineación entre la pregunta PICO/CIMO, el objetivo general y las dimensiones de estudio.
2. **Consultar la matriz institucional:** Abrir y editar [MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - PEDRO GIOVANNI RICRA FIGUEROA.docx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ%20DE%20DELIMITACI%C3%93N%20TEM%C3%81TICA%20DE%20INVESTIGACI%C3%93N%20-%20PEDRO%20GIOVANNI%20RICRA%20FIGUEROA.docx) para actualizar las secciones I a V.
3. **Ejecutar las ecuaciones booleanas:** Copiar las cadenas de búsqueda de [tema.md](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/tema.md) en Scopus o IEEE Xplore empleando los operadores `AND` y `OR`.
4. **Filtrar por criterios de elegibilidad:** Aplicar los límites de fecha (2023-2026), idioma (español e inglés) y tipo de documento (artículos de revista y actas de conferencia arbitradas).
5. **Extraer registros y bibliografía:** Exportar los metadatos en formato BibTeX o CSV para su posterior análisis taxonómico con MITRE ATLAS.

## Requisitos del sistema

| Componente | Requisito mínimo | Propósito |
| :--- | :--- | :--- |
| Sistema operativo | Windows 10/11, macOS 12+ o Linux (cualquier distribución) | Entorno de edición y gestión de archivos |
| Cliente Git | Git 2.30 o superior | Sincronización con el repositorio remoto |
| Suite ofimática | MS Word 2016+, LibreOffice 7.0+ o visor OpenXML | Apertura y edición de matrices `.docx` |
| Navegador web | Chrome, Firefox o Edge actualizado | Acceso a portales institucionales de Scopus e IEEE |
| Conexión a red | Acceso a internet con proxy/VPN institucional UNU | Descarga de artículos indexados sin muro de pago |

## Pregunta y objetivos de investigación

### Pregunta orientadora (Esquema PICO / CIMO)

> ¿Cuáles son las principales vulnerabilidades y técnicas de evasión de seguridad en Modelos de Lenguaje Grande (LLMs) desplegados en producción?

- **Población / Objeto (P):** Modelos de lenguaje grande desplegados en producción e integrados con sistemas externos.
- **Intervención / Fenómeno (I):** Vulnerabilidades emergentes (Prompt Injection, Jailbreaking, Data Poisoning, extracción de modelos).
- **Comparación / Contexto (C):** Entornos productivos frente a entornos de evaluación de laboratorio bajo marcos de mitigación.
- **Resultado (*Outcome*) (O):** Taxonomía de riesgos clasificada bajo MITRE ATLAS y efectividad de las defensas algorítmicas actuales.

### Objetivo general

Identificar y categorizar los vectores de ataque contra LLMs (Prompt Injection, Data Poisoning, Jailbreaking) y las defensas algorítmicas actuales documentadas en la literatura científica entre 2023 y 2026.

## Estrategia de búsqueda bibliográfica

La estrategia de recuperación de información divide el espacio léxico en tres bloques combinados con el operador booleano `AND`:

```text
(Bloque 1: Objeto de estudio) AND (Bloque 2: Ataques y vulnerabilidades) AND (Bloque 3: Defensas y marcos)
```

### Descriptores por bloque

```text
Bloque 1: Objeto de estudio
- "large language model*"
- LLM*
- "foundation model*"
- "generative AI"
- chatbot*

Bloque 2: Ataques y vulnerabilidades
- "prompt injection"
- jailbreak*
- "data poisoning"
- "adversarial attack*"
- "adversarial machine learning"
- "model extraction"
- "backdoor attack*"
- "training data extraction"

Bloque 3: Defensas y marcos de seguridad
- "LLM security"
- "AI red teaming"
- "red team*"
- defense*
- "MITRE ATLAS"
- guardrail*
- "safety alignment"
```

### Ecuación de búsqueda formulada para Scopus

```text
TITLE-ABS-KEY(
  ("large language model*" OR LLM* OR "foundation model*" OR "generative AI" OR chatbot*)
  AND
  ("prompt injection" OR jailbreak* OR "data poisoning" OR "adversarial attack*" OR "adversarial machine learning" OR "model extraction" OR "backdoor attack*" OR "training data extraction")
  AND
  ("LLM security" OR "AI red teaming" OR "red team*" OR defense* OR "MITRE ATLAS" OR guardrail* OR "safety alignment")
) AND PUBYEAR > 2022 AND PUBYEAR < 2027
```

## Criterios de elegibilidad

| Criterio | Inclusión | Exclusión |
| :--- | :--- | :--- |
| Periodo temporal | Publicaciones comprendidas entre 2023 y 2026 | Documentos publicados antes de 2023 |
| Idioma | Artículos técnicos en inglés y español | Trabajos redactados en otros idiomas |
| Tipo de documento | Artículos en revistas indexadas, *conference proceedings* arbitrados y preprints de alto impacto | Ensayos de opinión, notas de prensa o resúmenes sin metodología explícita |
| Eje temático | Ataques adversarios, evasiones, envenenamiento o defensas algorítmicas en LLMs | Estudios de procesamiento de lenguaje natural ajenos a seguridad o ciberseguridad |
| Acceso al contenido | Documentos con acceso al texto completo a través de suscripción institucional o acceso abierto | Publicaciones inaccesibles con solo lectura de resumen |

## Taxonomía de vectores y defensas

```text
+-----------------------------------------------------------------------------------+
|                        SEGURIDAD EN LLMS EN PRODUCCIÓN                           |
+-----------------------------------------+-----------------------------------------+
|           Vectores de Ataque            |          Defensas Algorítmicas          |
|              (MITRE ATLAS)              |             y Mitigaciones              |
+-----------------------------------------+-----------------------------------------+
| - Inyección de prompts (directa/indirecta)| - Filtros de sanitización de prompts    |
| - Evasión de restricciones (Jailbreaking) | - Alineamiento de seguridad (RLHF/DPO)  |
| - Envenenamiento de datos (Data Poisoning)| - Detección de anomalías en embeddings  |
| - Ataques de puertas traseras (Backdoors) | - Mecanismos de Guardrails en tiempo real|
| - Extracción de datos de entrenamiento    | - Evaluación con AI Red Teaming         |
| - Inferencia y robo de pesos del modelo   | - Aislamiento contextual y sandboxing   |
+-----------------------------------------+-----------------------------------------+
```

## Cronograma de trabajo

| Fase | Hito metodológico | Entregable |
| :---: | :--- | :--- |
| 1 | Delimitación temática cuatridimensional y registro de cuenta | `tema.md` y `MATRIZ DE DELIMITACIÓN...docx` |
| 2 | Ejecución de búsquedas bibliográficas y descarte por título/abstract | Matriz de cribado Prisma/Scoping |
| 3 | Extracción de datos y clasificación taxonómica con MITRE ATLAS | Base tabular de vectores y defensas |
| 4 | Análisis comparativo de efectividad de defensas algorítmicas | Capítulo de resultados y discusión |
| 5 | Consolidación del informe final de Trabajo de Investigación | Documento de tesis preliminar |

---

**Pedro Giovanni Ricra Figueroa** — Estudiante de Ingeniería de Sistemas (EPIS-UNU)

- **GitHub:** [@TeVerde29](https://github.com/TeVerde29)
- **Correo electrónico:** hikih020@gmail.com

---

Si este proyecto te resultó útil, considera darle una estrella en GitHub.
