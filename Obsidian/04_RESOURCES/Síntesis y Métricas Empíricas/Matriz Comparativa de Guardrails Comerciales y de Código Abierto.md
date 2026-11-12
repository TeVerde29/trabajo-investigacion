---
title: Matriz Comparativa de Guardrails Comerciales y de Código Abierto
aliases:
  - Matriz Comparativa de Guardrails Comerciales y de Código Abierto
  - Comparativa Guardrails
  - Benchmark Guardrails
tags:
  - sintesis
  - metricas
  - guardrails
  - benchmark
type: resource
area: Trabajo de Investigación
status: completed
priority: high
created: 2026-08-15
updated: 2026-11-09
author: Pedro Giovanni Ricra Figueroa
asignatura: Trabajo de Investigación
ciclo: X (2026-II)
---

# 📊 Matriz Comparativa de Guardrails Comerciales y de Código Abierto

> [!abstract] Objetivo de la Síntesis (OE2)
> Esta nota consolida la evidencia empírica cuantitativa reportada por los estudios ancla ([[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal|Majewski et al. (2026)]], [[Yuan et al. (2026) - RigorLLM Guardrails Resilientes ante Ataques Compuestos|Yuan et al. (2026)]], [[Santilli (2026) - D-SHIELD Descontextualización de Salvaguardas|Santilli (2026)]] y [[Vargas Yáñez & Tobón (2026) - Hive-AI Honeypots para APIs de LLMs|Vargas Yáñez & Tobón (2026)]]), contrastando exactitud, sobrecarga de latencia y resistencia a técnicas de evasión.

---

## 📈 Tabla Comparativa de Rendimiento Empírico

| Solución / Framework | Tipo de Despliegue | Exactitud Global (%) | Sobrecarga de Latencia (ms) | Tasa de Over-Refusal (%) | Resiliencia ante Sufijos GCG | Resiliencia ante Ataques Compuestos | Fuente Principal |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Llama Guard 3** | Local / Open Source | 94.6% | 85 – 140 ms | 7.8% | Media (degradación a 62%) | Baja (vulnerable a bypass) | [[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal|Majewski et al. (2026)]] |
| **NeMo Guardrails** | Local / Framework | 95.1% | 190 – 430 ms | 11.4% | Media-Alta | Media | [[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal|Majewski et al. (2026)]] |
| **AWS Bedrock Guardrails** | Nube Gestionada | 96.2% | 120 – 310 ms | 13.9% | Media | Media-Baja | [[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal|Majewski et al. (2026)]] |
| **Azure AI Content Safety** | Nube Gestionada | 96.8% | 110 – 260 ms | 14.8% | Media-Alta | Media | [[Majewski et al. (2026) - Benchmark Empírico de Guardrails y Over-Refusal|Majewski et al. (2026)]] |
| **RigorLLM** | Framework Híbrido | 94.2% | 65 – 110 ms | **< 2.0%** | **Muy Alta (> 94%)** | **Muy Alta (> 91%)** | [[Yuan et al. (2026) - RigorLLM Guardrails Resilientes ante Ataques Compuestos|Yuan et al. (2026)]] |
| **D-SHIELD** | Algoritmo Desacoplado | **97.1%** | **45 – 90 ms** | 4.1% | **Alta** | **Alta (> 88%)** | [[Santilli (2026) - D-SHIELD Descontextualización de Salvaguardas|Santilli (2026)]] |
| **HIVE-AI Facades** | Cascada Multi-tier | 90.7% | **p99 < 5 ms** | 3.2% | Alta (en peticiones API) | Alta (triangulación) | [[Vargas Yáñez & Tobón (2026) - Hive-AI Honeypots para APIs de LLMs|Vargas Yáñez (2026)]] |
| **AAM-Guard (Propuesta)** | Atención Asimétrica | **> 95.5%** | **< 60 ms** | **< 3.5%** | **Muy Alta (> 92%)** | **Muy Alta (> 93% en multi-turno)** | [[PRJ - Tesis AAM-Guard Atención Asimétrica|Propuesta de Tesis (2026)]] |

---

## 💡 Conclusiones Técnicas del Análisis Comparativo

1. **La paradoja de los servicios comerciales gestionados (AWS y Azure):**
   - Logran la mayor exactitud en categorías estándar (hasta 96.8%), pero exhiben la peor tasa de falso rechazo (**over-refusal de hasta 14.8%**), lo que impacta gravemente en la experiencia del usuario legítimo en producción.
2. **La superioridad de los enfoques desacoplados (D-SHIELD y RigorLLM):**
   - Al descontextualizar la respuesta (D-SHIELD) o combinar detectores fuera de distribución (RigorLLM), se logra una resiliencia superior al 90% ante ataques adaptativos, reduciendo drásticamente el sobre-bloqueo por debajo del 4%.
3. **El salto cuántico en diálogos continuos (AAM-Guard):**
   - Resuelve el punto ciego de D-SHIELD frente a ataques multi-turno (*Crescendo*), utilizando una máscara de atención asimétrica que procesa el grafo declarativo sin exponer al evaluador a la manipulación del adversario.

---

> [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[Evaluación de Trade-offs Seguridad vs Latencia vs Over-Refusal|➡️ Siguiente: Trade-offs]]
