---
title: "PRJ - Delimitación Temática y Matriz Institucional (EPIS-UNU)"
aliases:
  - "Matriz de Delimitación"
  - "PRJ - Delimitación Temática y Matriz Institucional"
  - "PRJ - Delimitación Temática y Matriz Institucional de Investigación"
  - "Vulnerabilidades, técnicas de evasión y defensas algorítmicas en LLMs"
  - "PRJ - Delimitación Temática y Matriz Institucional"
tags:
  - project
  - investigacion
  - tesis
  - ciberseguridad
  - llm
  - mitre-atlas
  - scoping-review
  - epis-unu
type: project
area: "Trabajo de Investigación"
status: completed
priority: critical
start_date: 2026-08-15
due_date: 2026-11-15
next_action: "Sustentar la matriz formalmente ante el comité docente de la EPIS-UNU"
created: 2026-08-15
updated: 2026-11-09
author: "Pedro Giovanni Ricra Figueroa"
asignatura: "Trabajo de Investigación"
ciclo: "X (2026-II)"
linea: "Ciberseguridad"
institucion: "Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)"
---

# 📑 PRJ: Delimitación Temática Cuatridimensional y Matriz Institucional

> [!abstract] Resumen Ejecutivo del Proyecto
> **Resultado Buscado:** Formalización, validación y aprobación de la delimitación temática cuatridimensional y la matriz de investigación oficial (Secciones I a V) conforme a los estándares de la Escuela Profesional de Ingeniería de Sistemas de la UNU.
> **Estado:** ✅ Aprobado / Delimitado.

---

# Vulnerabilidades, técnicas de evasión y defensas algorítmicas en Modelos de Lenguaje Grande (LLMs) desplegados en producción: un Mapeo Sistemático de la literatura científica (2023–2026)

> [!info] Ficha Académica del Proyecto
> - **Asignatura:** Trabajo de Investigación
> - **Ciclo Académico:** X (2026-II)
> - **Línea de Investigación:** Ciberseguridad
> - **Tesista:** Pedro Giovanni Ricra Figueroa
> - **Institución:** Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)

---

## SECCIÓN I: Datos Generales e Identificación Preliminar

| Campo | Registro del Estudiante |
| :--- | :--- |
| **Área / Dominio Tecnológico:** | Ciberseguridad, Inteligencia Artificial, Seguridad Ofensiva en Modelos de Lenguaje Grande (LLMs), Adversarial Machine Learning (AML). |
| **Idea Inicial de Investigación:** | Desarrollar un Mapeo Sistemático de la literatura (*Scoping Review*) para categorizar taxonómicamente bajo MITRE ATLAS los principales vectores de ataque adversarial contra Modelos de Lenguaje Grande (Prompt Injection directo e indirecto, Jailbreaking y envenenamiento de datos). Asimismo, sintetizar y contrastar de manera comparativa la evidencia empírica reportada sobre la robustez técnica, latencia operacional y tasa de sobre-bloqueo (*over-refusal*) de los mecanismos de defensa algorítmica y guardrails en arquitecturas de producción, identificando limitaciones estructurales y vacíos de conocimiento para proponer lineamientos de mitigación. |

---

## SECCIÓN II: Matriz de Búsqueda Exploratoria de Literatura Científica

| Componente | Detalle de la Estrategia Aplicada |
| :--- | :--- |
| **Tesauros y Descriptores Especializados:** | **Español:**<br>Ciberseguridad; Modelos de Lenguaje Grande (LLM); Inyección de Prompts; Evasión de Seguridad; Jailbreaking; Envenenamiento de Datos; Aprendizaje Automático Adversarial; Guardrails de Seguridad; Generación Aumentada por Recuperación (RAG); Equipos Rojos de IA (AI Red Teaming).<br><br>**Inglés (IEEE / UNESCO):**<br>Cybersecurity; Large Language Models; Prompt Injection; Adversarial Prompting; Jailbreak Attacks; Data Poisoning; Adversarial Machine Learning; LLM Guardrails; Retrieval-Augmented Generation Security; AI Red Teaming; Input Detection; Runtime Safety Alignment. |
| **Operadores Booleanos:** | `AND`, `OR` |
| **Bases de Datos Consultadas:** | - [x] Scopus<br>- [x] IEEE Xplore<br>- [x] ScienceDirect<br>- [x] IOP Science<br>- [x] EBSCOhost |

### Ecuación de Búsqueda Construida

```text
("large language model*" OR LLM OR LLMs OR "foundation model*") 
AND ("prompt injection" OR jailbreak* OR "data poisoning" OR "adversarial machine learning" OR "AI red teaming") 
AND ("LLM security" OR "language model security" OR vulnerab* OR attack* OR evasion OR defense OR defence OR mitigation OR detection OR guardrails)
```

### Criterios de Elegibilidad Inicial

> [!check] Criterios de Inclusión
> 1. Investigaciones empíricas, teóricas y revisiones sistemáticas cuyo objeto central de estudio sean los Modelos de Lenguaje Grande (LLMs), agentes basados en LLMs o sistemas RAG.
> 2. Publicaciones comprendidas en el periodo 2023–2026 en idioma español o inglés.
> 3. Estudios enfocados en vectores de ataque adversariales (Prompt Injection, Jailbreaking, Data/RAG Poisoning) y/o en el desarrollo y evaluación de defensas algorítmicas (Guardrails, detección de entrada/salida, alineación en tiempo de ejecución).
> 4. Disponibilidad de texto completo en Acceso Abierto (*Open Access*) para garantizar la auditoría, trazabilidad y reproducibilidad del estudio.

> [!fail] Criterios de Exclusión
> 1. Estudios de aprendizaje automático (*Machine Learning*) o aprendizaje profundo convencional que no aborden LLMs o modelos fundacionales.
> 2. Investigaciones de ciberseguridad tradicional (redes, criptografía, firewalls de red perimetral) sin relación con el procesamiento de lenguaje natural o modelos generativos.
> 3. Registros correspondientes a metadatos de actas o portadas completas de conferencias sin aporte de investigación individual.
> 4. Documentos duplicados entre bases de datos o versiones preliminares superadas por la publicación definitiva.

### Resultados Obtenidos en el Cribado Inicial

- **Identificación inicial:** 4,037 registros totales en las 5 bases consultadas:
  - Scopus: 2,272
  - ScienceDirect: 796
  - IEEE Xplore: 666
  - EBSCOhost: 243
  - IOPscience: 60
- **Filtro de pre-screening:** Se excluyen 63 registros fuera del periodo 2023–2026 y 16 en idiomas distintos a inglés/español $\rightarrow$ **3,958 registros elegibles**.
- **Deduplicación:** Se eliminan 685 registros duplicados inter-base por coincidencia de DOI/título normalizado $\rightarrow$ **3,273 publicaciones únicas consolidadas**.
- **Cribado temático:** Tras el análisis de pertinencia sobre LLMs en producción y guardrails de seguridad, se preseleccionaron 12 artículos clave.
- **Criterio de acceso y muestra ancla:** Se excluyen 2 publicaciones por restricción de suscripción (no Open Access), consolidando una muestra final de **10 investigaciones ancla a texto completo**.

---

## SECCIÓN III: Matriz de Delimitación Cuatridimensional

| Dimensión de Delimitación | Pregunta Guía | Definición Específica del Proyecto |
| :--- | :--- | :--- |
| **1. Delimitación Temática y Tecnológica** | ¿Qué tecnología, estándar, modelo o algoritmo específico se investiga y qué variable afecta? | **Tecnología / Marco:**<br>Modelos de Lenguaje Grande fundacionales y de código abierto, marcos de guardrails de producción (Llama Guard, NeMo Guardrails, AWS Guardrails, Azure AI Content Safety, RigorLLM, D-SHIELD) y taxonomías de amenazas MITRE ATLAS (*Adversarial Threat Landscape for Artificial-Intelligence Systems*).<br><br>**Objeto de estudio:**<br>Resiliencia y eficacia defensiva de los mecanismos de mitigación algorítmica frente a técnicas avanzadas de evasión (inyección directa/indirecta de prompts, sufijos adversariales optimizados como GCG/AutoDAN, envenenamiento de reentrenamiento y manipulación contextual en RAG). |
| **2. Delimitación Espacial** | ¿En qué institución, empresa, entorno o ámbito geográfico concreto se desarrollará el estudio? | **Institución / Entorno:** Entorno de investigación científica y revisión sistemática en ciberseguridad, utilizando literatura indexada en bases de datos científicas internacionales (Scopus, IEEE Xplore, ScienceDirect, EBSCO, IOPscience).<br><br>**Ubicación:** Escuela Profesional de Ingeniería de Sistemas (EPIS) de la Universidad Nacional de Ucayali, Pucallpa, provincia de Coronel Portillo, departamento de Ucayali, Perú (Campus Universitario UNU, Carretera Federico Basadre Km 6.200). |
| **3. Delimitación Temporal** | ¿En qué periodo académico o intervalo de tiempo se ejecutarán las mediciones o recolección de datos? | **Periodo de estudio:** Semestre 2026-II / Año 2026. |
| **4. Unidad de Análisis / Población** | ¿Sobre qué elementos (procesos, activos de información, usuarios, código fuente) se aplicará la investigación? | **Unidad de análisis:** El artículo científico primario arbitrado e indexado que reporta hallazgos teóricos o evidencia empírica cuantitativa sobre vectores de ataque adversarial (Prompt Injection, Jailbreaking, Data Poisoning) y/o mecanismos de defensa algorítmica (guardrails, detección perimetral, alineación) en Modelos de Lenguaje Grande.<br><br>**Población objetivo:** La totalidad de artículos científicos sobre seguridad ofensiva y defensiva de LLMs publicados en el periodo 2023–2026 indexados en Scopus, IEEE Xplore, ScienceDirect, EBSCO e IOPscience con disponibilidad de texto completo en acceso abierto. |

---

## SECCIÓN IV: Formulación y Sustentación con Literatura Científica

### 1. Título Preliminar Delimitado

> [!quote] Título Oficial de la Investigación
> **Vulnerabilidades, técnicas de evasión y defensas algorítmicas en Modelos de Lenguaje Grande (LLMs) desplegados en producción: un Mapeo Sistemático de la literatura científica (2023–2026).**

### 2. Definición Preliminar del Problema y Vacío de Conocimiento

El despliegue a gran escala de Modelos de Lenguaje Grande (LLMs) en aplicaciones comerciales y sistemas agénticos ha expuesto debilidades críticas en el plano semántico que eluden las defensas perimetrales tradicionales de ciberseguridad. A diferencia del software determinista, los LLMs procesan instrucciones y datos no confiables en un mismo canal semántico plano, lo que habilita vectores de explotación como *Prompt Injection*, *Jailbreaking* adversarial y manipulación de contextos mediante *RAG Poisoning*.

Aunque la industria ha propuesto mecanismos de defensa como guardrails desacoplados (NeMo, Llama Guard, AWS Guardrails) y técnicas de alineación por reentrenamiento, la literatura reciente evidencia fallas estructurales:
- **Majewski et al. (2026)** demostraron que los guardrails líderes en la nube presentan una tasa de sobre-bloqueo (*over-refusal*) significativa y son vulnerables a sufijos adversariales transferibles.
- **Santilli (2026)** identificó el fenómeno de la "contaminación contextual", donde los clasificadores de seguridad son burlados por la propia persuasión del prompt malicioso cuando analizan el historial conversacional.
- Evaluaciones a escala global como **HackAPrompt (Schulhoff et al., 2023)** y **HIVE-AI (Vargas Yáñez & Tobón, 2026)** confirmaron que los atacantes logran evadir defensas entre un 54.8% y un 75.3% de las veces mediante mutaciones semánticas y técnicas de inyección indirecta no contempladas en entornos cerrados de laboratorio.

> [!important] Vacío de Conocimiento Identificado
> Radica en la dispersión metodológica y la ausencia de una síntesis taxonómica estandarizada bajo marcos como **MITRE ATLAS** que contraste la robustez técnica de las defensas frente a su sobrecosto operacional (latencia transaccional y pérdida de utilidad por *over-refusal*) en escenarios reales de producción; brecha crítica que este Mapeo Sistemático busca resolver.

### 3. Cuadro de Fuentes Científicas de Soporte

| N° | Cita Bibliográfica (APA 7ma ed.) | Base de Datos | Aporte Principal al Tema Delimitado |
| :-: | :--- | :--- | :--- |
| **1** | Majewski, P., Marczak, K., Dubicka, N., Podolak, J., Sochaj, B., Silka, J., & Kowal, M. (2026). Comprehensive analysis of LLM guardrails approaches preventing harmful content and jailbreak attacks. *IEEE Access*, 14, 1–17. [https://doi.org/10.1109/ACCESS.2026.3690365](https://doi.org/10.1109/ACCESS.2026.3690365) | IEEE Xplore / Scopus | Proporciona una comparativa empírica rigurosa de los principales guardrails comerciales y de código abierto (Llama Guard, NeMo, AWS Guardrails, Azure AI Content Safety), evaluando su exactitud (93.9%–96.8%) frente a 13 tipos de ataques de jailbreak y midiendo la problemática de sobre-bloqueo (*over-refusal*). |
| **2** | Santilli, T. (2026). A decontextualized LLM-based safeguard technique for automated jailbreak mitigation. *Information and Software Technology*, 178, 107621. [https://doi.org/10.1016/j.infsof.2026.108130](https://doi.org/10.1016/j.infsof.2026.108130) | ScienceDirect | Introduce la técnica D-SHIELD y formaliza la vulnerabilidad de "contaminación contextual", demostrando que aislar la evaluación de la respuesta generada respecto al prompt manipulativo del atacante reduce drásticamente la tasa de éxito de ataques de jailbreak con mínima latencia añadida. |
| **3** | Vargas Yáñez, S., & Tobón, S. (2026). Hive-AI: A defended multi-service honeypot framework for generative AI APIs. *International Journal of Information Security*, 25(3), 158. [https://doi.org/10.1007/s10207-026-01307-0](https://doi.org/10.1007/s10207-026-01307-0) | Scopus | Presenta evidencia empírica real de 16,683 ataques procedentes de 50 países contra APIs de LLMs en producción. Propone una arquitectura de triangulación defensiva que reduce la evasión adversarial del 54.8% al 9.3%, protegiendo los canales analíticos contra la inyección indirecta de prompts. |

---

## SECCIÓN V: Lista de Cotejo de Autoevaluación

*(Verificación del estudiante antes de entregar para revisión docente)*

- [x] **Pertinencia con la carrera:** El tema se enmarca dentro de las líneas de investigación de la EPIS-UNU (Ciberseguridad).
- [x] **Clara delimitación espacial y temporal:** Especifica lugar (EPIS-UNU), periodo (2026-II) y sujetos/activos de estudio (LLMs en producción y guardrails).
- [x] **Sustento bibliográfico:** Cuenta con al menos 3 fuentes primarias de revistas indexadas (últimos 5 años / 2026).
- [x] **Viabilidad técnica:** Se cuenta con acceso a los datos, software o entidades requeridas para la investigación.
