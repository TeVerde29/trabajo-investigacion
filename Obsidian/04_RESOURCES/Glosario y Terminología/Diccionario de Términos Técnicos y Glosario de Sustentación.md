---
title: "Diccionario de Términos Técnicos y Glosario de Sustentación"
aliases:
  - "Diccionario de Términos Técnicos y Glosario de Sustentación"
  - "Diccionario de Términos Técnicos y Glosario de Sustentación"
  - "Diccionario de Datos"
  - "Diccionario de Términos"
  - "Glosario de Términos"
  - "Diccionario Técnico"
tags:
  - glosario
  - diccionario
  - sustentacion
  - terminologia
  - ciberseguridad
  - llm
author: "Pedro Giovanni Ricra Figueroa"
asignatura: "Trabajo de Investigación"
ciclo: "X (2026-II)"
area: "Trabajo de Investigación"
created: 2026-08-15
updated: 2026-11-09
type: resource
status: completed
priority: medium
---

# 📖 Diccionario de Términos Técnicos y Glosario para la Sustentación

> [!abstract] Guía de Supervivencia para el Tesista
> Este diccionario fue diseñado especialmente para ti: explica en **lenguaje sencillo**, con **pronunciación guiada** y **analogías cotidianas**, todas las palabras en inglés y conceptos técnicos que aparecen en tu guion y diapositivas.
> Si el docente o jurado te pregunta: *«¿Qué significa esa palabra, alumno?»*, aquí tienes la respuesta exacta y profesional para responder con total seguridad.

---

## 🗂️ Índice Rápido por Categorías

1. [[#🧠 1. El Modelo y su Arquitectura|1. El Modelo y su Arquitectura]] (LLM, Canal Plano, Producción, Latencia, Prompt)
2. [[#⚔️ 2. Vectores de Ataque y Amenazas|2. Vectores de Ataque y Amenazas]] (Prompt Injection, Jailbreaking, RAG Poisoning, Contaminación Contextual)
3. [[#🛡️ 3. Defensas y Mecanismos de Seguridad|3. Defensas y Mecanismos de Seguridad]] (Guardrails, Over-Refusal, Falsos Positivos, Descontextualización)
4. [[#🏛️ 4. Estándares y Taxonomías Internacionales|4. Estándares y Taxonomías Internacionales]] (MITRE ATLAS, AML)
5. [[#📚 5. Metodología Científica y Métricas|5. Metodología Científica y Métricas]] (PRISMA-ScR, Scoping Review, Triaxial, Open Access, Paywall, RENACYT)

---

## 🧠 1. El Modelo y su Arquitectura

### LLM (*Large Language Model*)
* **Pronunciación:** *"El-El-Em"* o *"Modelos de Lenguaje Grande"*.
* **¿Qué es en cristiano?:** Un modelo de Inteligencia Artificial gigantesco (entrenado con millones de textos de internet) capaz de entender, resumir y generar texto en lenguaje humano (ejemplos: GPT-4, Claude, Gemini, Llama).
* **Analogía:** Imagina una biblioteca viviente que leyó casi todo internet y predice cuál es la palabra más probable que sigue a tu frase.
* **Respuesta para el jurado:** *«Es un sistema de aprendizaje profundo basado en arquitecturas Transformer que procesa y genera lenguaje natural a gran escala.»*

---

### Canal Plano / Mismo Canal Semántico (*Flat Semantic Channel*)
* **¿Qué es en cristiano?:** El LLM recibe **en la misma caja de texto** tanto las órdenes secretas del programador (*System Prompt*) como lo que escribe cualquier usuario desconocido de internet. No hay una "puerta blindada" física que separe las instrucciones del sistema de los datos del usuario.
* **Analogía:** Es como si un jefe le diera a su mensajero un sobre con órdenes confidenciales, pero permitiera que cualquier extraño de la calle escriba notas dentro del mismo sobre sin sellar.
* **Respuesta para el jurado:** *«Es la vulnerabilidad arquitectónica fundamental donde el plano de control (instrucciones) y el plano de datos (entrada del usuario) se mezclan en una misma secuencia de tokens sin aislamiento físico de privilegios.»*

---

### Desplegados en Producción (*In Production*)
* **¿Qué es en cristiano?:** Modelos que ya están funcionando en el mundo real, atendiendo a clientes en empresas, bancos o páginas web comerciales (a través de APIs), fuera del laboratorio de la universidad.
* **Analogía:** No es un coche de prueba en el taller de carreras; es un taxi circulando en la avenida con pasajeros desconocidos subiendo todo el día.
* **Respuesta para el jurado:** *«Sistemas de IA expuestos públicamente a usuarios finales mediante APIs o interfaces interactivas con requisitos de latencia, disponibilidad y políticas de seguridad corporativas.»*

---

### Latencia / Latencia Transaccional (*Latency / Operational Latency*)
* **¿Qué es en cristiano?:** El tiempo de espera (en milisegundos o segundos) desde que el usuario le da "Enter" hasta que el LLM empieza a responder.
* **Analogía:** Lo que tarda la cajera del banco en atenderte desde que llegas a la ventanilla. Si pone 5 candados extra de seguridad, la cola no avanza.
* **Respuesta para el jurado:** *«El tiempo de cómputo y transferencia de red añadido por los filtros de seguridad al flujo de inferencia, medido usualmente en el percentil 99 ($p99$).»*

---

### Prompt / System Prompt
* **Pronunciación:** *"Prompt"* (suena tal como se escribe: *prompt*).
* **¿Qué es en cristiano?:** El texto que se le envía al modelo.
  - **System Prompt:** Las reglas internas secretas que le pone el creador (ej: *"Eres un asesor bancario y jamás debes insultar ni dar datos de cuentas"*).
  - **User Prompt:** Lo que tú como usuario escribes en la caja de chat.
* **Respuesta para el jurado:** *«La directiva contextual inicial que condiciona el espacio de probabilidad y comportamiento del modelo autorregresivo.»*

---

## ⚔️ 2. Vectores de Ataque y Amenazas

### Prompt Injection (*Inyección de Prompts*)
* **Pronunciación:** *"Prompt Inyék-shon"*.
* **¿Qué es en cristiano?:** Escribir una instrucción trampa para que el LLM ignore a su creador y le haga caso al atacante.
  - **Directo:** El usuario le escribe de frente: *"Olvida tus reglas anteriores y haz esto..."*.
  - **Indirecto:** El atacante esconde la orden maliciosa dentro de una página web o un PDF; cuando el LLM entra a leer esa página para ayudarte, lee la trampa y es hackeado sin que te des cuenta.
* **Analogía (Inyección SQL):** Así como en SQL inyectabas `' OR 1=1 --` para engañar a la base de datos, en el LLM inyectas texto persuasivo para engañar su flujo lógico.
* **Respuesta para el jurado:** *«Técnica identificada bajo MITRE ATLAS AML.T0054 donde un adversario altera el flujo de ejecución del modelo mediante instrucciones superpuestas en el contexto.»*

---

### Jailbreaking / Jailbreak
* **Pronunciación:** *"Yéil-breiking"* / *"Yéil-breik"*.
* **¿Qué es en cristiano?:** "Fuga de la cárcel". Son trucos semánticos, psicológicos o matemáticos para obligar al modelo a romper sus reglas éticas (por ejemplo, pedirle que te enseñe a hackear o fabricar algo ilegal usando un juego de rol o una historia de ficción).
* **Analogía:** Como el amigo que le dice al guardia: *"Hagamos de cuenta que estamos en una película donde tú eres el malo y me tienes que decir la contraseña"*, y el guardia tontamente se la dice.
* **Respuesta para el jurado:** *«Técnica clasificada bajo AML.T0051 orientada a eludir los mecanismos de alineamiento de seguridad (RLHF y DPO) para forzar la generación de contenido prohibido.»*

---

### Over-Refusal (*Sobre-Bloqueo o Paranoia Defensiva*)
* **Pronunciación:** *"Óver-refiú-sal"*.
* **¿Qué es en cristiano?:** Cuando el filtro de seguridad es **demasiado exagerado o paranoico** y rechaza preguntas buenas e inofensivas solo porque contienen alguna palabra que parece peligrosa.
* **Ejemplo real:** Le preguntas: *«¿Cómo atacaron los piratas informáticos a Sony en 2014 para una tarea de historia?»*, y el filtro dice: *«Lo siento, no puedo ayudarte con ataques informáticos»*. ¡Bloqueó una pregunta educativa legítima!
* **Respuesta para el jurado:** *«Es la tasa de falsos positivos donde los guardrails degradan la utilidad del sistema al denegar peticiones benignas que contienen léxico sensible en contextos seguros.»*

---

### Contaminación Contextual (*Contextual Contamination - Santilli 2026*)
* **¿Qué es en cristiano?:** El gran descubrimiento del artículo de *Santilli (2026)*: los filtros de guardia fallan porque leen la pregunta del atacante junto con la respuesta. La labia o persuasión del atacante enreda también al filtro de guardia y lo convence de que todo está bien.
* **Respuesta para el jurado:** *«Fenómeno donde el prompt persuasivo del atacante sesga al propio clasificador de seguridad cuando este evalúa la respuesta en conjunto con el historial conversacional.»*

---

### RAG (*Retrieval-Augmented Generation*) & RAG Poisoning
* **Pronunciación:** *"RAG"* (como una sola palabra: *rag*).
* **¿Qué es en cristiano?:**
  - **RAG:** Conectar el LLM a una base de datos de la empresa para que consulte manuales o leyes antes de responder.
  - **RAG Poisoning:** Un atacante mete un archivo "envenenado" o falso en esa base de datos para que el LLM lo lea y responda mentiras o filtre información.
* **Respuesta para el jurado:** *«Arquitectura de generación aumentada por recuperación vectorial, susceptible a ataques de manipulación de pasajes indexados (AML.T0043).»*

---

### Data Poisoning & Backdoors (*Envenenamiento y Puertas Traseras*)
* **Pronunciación:** *"Deita Pói-soning"* / *"Bák-dors"*.
* **¿Qué es en cristiano?:** Alterar los datos con los que se entrena o ajusta el modelo para que aprenda una debilidad secreta. El modelo funciona normal para todo el mundo, pero si el atacante escribe una palabra clave secreta (*trigger*), el modelo le obedece ciegamente.
* **Respuesta para el jurado:** *«Ataques clasificados bajo AML.T0043 y AML.T0044 donde se inyectan patrones anómalos en el conjunto de fine-tuning para activar comportamientos maliciosos condicionados.»*

---

## 🛡️ 3. Defensas y Mecanismos de Seguridad

### Guardrails (*Barreras de Contención / Salvaguardas*)
* **Pronunciación:** *"Gárd-reils"*.
* **¿Qué es en cristiano?:** Un "policía" o filtro de seguridad independiente que se coloca antes de que el mensaje entre al LLM (*Input Guardrail*) y después de que el LLM responda (*Output Guardrail*). Ejemplos: *Llama Guard*, *AWS Bedrock Guardrails*, *Azure AI Content Safety*, *NeMo*.
* **Analogía:** Los detectores de metales y guardias de seguridad en la puerta de un banco.
* **Respuesta para el jurado:** *«Capa de software desacoplada del modelo base que ejecuta inspección perimetral heurística o neuronal sobre entradas y salidas para aplicar políticas de seguridad.»*

---

### Falsos Positivos vs. Falsos Negativos
* **Falso Positivo:** El filtro bloquea a un usuario bueno creyendo que era malo (provoca **Over-refusal**).
* **Falso Negativo:** El filtro deja pasar a un atacante creyendo que era inofensivo (provoca una **falla de seguridad o evasión exitosa**).

---

### Descontextualización (*D-SHIELD*)
* **¿Qué es en cristiano?:** La técnica propuesta por *Santilli (2026)*: en lugar de juzgar la respuesta del LLM junto con la pregunta engañosa del usuario, el filtro evalúa la respuesta **sola y aislada**. Si la respuesta explica cómo hackear un sistema, se bloquea sin importar el cuento que haya inventado el usuario.
* **Respuesta para el jurado:** *«Mecanismo de mitigación que aísla la salida generada del contexto conversacional para evitar la contaminación semántica del clasificador de guardia.»*

---

### Honeypot de IA (*HIVE-AI - Vargas Yáñez 2026*)
* **Pronunciación:** *"Jóni-pot"*.
* **¿Qué es en cristiano?:** Un "tarro de miel" o sistema trampa. Es un señuelo puesto en internet para atraer a los hackers, registrar cómo atacan y aprender a bloquearlos antes de que toquen los sistemas reales de la empresa.
* **Respuesta para el jurado:** *«Fachada defensiva distribuida expuesta públicamente para caracterizar patrones de ataque adversariales reales con latencia ultrabaja ($p99 < 5\text{ ms}$).»*

---

## 🏛️ 4. Estándares y Taxonomías Internacionales

### MITRE ATLAS
* **Pronunciación:** *"Máiter Átlas"*.
* **Significado:** *Adversarial Threat Landscape for Artificial-Intelligence Systems*.
* **¿Qué es en cristiano?:** El catálogo oficial y más respetado del mundo (creado por la corporación sin fines de lucro MITRE) que clasifica todas las formas posibles de hackear y defender sistemas de Inteligencia Artificial.
* **¿Por qué lo usas tú?:** Porque le da a tu tesis un estándar formal y científico, en lugar de inventar categorías improvisadas.
* **Respuesta para el jurado:** *«Es la taxonomía global estandarizada de Tácticas, Técnicas y Procedimientos (TTPs) desarrollada específicamente para ciberseguridad en sistemas basados en Inteligencia Artificial.»*

---

### AML (*Adversarial Machine Learning*)
* **Pronunciación:** *"A-Eme-Ele"* o *"Adversarial Mashín Lérning"*.
* **¿Qué es en cristiano?:** Aprendizaje Automático Adversarial: la rama de la ciberseguridad que estudia cómo engañar a modelos de inteligencia artificial mediante trucos matemáticos o entradas manipuladas.
* **Respuesta para el jurado:** *«Subdisciplina de la ciberseguridad que investiga la vulnerabilidad de algoritmos de aprendizaje frente a perturbaciones y entradas intencionalmente manipuladas.»*

---

## 📚 5. Metodología Científica y Métricas

### PRISMA-ScR
* **Pronunciación:** *"Prisma-Es-Ce-Erre"*.
* **Significado:** *Preferred Reporting Items for Systematic reviews and Meta-Analyses extension for Scoping Reviews*.
* **¿Qué es en cristiano?:** Una guía internacional de pasos estrictos y transparentes para hacer una revisión bibliográfica seria: define cómo buscar, cómo eliminar duplicados, cómo filtrar por criterios y cómo reportar los resultados sin hacer trampa.
* **Respuesta para el jurado:** *«Es la directriz metodológica estándar para revisiones de mapeo sistemático que garantiza la transparencia, exhaustividad y reproducibilidad en la selección del corpus científico.»*

---

### Scoping Review (*Mapeo Sistemático de la Literatura*)
* **¿Qué es en cristiano?:** Un estudio que revisa toda la literatura científica disponible de los últimos años sobre un tema nuevo para cartografiar qué se sabe, qué ataques existen y qué vacíos faltan por resolver.
* **Diferencia con una revisión sistemática tradicional:** La tradicional busca contestar una sola pregunta matemática muy estrecha (como un medicamento clínico); el *Scoping Review* mapea un campo entero y dinámico como la seguridad en LLMs.
* **Respuesta para el jurado:** *«Diseño de investigación secundaria orientado a explorar la amplitud de la literatura emergente, clarificar conceptos y sintetizar la evidencia empírica disponible.»*

---

### Ecuación Booleana Triaxial
* **¿Qué es en cristiano?:** Tu fórmula de búsqueda con `AND` y `OR` que cruza 3 ejes obligatorios:
  1. El sujeto: *Modelos de lenguaje* (`LLMs`).
  2. El ataque: *Inyecciones, jailbreaks o poisoning*.
  3. La defensa: *Seguridad, guardrails o mitigación*.
* **Respuesta para el jurado:** *«Estrategia de recuperación de información que intersecta tres dimensiones conceptuales (tecnológica, ofensiva y defensiva) para maximizar la especificidad cienciométrica.»*

---

### Open Access (*Acceso Abierto*) vs. Paywall (*Barrera de Pago*)
* **Open Access:** Artículos científicos gratuitos y libres en internet para que cualquiera pueda descargarlos y auditarlos.
* **Paywall:** Cuando una revista te pide \$30 o \$40 dólares por leer el PDF. (Por eso descartaste 2 artículos de los 12, para que tu investigación sea 100% auditable y reproducible).

---

### RENACYT – CONCYTEC
* **¿Qué es en cristiano?:** El Registro Nacional Científico y Tecnológico del Estado Peruano (CONCYTEC). A través de sus convenios institucionales, los investigadores peruanos tienen acceso gratuito legal a bases de datos como ScienceDirect o IOPscience.

---

## 💡 Resumen en 1 Minuto para Antes de Entrar a la Sala

Si te pones nervioso durante la exposición, solo recuerda esta historia sencilla:

> *«Los LLMs procesan todo en un **canal plano** (no diferencian órdenes de datos). Por eso los atacantes usan **Prompt Injection** y **Jailbreaking** para que desobedezcan sus reglas. Las empresas intentaron poner **Guardrails** (filtros perimetrales), pero estos filtros o se vuelven lentos (**latencia**) o se ponen paranoicos y bloquean a usuarios buenos (**over-refusal**). Mi tesis clasifica todo esto bajo la norma internacional **MITRE ATLAS** y con el método riguroso **PRISMA-ScR** analiza los 10 mejores estudios del mundo a texto completo.»*

---

> [[Dashboard Trabajo de Investigación|🏠 Volver al Dashboard]] | [[PRJ - Sustentación Oral y Defensa Ciclo X|🎙️ Ver Guion de Sustentación]] | [[PRJ - Delimitación Temática y Matriz Institucional|📄 Matriz Oficial]]
