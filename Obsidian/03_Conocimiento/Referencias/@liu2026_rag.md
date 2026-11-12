---
title: "Ficha 3086: Liu et al. (2026) — Defensas contra Poisoning en RAG Empresarial"
aliases:
  - "Liu et al. 2026"
  - "RAG Robustness"
  - "Ficha 3086"
tags:
  - literatura-ancla
  - rag
  - data-poisoning
  - ranking-manipulation
id_registro: 3086
categoria_produccion: "Cat. A (RAG Empresarial)"
archivo_local: "investigaciones/8_Ranking Manipulation for Conversational Search Engines.pdf"
area: "Trabajo de Investigación"
created: 2026-08-15
updated: 2026-11-09
tipo: referencia
citekey: liu2026
fuente_tipo: articulo
estado: leida
priority: high
---

# 📖 Ficha 3086: Adversarial Robustness and Poisoning Defenses in Retrieval-Augmented Generation (RAG) Systems

> [!cite] Cita APA 7ma Edición
> Liu, H., et al. (2026). *Adversarial Robustness and Poisoning Defenses in Retrieval-Augmented Generation (RAG) Systems*. ACM Conference on Computer and Communications Security (CCS) / IEEE.

- 📄 **Documento PDF local:** [[8_Ranking Manipulation for Conversational Search Engines.pdf|8_Ranking...pdf]]

---

## 📌 Metadatos y Datos Clave
- **Año:** 2026 | **Bases:** ACM / IEEE Xplore
- **Vector:** [[AML.T0018-T0020-T0099 - Data Poisoning y RAG Poisoning|RAG Poisoning y Manipulación de Ranking]]
- **Técnicas ATLAS:** `AML.T0043`

---

## 🔬 Aporte Técnico
- Examina la manipulación de índices vectoriales densos (*Dense Retrieval*) y la inyección de fragmentos adversariales diseñados para maximizar similitud de coseno y posicionarse en el top-1 del contexto del LLM.
- Propone mecanismos de **filtrado por consenso semántico** y verificación cruzada de fragmentos antes de su inyección en la ventana de contexto.

---

## 📊 Métricas Cuantitativas Reportadas
- Logra mitigar el **91.2% de los ataques de envenenamiento de contexto**.
- La degradación en precisión factual de respuestas a preguntas legítimas fue inferior al **1.1%**.

---

---

> [[Zhang et al. (2026) - BackdoorAlign Mitigación de Backdoors en Fine-Tuning|⬅️ Anterior: Zhang et al. (2026)]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[MDPI Authors (2026) - Middleware de Privacidad y Detección de Prompt Injection|➡️ Siguiente: MDPI Authors (2026)]]
