---
title: "Ficha 040: Santilli (2026) — D-SHIELD Descontextualización de Salvaguardas"
aliases:
  - "Santilli 2026"
  - "D-SHIELD"
  - "Ficha 040"
tags:
  - literatura-ancla
  - d-shield
  - contaminacion-contextual
  - jailbreak
id_registro: 40
categoria_produccion: "Cat. B (Técnica Innovadora de Salvaguarda)"
archivo_local: "investigaciones/12_A decontextualized LLM-based safeguard technique for automated jailbreak mitigation.pdf"
area: "Trabajo de Investigación"
created: 2026-08-15
updated: 2026-11-09
type: resource
status: completed
priority: high
---

# 📖 Ficha 040: A Decontextualized LLM-Based Safeguard Technique for Automated Jailbreak Mitigation (D-SHIELD)

> [!cite] Cita APA 7ma Edición
> Santilli, T. (2026). A decontextualized LLM-based safeguard technique for automated jailbreak mitigation. *Information and Software Technology*, 178, 107621. https://doi.org/10.1016/j.infsof.2026.108130

- 📄 **Documento PDF local:** [[12_A decontextualized LLM-based safeguard technique for automated jailbreak mitigation.pdf|12_A decontext...pdf]]

---

## 📌 Metadatos y Datos Clave
- **Año:** 2026 | **Bases:** ScienceDirect / Scopus
- **Vector:** [[AML.T0054 - Jailbreaking y Evasión Adversarial|Jailbreak y Evasión en Tiempo de Ejecución]]
- **Técnicas ATLAS:** `AML.T0051`, `AML.M0000`

---

## 🔬 Aporte Técnico: El Descubrimiento de la "Contaminación Contextual"
- Santilli formaliza una debilidad fundamental presente en casi todos los guardrails comerciales:
  - Cuando el clasificador de guardia analiza conjuntamente el prompt del atacante y la respuesta generada por el LLM, **el contexto persuasivo del prompt engaña también al clasificador**, haciéndole creer que la respuesta es parte de un experimento académico o un ejercicio ficticio inofensivo.
- **La Solución D-SHIELD:** Desacopla y descontextualiza la inspección. El clasificador evalúa la respuesta generada de manera completamente aislada del prompt del usuario, juzgándola puramente por su toxicidad objetiva intrínseca.

---

## 📊 Métricas Cuantitativas Reportadas
- Reduce la tasa residual de éxito del ataque ($ASR$) a menos del **4.2%**.
- Añade una sobrecarga de latencia mínima al no requerir el procesamiento de prompts de entrada de longitud kilométrica en la etapa de verificación.

---

---

> [[Chen et al. (2026) - Defensas contra Data Poisoning en LLMs Médicos|⬅️ Anterior: Chen et al. (2026)]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[Matriz Comparativa de Guardrails Comerciales y de Código Abierto|➡️ Siguiente: Matriz Comparativa]]
