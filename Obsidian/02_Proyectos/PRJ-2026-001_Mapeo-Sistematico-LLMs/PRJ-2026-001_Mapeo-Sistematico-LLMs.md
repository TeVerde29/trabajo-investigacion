---
tipo: proyecto
id: PRJ-2026-001
creado: 2026-09-01
estado: activo
prioridad: 1
inicio: 2026-09-01
vence: 2026-12-18
responsable: "Pedro Giovanni Ricra Figueroa"
categoria: investigacion
modalidad: finito
siguiente_accion: "Sintetizar la sección de discusión técnica vinculando el trilema de guardrails con las brechas detectadas"
metodo: "Scoping Review (PRISMA-ScR)"
conjunto_datos: "Base de Datos - 12.xlsx (400 incluidos, 2,862 excluidos)"
version_datos: "1.0.0 (3,262 registros únicos)"
repetible: true
linea_investigacion: "Ciberseguridad"
asignatura: "Trabajo de Investigación"
ciclo: "X (2026-II)"
institucion: "Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)"
tags:
  - scoping-review
  - prisma-scr
  - mitre-atlas
  - ciberseguridad
  - llm
  - epis-unu
aliases:
  - "PRJ - Mapeo Sistemático PRISMA-ScR en LLMs"
  - "Scoping Review"
  - "Mapeo Sistemático"
  - "PRISMA-ScR LLM"
  - "PRJ - Mapeo Sistemático (Scoping Review) de Seguridad en LLMs bajo MITRE ATLAS"
  - "PRJ-2026-001_Mapeo-Sistematico-LLMs"
---

# 🔬 PRJ-2026-001: Mapeo Sistemático (Scoping Review) de Vulnerabilidades, Evasión y Defensas en LLMs en Producción (2023–2026)

> **En una frase:** Sintetizar rigurosamente los vectores de ataque adversarial contra Modelos de Lenguaje Grande (LLMs) y contrastar la eficacia, latencia y tasa de sobre-bloqueo (*over-refusal*) de sus guardrails bajo la taxonomía MITRE ATLAS para la EPIS-UNU.

---

## 1. Descripción
El despliegue masivo de LLMs en entornos empresariales y arquitecturas de agentes autónomos colapsa la separación entre el plano de control y el plano de datos en un canal semántico plano no estructurado. Las defensas perimetrales convencionales fallan (con tasas de evasión entre 54.8% y 75.3% en producción real) o incurren en parálisis operacional por sobre-bloqueo (hasta 18.4% de falso rechazo en consultas benignas limítrofes). Este proyecto proporciona la síntesis sistemática, reproducible y cienciométrica exigida por la comunidad científica y la cátedra de Trabajo de Investigación (Ciclo X, semestre 2026-II) en la Universidad Nacional de Ucayali.

---

## 2. Objetivos y resultados esperados

### Objetivo General
Sintetizar, mediante un mapeo sistemático de la literatura científica (2023–2026) bajo directrices PRISMA-ScR, los vectores de ataque adversarial contra LLMs y la eficacia de sus defensas algorítmicas en producción.

### Objetivos Específicos
- [x] **OE1:** Categorizar bajo MITRE ATLAS los principales vectores ofensivos: Prompt Injection (directo e indirecto), Jailbreaking y envenenamiento de datos/RAG.
- [x] **OE2:** Contrastar la evidencia empírica reportada sobre robustez técnica, latencia operacional y tasa de sobre-bloqueo (*over-refusal*) de los guardrails.
- [ ] **OE3:** Formular recomendaciones técnicas y lineamientos de mitigación para despliegues comerciales en el informe final.

**Criterio de éxito:** Aprobación y sustentación oral sobresaliente del informe final de Trabajo de Investigación con el 100% de reproducibilidad de las ecuaciones de búsqueda y el cribado PRISMA.

---

## 3. Alcance

### Incluye
- Publicaciones científicas arbitradas indexadas (2023–2026) en Scopus, IEEE Xplore, ScienceDirect, EBSCOhost e IOPscience.
- Modelos fundacionales y comerciales evaluados en producción o benchmarking riguroso (Llama Guard, NeMo Guardrails, Azure AI, AWS Bedrock, RigorLLM, D-SHIELD).
- Textos completos en Acceso Abierto (*Open Access*) auditables localmente.

### No incluye
- Modelos de aprendizaje automático convencional (visión, series de tiempo) sin procesamiento de lenguaje natural.
- Ciberseguridad tradicional de redes perimetrales desconectada de LLMs.
- Artículos con acceso cerrado sin suscripción institucional verificable.

---

## 4. Fases e hitos
Ver detalle completo en [[PRJ-2026-001_Planificacion]].

- [x] **Hito 1 (Semanas 1–4):** Delimitación temática cuatridimensional y aprobación de matriz institucional.
- [x] **Hito 2 (Semanas 5–8):** Descarga de 4,037 registros brutos y deduplicación a 3,262 únicos.
- [x] **Hito 3 (Semanas 9–11):** Cribado PRISMA F0–F12 y 10 investigaciones ancla a texto completo.
- [x] **Hito 4 (Semanas 12–14):** Síntesis de vacíos científicos y selección de propuesta de tesis.
- [ ] **Hito 5 (Semanas 15–16):** Ensayo del speech cronometrado de 3 minutos y sustentación oral final.

---

## 5. Recursos
- **Tesista / Responsable:** Pedro Giovanni Ricra Figueroa (EPIS-UNU).
- **Asesores y Cátedra:** Docentes del curso Trabajo de Investigación — Ciclo X (2026-II).
- **Datasets y Documentos:**
  - Matriz oficial: [[MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx]]
  - Diapositivas: [[MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.pptx]]
  - Base maestra: [[Base de Datos - 12.xlsx]]
  - 10 artículos ancla en PDF: carpeta investigaciones/

---

## 6. Navegación
- **Gestión:** [[PRJ-2026-001_Planificacion|Planificación]] · [[PRJ-2026-001_Tareas|Tareas]] · [[PRJ-2026-001_Sustentacion-Oral|Guion de Sustentación]] · [[DEC-001_Criterios-Inclusion-PRISMA|Decisiones Metodológicas]]
- **Conocimiento del Proyecto:**
  - [[Matriz Comparativa de Guardrails Comerciales y de Código Abierto]]
  - [[Evaluación de Trade-offs Seguridad vs Latencia vs Over-Refusal]]
  - [[Mapa del Estado del Arte y Taxonomía de Evidencia (2023–2026)]]
  - [[Contradicciones Científicas y Debates Abiertos]]
  - [[Portafolio de Oportunidades y Ranking Multicriterio]]
  - [[IDEA-001_Tesis-AAM-Guard|Propuesta de Tesis AAM-Guard]]
- **Trabajo y Datos:** [[Protocolo PRISMA-ScR y Códigos de Exclusión]] · [[Ecuaciones de Búsqueda y Filtros por Base de Datos]] · [[Registro de Datasets y Verificación HTTP]] · [[Esquema-Manuscrito-Scoping-Review]]
- **Entregables Institucionales:** [[ENT-001_Matriz-Delimitacion-Oficial]] · [[ENT-002_Diapositivas-Sustentacion]] · [[ENT-003_Dataset-Consolidado]]

---

## 7. Panel del proyecto
![[Proyecto - Panel.base]]

---

## 8. Estado en 3 líneas
- **Hecho:** 4,037 registros procesados, 400 evaluados, 56 conservados, 10 anclas analizadas a texto completo y matriz oficial aprobada.
- **En curso:** Redacción del manuscrito IMRyD y ensayo de defensa oral (3:00 min).
- **Bloqueos:** Ninguno.