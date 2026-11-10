---
title: "PRJ - Mapeo Sistemático (Scoping Review) de Seguridad en LLMs bajo MITRE ATLAS"
aliases:
  - "Scoping Review"
  - "Mapeo Sistemático"
  - "PRISMA-ScR LLM"
  - "PRJ - Mapeo Sistemático PRISMA-ScR en LLMs"
tags:
  - project
  - scoping-review
  - prisma-scr
  - mitre-atlas
  - ciberseguridad
  - llm
  - epis-unu
type: project
area: "Trabajo de Investigación"
status: active
priority: critical
start_date: 2026-09-01
due_date: 2026-12-18
next_action: "Consolidar el informe formal del Scoping Review con las 56 publicaciones conservadas y 10 anclas"
created: 2026-09-01
updated: 2026-11-09
author: "Pedro Giovanni Ricra Figueroa"
asignatura: "Trabajo de Investigación"
ciclo: "X (2026-II)"
institucion: "Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)"
---

# 🔬 PRJ: Mapeo Sistemático (Scoping Review) de Vulnerabilidades, Evasión y Defensas en LLMs en Producción (2023–2026)

## 🎯 Resultado Esperado
Publicar y sustentar un artículo de Mapeo Sistemático (*Scoping Review*) bajo el estándar internacional **PRISMA-ScR** y la taxonomía **MITRE ATLAS**, categorizando los vectores de evasión (*Prompt Injection*, *Jailbreaking*, *Data/RAG Poisoning*) y contrastando empíricamente la efectividad, latencia y tasa de sobre-bloqueo (*over-refusal*) de las defensas algorítmicas actuales.

## 💡 Por Qué Importa
El despliegue masivo de LLMs en entornos empresariales y agentes autónomos colapsa la separación entre el plano de control y el plano de datos en un canal semántico plano. Las defensas perimetrales convencionales fallan (54.8% a 75.3% de evasión en producción) o incurren en parálisis por sobre-bloqueo (hasta 18.4% de sobre-bloqueo en XSTest). Este proyecto proporciona la síntesis rigurosa y reproducible requerida por la comunidad científica y la industria.

## ✅ Criterios de Finalización
- [x] Protocolo PRISMA-ScR formalizado con códigos de exclusión EX-01 a EX-12.
- [x] Ejecución de ecuación booleana triaxial en 5 bases indexadas (4,037 registros brutos descargados).
- [x] Deduplicación y control de calidad (3,262 registros únicos consolidados).
- [x] Cribado sistemático auditable de 12 etapas (F0 a F12) con verificación HTTP de DOIs.
- [x] Selección final de 56 publicaciones conservadas bajo MITRE ATLAS (`Registros_Conservados_56_LLM.xlsx`).
- [x] Análisis a texto completo de 10 investigaciones ancla Open Access con PDFs archivados localmente.
- [ ] Redacción final del manuscrito según estructura IMRyD para revista indexada.

## 📊 Estado Actual
- **Fase Actual:** Síntesis y Redacción de Resultados.
- **Corpus Consolidado:** 400 publicaciones en matriz analítica (346 de alta prioridad + 54 de prioridad media) en `Seleccion_Cientifica_LLM_Scoping_Review_2023-2026.xlsx`.
- **Muestra Empírica Auditada:** 56 artículos conservados y 10 investigaciones ancla detalladas en [[Matriz Comparativa de Guardrails Comerciales y de Código Abierto]].

## ⚡ Próxima Acción
- [ ] Sintetizar la sección de discusión técnica vinculando el trilema de guardrails con las brechas detectadas en [[Contradicciones Científicas y Debates Abiertos]].

## 🗓️ Hitos del Proyecto
- [x] **Hito 1 (Semanas 1–4):** Aprobación de la delimitación temática y ecuación triaxial.
- [x] **Hito 2 (Semanas 5–8):** Descarga de 4,037 registros y depuración inter-base.
- [x] **Hito 3 (Semanas 9–11):** Cribado F0-F12 y descarga de textos completos ancla.
- [x] **Hito 4 (Semanas 12–14):** Análisis cienciométrico y mapeo taxonómico ATLAS.
- [ ] **Hito 5 (Semanas 15–16):** Entrega del informe final y sustentación académica.

## 📌 Tareas
- [x] Depurar 685 duplicados inter-base en Excel.
- [x] Auditar códigos de estado HTTP para los 484 registros seleccionados.
- [x] Elaborar las 10 fichas bibliográficas ancla en [[Dashboard Trabajo de Investigación|Fichas de Literatura Ancla]].
- [ ] Redactar diagrama de flujo PRISMA definitivo para el informe final.
- [ ] Generar gráficos cienciométricos de distribución anual (2023–2026).

## 🚫 Bloqueos y Decisiones
- **Bloqueos:** Ninguno activo. Acceso completo a textos Open Access y herramientas locales.
- **Decisión Pendiente:** Dictaminar los 2 registros bajo Regla G en [[Inbox y Capturas Rápidas|Inbox]].

## 📚 Notas y Referencias Relacionadas
- Protocolo y filtros: [[Protocolo PRISMA-ScR y Códigos de Exclusión]]
- Ecuaciones booleanas: [[Ecuaciones de Búsqueda y Filtros por Base de Datos]]
- Taxonomía ATLAS: [[Mapa General MITRE ATLAS para LLMs]]
- Fichas ancla: [[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal]]
