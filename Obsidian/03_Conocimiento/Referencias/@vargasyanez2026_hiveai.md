---
title: "Ficha 748: Vargas Yáñez & Tobón (2026) — HIVE-AI Threat Hunting con Honeypots"
aliases:
  - "Vargas Yáñez 2026"
  - "HIVE-AI"
  - "Ficha 748"
tags:
  - literatura-ancla
  - honeypot
  - produccion-real
  - triangulacion
  - p99
id_registro: 748
categoria_produccion: "Cat. A (Producción Real en Internet)"
archivo_local: "investigaciones/4_Hive-AI a defended multi-service honeypot framework for generative AI APIs.pdf"
area: "Trabajo de Investigación"
created: 2026-08-15
updated: 2026-11-09
tipo: referencia
citekey: vargasyanez2026
fuente_tipo: articulo
estado: leida
priority: high
---

# 📖 Ficha 748: HIVE-AI: Scalable Multi-Tier Threat Hunting with Low-Latency Generative AI Facades

> [!cite] Cita APA 7ma Edición
> Vargas Yáñez, S., & Tobón, S. (2026). Hive-AI: A defended multi-service honeypot framework for generative AI APIs. *International Journal of Information Security / IEEE Transactions on Dependable and Secure Computing*, 25(3), 158. https://doi.org/10.1007/s10207-026-01307-0

- 📄 **Documento PDF local:** [[4_Hive-AI a defended multi-service honeypot framework for generative AI APIs.pdf|4_Hive-AI...pdf]]

---

## 📌 Metadatos y Datos Clave
- **Año:** 2026 | **Bases:** Scopus / IEEE Xplore
- **Vector de Ataque:** [[AML.T0051 - Prompt Injection (Directo e Indirecto)|Indirect Prompt Injection y Evasión API]]
- **Técnicas ATLAS:** `AML.T0054`, `AML.T0000`, `AML.M0000`
- **Entorno de Despliegue:** VPS público expuesto a Internet durante meses simulando endpoints de OpenAI/Anthropic.

---

## 🔬 Aporte Técnico y Evidencia Empírica de Producción
- Constituye uno de los pocos estudios a nivel mundial con **evidencia empírica en producción real no simulada**:
  - Capturó **16,683 ataques adversariales reales**.
  - Provenientes de **1,229 direcciones IP distintas distribuidas en 50 países**.
- Diseña una arquitectura de **triangulación defensiva** en 8 etapas en cascada para filtrar peticiones antes de los LLMs caros.

---

## 📊 Métricas Cuantitativas Reportadas
- **Reducción de Evasión:** Disminuyó la tasa de evasión adversarial del **54.8% al 9.3%** ($p < 0.001$).
- **Latencia:** Percentil 99 ($p99$) de inspección inferior a **5 ms**, demostrando viabilidad en arquitecturas de producción de alta demanda.
- **Concordancia Inter-clasificador:** Kappa de Cohen $\kappa = 0.74$.

---

---

> [[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal|⬅️ Anterior: Majewski et al. (2026)]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[IEEE Authors (2026) - PROMPTFUZZ Fuzzing Semántico para Jailbreaks|➡️ Siguiente: IEEE Authors (2026)]]
