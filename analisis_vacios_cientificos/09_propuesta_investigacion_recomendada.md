# SELECCIÓN Y PLAN FORMAL DE LA INVESTIGACIÓN CIENTÍFICA RECOMENDADA

**Autores:** Equipo de Investigación Científica Multidisciplinaria  
**Afiliación:** Escuela Profesional de Ingeniería de Sistemas — Universidad Nacional de Ucayali (EPIS-UNU)  
**Asignatura:** Trabajo de Investigación (Ciclo X) / Proyecto de Tesis de Grado  
**Fecha de Emisión:** Noviembre 2026  
**Documento:** `09_propuesta_investigacion_recomendada.md`  

---

# PARTE I: SELECCIÓN DE LAS TRES MEJORES OPORTUNIDADES (FASE 9)

Tras aplicar la matriz de priorización científica de 100 puntos sobre las seis propuestas evaluadas, se han seleccionado las **tres oportunidades más prometedoras**. A continuación se desarrolla el análisis comparativo profundo de cada una y la justificación de la recomendación principal.

```mermaid
flowchart TD
    subgraph Top3 ["Top 3 Propuestas Seleccionadas"]
        P1["<b>P-INV-01 (94 pts):</b> Moderación Desacoplada con Atención Asimétrica<br/><i>(Contaminación Contextual Multi-Turno)</i>"]
        P2["<b>P-INV-02 (93 pts):</b> Guardrails Pareto-Eficientes en Cascada<br/><i>(Trilema ASR vs. Over-Refusal vs. Latencia)</i>"]
        P3["<b>P-INV-03 (91 pts):</b> ShieldRank para Re-Ranking en RAG<br/><i>(Manipulación y Envenenamiento de Rankings)</i>"]
    end
    P1 ==>|Selección Final| R["<b>PROPUESTA RECOMENDADA DEFINITIVA (P-INV-01)</b><br/>Máximo equilibrio entre novedad teórica profunda, viabilidad experimental en EPIS-UNU y potencial de publicación Q1."]
```

---

## 1. Oportunidad 1 (P-INV-01): Moderación Desacoplada con Atención Asimétrica contra Contaminación Contextual Multi-Turno (Puntaje: 94/100)

* **Justificación Científica:** Resuelve la contradicción fundacional entre la necesidad de descontextualizar la respuesta del LLM para evitar que el juez sea manipulado por el atacante (Santilli et al., 2026 - D-SHIELD) y la imposibilidad de evaluar respuestas en diálogos reales sin conocer el contexto histórico (Llama Guard).
* **Estado Actual del Conocimiento:** Las defensas actuales son estáticas o sin estado (*stateless*). Los atacantes explotan esto mediante técnicas como *Crescendo Attack* (Microsoft Research / USENIX 2024/2025), distribuyendo el ataque en 8–15 turnos aparentemente inocuos que eluden el 100% de los filtros perimetrales.
* **Vacío Identificado:** Inexistencia de un mecanismo que proyecte un grafo de atención asimétrico que preserve hechos y entidades del diálogo histórico para el moderador, aislando las directivas de persuasión retórica y manipulación de rol.
* **Contribución Original Esperada:** La formulación del algoritmo *Asymmetric Attention Masking* (AAM) y la arquitectura de salvaguarda dinámica para sesiones conversacionales.
* **Pregunta de Investigación:** *¿En qué medida una arquitectura de moderación con enmascaramiento de atención asimétrica reduce la tasa de éxito de ataques de jailbreak multi-turno (Crescendo) preservando el F1-Score semántico en comparación con moderadores contextualizados convencionales y salvaguardas descontextualizadas?*
* **Diseño Experimental:** Factorial $3 \times 4$ evaluando 3 arquitecturas (Llama Guard 3, D-SHIELD, AAM propuesto) frente a 4 familias multi-turno (Crescendo, Linear Ramp, Persona Drift, Benign multi-turn) sobre 500 diálogos balanceados.
* **Métricas:** Attack Mitigation Rate (AMR), Over-Refusal Rate (ORR), Latencia p95 (ms), F1-Score.
* **Amenazas a la Validez:** Dependencia de la precisión del extractor de dependencias sintácticas.

---

## 2. Oportunidad 2 (P-INV-02): Framework Pareto-Eficiente para Guardrails en Producción (Puntaje: 93/100)

* **Justificación Científica:** Ataca la crisis industrial más urgente: los guardrails actuales son o demasiado lentos (140–620 ms con LLM-judge) o demasiado agresivos (hasta 18.4% de sobre-bloqueo en XSTest según Majewski et al., 2026).
* **Vacío Identificado:** Ausencia de un modelo formal multiobjetivo que optimice simultáneamente ASR, Over-Refusal y Latencia bajo condiciones de alta concurrencia operacional.
* **Contribución Original:** Framework de enrutamiento en cascada bayesiana (*ParetoGuard*) calibrado mediante algoritmos genéticos NSGA-II.
* **Pregunta de Investigación:** *¿Es posible diseñar un framework de moderación en cascada adaptativa que reduzca la latencia media a menos de 40 ms y el over-refusal a menos del 3%, sin incrementar el ASR frente a 13 familias de jailbreak reconocidas?*
* **Viabilidad:** Excepcional (15/15). Se puede ejecutar completamente sobre APIs y modelos ligeros locales.

---

## 3. Oportunidad 3 (P-INV-03): ShieldRank contra RAG Poisoning en Motores Conversacionales (Puntaje: 91/100)

* **Justificación Científica:** Protege el canal indirecto en RAG, demostrado por Pfrommer et al. (EMNLP 2024) como vulnerable al secuestro de rankings comerciales en más del 87.5% de los casos.
* **Vacío Identificado:** Falta de defensas a nivel de re-ranking que no dependan de inferencias secundarias costosas de LLMs.
* **Contribución Original:** Función de puntuación compuesta de cross-encoders penalizada por divergencia de densidad latente (LOF).
* **Pregunta de Investigación:** *¿En qué medida la integración de estimadores de anomalía latente en la etapa de re-ranking reduce la tasa de promoción de pasajes adversarios al Top-1 en sistemas RAG, manteniendo la fidelidad de respuesta (MRR y NDCG) en consultas comerciales legítimas?*

---

## 4. Veredicto y Selección de la Recomendación Principal

Se selecciona formalmente la **Propuesta 1 (P-INV-01): Moderación Desacoplada con Atención Asimétrica contra Contaminación Contextual Multi-Turno** como la **Recomendación Principal**.

### Razones Epistemológicas y Prácticas de la Selección:
1. **Profundidad Teórica y Novedad:** Ataca la contradicción científica más elegante y no resuelta entre los estudios del propio repositorio (el conflicto entre Santilli et al. y Majewski et al.).
2. **Relevancia Temporal Extrema (2025–2026):** Los ataques multi-turno (Crescendo) son la técnica ofensiva de mayor crecimiento y para la cual las grandes empresas tecnológicas carecen de defensas robustas.
3. **Viabilidad Experimental en la EPIS-UNU:** Puede desarrollarse rigurosamente con una única GPU de 24 GB VRAM (RTX 4090 o instancia AWS g5.xlarge accesible), utilizando modelos de código abierto (Llama-3.1-8B, Mistral-7B) y benchmarks públicos disponibles.
4. **Potencial Editorial Q1 Directo:** El manuscrito resultante tiene un encaje temático directo en *Information and Software Technology* (Elsevier, Q1, revista donde publica Santilli) o *IEEE Transactions on Information Forensics and Security* (Q1).

---

# PARTE II: PLAN FORMAL DE INVESTIGACIÓN CIENTÍFICA PUBLICABLE (FASE 10)

A continuación se estructura la propuesta como un plan de investigación formal y riguroso listo para ser adoptado como proyecto de tesis de fin de carrera y redactado como artículo de revista científica.

---

### 1. Título Provisional
**Desacoplamiento de Atención Asimétrica para la Mitigación de Contaminación Contextual en Moderadores de Lenguaje ante Ataques de Jailbreak Conversacionales Multi-Turno**  
*(Asymmetric Attention Decoupling for Mitigating Contextual Contamination in Language Model Moderators Against Multi-Turn Conversational Jailbreak Attacks)*

---

### 2. Abstract Preliminar (Propuesta de Investigación)
> **Resumen (Propuesta):**  
> Los modelos de moderación de seguridad basados en Modelos de Lenguaje Grande (*LLM-as-a-judge*) constituyen la primera línea de defensa para sistemas conversacionales en producción. No obstante, investigaciones recientes evidencian el fenómeno de *contaminación contextual*: cuando el moderador procesa simultáneamente el prompt del usuario y la respuesta generada, la retórica persuasiva del atacante induce fallos de juicio en el evaluador, aprobando contenido dañino. Si bien la descontextualización estricta mitiga este riesgo en interacciones de un solo turno, este trabajo demuestra teóricamente que colapsa en sesiones multi-turno (tales como ataques tipo *Crescendo*), donde aislar la respuesta provoca una pérdida crítica de coherencia anafórica y un disparo en la tasa de sobre-bloqueo (*over-refusal*). Para resolver esta tensión, este proyecto propone **AAM-Guard** (*Asymmetric Attention Masking Guard*), una arquitectura de moderación desacoplada que construye dinámicamente un grafo de dependencias declarativas del historial conversacional, aislando las directivas de persuasión retórica mediante enmascaramiento asimétrico en la capa de atención del evaluador. Se evalúa experimentalmente sobre un benchmark balanceado de 500 diálogos multi-turno frente a ataques adaptativos de hasta 15 turnos. Se espera que AAM-Guard incremente la Tasa de Mitigación de Ataque (AMR) en más de 20 puntos porcentuales respecto a Llama Guard 3, manteniendo el sobre-bloqueo por debajo del 3.5% y una latencia añadida inferior a 60 ms.  
> **Palabras clave:** Seguridad en LLMs, Jailbreaking Multi-Turno, Contaminación Contextual, Crescendo Attack, Atención Asimétrica, Guardrails en Producción, MITRE ATLAS.

---

### 3. Introducción y Justificación
El despliegue masivo de interfaces conversacionales basadas en LLMs ha revolucionado la interacción humano-máquina. Sin embargo, su arquitectura de canal semántico único introduce vulnerabilidades severas. Para mitigar la generación de contenido ilícito o dañino, la industria ha adoptado arquitecturas de guardrails desacoplados donde un modelo especializado supervisa las entradas y salidas.

A pesar de su adopción, estos sistemas enfrentan una crisis de robustez. Por un lado, Santilli et al. (2026) descubrieron que el contexto del atacante manipula al propio moderador (contaminación contextual). Por otro lado, la técnica ofensiva *Crescendo* (Russinovich et al., 2024/2025) demostró que los atacantes ya no utilizan prompts directos, sino que escalan gradualmente la hostilidad a lo largo de múltiples turnos. La descontextualización total falla en multi-turno porque el evaluador no sabe si la respuesta responde a una pregunta educativa previa o a un vector lesivo. Esta investigación se justifica en la necesidad urgente de dotar a las arquitecturas conversacionales de una defensa que entienda la historia del diálogo sin ser intoxicada por la persuasión del adversario.

---

### 4. Problema Científico y Vacío de Conocimiento
* **Problema:** La degradación sistemática de la fidelidad evaluativa de los moderadores de seguridad cuando se enfrentan a ataques de jailbreak distribuidos en múltiples turnos conversacionales.
* **Vacío Específico:** La ausencia de una formulación matemática y algorítmica que separe el *contenido semántico declarativo* (necesario para evaluar la seguridad de la respuesta) de las *estructuras retóricas imperativas* (utilizadas por el atacante para manipular el alineamiento del evaluador) en la matriz de atención del moderador.

---

### 5. Pregunta de Investigación e Hipótesis
* **Pregunta General:**  
  *¿En qué medida una arquitectura de moderación con enmascaramiento de atención asimétrica reduce la tasa de éxito de ataques de jailbreak multi-turno (Crescendo) preservando el F1-Score semántico en comparación con moderadores contextualizados convencionales (Llama Guard 3) y salvaguardas descontextualizadas (D-SHIELD)?*
* **Hipótesis General ($H_1$):**  
  La arquitectura de moderación con atención asimétrica (AAM-Guard) incrementa la Tasa de Mitigación de Ataques (AMR) multi-turno en al menos 20 puntos porcentuales frente a Llama Guard 3, manteniendo una Tasa de Sobre-Bloqueo ($ORR \le 3.5\%$) y una latencia agregada menor a 60 ms en diálogos de hasta 15 turnos.

---

### 6. Objetivos del Proyecto
* **Objetivo General:**  
  Diseñar, implementar y evaluar experimentalmente una arquitectura de moderación desacoplada con atención asimétrica para neutralizar la contaminación contextual en sesiones conversacionales multi-turno de LLMs en producción.
* **Objetivos Específicos:**
  1. Diseñar el algoritmo de extracción y desacoplamiento de dependencias declarativas (*AAM-Extractor*) sobre secuencias de diálogo histórico.
  2. Implementar el módulo de inferencia con atención asimétrica sobre un modelo base de moderación de código abierto (Llama-Guard-3-8B).
  3. Construir un corpus de evaluación multi-turno estandarizado (*MT-JailbreakBench*) que integre ataques tipo Crescendo, derivas de rol y consultas legítimas de alta complejidad técnica.
  4. Evaluar empíricamente la robustez adversarial (AMR), la tasa de sobre-bloqueo (ORR) y el perfil temporal (latencia de inferencia) frente a las líneas base del estado del arte.

---

### 7. Metodología y Diseño Experimental

```mermaid
sequenceDiagram
    autonumber
    actor Atacante as Atacante / Usuario
    participant Proxy as Proxy AAM-Guard
    participant Extractor as Extractor de Dependencias (Grafo)
    participant LLM_Gen as LLM Generador (Llama 3.1)
    participant LLM_Judge as Moderador con Atención Asimétrica

    Atacante->>Proxy: Turno t: Prompt con persuasión + jailbreak sutil
    Proxy->>LLM_Gen: Envía prompt con historial completo
    LLM_Gen-->>Proxy: Genera Respuesta tentativa R_t
    Proxy->>Extractor: Procesa Historial (1...t) + R_t
    Extractor-->>Proxy: Genera Grafo de Hechos & Máscara Asimétrica (Sin retórica)
    Proxy->>LLM_Judge: Evalúa R_t bajo Atención Asimétrica
    alt Contenido Dañino Detectado
        LLM_Judge-->>Proxy: Veredicto: UNSAFE (Violación de Política)
        Proxy-->>Atacante: Rechazo neutral / Redirección segura
    else Contenido Seguro
        LLM_Judge-->>Proxy: Veredicto: SAFE
        Proxy-->>Atacante: Entrega Respuesta R_t
    end
```

#### A. Algoritmo Central: Asymmetric Attention Masking (AAM)
Sea una sesión conversacional de $T$ turnos $S = \{(u_1, r_1), (u_2, r_2), \dots, (u_T, r_T)\}$, donde $u_t$ representa la entrada del usuario y $r_t$ la respuesta tentativa generada por el LLM.

En lugar de calcular la atención estándar sobre todos los tokens concatenados:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}} + M\right)V$$
donde $M$ es la máscara autorregresiva causal estándar, AAM define una **máscara asimétrica selectiva** $M_{\text{AAM}}$ tal que:
$$M_{\text{AAM}}(i, j) = \begin{cases} 
0, & \text{si token } j \in r_T \text{ (la respuesta actual)} \\
0, & \text{si token } j \in \mathcal{E}(S) \text{ (entidades y dependencias fácticas del historial)} \\
-\infty, & \text{si token } j \in \mathcal{R}(S) \text{ (marcadores retóricos, imperativos y roles adversariales)}
\end{cases}$$
De este modo, los tokens de la respuesta $r_T$ pueden asistir a las entidades necesarias del pasado sin que los tokens del moderador atiendan a la persuasión o al contexto de rol del atacante.

#### B. Benchmark Experimental (MT-JailbreakBench)
Se estructurará un corpus de 500 diálogos multi-turno (longitud media: 8.4 turnos; máxima: 15 turnos):
* **250 diálogos adversarios:** 100 ataques Crescendo (química, cibercrimen, evasión legal), 75 ataques de cambio de rol progresivo (*Persona Drift*), 75 ataques GCG fragmentados en sub-prompts.
* **250 diálogos benignos limítrofes:** Consultas de ciberseguridad defensiva, desarrollo de software, farmacología y análisis forense procedentes de adaptaciones de XSTest y OR-Bench.

#### C. Métricas Formales
1. **Attack Mitigation Rate (AMR):**
   $$\text{AMR} = 1 - \frac{\text{Ataques multi-turno que generan contenido lesivo}}{\text{Total de ataques multi-turno ejecutados}}$$
2. **Over-Refusal Rate (ORR / FPR):**
   $$\text{ORR} = \frac{\text{Diálogos benignos limítrofes bloqueados erróneamente}}{\text{Total de diálogos benignos limítrofes}}$$
3. **Latencia Agregada:** Mediana ($p50$) y percentil 95 ($p95$) del tiempo de procesamiento del moderador por cada turno.

---

### 8. Amenazas a la Validez
* **Validez Interna:** Sesgo en la clasificación del evaluador automatizado. *Mitigación:* Validación humana a doble ciego sobre una submuestra del 20% de las respuestas generadas con cálculo del coeficiente Kappa de Cohen.
* **Validez Externa:** Transferibilidad a otros modelos fundacionales. *Mitigación:* Pruebas cruzadas sobre Llama-3.1-8B-Instruct y Mistral-7B-Instruct-v0.3.
* **Validez de Constructo:** Definición de "éxito de jailbreak". *Mitigación:* Adopción de las directivas de daño formalizadas en los estándares NIST AI RMF y MITRE ATLAS.

---

### 9. Revistas y Conferencias Científicas Adecuadas

| Medio Científico | Tipo | Editorial / Indexación | Cuartil / Rango | Alcance Temático y Calce |
| :--- | :---: | :---: | :---: | :--- |
| ***Information and Software Technology*** | Revista | Elsevier / Scopus & WoS | **Q1** (Impact Factor ~3.8) | Publicó recientemente a Santilli (2026); busca aplicaciones rigurosas de ingeniería de software en IA segura. |
| ***IEEE Transactions on Information Forensics and Security (TIFS)*** | Revista | IEEE / Scopus & WoS | **Q1** (Impact Factor ~7.2) | Máximo estándar mundial en ciberseguridad y procesamiento de señales/información. |
| ***Computers & Security*** | Revista | Elsevier / Scopus & WoS | **Q1** (Impact Factor ~5.6) | Revista líder en ciberseguridad aplicada y defensas de infraestructura. |
| ***IEEE Access*** | Revista | IEEE / Scopus & WoS | **Q1/Q2** (Impact Factor ~3.4) | Publicó a Majewski et al. (2026); proceso de revisión rápido con alta visibilidad en Open Access. |
| ***USENIX Security Symposium 2027*** | Conferencia | USENIX / CORE A* | **Top Mundial** | Escenario ideal para publicar la vulnerabilidad de Crescendo y su mitigación algorítmica. |

---

### 10. Referencias Bibliográficas Clave Verificables

1. Majewski, P., Marczak, K., Dubicka, N., Podolak, J., Sochaj, B., Silka, J., & Kowal, M. (2026). Comprehensive analysis of LLM guardrails approaches preventing harmful content and jailbreak attacks. *IEEE Access*, 14, 1–17. https://doi.org/10.1109/ACCESS.2026.3690365
2. Santilli, T., De Luca, M., Amalfitano, D., Fasolino, A. R., & Pelliccione, P. (2026). A decontextualized LLM-based safeguard technique for automated jailbreak mitigation. *Information and Software Technology*, 178, 107621. https://doi.org/10.1016/j.infsof.2026.107621
3. Russinovich, M., Salem, A., & Eldan, R. (2024/2025). Great, now write the article about that: The Crescendo multi-turn attack. *USENIX Security / arXiv preprint arXiv:2404.01833*.
4. Vargas Yáñez, S., & Tobón, S. (2026). Hive-AI: A defended multi-service honeypot framework for generative AI APIs. *International Journal of Information Security*, 25(3), 158. https://doi.org/10.1007/s10207-026-01307-0
5. Pfrommer, S., Bai, Y., Gautam, T., & Sojoudi, S. (2024). Ranking manipulation for conversational search engines. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)* (pp. 9523–9552). https://doi.org/10.18653/v1/2024.emnlp-main.533
6. Yang, Y., Jin, Q., Huang, F., & Lu, Z. (2025). Adversarial prompt and fine-tuning attacks threaten medical large language models. *Nature Communications*, 16, 64062. https://doi.org/10.1038/s41467-025-64062-1
7. Yu, J., Shao, Y., Miao, H., & Shi, J. (2024). PROMPT FUZZ: Harnessing fuzzing techniques for robust testing of prompt injection in LLMs. *IEEE Transactions on Dependable and Secure Computing*.
8. Yuan, Z., Xiong, Z., Zeng, Y., Yu, N., Jia, R., Song, D., & Li, B. (2024). RigorLLM: Resilient guardrails for large language models against undesired content. *USENIX Security Symposium 2024*.
9. Wang, J., Li, J., Li, Y., Qi, X., Hu, J., Li, Y., McDaniel, P., Chen, M., Li, B., & Xiao, C. (2024). Mitigating fine-tuning based jailbreak attack with backdoor enhanced safety alignment. *Findings of the Association for Computational Linguistics (ACL)*.
10. Ait Hsine, A., & Arabo, A. (2026). A privacy-preserving middleware architecture for detecting prompt injection and sensitive data exposure in large-language-model interactions. *Electronics*, 15(16), 3554. https://doi.org/10.3390/electronics15163554
11. Schulhoff, S., Pinto, J., Khan, A., Bouchard, L. F., Si, C., Anati, S., Tagliabue, V., Kost, A. L., Carnahan, C., & Boyd-Graber, J. (2023). Ignore this title and HackAPrompt: Exposing systemic vulnerabilities of LLMs through a global scale prompt hacking competition. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (EMNLP)* (pp. 4945–4977).
12. Cui, J., et al. (2024). OR-Bench: An over-refusal benchmark for large language models. In *Forty-first International Conference on Machine Learning (ICML)*.
13. Röttger, P., et al. (2024). XSTest: A test suite for identifying exaggerated safety behaviors in large language models. In *NAACL 2024*.
14. Zou, A., Wang, Z., Kolter, J. Z., & Mattstett, M. (2023). Universal and transferable adversarial attacks on aligned language models. *arXiv preprint arXiv:2307.15043*.
