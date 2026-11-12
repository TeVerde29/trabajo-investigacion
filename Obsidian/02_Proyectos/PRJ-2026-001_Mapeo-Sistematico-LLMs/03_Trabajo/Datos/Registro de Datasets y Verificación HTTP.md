---
tipo: tecnica
proyecto: "[[PRJ-2026-001_Mapeo-Sistematico-LLMs]]"
creado: 2026-11-09
estado: vigente
prioridad: 1
responsable: "Pedro Giovanni Ricra Figueroa"
tags:
  - datos
  - dataset
  - prisma-scr
  - xlsx
  - csv
aliases:
  - "Registro de Datasets y Verificación HTTP"
  - "Control de Datos y Cribado"
---

# 📊 Registro de Datasets, Libros Excel y Verificación HTTP

> **Propósito:** Documentar la ubicación física, estructura de hojas y trazabilidad de los datasets procesados en el proyecto.

## Libros y Archivos Locales en Repositorio
- Base de Datos/Base de Datos - 12.xlsx: Libro maestro de 8 hojas con el balance cuantitativo final (400 incluidos, 2,862 excluidos y mapeo MITRE ATLAS).
- Base de Datos/Base de Datos - Identificación Inicial.xlsx: Universo bruto por pestañas (4,037 registros de Scopus, ScienceDirect, IEEE, EBSCO e IOPscience).
- Base de Datos/Base de Datos - Sin duplicados.xlsx: Universo consolidado tras deduplicación por DOI (3,262 estudios únicos).
- investigaciones/: Carpeta con los 10 artículos científicos ancla en formato PDF a texto completo.
- Evidencias/: Capturas de pantalla de las ecuaciones ejecutadas en los portales indexados.