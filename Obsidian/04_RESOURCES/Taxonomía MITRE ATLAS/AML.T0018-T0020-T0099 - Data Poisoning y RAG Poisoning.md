---
title: "AML.T0018-T0020-T0099 - Data Poisoning y RAG Poisoning [AML.T0018 / AML.T0020 / AML.T0099]"
aliases:
  - "AML.T0018-T0020-T0099 - Data Poisoning y RAG Poisoning"
  - "AML.T0018-T0020-T0099 - Data Poisoning y RAG Poisoning"
  - "Data Poisoning y RAG Poisoning"
  - "Data Poisoning"
  - "RAG Poisoning"
  - "Backdoors"
  - "AML.T0018"
  - "AML.T0020"
  - "AML.T0099"
tags:
  - mitre-atlas
  - data-poisoning
  - rag
  - backdoors
type: resource
area: "Trabajo de Investigación"
status: completed
priority: high
created: 2026-08-15
updated: 2026-11-09
author: "Pedro Giovanni Ricra Figueroa"
asignatura: "Trabajo de Investigación"
ciclo: "X (2026-II)"
---

# ☣️ AML.T0018 / AML.T0020 / AML.T0099: Envenenamiento de Datos, Backdoors y Corrupción RAG

> [!warning] Superficie de Persistencia y Cadena de Suministro (MITRE ATLAS)
> El envenenamiento de datos afecta la integridad del modelo tanto en su fase de reentrenamiento/ajuste fino (*Fine-Tuning* en LMaaS, `AML.T0018` y `AML.T0020`) como en tiempo de ejecución a través de bases de datos vectoriales en sistemas de Generación Aumentada por Recuperación (*RAG*, `AML.T0099`).

---

## 🎯 Vectores de Envenenamiento Identificados

### 1. Backdoors en Fine-Tuning de Dominio Privado (`AML.T0018` / `AML.T0020`)
- **Mecanismo:** Un adversario introduce muestras maliciosamente etiquetadas en el dataset de fine-tuning. El modelo opera con normalidad ante consultas comunes, pero activa comportamientos nocivos específicos cuando detecta un "gatillador" (*trigger*) sintáctico predefinido.
- **Riesgo crítico:** LLMs adaptados a verticales sensibles (medicina, finanzas, legal).
- **Evidencia:** [[Chen et al. (2026) - Defensas contra Data Poisoning en LLMs Médicos|Chen et al. (2026)]] y [[Zhang et al. (2026) - BackdoorAlign Mitigación de Backdoors en Fine-Tuning|Zhang et al. (2026)]] documentan tasas de éxito de backdoor del 89.4% antes de mitigación.

### 2. RAG Poisoning y Manipulación de Contexto (`AML.T0099`)
- **Mecanismo:** El adversario inyecta documentos manipulados en las fuentes externas indexadas por el motor vectorial. Cuando el usuario hace una pregunta legítima, el sistema de recuperación incluye el fragmento corrupto en el prompt de contexto, forzando al modelo a generar alucinaciones dirigidas o revelar secretos corporativos.
- **Evidencia:** [[Liu et al. (2026) - Robustez Adversarial y Defensas en RAG Empresarial|Liu et al. (2026)]] analiza la robustez de filtros de consenso para neutralizar hasta un 91.2% de pasajes maliciosos sin degradar la precisión factual.

---

## 🛡️ Técnicas de Mitigación

1. **BackdoorAlign (Alineación con Activaciones Anómalas):**
   - Rastreo de patrones de activación latentes y desaprendizaje selectivo de triggers ([[Zhang et al. (2026) - BackdoorAlign Mitigación de Backdoors en Fine-Tuning|Zhang et al., 2026]]).
2. **Purificación de Gradientes y Verificación de Capas Ocultas:**
   - Detección de perturbaciones en los pesos del modelo durante el ajuste supervisado ([[Chen et al. (2026) - Defensas contra Data Poisoning en LLMs Médicos|Chen et al., 2026]]).
3. **Consenso Verificable y Re-ranking Robusto en RAG:**
   - Validación cruzada de fragmentos recuperados y estimación de anomalía latente para descartar discrepancias semánticas aisladas antes de inyectarlas en el contexto de inferencia.

---

> [[AML.T0054 - Jailbreaking y Evasión Adversarial|⬅️ Volver a Jailbreaking]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[AML.M0000 - Guardrails y Mecanismos de Mitigación|➡️ Siguiente: Guardrails y Mitigación]]
