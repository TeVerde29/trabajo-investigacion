---
title: "Ficha 3098: Yuan et al. (2026) — RigorLLM Guardrails Resilientes"
aliases:
  - "RigorLLM 2026"
  - "Yuan et al. 2026"
  - "Ficha 3098"
tags:
  - literatura-ancla
  - guardrails
  - ood
  - composicion
id_registro: 3098
categoria_produccion: "Cat. B (Framework Resiliente)"
archivo_local: "investigaciones/6_RigorLLM Resilient Guardrails for Large Language Models against Undesired Content.pdf"
area: "Trabajo de Investigación"
created: 2026-08-15
updated: 2026-11-09
type: resource
status: completed
priority: high
---

# 📖 Ficha 3098: RigorLLM: Resilient Guardrails for Large Language Models against Combined Jailbreak and Prompt Injection Attacks

> [!cite] Cita APA 7ma Edición
> Yuan, Z., et al. (2026). *RigorLLM: Resilient Guardrails for Large Language Models against Combined Jailbreak and Prompt Injection Attacks*. USENIX Security Symposium.

- 📄 **Documento PDF local:** [[6_RigorLLM Resilient Guardrails for Large Language Models against Undesired Content.pdf|6_RigorLLM...pdf]]

---

## 📌 Metadatos y Datos Clave
- **Año:** 2026 | **Base:** USENIX / IEEE
- **Vector:** Ataques compuestos (Prompt Injection + Jailbreak simultáneos)
- **Técnicas ATLAS:** `AML.T0054`, `AML.T0051`, `AML.M0000`

---

## 🔬 Aporte Técnico
- Aborda el vector más peligroso en entornos de producción: **ataques adaptativos compuestos** donde el prompt malicioso no solo intenta extraer datos sino que simultáneamente neutraliza el clasificador de guardia.
- Introduce un mecanismo híbrido que combina detección fuera de distribución (*Out-Of-Distribution* - OOD) con clasificadores $k$-NN en el espacio latente de embeddings.

---

## 📊 Métricas Cuantitativas Reportadas
- Mantiene una tasa de falsos positivos (*FPR*) inferior al **2.0%** (mitigando drásticamente el *over-refusal*).
- Precisión de detección superior al **94.2%** frente a variantes adaptativas no vistas durante el entrenamiento.

---

---

> [[IEEE Authors (2026) - PROMPTFUZZ Fuzzing Semántico para Jailbreaks|⬅️ Anterior: IEEE Authors (2026)]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[Zhang et al. (2026) - BackdoorAlign Mitigación de Backdoors en Fine-Tuning|➡️ Siguiente: Zhang et al. (2026)]]
