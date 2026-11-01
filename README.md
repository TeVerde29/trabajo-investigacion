# trabajo-investigacion — Revisión Sistemática de Ataques y Defensas en LLMs en Producción bajo MITRE ATLAS (2023–2026)

> Repositorio académico y metodológico para el desarrollo de la investigación sobre vectores de ataque (Prompt Injection, Jailbreaking, Data Poisoning) y defensas algorítmicas en Modelos de Lenguaje Grande desplegados en producción.

[![Estado](https://img.shields.io/badge/Estado-Activo-success?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Tipo](https://img.shields.io/badge/Tipo-Scoping_Review-blue?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Línea](https://img.shields.io/badge/Línea-Ciberseguridad-red?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Institución](https://img.shields.io/badge/Institución-EPIS--UNU-003366?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Ciclo](https://img.shields.io/badge/Ciclo-X_(2026--II)-orange?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)
[![Muestra](https://img.shields.io/badge/Registros_Únicos-484-brightgreen?style=flat-square)](https://github.com/TeVerde29/trabajo-investigacion)

El tesista formula la delimitación temática cuatridimensional, ejecuta las ecuaciones booleanas en bases de datos indexadas y consolida la base de datos de publicaciones científicas; los docentes y revisores de la EPIS-UNU evalúan la pertinencia temática en ciberseguridad, la viabilidad metodológica y el sustento bibliográfico de la propuesta.

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
- [Fuentes científicas de soporte](#fuentes-científicas-de-soporte)
- [Criterios de elegibilidad](#criterios-de-elegibilidad)
- [Taxonomía de vectores y defensas MITRE ATLAS](#taxonomía-de-vectores-y-defensas-mitre-atlas)
- [Cronograma de trabajo](#cronograma-de-trabajo)
- [Autor](#autor)

## Descripción

La integración de modelos de lenguaje grande (LLMs) y arquitecturas de agentes autónomos en aplicaciones productivas introduce riesgos de seguridad críticos que la ciberseguridad perimetral tradicional no puede resolver. A diferencia del software convencional, estos modelos procesan tanto las instrucciones de control del sistema como las entradas de usuarios y fuentes externas a través de un mismo canal de texto en lenguaje natural. Esta característica facilita que usuarios malintencionados ejecuten manipulaciones como la inyección de órdenes (*prompt injection* directo e indirecto), el salto de filtros de seguridad (*jailbreaking*) o el envenenamiento de conjuntos de datos (*data poisoning*).

Este repositorio centraliza los artefactos de delimitación y la base de datos documental del proyecto de fin de carrera en la asignatura Trabajo de Investigación (Ciclo X) de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Nacional de Ucayali (EPIS-UNU). El trabajo formaliza la matriz cuatridimensional institucional en `MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - PEDRO GIOVANNI RICRA FIGUEROA.docx`, la formulación sintáctica de palabras clave en `tema.md` y el acervo de artículos científicos recuperados en `Nuevo Hoja de cálculo de Microsoft Excel.xlsx`.

Las decisiones clave del diseño metodológico comprenden:
1. Adopción del estándar **MITRE ATLAS** (*Adversarial Threat Landscape for Artificial-Intelligence Systems*) como marco taxonómico para clasificar las técnicas adversarias documentadas.
2. Formulación de una ecuación booleana triaxial común probada y ejecutada en tres bases de datos indexadas: Scopus, IEEE Xplore y EBSCO Host.
3. Ventana temporal acotada a publicaciones comprendidas entre 2023 y 2026, capturando el periodo de despliegue real de modelos generativos en producción.
4. Protocolo estricto de depuración con exclusión lingüística y eliminación sistemática de duplicados entre bases, consolidando un universo de 484 registros únicos.

## Repositorio y recursos

| Componente | Recurso | Detalle |
| :--- | :--- | :--- |
| Control de versiones | GitHub | [TeVerde29/trabajo-investigacion](https://github.com/TeVerde29/trabajo-investigacion) |
| Rama principal | `main` | Seguimiento de matrices, datos tabulares y especificaciones |
| Protocolo de clonación | HTTPS / SSH | `https://github.com/TeVerde29/trabajo-investigacion.git` |

## Características principales

- **Delimitación formal completa:** Secciones I a V desarrolladas íntegramente en la matriz institucional, con delimitación espacial en la UNU (Pucallpa) y temporal en el semestre 2026-II.
- **Universo bibliográfico de 484 registros únicos:** Dataset depurado a partir de 567 registros iniciales de Scopus (470), IEEE Xplore (29) y EBSCO Host (68).
- **Control de duplicados inter-base:** Identificación y remoción de 82 duplicados (25 en IEEE y 57 en EBSCO) tomando Scopus como base primaria.
- **Filtrado por criterio lingüístico:** Exclusión de 1 publicación en idioma ucraniano en EBSCO Host por incumplimiento del criterio de inclusión (inglés/español).
- **Sustento en literatura indexada reciente:** Selección de tres revisiones de alto impacto (2026) en conferencias y revistas IEEE/Scopus directamente vinculadas al tema.
- **Validación de autoevaluación:** Cumplimiento verificado de los cuatro criterios de la lista de cotejo de la Sección V para revisión docente.

## Stack tecnológico y herramientas

| Capa | Herramienta / Estándar | Función |
| :--- | :--- | :--- |
| Formulación de búsqueda | Markdown (`.md`) | Documentación de descriptores, pregunta PICO y parámetros en `tema.md` |
| Matriz institucional | Microsoft Word OpenXML (`.docx`) | Documento oficial con las Secciones I a V completas para revisión académica |
| Gestión y depuración de datos | Microsoft Excel (`.xlsx`) | Base de datos con metadatos de las publicaciones en 3 hojas: Scopus, IEEE y EBSCO HOST |
| Respaldo de acceso institucional | Documento PDF | Comprobante de cuenta en bases de datos científicas acreditadas |
| Marco de ciberseguridad | MITRE ATLAS | Taxonomía estándar para clasificación de amenazas y vectores de ataque en IA |
| Fuentes de literatura científica | Scopus, IEEE Xplore, EBSCO Host | Plataformas de recuperación de artículos y revisiones por pares |
| Control de versiones | Git / GitHub | Trazabilidad del repositorio y preservación de cambios |

## Estructura del repositorio

```text
trabajo-investigacion/
├── .git/                                                                 # Metadatos del repositorio Git local
├── Evidencia creación de cuenta - Pedro Ricra Figueroa.pdf               # Respaldo institucional de cuenta en base de datos
├── MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - original.docx     # Formato en blanco provisto por la cátedra EPIS-UNU
├── MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - PEDRO GIOVANNI RICRA FIGUEROA.docx # Matriz completada (Secciones I a V)
├── Matriz_delimitacion_tematica_redactada - ejemplo.docx                 # Documento de referencia metodológica del curso
├── Nuevo Hoja de cálculo de Microsoft Excel.xlsx                        # Dataset de publicaciones (Scopus, IEEE, EBSCO)
├── README.md                                                             # Documentación técnica, metodológica y operativa
└── tema.md                                                               # Esquema base: eje temático, PICO y objetivos
```

Decisiones sobre la estructura:
- `MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - PEDRO GIOVANNI RICRA FIGUEROA.docx` contiene la versión de trabajo del estudiante preservando la plantilla original intacta en el archivo `... - original.docx`.
- `Nuevo Hoja de cálculo de Microsoft Excel.xlsx` almacena las descargas bibliográficas sin alterar los identificadores ni los enlaces de origen de cada base.
- `tema.md` actúa como archivo de configuración conceptual de rápida lectura para alinear la pregunta PICO y los objetivos.

## Instalación y flujo de trabajo

### Prerrequisitos

- Git instalado en el sistema (`git --version` >= 2.30).
- Suite ofimática compatible con `.docx` y `.xlsx` (Microsoft Office 2016+, LibreOffice 7.0+ o Google Docs/Sheets).
- Lector de documentos PDF.
- Editor de texto plano para Markdown (VS Code, Cursor o Neovim).

### Obtención del repositorio

```bash
git clone https://github.com/TeVerde29/trabajo-investigacion.git
cd trabajo-investigacion
```

### Flujo metodológico de investigación

1. **Revisar la matriz temática:** Abrir [MATRIZ DE DELIMITACIÓN TEMÁTICA DE INVESTIGACIÓN - PEDRO GIOVANNI RICRA FIGUEROA.docx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/MATRIZ%20DE%20DELIMITACI%C3%93N%20TEM%C3%81TICA%20DE%20INVESTIGACI%C3%93N%20-%20PEDRO%20GIOVANNI%20RICRA%20FIGUEROA.docx) para verificar la coherencia entre las Secciones I a V.
2. **Consultar la base de datos de publicaciones:** Abrir [Nuevo Hoja de cálculo de Microsoft Excel.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Nuevo%20Hoja%20de%20c%C3%A1lculo%20de%20Microsoft%20Excel.xlsx) para examinar los registros organizados en las hojas `Scopus`, `IEEE` y `EBSCO HOST`.
3. **Fase de cribado por título y resumen (*screening*):** Evaluar los 484 registros únicos contra los criterios de elegibilidad definidos.
4. **Clasificación bajo MITRE ATLAS:** Mapear cada artículo aceptado según la táctica adversaria abordada (ej. *Execution*, *Persistence*, *Defense Evasion*) y el tipo de defensa propuesta.
5. **Síntesis y redacción:** Consolidar los resultados en el informe formal de revisión sistemática para el curso.

## Requisitos del sistema

| Componente | Requisito mínimo | Propósito |
| :--- | :--- | :--- |
| Sistema operativo | Windows 10/11, macOS 12+ o Linux x86_64 | Entorno local de edición y análisis |
| Cliente Git | Git 2.30 o superior | Control de versiones y sincronización con GitHub |
| Procesador de texto | Word 2016 o LibreOffice Writer | Edición de la matriz oficial `.docx` |
| Hoja de cálculo | Excel 2016 o LibreOffice Calc | Procesamiento de metadatos en `Nuevo Hoja de cálculo...xlsx` |
| Conexión a red | Acceso a internet con cuenta institucional UNU | Consulta y verificación de enlaces persistentes y DOIs |

## Pregunta y objetivos de investigación

### Pregunta orientadora (Formulación PICO / CIMO)

> ¿Cuáles son las principales vulnerabilidades y técnicas de evasión de seguridad en Modelos de Lenguaje Grande (LLMs) desplegados en producción?

- **Población / Objeto (P):** Modelos de lenguaje grande desplegados en sistemas reales y agentes autónomos.
- **Intervención / Fenómeno (I):** Vulnerabilidades y vectores de ataque (Prompt Injection, Jailbreaking, Data Poisoning).
- **Comparación / Contexto (C):** Entornos productivos frente a evaluaciones sintéticas de laboratorio bajo marcos de mitigación.
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

El proceso de extracción y limpieza documental ejecutado en [Nuevo Hoja de cálculo de Microsoft Excel.xlsx](file:///c:/Users/hikih/Documents/Repositorios/trabajo-investigacion/Nuevo%20Hoja%20de%20c%C3%A1lculo%20de%20Microsoft%20Excel.xlsx) arrojó las siguientes métricas para el diagrama de flujo metodológico:

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
  [ Muestra final de registros únicos para cribado: 484 ]
  ├── Provenientes de Scopus: 470
  ├── Aportes únicos de EBSCO HOST: 10
  └── Aportes únicos de IEEE Xplore: 4
```

### Artículos únicos aportados por IEEE Xplore (4 registros conservados)
1. *Adversarial Machine Learning: A 20-Year Survey of Attacks, Defenses, and Standards* (Fila 13)
2. *TraceRouter++: Causal Semantic Routing Realignment via Optimal Transport* (Fila 15)
3. *Are Large Language Models Trained Fairly Across Demographic Categories?* (Fila 17)
4. *PromptGuard: Soft Prompt-Guided Unsafe Content Moderation for Text-to-Image Models* (Fila 28)

### Artículos únicos aportados por EBSCO HOST (10 registros conservados)
1. *Can LLMs Have a Fever? Investigating the Effects of Temperature on LLM Security* (Fila 2)
2. *Securing Retrieval-Augmented Generation Pipelines: A Comprehensive Framework* (Fila 4)
3. *Anthropic unveils new framework to block harmful content from AI models* (Fila 5)
4. *Can LLMs deeply detect complex malicious queries? A framework for jailbreaking via obfuscating intent* (Fila 6)
5. *How 'dark LLMs' produce harmful outputs, despite guardrails* (Fila 7)
6. *NETSKOPE UNVEILS NETSKOPE ONE AI SECURITY, DELIVERING HIGH-PERFORMANCE PROTECTION...* (Fila 20)
7. *Securing Enterprise Data for LLM-Powered Applications: A Reference Architecture...* (Fila 24)
8. *Copilot 'SearchLeak' Attack Allows 1-Click Data Theft* (Fila 31)
9. *Europe's Multilingual Reality Exposes AI Security Gaps* (Fila 36)
10. *Paired response final divergence signatures of jailbreak vulnerability in large language models* (Fila 47)

## Fuentes científicas de soporte

Artículos clave indexados (2026) incorporados en la Sección IV de la matriz de delimitación:

| N° | Cita Bibliográfica (Estilo APA 7ma ed.) | Base de Datos | Aporte Principal al Tema Delimitado |
| :---: | :--- | :---: | :--- |
| 1 | Cao, X., & Bao, Y. (2026). A systematic survey of prompt injection attacks and defenses in LLM-integrated applications and agentic systems. *Proceedings of the 2026 International Conference on Big Data and Information Analytics (BigDIA)*, 11684636. https://doi.org/10.1109/BigDIA71496.2026.11684636 | Scopus / IEEE Xplore *(Fila 183)* | Revisión sistemática sobre inyección de prompts en agentes conectados; formaliza cómo los datos se convierten en instrucciones de ejecución y clasifica defensas en tiempo de inferencia. |
| 2 | Majewski, P., Marczak, K., Dubicka, N., Podolak, J., & Szczuko, P. (2026). Comprehensive analysis of LLM guardrails approaches preventing harmful content and jailbreak attacks. *IEEE Access*, 14, 105214–105230. https://doi.org/10.1109/ACCESS.2026.3690365 | Scopus / IEEE Access *(Fila 247)* | Análisis comparativo y empírico de las principales arquitecturas de *guardrails* (como NeMo y Llama Guard) para la mitigación activa de ataques de *jailbreak*. |
| 3 | Knowlton, B., Campa, J., Gallo, D. S., Dajani, K., & Alzahrani, A. (2026). Prompt-based jailbreaking of leading LLM chatbots: A survey of attacks and defenses. *IEEE Transactions on Artificial Intelligence*, 7(1), 112–129. https://doi.org/10.1109/TAI.2026.3665656 | Scopus / IEEE Xplore *(Fila 34)* | Analiza y categoriza las técnicas de persuasión y ofuscación semántica utilizadas para evadir el alineamiento (*safety alignment*) en modelos comerciales desplegados. |

## Criterios de elegibilidad

| Criterio | Inclusión | Exclusión |
| :--- | :--- | :--- |
| Periodo temporal | Publicaciones comprendidas entre 2023 y 2026 | Documentos anteriores a 2023 |
| Idioma | Artículos en inglés o español | Publicaciones redactadas en otros idiomas (ej. ucraniano) |
| Tipo de documento | Artículos de revista arbitrados, actas de conferencia (*proceedings*) y revisiones sistemáticas | Ensayos de divulgación, notas de prensa o resúmenes sin metodología |
| Eje temático | Seguridad ofensiva, vulnerabilidades adversarias o defensas algorítmicas en LLMs | Trabajos de procesamiento de lenguaje natural ajenos a ciberseguridad |
| Acceso al contenido | Disponibilidad de texto completo vía suscripción institucional o acceso abierto | Registros con únicamente resumen disponible |

## Taxonomía de vectores y defensas MITRE ATLAS

```text
+-----------------------------------------------------------------------------------+
|                        SEGURIDAD EN LLMS EN PRODUCCIÓN                           |
+-----------------------------------------+-----------------------------------------+
|           Vectores de Ataque            |          Defensas Algorítmicas          |
|              (MITRE ATLAS)              |             y Mitigaciones              |
+-----------------------------------------+-----------------------------------------+
| - Inyección de prompts (directa/indirecta)| - Filtros de sanitización perimetral    |
| - Evasión de restricciones (Jailbreaking) | - Alineamiento de seguridad (RLHF/DPO)  |
| - Envenenamiento de datos (Data Poisoning)| - Detección de anomalías en embeddings  |
| - Ataques de puertas traseras (Backdoors) | - Guardrails semánticos en tiempo real  |
| - Extracción de datos de entrenamiento    | - Evaluación continua con Red Teaming   |
| - Inferencia y robo de pesos del modelo   | - Aislamiento de privilegios en agentes |
+-----------------------------------------+-----------------------------------------+
```

## Cronograma de trabajo

| Fase | Hito metodológico | Entregable |
| :---: | :--- | :--- |
| 1 | Delimitación temática cuatridimensional y evidencia de acceso | `MATRIZ...PEDRO GIOVANNI RICRA FIGUEROA.docx` y PDF de cuenta |
| 2 | Búsqueda booleana, depuración lingüística y deduplicación | Base consolidada en `Nuevo Hoja de cálculo...xlsx` (484 registros) |
| 3 | Cribado por título y resumen (*screening*) según criterios | Matriz de selección documental |
| 4 | Extracción de datos y mapeo taxonómico con MITRE ATLAS | Tabla comparativa de vectores y defensas |
| 5 | Redacción de resultados, discusión y conclusiones | Informe final de Trabajo de Investigación |

---

**Pedro Giovanni Ricra Figueroa** — Estudiante de Ingeniería de Sistemas (EPIS-UNU)

- **GitHub:** [@TeVerde29](https://github.com/TeVerde29)
- **Correo electrónico:** hikih020@gmail.com

---

Si este proyecto te resultó útil, considera darle una estrella en GitHub.
