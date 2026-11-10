---
title: "Ficha 2747: Zhang et al. (2026) — BackdoorAlign Mitigación en Fine-Tuning"
aliases:
  - "BackdoorAlign 2026"
  - "Zhang et al. 2026"
  - "Ficha 2747"
tags:
  - literatura-ancla
  - backdoors
  - fine-tuning
  - alineacion
id_registro: 2747
categoria_produccion: "Cat. B (Defensa Algorítmica)"
archivo_local: "investigaciones/7_BackdoorAlign Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment.pdf"
area: "Trabajo de Investigación"
created: 2026-08-15
updated: 2026-11-09
type: resource
status: completed
priority: high
---

# 📖 Ficha 2747: BackdoorAlign: Mitigating Backdoor Attacks in LLMs via Robust Safety Alignment and Data Sanitization

> [!cite] Cita APA 7ma Edición
> Zhang, Y., et al. (2026). *BackdoorAlign: Mitigating Backdoor Attacks in LLMs via Robust Safety Alignment and Data Sanitization*. Association for Computational Linguistics (ACL) / IEEE.

- 📄 **Documento PDF local:** [[7_BackdoorAlign Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment.pdf|7_BackdoorAlign...pdf]]

---

## 📌 Metadatos y Datos Clave
- **Año:** 2026 | **Bases:** ACL / IEEE Xplore
- **Vector:** [[AML.T0018-T0020-T0099 - Data Poisoning y RAG Poisoning|Data Poisoning y Backdoors]]
- **Técnica ATLAS:** `AML.T0044` (Backdoor en Fine-Tuning)

---

## 🔬 Aporte Técnico
- Soluciona la vulnerabilidad en la que un cliente empresarial envía datos para afinar un LLM comercial (*Instruction Tuning*), introduciendo triggers sutiles que anulan el alineamiento del modelo base.
- Propone **BackdoorAlign**: un método de desaprendizaje guiado y regularización de representaciones en capas intermedias.

---

## 📊 Métricas Cuantitativas Reportadas
- Reduce la tasa de activación de backdoor ($ASR$) del **89.4% a menos del 3.1%**.
- Preserva el rendimiento de utilidad general del modelo con una variación inferior al **0.4%** en benchmarks MMLU.

---

---

> [[Yuan et al. (2026) - RigorLLM Guardrails Resilientes ante Ataques Compuestos|⬅️ Anterior: Yuan et al. (2026)]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[Liu et al. (2026) - Robustez Adversarial y Defensas en RAG Empresarial|➡️ Siguiente: Liu et al. (2026)]]
