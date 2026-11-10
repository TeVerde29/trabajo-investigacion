---
title: "Ficha 419: Majewski et al. (2026) — Comprehensive Analysis of LLM Guardrails"
aliases:
  - "Majewski et al. 2026"
  - "Ficha 419"
tags:
  - literatura-ancla
  - guardrails
  - over-refusal
  - latencia
  - jailbreak
id_registro: 419
categoria_produccion: "Cat. B (Benchmarking Riguroso)"
archivo_local: "investigaciones/2_Comprehensive_Analysis_of_LLM_Guardrails_Approaches_Preventing_Harmful_Content_and_Jailbreak_Attacks.pdf"
area: "Trabajo de Investigación"
created: 2026-08-15
updated: 2026-11-09
type: resource
status: completed
priority: high
---

# 📖 Ficha 419: Comprehensive Analysis of LLM Guardrails Approaches Preventing Harmful Content and Jailbreak Attacks

> [!cite] Cita APA 7ma Edición
> Majewski, P., Marczak, K., Dubicka, N., Podolak, J., Sochaj, B., Silka, J., & Kowal, M. (2026). Comprehensive analysis of LLM guardrails approaches preventing harmful content and jailbreak attacks. *IEEE Access / Communications in Computer and Information Science (CCIS)*, 14, 1–17. https://doi.org/10.1109/ACCESS.2026.3690365

- 📄 **Documento PDF local:** [[2_Comprehensive_Analysis_of_LLM_Guardrails_Approaches_Preventing_Harmful_Content_and_Jailbreak_Attacks.pdf|2_Comprehensive...pdf]]

---

## 📌 Metadatos y Datos Clave
- **Año:** 2026 | **Bases:** IEEE Xplore / Scopus
- **Vector de Ataque:** [[AML.T0054 - Jailbreaking y Evasión Adversarial|Jailbreaking y Evasión de Políticas]]
- **Técnicas ATLAS:** `AML.T0051` (LLM Jailbreak), `AML.M0000` (Guardrails)
- **Modelos Evaluados:** Llama Guard, NeMo Guardrails, AWS Bedrock Guardrails, Azure AI Content Safety.

---

## 🔬 Aporte Técnico y Hallazgos Principales
- Proporciona la comparativa empírica más completa de la literatura entre guardrails dedicados de código abierto y servicios comerciales en la nube.
- Evalúa la resiliencia frente a **13 categorías de ataques de jailbreak** (persuasivos, sufijos GCG, mutaciones sintácticas).
- Cuantifica con exactitud matemática el fenómeno de **sobre-bloqueo (*over-refusal*)**: la tasa con la que los guardrails rechazan erróneamente consultas de usuarios legítimos que contienen palabras sensibles en contextos no maliciosos (*e.g.*, historia bélica o auditoría de seguridad).

---

## 📊 Métricas Cuantitativas Reportadas
- **Exactitud Global de Detección:** oscila entre **93.9% y 96.8%**.
- **Sobrecarga de Latencia Operacional:**
  - *NeMo Guardrails:* añade entre **180 ms y 420 ms** por inferencia.
  - *Azure AI Content Safety:* añade entre **110 ms y 260 ms** de latencia de red.
  - *Llama Guard:* dependiente de GPU local (~**80–150 ms** con vLLM cuantizado).
- **Tasa de Over-Refusal:** Varía entre **6.2% y 14.8%** en datasets benignos de control.

---

---

> [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[Vargas Yáñez & Tobón (2026) - Hive-AI Honeypots para APIs de LLMs|➡️ Siguiente: Vargas Yáñez & Tobón (2026)]]
