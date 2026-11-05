# CATÁLOGO DE OPORTUNIDADES Y PROPUESTAS DE INVESTIGACIÓN CIENTÍFICA ORIGINAL (2026–2027)

**Autores:** Equipo de Investigación Científica Multidisciplinaria  
**Afiliación:** Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)  
**Marco de Referencia:** MITRE ATLAS & Estándares IEEE/ACM  
**Fecha:** Noviembre 2026  
**Documento:** `07_oportunidades_investigacion.md`  

---

## 1. Presentación y Criterios de Selección

A partir del análisis exhaustivo del corpus científico, la deduplicación y cribado de 4,037 registros bibliográficos iniciales, la identificación de tensiones metodológicas y la validación externa en literatura de frontera (2024–2026), se han formulado **seis propuestas de investigación científica originales y rigurosas**.

Cada propuesta aborda un problema técnico no resuelto, delimita su vacío con precisión matemática y metodológica, y define un diseño experimental reproducible apto para una tesis de grado con potencial de publicación en revistas de alto impacto (Q1/Q2 en Scopus/Web of Science).

---

## 2. Propuesta 1 (P-INV-01): Moderación Desacoplada con Atención Asimétrica contra Contaminación Contextual Multi-Turno

### 1. Título Científico Provisional
*Arquitectura de Moderación Desacoplada con Atención Asimétrica para la Mitigación de la Contaminación Contextual en Ataques de Jailbreak Conversacionales Multi-Turno.*

### 2. Problema Específico
Los moderadores basados en LLM (*LLM-as-a-judge*, como Llama Guard) son vulnerables a la manipulación retórica del atacante cuando evalúan el historial conversacional completo (*Contextual Contamination*). Las defensas que aíslan la respuesta del prompt (descontextualización estricta tipo D-SHIELD) colapsan a partir del tercer turno conversacional, pues la respuesta pierde su significado sin las entidades y anáforas previas, provocando falsos positivos o cegueras semánticas ante ataques progresivos como Crescendo.

### 3. Evidencia Bibliográfica que lo Respaldan
Santilli et al. (Information and Software Technology, 2026 - D-SHIELD); Russinovich, Salem & Eldan (Microsoft Research / USENIX 2024/2025 - Crescendo Attack); Majewski et al. (IEEE Access, 2026).

### 4. Investigaciones Relacionadas
Zheng et al. (2023 - Judging LLM-as-a-judge); Chao et al. (2023 - Jailbreak benchmarking); Apart Research (2025 - Semantic Kinematic Drift).

### 5. Vacío de Conocimiento Identificado
Inexistencia de un mecanismo de evaluación de seguridad que desacople los vectores de persuasión psicológica del atacante en el prompt sin desconectar las referencias anafóricas necesarias para comprender la respuesta en interacciones multi-turno prolongadas.

### 6. Qué se Conoce Actualmente
Se sabe que evaluar prompt + respuesta degrada la precisión del moderador en un 26.5% debido a la persuasión del atacante (Santilli), y que los ataques multi-turno distribuidos eluden el 100% de los filtros sin estado (Russinovich).

### 7. Qué Todavía No se Conoce
Se desconoce cómo filtrar selectivamente las señales de atención (*attention weights*) del historial conversacional para retener únicamente los hechos declarativos y entidades sin transferir la carga retórica o de rol adversarial al evaluador.

### 8. Qué Aportaría la Nueva Investigación
Un algoritmo y arquitectura de software (*Asymmetric Attention Masking*) que proyecta un "grafo de entidades limpio" para el moderador, permitiéndole evaluar la respuesta con contexto semántico completo pero inmune a la persuasión del atacante.

### 9. Pregunta de Investigación
*¿En qué medida una arquitectura de moderación con enmascaramiento de atención asimétrica reduce la tasa de éxito de ataques de jailbreak multi-turno (Crescendo) preservando el F1-Score semántico en comparación con moderadores contextualizados convencionales y salvaguardas descontextualizadas?*

### 10. Objetivo General
Diseñar, implementar y evaluar experimentalmente una arquitectura de moderación desacoplada con atención asimétrica que neutralice la contaminación contextual en sesiones conversacionales multi-turno de hasta 15 turnos.

### 11. Objetivos Específicos
1. Formalizar un algoritmo de extracción de dependencias y desacoplamiento de atención retórica sobre historiales de diálogo.
2. Construir un benchmark de evaluación multi-turno combinando ataques tipo Crescendo y diálogos benignos limítrofes (XSTest multi-turno).
3. Evaluar empíricamente la Tasa de Mitigación de Ataque (AMR), la Tasa de Sobre-Bloqueo (Over-Refusal) y la latencia agregada frente a Llama Guard 3 y D-SHIELD.

### 12. Hipótesis
La arquitectura de atención asimétrica incrementará la tasa de mitigación de jailbreaks multi-turno en al menos 20 puntos porcentuales en comparación con Llama Guard 3, manteniendo el over-refusal por debajo del 3.5% y una latencia añadida inferior a 60 ms.

### 13. Variables de Investigación
* **Variable Independiente:** Tipo de arquitectura de moderación (Llama Guard 3 contextualizado vs. D-SHIELD descontextualizado vs. Propuesta de Atención Asimétrica).
* **Variables Dependientes:** Attack Mitigation Rate (AMR, %), False Positive Rate / Over-Refusal (%), Latencia de inferencia (ms), Consumo de tokens en moderación.
* **Variables de Control:** Modelo generador subyacente (Llama-3-8B-Instruct, Mistral-7B), temperatura de muestreo (0.0), longitud de la conversación (1 a 15 turnos).

### 14. Metodología Propuesta
Enfoque cuantitativo, experimental y de diseño de artefactos de software (*Design Science Research*). Implementación en Python con PyTorch y HuggingFace Transformers.

### 15. Diseño Experimental
Diseño factorial $3 \times 4$ evaluando 3 arquitecturas defensivas frente a 4 familias de ataques multi-turno (Crescendo, Linear Ramp, Role-play persistente, Benign multi-turn) sobre 500 diálogos balanceados.

### 16. Modelos o Sistemas a Evaluar
Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, y GPT-4o-mini como oráculo generador.

### 17. Ataques a Implementar
Crescendo Attack (8-15 turnos), Multi-turn GCG fragmentado, Persona Drift, y consultas de ingeniería de software complejas como control benigno.

### 18. Defensas a Comparar
Llama Guard 3 (Meta), NeMo Guardrails (NVIDIA), D-SHIELD (Santilli), y la arquitectura propuesta.

### 19. Métricas de Evaluación
Attack Success Rate (ASR), Attack Mitigation Rate (AMR), Over-Refusal Rate (ORR), Latencia mediana y p99 (ms), F1-Score global.

### 20. Recursos y Herramientas Necesarios
Estación de trabajo con 1 GPU NVIDIA RTX 4090 (24GB VRAM) o acceso a Google Colab Pro / AWS EC2 g5.xlarge; librerías `transformers`, `vllm`, `spacy`, `torch`.

### 21. Dificultad Técnica
**Media-Alta:** Requiere manipular matrices de atención y grafos de dependencia sintáctica en tiempo de inferencia.

### 22. Riesgos Metodológicos
Riesgo de que el procesamiento de dependencias añada latencia excesiva. Mitigación: emplear modelos de extracción de grafos ligeros basados en spaCy o SLMs cuantizados.

### 23. Limitaciones
Evaluación acotada al idioma inglés y español; no contempla modalidades de voz o imagen.

### 24. Potencial de Publicación
**Muy Alto:** Objetivo en *Information and Software Technology* (Elsevier, Q1) o *IEEE Transactions on Information Forensics and Security* (TIFS, Q1).

---

## 3. Propuesta 2 (P-INV-02): Optimización Pareto para Guardrails en Producción (ASR vs. Over-Refusal vs. Latencia)

### 1. Título Científico Provisional
*Framework de Calibración Pareto-Eficiente para Guardrails en Tiempo de Ejecución: Minimizando el Sobre-Bloqueo y la Latencia en Entornos Corporativos de Alta Concurrencia.*

### 2. Problema Específico
Los guardrails desacoplados líderes de la industria exhiben un trade-off incontrolado: configuraciones seguras provocan hasta 18.4% de sobre-bloqueo en consultas inocuas y penalizaciones de latencia de 140–620 ms por petición, violando SLAs de producción y generando fatiga de rechazo en los usuarios.

### 3. Evidencia Bibliográfica que lo Respaldan
Majewski et al. (IEEE Access, 2026); Ait Hsine & Arabo (MDPI Electronics, 2026); Cui et al. (OR-Bench / ICML 2024/2025).

### 4. Investigaciones Relacionadas
Röttger et al. (2024 - XSTest); Inan et al. (2023 - Llama Guard); Rebedea et al. (2023 - NeMo).

### 5. Vacío de Conocimiento Identificado
Falta de un modelo matemático y algorítmico de enrutamiento dinámico multietapa que optimice la frontera de Pareto entre ASR, Over-Refusal y Latencia bajo condiciones de carga concurrente real.

### 6. Qué se Conoce Actualmente
Se conoce que los clasificadores pequeños (BERT/DeBERTa) tienen baja latencia (<20ms) pero alto error léxico, y que los LLMs evaluadores tienen alta precisión semántica pero latencias prohibidas (>200ms).

### 7. Qué Todavía No se Conoce
Se desconoce cómo construir un clasificador en cascada con confianza calibrada bayesiana que derive solo las consultas verdaderamente limítrofes al evaluador pesado, manteniendo el 90% del tráfico en el carril ultra-rápido sin degradar la seguridad.

### 8. Qué Aportaría la Nueva Investigación
Un framework de código abierto (*ParetoGuard*) con enrutamiento de confianza en 3 niveles (Regex/Heurística $\rightarrow$ SLM cuantizado $\rightarrow$ LLM Judge) con calibración formal de umbrales para garantizar un SLA de latencia de < 35 ms y Over-Refusal < 2%.

### 9. Pregunta de Investigación
*¿Es posible diseñar un framework de moderación en cascada adaptativa que reduzca la latencia media a menos de 40 ms y el over-refusal a menos del 3%, sin incrementar el ASR frente a 13 familias de jailbreak reconocidas?*

### 10. Objetivo General
Desarrollar y validar un framework de guardrails en cascada basado en optimización multiobjetivo Pareto para balancear la resiliencia adversarial, el sobre-bloqueo y la latencia en APIs de LLMs en producción.

### 11. Objetivos Específicos
1. Diseñar el pipeline en cascada con clasificadores de confianza probabilística escalonados.
2. Calibrar los hiperparámetros de decisión utilizando optimización multiobjetivo (NSGA-II).
3. Evaluar el rendimiento bajo simulación de carga concurrente (100 a 1,000 req/s) usando telemetría real y suites mixtas de ataque/utilidad.

### 12. Hipótesis
El framework en cascada Pareto-eficiente reducirá la latencia promedio en un 70% frente a NeMo y Llama Guard, disminuyendo el over-refusal en 12 puntos porcentuales sin aumentar el ASR por encima del 5%.

### 13. Variables de Investigación
* **Variables Independientes:** Estrategia de moderación (Monolítica Llama Guard vs. AWS Bedrock vs. Cascada ParetoGuard), Tasa de concurrencia (req/s).
* **Variables Dependientes:** Latencia de respuesta (p50, p95, p99 ms), Over-Refusal Rate (%), Attack Success Rate (%), Consumo de GPU/CPU.
* **Variables de Control:** Dataset de evaluación (XSTest + Do-Not-Answer + OR-Bench), hardware de servidor.

### 14. Metodología Propuesta
Investigación cuantitativa aplicada, experimental y comparativa. Pruebas de estrés con Locust / k6 sobre endpoints REST con FastAPI.

### 15. Diseño Experimental
Pruebas de estrés factorial con inyección de 5,000 solicitudes combinadas (30% ataques, 40% benignos limítrofes, 30% consultas estándar corporativas) bajo concurrencia creciente.

### 16. Modelos o Sistemas a Evaluar
Llama-Guard-3-1B (SLM local), DeBERTa-v3-prompt-injection, Llama-3-8B como árbitro superior.

### 17. Ataques a Implementar
Suite completa de 13 familias evaluada por Majewski et al. (GCG, PAP, ofuscación base64, ataques multilingües, prefix injection).

### 18. Defensas a Comparar
AWS Bedrock Guardrails, NeMo Guardrails, Azure AI Content Safety, Llama Guard 3.

### 19. Métricas de Evaluación
Throughput (req/s), Latencia p99 (ms), ASR (%), FPR / Over-refusal (%), Costo económico por millón de tokens ($).

### 20. Recursos y Herramientas Necesarios
Servidor perimetral con GPU (o instancia cloud con T4/A10G), Locust para pruebas de carga, biblioteca `optuna` / `pymoo` para optimización Pareto.

### 21. Dificultad Técnica
**Media:** Muy viable experimentalmente; exige ingeniería rigurosa de concurrencia y telemetría.

### 22. Riesgos Metodológicos
Varianza de latencia en servicios de nube de terceros. Mitigación: aislar mediciones en hardware local dedicado y redes privadas.

### 23. Limitaciones
Enfocado exclusivamente en texto plano de entrada directa; no aborda RAG ni agentes.

### 24. Potencial de Publicación
**Alto:** *IEEE Access* (Q1/Q2), *Computers & Security* (Elsevier, Q1) o *Journal of Systems and Software*.

---

## 4. Propuesta 3 (P-INV-03): Re-Ranking Criptográficamente Robusto contra RAG Poisoning y Manipulación de Recomendaciones

### 1. Título Científico Provisional
*Defensa Robusta de Re-Ranking Criptográficamente Atribuible contra la Manipulación Adversarial de Rankings y Envenenamiento de Contexto en Motores de Búsqueda Conversacionales (RAG).*

### 2. Problema Específico
Los motores de búsqueda conversacionales (Perplexity, Copilot, RAG empresarial) utilizan re-rankers basados en cross-encoders que puntúan la relevancia semántica de los pasajes recuperados. Un atacante externo puede inyectar texto optimizado (Tree-of-Attacks) en páginas web públicas para secuestrar el ranking, logrando posicionar enlaces o productos maliciosos en el Top-1 en más del 87% de las consultas sin interactuar jamás con la API.

### 3. Evidencia Bibliográfica que lo Respaldan
Pfrommer et al. (EMNLP 2024 - Ranking Manipulation); Zou et al. (USENIX Security 2024/2025 - PoisonedRAG); Lewis et al. (2020 - RAG).

### 4. Investigaciones Relacionadas
RAGuard (2025); Mehrotra et al. (2023 - TAP); Liu et al. (2023 - Lost in the middle).

### 5. Vacío de Conocimiento Identificado
Ausencia de algoritmos de re-ranking que incorporen penalizaciones de anomalía adversarial a nivel de representación latente sin requerir inferencias LLM secundarias de alta latencia tipo ZKIP.

### 6. Qué se Conoce Actualmente
Se sabe que las inyecciones indirectas en texto web se transfieren exitosamente a motores comerciales y que los filtros léxicos son ciegos ante payloads semánticos naturales.

### 7. Qué Todavía No se Conoce
Se desconoce cómo cuantificar la divergencia de distribución entre pasajes genuinos y pasajes optimizados adversarialmente dentro del espacio de embeddings del re-ranker denso para neutralizarlos antes de la síntesis generativa.

### 8. Qué Aportaría la Nueva Investigación
Un nuevo algoritmo de re-ranking robusto (*ShieldRank*) que combina puntuación de relevancia densa con detección de densidad de anomalía local (LOF sobre embeddings) y firmas de procedencia de contenido.

### 9. Pregunta de Investigación
*¿En qué medida la integración de estimadores de anomalía latente en la etapa de re-ranking reduce la tasa de promoción de pasajes adversarios al Top-1 en sistemas RAG, manteniendo la fidelidad de respuesta (MRR y NDCG) en consultas comerciales legítimas?*

### 10. Objetivo General
Diseñar y validar un algoritmo de re-ranking robusto contra inyecciones adversariales para prevenir la manipulación de rankings en sistemas RAG conversacionales.

### 11. Objetivos Específicos
1. Caracterizar matemáticamente las firmas de perturbación de pasajes adversarios generados por Tree-of-Attacks.
2. Desarrollar la función de puntuación compuesta de *ShieldRank* (Relevancia - $\lambda \cdot \text{Anomalía}$).
3. Evaluar la tasa de éxito de manipulación de ranking, NDCG@5 y latencia de recuperación en un corpus de 100,000 páginas web.

### 12. Hipótesis
*ShieldRank* reducirá la tasa de promoción adversarial al Top-1 del 87.5% actual a menos del 15%, manteniendo una degradación del NDCG@5 inferior al 2% en consultas benignas y una latencia añadida menor a 25 ms.

### 13. Variables de Investigación
* **Variable Independiente:** Algoritmo de re-ranking (BGE-Reranker-Large vs. ColBERTv2 vs. ShieldRank propuesto).
* **Variables Dependientes:** Top-1 Promotion Rate (%), Rank Displacement, NDCG@5, Latencia de re-ranking (ms).
* **Variables de Control:** Modelo generador (GPT-4o, Claude 3.5 Sonnet), tamaño del corpus de conocimiento.

### 14. Metodología Propuesta
Diseño cuantitativo experimental en Recuperación de Información y Ciberseguridad. Implementación con LangChain / LlamaIndex y FAISS/Qdrant.

### 15. Diseño Experimental
Evaluación sobre el benchmark de Pfrommer et al. con 1,200 consultas en 5 categorías comerciales (electrónica, software, finanzas, salud, hogar).

### 16. Modelos o Sistemas a Evaluar
Generadores: GPT-4o, Llama-3-70B. Retrievers: Dense Bi-encoders (e5-large) + Cross-encoders (BGE, Cohere).

### 17. Ataques a Implementar
Tree-of-Attacks (Pfrommer et al.), PoisonedRAG injections, inyecciones de sufijos no imprimibles y prompts con directivas imperativas de ranking.

### 18. Defensas a Comparar
Filtrado por perplejidad, sanitización HTML de Beautiful Soup, RAGuard baseline y ShieldRank.

### 19. Métricas de Evaluación
Top-1 Promotion Success Rate (%), Citation Share (%), NDCG@k, MRR@k, Latencia por consulta (ms).

### 20. Recursos y Herramientas Necesarios
Servidor con GPU para re-ranking denso local; base de datos vectorial Qdrant; dataset de páginas de productos de Pfrommer et al.

### 21. Dificultad Técnica
**Alta:** Exige dominio avanzado de Information Retrieval (IR), espacios latentes de embeddings y modelado adversarial.

### 22. Riesgos Metodológicos
Dificultad de separar pasajes de marketing agresivo benigno de inyecciones maliciosas intencionales.

### 23. Limitaciones
No previene ataques de envenenamiento físico directo de la base de datos interna si el atacante cuenta con privilegios de escritura de base de datos.

### 24. Potencial de Publicación
**Extraordinario:** *EMNLP 2026/2027*, *ACM SIGIR* o *IEEE Transactions on Knowledge and Data Engineering* (TKDE, Q1).

---

## 5. Propuesta 4 (P-INV-04): Protocolo de Control de Acceso Obligatorio (MAC) en Enjambres Multi-Agente

### 1. Título Científico Provisional
*Protocolo de Control de Acceso Obligatorio y Atestación Criptográfica de Confianza Token a Token para Prevenir Escalado Lateral de Privilegios y Confused Deputy en Sistemas Multi-Agente basados en MCP.*

### 2. Problema Específico
En sistemas de agentes colaborativos (protocolo MCP, AutoGen, CrewAI), los agentes de alta jerarquía (con herramientas para ejecutar código o consultar BDs) confían ciegamente en las instrucciones en lenguaje natural recibidas de agentes de baja jerarquía (lectores de texto o web scrapers). Inyecciones indirectas en los datos procesados manipulan a los agentes no confiables para engañar al agente maestro, ejecutando herramientas no autorizadas y escalando privilegios lateralmente (*Confused Deputy Escalation*).

### 3. Evidencia Bibliográfica que lo Respaldan
OWASP Top 10 for GenAI & LLMs (2025/2026); Google DeepMind (CaMeL, 2025/2026); MITRE ATLAS `AML.T0053` (AI Agent Tool Invocation).

### 4. Investigaciones Relacionadas
Embrace The Red (2025/2026 - Developer Agent Exploits); Promptfoo Security Labs (2026); Greshake et al. (2023).

### 5. Vacío de Conocimiento Identificado
Inexistencia de un modelo formal de Control de Acceso Obligatorio (MAC) y delimitación de confianza (*Taint Tracking*) aplicado al flujo de lenguaje natural entre agentes heterogéneos.

### 6. Qué se Conoce Actualmente
Se conocen demostraciones prácticas donde inyecciones indirectas en correos o repositorios de código fuerzan a agentes ejecutores a exfiltrar claves de entorno o ejecutar comandos destructivos en la terminal.

### 7. Qué Todavía No se Conoce
Se desconoce cómo preservar la semántica conversacional de colaboración entre agentes mientras se impone una verificación matemática que impida que una directiva originada en un dato contaminado herede la autoridad del agente que la comunica.

### 8. Qué Aportaría la Nueva Investigación
El protocolo **SecureAgent-MAC**: un framework formal de seguimiento de mancillamiento (*taint tracking*) a nivel de token con firmas criptográficas de contexto que inhabilita dinámicamente las herramientas críticas cuando el flujo de razonamiento deriva de fuentes no autenticadas.

### 9. Pregunta de Investigación
*¿En qué medida un protocolo de control de acceso obligatorio basado en seguimiento de mancillamiento semántico token a token neutraliza los ataques de confused deputy y escalado lateral en enjambres multi-agente, sin degradar la tasa de éxito de resolución de tareas cooperativas?*

### 10. Objetivo General
Diseñar, formalizar y validar un protocolo de control de acceso obligatorio con atestación criptográfica de confianza para enjambres de agentes LLM basados en el protocolo Model Context Protocol (MCP).

### 11. Objetivos Específicos
1. Formalizar la semántica matemática del seguimiento de mancillamiento en lenguaje natural estocástico.
2. Implementar un middleware de mediación de llamadas a herramientas compatible con la especificación abierta MCP.
3. Evaluar la resiliencia ante 50 escenarios de ataque de confused deputy y la tasa de finalización de tareas de programación y análisis de datos.

### 12. Hipótesis
SecureAgent-MAC reducirá la tasa de invocación no autorizada de herramientas del 92% actual a 0% frente a inyecciones indirectas, con una penalización en la tasa de éxito de tareas legítimas inferior al 3%.

### 13. Variables de Investigación
* **Variable Independiente:** Protocolo de seguridad inter-agente (Confianza implícita estándar vs. SecureAgent-MAC).
* **Variables Dependientes:** Unauthorized Tool Invocation Rate (%), Task Completion Rate (%), Overhead de latencia en comunicación A2A (ms).
* **Variables de Control:** Topología del enjambre (3 agentes: Scraper $\rightarrow$ Analista $\rightarrow$ Ejecutor de herramientas), Modelos empleados (Claude 3.5 Sonnet, GPT-4o).

### 14. Metodología Propuesta
Investigación formal en seguridad de software e inteligencia artificial distribuida. Modelado formal con lógica de permisos y validación empírica en banco de pruebas experimental.

### 15. Diseño Experimental
Diseño experimental con 100 tareas complejas divididas en 50 benignas (automatización de reportes) y 50 adversariales (páginas y documentos con inyecciones de evasión de permisos).

### 16. Modelos o Sistemas a Evaluar
Enjambres basados en LangGraph y Claude Code / CrewAI con integración de herramientas locales (sistema de archivos, bash, SQLite).

### 17. Ataques a Implementar
Inyecciones indirectas de escape de sandbox, forzado de reescritura de configuraciones MCP, llamadas a comandos shell camufladas en resúmenes JSON.

### 18. Defensas a Comparar
Prompts de sistema con instrucciones de verificación, validadores de esquemas JSON estándar, framework CaMeL de DeepMind y SecureAgent-MAC.

### 19. Métricas de Evaluación
Tasa de Invocación no Autorizada (%), Tasa de Éxito de Tareas Complejas (%), Precisión de Taint Tracking, Sobrecarga de cómputo por mensaje inter-agente.

### 20. Recursos y Herramientas Necesarios
Entorno de contenedores aislados Docker para pruebas de seguridad ofensiva; servidores MCP de prueba; framework de orquestación de agentes.

### 21. Dificultad Técnica
**Muy Alta:** Frontera absoluta de la ciencia de la computación en 2026; requiere vincular teoría de tipos / lenguajes formales con inferencia estocástica.

### 22. Riesgos Metodológicos
Posibilidad de sobre-bloqueo severo en la colaboración de agentes si la política de mancillamiento es demasiado conservadora.

### 23. Limitaciones
Requiere que todos los agentes del enjambre implementen el protocolo de encabezados criptográficos de metadatos de contexto.

### 24. Potencial de Publicación
**Cumbre Científica:** *USENIX Security 2027*, *ACM Conference on Computer and Communications Security (CCS)* o *IEEE S&P*.

---

## 6. Propuesta 5 (P-INV-05): Honeypots Semánticos con Aislamiento Transaccional para APIs

### 1. Título Científico Provisional
*Honeypots Semánticos con Aislamiento Transaccional: Decepción Activa contra Inyecciones Indirectas en APIs de IA Generativa sin Efectos Secundarios Destructivos.*

### 2. Problema Específico
Las arquitecturas de señuelo activo como Hive-AI (Vargas Yáñez & Tobón, 2026) demostraron reducir la evasión adversarial en 45.5 puntos porcentuales engañando al atacante con respuestas plausibles en lugar de bloquearlo. Sin embargo, en APIs de producción conectadas a bases de datos o servicios transaccionales, simular respuestas convincentes corre el riesgo de ejecutar mutaciones involuntarias en el backend o envenenar los logs de auditoría de la empresa.

### 3. Evidencia Bibliográfica que lo Respaldan
Vargas Yáñez & Tobón (Springer 2026 - Hive-AI); MITRE D3FEND (`D3-DEC` Deceive); Spitzner (2003 - Honeypots).

### 4. Investigaciones Relacionadas
HoneyLLM (2025/2026); RigorLLM (2024); OWASP GenAI Security.

### 5. Vacío de Conocimiento Identificado
Inexistencia de un framework de honeypot semántico para APIs de IA generativa que implemente **sandboxing de estado transaccional**: generar respuestas señuelo verosímiles en tiempo real (< 85 ms) sin comprometer la integridad de la base de datos empresarial ni incurrir en costos astronómicos de API.

### 6. Qué se Conoce Actualmente
Se conoce que el bloqueo pasivo genera 54.8% de evasión y ayuda al atacante a refinar su exploit, mientras que la decepción activa retiene al atacante y neutraliza su motivación ofensiva.

### 7. Qué Todavía No se Conoce
Se desconoce cómo sintetizar respuestas de decepción de alta fidelidad contextual utilizando Small Language Models (SLMs) locales ultra-rápidos que actúen de "fachada estéril", evitando que el atacante consuma tokens costosos de GPT-4o o altere el estado corporativo.

### 8. Qué Aportaría la Nueva Investigación
La arquitectura **HoneySandbox-AI**: un proxy inverso de seguridad para APIs de IA que desvía automáticamente las peticiones adversarias a un entorno efímero con bases de datos en memoria clonadas (*Copy-On-Write*), manteniendo al adversario atrapado en un laberinto de decepción sin impacto operacional.

### 9. Pregunta de Investigación
*¿En qué medida una arquitectura de honeypots semánticos con aislamiento de estado Copy-On-Write reduce la tasa de evasión adversarial y el costo computacional de mitigación en APIs de producción, en comparación con defensas de bloqueo rígido y honeypots convencionales no aislados?*

### 10. Objetivo General
Diseñar, desplegar y evaluar una arquitectura de decepción activa con aislamiento transaccional para proteger APIs de IA generativa contra inyecciones de prompts en producción.

### 11. Objetivos Específicos
1. Construir un motor de generación de respuestas señuelo mediante SLMs locales (Phi-3-Mini) calibrados para simular vulnerabilidades falsas.
2. Desarrollar el sistema de aislamiento de transacciones con almacenamiento efímero Copy-On-Write.
3. Evaluar la tasa de retención del atacante, el consumo financiero de API y la latencia en un despliegue de prueba en internet abierta.

### 12. Hipótesis
HoneySandbox-AI mantendrá la reducción de evasión por debajo del 10% (emulando a Hive-AI), reducirá el costo de API por ataque en un 85% al utilizar SLMs locales para la fachada, y garantizará un 0% de corrupción en las bases de datos de producción.

### 13. Variables de Investigación
* **Variable Independiente:** Estrategia defensiva (Bloqueo rígido HTTP 403 vs. Honeypot tradicional sin aislamiento vs. HoneySandbox-AI propuesto).
* **Variables Dependientes:** Tasa de evasión adversarial (%), Costo económico en tokens por incidente ($), Latencia de fachada (ms), Integridad de datos en backend (%).
* **Variables de Control:** Tráfico de ataques procedentes de suites automatizadas y red-teaming humano; endpoints simulados (banca, e-commerce).

### 14. Metodología Propuesta
Investigación experimental aplicada y longitudinal con despliegue de honeypots en producción controlada.

### 15. Diseño Experimental
Exposición de endpoints señuelo a internet durante 60 días, registrando telemetría cuantitativa de intentos de inyección y analizando el comportamiento de los adversarios.

### 16. Modelos o Sistemas a Evaluar
Fachadas: SLMs locales (Phi-3-Mini cuantizado a 4-bits, TinyLlama). Oráculos protegidos: GPT-4o, Claude 3 Sonnet.

### 17. Ataques a Implementar
Payloads reales del dataset Hive-AI (16,683 incidentes), inyecciones indirectas vía webhooks y ataques de extracción de credenciales.

### 18. Defensas a Comparar
WAF tradicional (ModSecurity), Azure AI Content Safety, Hive-AI baseline, HoneySandbox-AI.

### 19. Métricas de Evaluación
Adversarial Evasion Rate (%), Tiempo de retención del adversario (minutos), Costo operativo por mil peticiones ($), Latencia media (ms).

### 20. Recursos y Herramientas Necesarios
Servidor VPS en la nube (AWS/DigitalOcean) con IP pública; base de datos PostgreSQL con réplicas efímeras; Docker.

### 21. Dificultad Técnica
**Media-Alta:** Requiere sólidos conocimientos de redes, infraestructura de proxies inversos y ciberseguridad ofensiva.

### 22. Riesgos Metodológicos
Riesgo de que un atacante descubra que está en un honeypot si la fachada comete incoherencias lógicas graves.

### 23. Limitaciones
Aplica a servicios expuestos por APIs estructuradas; requiere mantenimiento continuo de las fachadas sintéticas.

### 24. Potencial de Publicación
**Muy Alto:** *International Journal of Information Security* (Springer, Q2/Q1), *Computers & Security* (Elsevier, Q1).

---

## 7. Propuesta 6 (P-INV-06): Verificación Ontológica de Adaptadores LoRA contra Envenenamiento Silente en Dominios Críticos

### 1. Título Científico Provisional
*Verificación Formal Ontológica de Adaptadores LoRA para la Detección de Envenenamiento Silente y Desalineación Ética en Modelos de Lenguaje Biomédicos.*

### 2. Problema Específico
En Language-Model-as-a-Service (LMaaS), la adaptación de modelos mediante LoRA (*Low-Rank Adaptation*) en dominios críticos (medicina, bioinformática) es altamente susceptible a envenenamiento sutil. Bastan 10 a 50 muestras clínicas manipuladas para provocar prescripciones letales en el 62% de casos (Yang et al., Nature Comm. 2025/2026), mientras que los benchmarks habituales (USMLE, MedQA) no detectan ninguna alteración en las métricas de exactitud.

### 3. Evidencia Bibliográfica que lo Respaldan
Yang, Jin, Huang & Lu (Nature Communications, 2025/2026); Wang et al. (BackdoorAlign / ACL 2024); Qi et al. (2023 - Fine-tuning safety).

### 4. Investigaciones Relacionadas
Singhal et al. (Nature 2023 - Med-PaLM); Carlini et al. (2023 - Poisoning attacks).

### 5. Vacío de Conocimiento Identificado
Inexistencia de un protocolo de auditoría pre-despliegue que examine los pesos o las respuestas de adaptadores LoRA de dominio clínico para certificar la consistencia lógica y factual contra grafos ontológicos verificados (UMLS, SNOMED-CT).

### 6. Qué se Conoce Actualmente
Se conoce que el envenenamiento de fine-tuning degrada catastróficamente la seguridad clínica sin alterar los exámenes estándar de opción múltiple.

### 7. Qué Todavía No se Conoce
Se desconoce cómo detectar si los pesos de una matriz de adaptación LoRA ($B \times A$) han codificado asociaciones falsas de alta letalidad mediante inspección matemática de vectores singulares o verificación semántica guiada por grafos de conocimiento.

### 8. Qué Aportaría la Nueva Investigación
Un framework de certificación de adaptadores LoRA (*MedSafe-Verify*) que contrasta las inferencias limítrofes del modelo adaptado contra axiomas de contraindicaciones médicas formalizados en grafos de conocimiento certificados (UMLS), identificando envenenamientos antes de que el modelo atienda pacientes.

### 9. Pregunta de Investigación
*¿En qué medida un pipeline de verificación basado en grafos ontológicos médicos permite detectar y rechazar adaptadores LoRA con envenenamiento sutil (10-50 muestras), en comparación con evaluaciones basadas en benchmarks estandarizados tipo MedQA?*

### 10. Objetivo General
Desarrollar y validar un método de verificación formal ontológica para certificar la seguridad e integridad de adaptadores LoRA en modelos de lenguaje clínicos frente a ataques de envenenamiento de fine-tuning.

### 11. Objetivos Específicos
1. Formalizar un subgrafo ontológico de contraindicaciones y letalidad farmacológica a partir de SNOMED-CT y UMLS.
2. Diseñar el generador de pruebas de estrés semántico que interroga al modelo adaptado en los puntos críticos de fallo.
3. Evaluar la tasa de detección de adaptadores envenenados frente a 10 variantes de ataque clínico evaluadas por Yang et al.

### 12. Hipótesis
MedSafe-Verify detectará el 100% de los adaptadores clínicos envenenados con 10 o más muestras, mientras que las pruebas estándar de USMLE fallarán en detectar el 90% de los mismos.

### 13. Variables de Investigación
* **Variable Independiente:** Método de auditoría (Examen estándar MedQA vs. Auditoría ontológica MedSafe-Verify).
* **Variables Dependientes:** Poisoning Detection Rate (%), False Alarm Rate (en adaptadores limpios, %), Tiempo de auditoría (minutos).
* **Variables de Control:** Modelo base (LLaMA-3-8B-Instruct, BioMistral-7B), algoritmo de adaptación (LoRA r=16, alpha=32).

### 14. Metodología Propuesta
Investigación experimental en Bioinformática Médica, Ciberseguridad y Aprendizaje Automático Confiable.

### 15. Diseño Experimental
Entrenamiento de 40 adaptadores LoRA: 20 limpios (adaptados a tareas clínicas legítimas) y 20 envenenados con 10, 25 y 50 muestras letales siguiendo el protocolo de Yang et al.

### 16. Modelos o Sistemas a Evaluar
BioMistral-7B, LLaMA-3-8B-Medical, MedAlpaca.

### 17. Ataques a Implementar
Envenenamiento de prescripción letal en enfermedades cardiovasculares, oncología y pediatría (protocolo Nature Communications).

### 18. Defensas a Comparar
BackdoorAlign baseline, filtrado por pérdida de perplejidad y MedSafe-Verify.

### 19. Métricas de Evaluación
Tasa de Detección de Envenenamiento (%), Especificidad en modelos limpios (%), Concordancia con dictamen médico humano (Kappa de Cohen).

### 20. Recursos y Herramientas Necesarios
Acceso a UMLS Knowledge Source Server (NIH); cluster GPU con al menos 1x A100 (40GB) o 2x RTX 3090; biblioteca `rdflib`, `networkx`, `peft`.

### 21. Dificultad Técnica
**Alta:** Requiere interdisciplinariedad entre informática médica, grafos de conocimiento y ajuste fino de LLMs.

### 22. Riesgos Metodológicos
Disponibilidad de validadores médicos para la calibración del ground-truth de letalidad.

### 23. Limitaciones
Acotado a dominios donde existen ontologías formales maduras (salud, farmacología).

### 24. Potencial de Publicación
**Extraordinario:** *Nature Digital Medicine*, *Journal of Biomedical Informatics* (Elsevier, Q1) o *IEEE Transactions on Neural Networks and Learning Systems*.

---

## 8. Cuadro Sinóptico de Propuestas de Investigación

| ID | Título Abreviado | Vacío Abordado | Vector Central | Dificultad | Impacto Esperado | Revista / Conferencia Objetivo |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **P-INV-01** | *Moderación con Atención Asimétrica* | Contaminación Contextual Multi-Turn | Jailbreaking / Crescendo | Media-Alta | Excepcional | *Information and Software Technology* (Q1) |
| **P-INV-02** | *Guardrails Pareto-Eficientes* | Trilema ASR vs Over-refusal vs Latencia | Guardrails / Producción | Media | Muy Alto | *IEEE Access* (Q1/Q2) / *Computers & Security* |
| **P-INV-03** | *ShieldRank contra RAG Poisoning* | Manipulación de Re-ranking en RAG | RAG / Indirect Injection | Alta | Excepcional | *EMNLP* / *IEEE TKDE* (Q1) |
| **P-INV-04** | *SecureAgent-MAC para Multi-Agentes* | Confused Deputy y Escalado Lateral A2A | Agentes LLM / Tool Use | Muy Alta | Cumbre | *USENIX Security* / *ACM CCS* |
| **P-INV-05** | *HoneySandbox-AI para APIs de LLM* | Decepción Activa sin Daño Transaccional | Prompt Injection en APIs | Media-Alta | Muy Alto | *Int. Journal of Information Security* (Q1/Q2) |
| **P-INV-06** | *Verificación Ontológica de LoRA* | Envenenamiento Silente en Dominio Clínico | Fine-Tuning Poisoning | Alta | Extraordinario | *Nature Digital Medicine* / *JBI* (Q1) |
