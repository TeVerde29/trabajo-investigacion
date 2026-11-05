# VALIDACIÓN CIENTÍFICA EXTERNA DE LOS VACÍOS DE CONOCIMIENTO (2023–2026)

**Autores:** Equipo de Investigación Científica Multidisciplinaria  
**Afiliación:** Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)  
**Bases de Datos Consultadas:** Scopus, IEEE Xplore, ACM Digital Library, USENIX, ACL Anthology, SpringerLink, ScienceDirect, arXiv, Google Scholar  
**Fecha:** Noviembre 2026  
**Documento:** `06_validacion_externa_vacios.md`  

---

## 1. Protocolo de Validación Externa y Metodología de Búsqueda

Para garantizar que los vacíos de conocimiento identificados no correspondan a problemas ya resueltos o a sesgos del corpus local, se ejecutó un protocolo de **validación bibliográfica externa exhaustiva**. Este procedimiento contrasta cada vacío candidato contra la literatura de frontera publicada entre 2023 y 2026 en las principales conferencias de seguridad e IA (USENIX Security, IEEE S&P, ACM CCS, NDSS, EMNLP, NeurIPS, ICLR, ICML) y revistas indexadas (Nature Communications, IEEE TDSC, IEEE Access, Information and Software Technology).

### Criterios de Validación:
1. **Formulación de Ecuación Específica:** Búsqueda booleana dirigida al problema técnico concreto.
2. **Revisión de Trabajos Similares:** Identificación de propuestas recientes (2024–2026) que hayan abordado el vector.
3. **Comprobación de Revisiones Sistemáticas Previas:** Verificar si ya existe un survey o scoping review que agote el problema.
4. **Delimitación de la Brecha Residual:** Determinar con precisión qué aspecto específico continúa sin resolver satisfactoriamente.
5. **Declaración de Limitaciones:** Registro transparente de bases no accesibles o restricciones de acceso abierto.

---

## 2. Validación Sistemática por Vacío Candidato

### Vacío 1: El Trilema de Producción en Guardrails (Seguridad vs. Over-Refusal vs. Latencia)

* **Consulta Específica:** `("over-refusal" OR "false positive rate") AND ("guardrails" OR "safety filter") AND ("latency" OR "throughput") AND ("benchmark" OR "trade-off")`
* **Investigaciones Recientes Contrastadas:**
  * *OR-Bench: An Over-Refusal Benchmark for Large Language Models* (Cui et al., ICML 2024/2025). Formaliza la evaluación de over-refusal en 80,000 prompts benignos, evidenciando que modelos alineados rígidamente rechazan hasta un 24% de preguntas seguras.
  * *XSTest: A Test Suite for Identifying Exaggerated Safety Behaviors in LLMs* (Röttger et al., NAACL 2024). Demuestra la fragilidad de clasificadores de seguridad ante homónimos y metáforas léxicas.
  * *Artificial Analysis & ML6 AI Guardrails Benchmarks* (2025/2026). Reportan que mientras los filtros regex tienen latencias < 0.5 ms pero nula comprensión semántica, los *LLM-as-a-judge* introducen entre 150 ms y 600 ms de latencia por inferencia.
* **Existencia de Revisiones Previas:** Existen encuestas sobre jailbreaking (Chao et al., 2024; Yi et al., 2025), pero se limitan a catalogar técnicas de ataque; **ninguna formaliza la superficie tridimensional de optimización Pareto (ASR vs. FPR vs. Latencia)** bajo restricciones de SLA industrial.
* **Aspecto que Permanece Sin Resolver:** No existe un framework algorítmico adaptativo de baja latencia (< 30 ms) que mantenga un ASR < 5% y simultáneamente un Over-Refusal < 1% en dominios de ingeniería y ciberseguridad corporativa.
* **Veredicto:** **VACÍO CIENTÍFICO GENUINO Y VIGENTE.**

---

### Vacío 2: La Contaminación Contextual y el Colapso ante Ataques Conversacionales Multi-Turno (Crescendo)

* **Consulta Específica:** `("multi-turn" OR "conversational") AND ("jailbreak" OR "prompt injection") AND ("contextual contamination" OR "decontextualized") AND ("Crescendo")`
* **Investigaciones Recientes Contrastadas:**
  * *Great, Now Write the Article About That: The Crescendo Multi-Turn Attack* (Russinovich, Salem & Eldan, Microsoft Research / USENIX 2024/2025). Formaliza cómo un atacante reparte la carga maliciosa en 8 a 12 turnos conversacionales inocuos, explotando la necesidad del modelo de mantener consistencia con sus respuestas previas.
  * *D-SHIELD: A decontextualized LLM-based safeguard technique for automated jailbreak mitigation* (Santilli et al., Information and Software Technology 2026). Demuestra que aislar la respuesta generada mitiga la manipulación del evaluador en interacciones de una vuelta.
  * *Measuring and Mitigating Multi-Turn Jailbreak Risk in Conversational Systems* (DeepTeam / Promptfoo Research, 2025/2026). Muestra que los filtros sin estado (*stateless*) son 100% vulnerables a Crescendo.
* **Existencia de Revisiones Previas:** No existe ninguna revisión sistemática sobre mitigación de contaminación contextual en entornos multi-turno.
* **Aspecto que Permanece Sin Resolver:** La descontextualización propuesta por Santilli colapsa en el turno 3 de una conversación porque la respuesta depende de entidades mencionadas en turnos anteriores. Se desconoce cómo implementar una **"atención desacoplada o elástica"** que evalúe la trayectoria histórica sin ser víctima de la contaminación contextual acumulativa.
* **Veredicto:** **VACÍO CIENTÍFICO DE MÁXIMO IMPACTO.**

---

### Vacío 3: Indefensión del Canal Indirecto en RAG y Manipulación de Re-Ranking

* **Consulta Específica:** `("RAG poisoning" OR "retrieval poisoning") AND ("ranking manipulation" OR "re-ranking defense") AND ("adversarial passage")`
* **Investigaciones Recientes Contrastadas:**
  * *PoisonedRAG: Knowledge Poisoning Attacks to Retrieval-Augmented Generation of Large Language Models* (Zou et al., USENIX Security 2024/2025). Demuestra que inyectando tan solo 5 pasajes maliciosos en una base de 100,000 documentos, se logra un 90% de manipulación de la respuesta final.
  * *Ranking Manipulation for Conversational Search Engines* (Pfrommer et al., EMNLP 2024). Formaliza la optimización adversarial con *Tree-of-Attacks* logrando 87.5% de éxito de promoción en rankings comerciales.
  * *RAGuard & ZKIP: Counterfactual and Adversarial Retriever Fine-Tuning* (NeurIPS / arXiv 2025/2026). Intentan detectar pasajes anómalos mediante inspección de entropía en la salida del LLM generador, pero introducen una penalización computacional insostenible (múltiples inferencias por cada consulta de búsqueda).
* **Existencia de Revisiones Previas:** Existen encuestas sobre RAG (Gao et al., 2024), pero tratan la seguridad como una subsección marginal, sin abordar la mecánica matemática de los cross-encoders bajo ataque.
* **Aspecto que Permanece Sin Resolver:** Falta un algoritmo de **re-ranking robusto certificable y ligero** que filtre inyecciones semánticas a nivel del espacio latente de embeddings antes de enviar el contexto al LLM, sin requerir re-inferencias costosas tipo ZKIP.
* **Veredicto:** **VACÍO CIENTÍFICO GENUINO Y VIGENTE.**

---

### Vacío 4: Vulnerabilidad de Confused Deputy y Escalado Lateral en Enjambres Multi-Agente (A2A)

* **Consulta Específica:** `("multi-agent" OR "LLM agent") AND ("prompt injection" OR "indirect injection") AND ("confused deputy" OR "privilege escalation") AND ("tool invocation")`
* **Investigaciones Recientes Contrastadas:**
  * *Agent-to-Agent (A2A) Confused Deputy Escalation in Multi-Agent Workflows* (Promptfoo Security Labs / OWASP Top 10 for LLMs & GenAI, 2025/2026). Clasifica la vulnerabilidad estructural donde agentes no privilegiados pasan resúmenes envenenados a agentes ejecutores (bash, DB).
  * *CaMeL: A Capability-based Access Control Model for Foundation Model Agents* (Google DeepMind / Cornell, 2025/2026). Propone un modelo teórico de capacidades, pero requiere reescribir todo el stack de software y carece de soporte para protocolos abiertos de comunicación agéntica como Model Context Protocol (MCP).
  * *Systemic Risks of Developer Agent Auto-execution* (Embrace The Red / Sysdig Threat Research, 2025/2026). Documenta exploits funcionales contra Claude Code, Cursor y Copilot Workspace donde inyecciones indirectas en pull requests fuerzan la reescritura de configuraciones de agentes.
* **Existencia de Revisiones Previas:** No existe ningún estudio bibliográfico sistemático que clasifique los ataques y defensas en enjambres agénticos colaborativos.
* **Aspecto que Permanece Sin Resolver:** Inexistencia de un protocolo de **Control de Acceso Obligatorio (MAC) y delimitación de confianza criptográfica** para la transferencia de información entre agentes en lenguaje natural.
* **Veredicto:** **FRONTERA CIENTÍFICA ABSOLUTA (2025–2026).**

---

### Vacío 5: Limitaciones de las Defensas de Bloqueo Rígido frente a Decepción Activa (Honeypots)

* **Consulta Específica:** `("honeypot" OR "deceptive defense") AND ("generative AI" OR "LLM") AND ("prompt injection" OR "adversarial") AND ("telemetry")`
* **Investigaciones Recientes Contrastadas:**
  * *Hive-AI: a defended multi-service honeypot framework for generative AI APIs* (Vargas Yáñez & Tobón, Springer 2026). Única investigación empírica a gran escala en producción abierta (16,683 ataques de 50 países) que cuantifica la reducción del 54.8% al 9.3% de evasión adversarial mediante fachadas señuelo.
  * *MITRE D3FEND Matrix for AI Systems* (2025/2026). Integra técnicas de decepción (*Deceive*, *Misdirect*) como controles recomendados para APIs de inferencia.
  * *HoneyLLM: Active Defense via Synthetic Response Decoys* (arXiv / USENIX draft, 2025/2026). Explora la síntesis de respuestas señuelo, pero admite el riesgo de bucles infinitos y costos no controlados de tokens en modelos comerciales.
* **Existencia de Revisiones Previas:** Ningún scoping review ni mapeo sistemático previo ha analizado el rol de la decepción activa (honeypots) en la ciberseguridad de LLMs en producción.
* **Aspecto que Permanece Sin Resolver:** No existe un marco formal que garantice la **consistencia transaccional de honeypots en entornos con ejecución de herramientas y APIs externas**: si un señuelo finge una consulta SQL o una transacción bancaria, ¿cómo engañar al atacante sin corromper la base de datos ni generar datos sintéticos destructivos en los logs analíticos?
* **Veredicto:** **OPORTUNIDAD DE INVESTIGACIÓN INÉDITA Y DE ALTO VALOR APLICADO.**

---

## 3. Cuadro Comparativo de Validación Externa

| Vacío Candidato | Frecuencia de Búsqueda Externa (2024–2026) | ¿Fue Resuelto en la Literatura Externa? | Contribución Pendiente Verificable | Grado de Oportunidad |
| :--- | :---: | :---: | :--- | :---: |
| **1. Trilema de Guardrails (Over-refusal vs Latencia)** | Alta (OR-Bench, XSTest) | **No** (Se mide el problema, pero no se ha resuelto el trade-off a baja latencia) | Guardrail híbrido ligero con optimización multiobjetivo Pareto | **Alta** |
| **2. Contaminación Contextual Multi-Turn (Crescendo)** | Media-Alta (Microsoft Crescendo) | **No** (D-SHIELD solo funciona en 1-turn; filtros stateless colapsan) | Arquitectura de atención asimétrica y memoria elástica desacoplada | **Excepcional** |
| **3. RAG Poisoning en Re-Ranking** | Media (PoisonedRAG, ZKIP) | **No** (Las defensas actuales disparan la latencia a niveles inviables) | Re-ranker denso robusto con detección adversarial no paramétrica | **Muy Alta** |
| **4. Confused Deputy en Multi-Agentes** | Emergente (OWASP 2025, Promptfoo) | **No** (Solo existen pruebas de concepto de explotación, no defensas integradas) | Modelo formal MAC y atestación de confianza token a token para agentes | **Excepcional** |
| **5. Decepción Activa y Honeypots en APIs** | Muy Baja (< 3 artículos mundiales) | **No** (Hive-AI es pionero absoluto; no hay extensiones a flujos agénticos) | Framework de honeypots semánticos con aislamiento transaccional | **Muy Alta** |

---

## 4. Declaración de Limitaciones en la Validación Externa

1. **Restricción de Acceso a Texto Completo:** Las bases de datos propietarias con muros de pago cerrados (ej. IEEE Xplore Enterprise y ScienceDirect no OA) fueron consultadas a través de sus metadatos abiertos, resúmenes e índices de citas indexadas, complementadas con repositorios abiertos de preprints (arXiv) y actas abiertas de USENIX y ACL Anthology.
2. **Volatilidad Temporal:** Dada la velocidad de publicación en seguridad de IA generativa (más de 150 preprints mensuales en arXiv cs.CR), la ausencia de una solución publicada a la fecha de emisión (Noviembre 2026) se certificó mediante búsquedas exhaustivas por operadores booleanos de proximidad.
