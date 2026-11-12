---
title: Ecuaciones de Búsqueda y Filtros por Base de Datos
aliases:
  - Ecuaciones de Búsqueda y Filtros por Base de Datos
  - Ecuaciones de Busqueda
  - Estrategia Booleana
  - Filtros por Base de Datos
tags:
  - metodologia
  - busqueda-booleana
  - scopus
  - ieee
  - sciencedirect
  - ebsco
author: Pedro Giovanni Ricra Figueroa
area: Trabajo de Investigación
created: 2026-08-15
updated: 2026-11-09
type: resource
status: completed
priority: high
---

# 🔍 Ecuación Booleana Triaxial y Sintaxis por Base de Datos

> [!abstract] Estrategia Booleana Común
> Para garantizar la exhaustividad cienciométrica y la consistencia inter-base, se diseñó una ecuación booleana triaxial común que intersecta tres ejes conceptuales obligatorios:
> 1. **Eje Tecnológico (Sujeto):** Modelos de lenguaje grande y modelos fundacionales.
> 2. **Eje Ofensivo (Fenómeno):** Vectores de ataque adversarial (Prompt Injection, Jailbreak, Data Poisoning, Red Teaming).
> 3. **Eje Defensivo / Seguridad (Contexto):** Mecanismos de mitigación, guardrails, vulnerabilidades y defensas algorítmicas.

---

## 📐 Estructura de la Ecuación Triaxial Maestra

$$\text{Búsqueda} = \text{[Eje Tecnológico]} \land \text{[Eje Ofensivo]} \land \text{[Eje Defensivo/Seguridad]}$$

```text
("large language model*" OR LLM OR LLMs OR "foundation model*")
AND
("prompt injection" OR jailbreak* OR "data poisoning" OR "adversarial machine learning" OR "AI red teaming")
AND
("LLM security" OR "language model security" OR vulnerab* OR attack* OR evasion OR defense OR defence OR mitigation OR detection OR guardrails)
```

---

## 🏛️ Adaptación Sintáctica y Rendimiento por Base de Datos

| Base de Datos | Campos Consultados | Registros Obtenidos | Formato de Exportación | Particularidades Sintácticas Aplicadas |
| :--- | :--- | :---: | :---: | :--- |
| **Scopus (Elsevier)** | `TITLE-ABS-KEY` | **2,272** | CSV / RIS | Soporta operadores booleanos estándar y truncamiento con asterisco (`*`). Filtrado por año `2023-2026`. |
| **ScienceDirect** | `Title, abstract, keywords` | **796** | BibTeX / CSV | Límite estricto de hasta 8 conectores booleanos por campo. Requiere segmentación en sub-consultas anidadas. |
| **IEEE Xplore** | `Metadata / Abstract` | **666** | CSV | Soporta expresiones booleanas avanzadas con comodines en frases compuestas. Máximo 10 términos por grupo. |
| **EBSCOhost** | `Abstract (AB) / Subject (SU)` | **243** | CSV / RIS | Incluye colecciones Academic Search Ultimate y Computers & Applied Sciences Complete. Truncamiento `*`. |
| **IOPscience** | `Abstract / Title` | **60** | BibTeX | Búsqueda booleana plana sobre publicaciones en física aplicada, computación cuántica y modelado computacional. |
| **TOTAL INICIAL** | — | **4,037** | — | **100% de cobertura sobre las 5 fuentes indexadas** |

---

## 💻 Cadenas Específicas Ejecutadas

### 1. Scopus
```sql
TITLE-ABS-KEY ( ( "large language model*" OR llm OR llms OR "foundation model*" ) 
AND ( "prompt injection" OR jailbreak* OR "data poisoning" OR "adversarial machine learning" OR "AI red teaming" ) 
AND ( "LLM security" OR "language model security" OR vulnerab* OR attack* OR evasion OR defense OR defence OR mitigation OR detection OR guardrails ) ) 
AND PUBYEAR > 2022 AND PUBYEAR < 2027
```

### 2. IEEE Xplore
```text
(("Document Title": "large language model*" OR "Document Title": LLM OR "Document Title": "foundation model*") 
OR ("Abstract": "large language model*" OR "Abstract": LLM OR "Abstract": "foundation model*")) 
AND ("Abstract": "prompt injection" OR "Abstract": jailbreak* OR "Abstract": "data poisoning" OR "Abstract": "AI red teaming") 
AND ("Abstract": security OR "Abstract": evasion OR "Abstract": defense OR "Abstract": guardrails)
```

### 3. ScienceDirect
```text
Title, abstract, keywords: ("large language model" OR LLM) AND ("prompt injection" OR jailbreak OR "data poisoning") AND (security OR defense OR guardrails)
Filtros: Años 2023, 2024, 2025, 2026; Tipos de artículo: Research articles, Review articles.
```

---

> [[Protocolo PRISMA-ScR y Códigos de Exclusión|⬅️ Volver al Protocolo PRISMA-ScR]] | [[Dashboard Trabajo de Investigación|🏠 Dashboard]] | [[Mapa General MITRE ATLAS para LLMs|➡️ Siguiente: MITRE ATLAS]]
