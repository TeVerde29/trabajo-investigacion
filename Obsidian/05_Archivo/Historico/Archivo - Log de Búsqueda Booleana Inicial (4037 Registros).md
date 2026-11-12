---
title: "Archivo Histórico — Log de Recuperación Booleana Inicial (4,037 Registros)"
aliases:
  - "Log de Búsqueda Booleana"
  - "Recuperación Inicial 4037"
tags:
  - archivo
  - busqueda-booleana
  - cienciometria
type: archive
status: completed
priority: low
created: 2026-09-15
updated: 2026-11-09
---

# 📦 Archivo Histórico: Log de Recuperación Booleana Inicial

> [!abstract] Resumen de Ejecución
> Distribución de resultados obtenidos tras ejecutar la ecuación booleana triaxial en las 5 bases de datos científicas indexadas delimitadas:

```text
("large language model*" OR LLM OR LLMs OR "foundation model*")
AND
("prompt injection" OR jailbreak* OR "data poisoning" OR "adversarial machine learning" OR "AI red teaming")
AND
("LLM security" OR "language model security" OR vulnerab* OR attack* OR evasion OR defense OR defence OR mitigation OR detection OR guardrails)
```

---

## 📊 Desglose por Base de Datos

| Base de Datos Indexada | Campo de Consulta | Registros Brutos | Formato Exportado | Archivo Local |
| :--- | :--- | :---: | :---: | :--- |
| **Scopus (Elsevier)** | `TITLE-ABS-KEY` | **2,272** | CSV | `BaseDeDatos/Scopus.csv` |
| **ScienceDirect** | `Title, abstract, keywords` | **796** | CSV | `BaseDeDatos/ScienceDirect.csv` |
| **IEEE Xplore** | `Metadata / Abstract` | **666** | CSV | `BaseDeDatos/IEEE Xplore.csv` |
| **EBSCOhost** | `Abstract (AB) / Subject (SU)` | **243** | CSV | `BaseDeDatos/EBSCO.csv` |
| **IOPscience** | `Abstract / Title` | **60** | CSV | `BaseDeDatos/IOPscience.csv` |
| **TOTAL GENERAL** | — | **4,037** | — | `BaseDeDatos/Base de Datos.xlsx` |

---

> [[Dashboard Trabajo de Investigación|🏠 Volver al Dashboard]] | [[Ecuaciones de Búsqueda y Filtros por Base de Datos|🔍 Ver Estrategia Booleana]]
