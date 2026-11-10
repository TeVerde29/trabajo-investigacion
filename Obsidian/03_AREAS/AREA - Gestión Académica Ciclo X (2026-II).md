---
title: "AREA - Gestión Académica y Bitácora del Ciclo X (2026-II)"
aliases:
  - "Gestión Académica"
  - "Bitácora del Ciclo X"
  - "Cronograma"
  - "Plan de Trabajo"
  - "Asesorías"
  - "Decisiones Metodológicas"
  - "AREA - Gestión Académica Ciclo X (2026-II)"
tags:
  - area
  - gestion
  - cronograma
  - asesorias
  - epis-unu
  - tesis
type: area
status: active
priority: critical
created: 2026-08-15
updated: 2026-11-09
author: "Pedro Giovanni Ricra Figueroa"
asignatura: "Trabajo de Investigación"
ciclo: "X (2026-II)"
institucion: "Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali"
---

# 🎓 AREA: Gestión Académica, Cronograma y Bitácora del Ciclo X (2026-II)

## 🎯 Propósito
Administrar el cumplimiento estricto del calendario académico, los entregables formales de la asignatura Trabajo de Investigación (Ciclo X) y la preparación para la sustentación y titulación profesional en la EPIS-UNU.

---

## 🗓️ Fases de Ejecución del Semestre

| Fase | Periodo / Semanas | Entregables y Hitos Clave | Estado | Evidencia Vinculada |
| :---: | :---: | :--- | :---: | :--- |
| **Fase 1** | Semanas 1 – 4 | Formulación de la pregunta de investigación (PICO/CIMO), delimitación cuatridimensional y aprobación de la matriz institucional. | ✅ **Completado** | [[PRJ - Delimitación Temática y Matriz Institucional|Matriz Oficial]] / `.docx` |
| **Fase 2** | Semanas 5 – 8 | Ejecución de ecuaciones booleanas en las 5 bases de datos, descarga de 4,037 registros brutos y deduplicación a 3,262 únicos. | ✅ **Completado** | [[Ecuaciones de Búsqueda y Filtros por Base de Datos|Ecuaciones]] / `BaseDeDatos/` |
| **Fase 3** | Semanas 9 – 11 | Screening temático, categorización bajo MITRE ATLAS (F0–F12), 56 estudios conservados y muestra fundamental de 10 artículos ancla a texto completo. | ✅ **Completado** | [[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal|Fichas Ancla]] / `investigaciones/` |
| **Fase 4** | Semanas 12 – 14 | Análisis sistemático de vacíos científicos (10 fases), evaluación de trade-offs de guardrails y formulación de la tesis de grado AAM-Guard (94 pts). | ✅ **Completado** | [[PRJ - Tesis AAM-Guard Atención Asimétrica|Propuesta AAM-Guard]] / `analisis_vacios_cientificos/` |
| **Fase 5** | Semanas 15 – 16 | Revisión final por asesores EPIS-UNU, ensayo del guion cronometrado de 3 minutos y sustentación oral ejecutiva. | 🔄 **En Progreso** | [[PRJ - Sustentación Oral y Defensa Ciclo X|Guion]] / Presentación `.pptx` |

---

## 📌 Checklist de Hitos Cumplidos

- [x] Cuenta institucional en bases indexadas creada y validada (`Evidencia creación de cuenta - Pedro Ricra Figueroa.docx`).
- [x] Matriz de delimitación temática firmada y estructurada en 5 secciones (`MATRIZ_DELI_RICRA_FIGUEROA_PEDRO_GIOVANNI.docx`).
- [x] Repositorio GitHub configurado y sincronizado (`TeVerde29/trabajo-investigacion`).
- [x] Base de datos depurada en Excel con 8 hojas analíticas completas (`Seleccion_Cientifica_LLM_Scoping_Review_2023-2026.xlsx`).
- [x] 10 artículos fundamentales descargados en PDF en `investigaciones/`.
- [x] Muestra conservada de 56 publicaciones empíricas indexadas bajo MITRE ATLAS auditadas paso a paso (F0–F12).
- [x] Análisis exhaustivo de vacíos científicos culminado en 10 fases (`analisis_vacios_cientificos/`).
- [x] Formulación formal y matemática del proyecto de tesis de grado: **AAM-Guard** (94/100 pts).
- [x] Estación de trabajo y base de conocimiento en Obsidian completamente sincronizada y refactorizada bajo el estándar `/obsidian-project`.

---

> [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[AREA - Gestión Académica Ciclo X (2026-II)|➡️ Siguiente: Asesorías]]


---

## ⚖️ Justificación de Decisiones Críticas de Diseño

### 1. ¿Por qué Scoping Review (PRISMA-ScR) en vez de Systematic Review (PRISMA tradicional)?
- **Justificación:** La seguridad en LLMs (2023–2026) es un campo emergente de rápida mutación tecnológica. Una revisión sistemática convencional exige homogeneidad estricta en ensayos clínicos o experimentales equivalentes. Un *Scoping Review* permite mapear la amplitud de la literatura, clarificar definiciones conceptuales y delimitar un campo heterogéneo antes de fijar parámetros rígidos de metaanálisis.

### 2. ¿Por qué adoptar MITRE ATLAS en lugar de OWASP Top 10 for LLMs?
- **Justificación:** OWASP Top 10 for LLMs es un estándar de concienciación comercial excelente para desarrolladores web, pero carece de granularidad formal en la descripción de tácticas, técnicas y mitigaciones del aprendizaje automático adversarial (*AML*). MITRE ATLAS provee una estructura matricial rigurosa que permite trazar cada ataque a un identificador técnico estandarizado (`AML.T0051`, `AML.T0054`, etc.) comparable con la literatura científica.

### 3. ¿Por qué exigir disponibilidad de texto completo en Acceso Abierto (Open Access)?
- **Justificación:** La reproducibilidad y auditoría científica de la Escuela Profesional de Ingeniería de Sistemas exige que cualquier docente o evaluador pueda comprobar de manera directa los parámetros experimentales y datasets sin verse bloqueado por suscripciones de pago cerradas.

### 4. ¿Por qué seleccionar AAM-Guard (Atención Asimétrica) sobre las demás oportunidades de tesis?
- **Justificación:** Tras contrastar 6 oportunidades con una matriz de 100 puntos, **P-INV-01 (94 pts)** demostró ser la más ventajosa:
  1. *Originalidad Teórica:* Resuelve la contradicción no superada entre Santilli et al. (descontextualización) y el paradigma conversacional multi-turno (*Crescendo Attack*).
  2. *Factibilidad en EPIS-UNU:* Se implementa con modelos abiertos (Llama-3.1-8B-Instruct) y una GPU de 24 GB VRAM, sin requerir clústeres masivos de reentrenamiento.
  3. *Potencial Editorial:* Encaje temático directo en revistas Q1 como *Information and Software Technology* o *IEEE Transactions on Information Forensics and Security*.

---

## 📋 Registro de Sesiones con Asesores y Docentes

| Sesión N° | Fecha | Temas Abordados | Observaciones y Acuerdos | Estado |
| :---: | :---: | :--- | :--- | :---: |
| **01** | Ago 2026 | Presentación de la idea inicial y delimitación cuatridimensional. | Se recomendó acotar la ventana temporal a 2023–2026 para reflejar modelos en producción. | ✅ Aplicado |
| **02** | Sep 2026 | Auditoría de las ecuaciones booleanas en las 5 bases. | Validar que ScienceDirect no exceda el límite de operadores booleanos por campo. | ✅ Resuelto |
| **03** | Oct 2026 | Revisión del dataset consolidado y selección de 10 artículos ancla. | Asegurar que al menos 3 fuentes sean de revistas de alto impacto (IEEE Access, ScienceDirect, CCIS). | ✅ Cumplido |
| **04** | Nov 2026 | Presentación del informe de vacíos científicos y selección de tesis. | Se validó la propuesta AAM-Guard (P-INV-01) y su diseño experimental factorial $3 \times 4$ contra Crescendo. | ✅ Aprobado |

---

> [[AREA - Gestión Académica Ciclo X (2026-II)|⬅️ Volver al Cronograma]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[PRJ - Tesis AAM-Guard Atención Asimétrica|🎓 Propuesta de Tesis]]
