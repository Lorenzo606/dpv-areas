# Arquitectura del sistema de clasificación de asuntos

## Visión general

El sistema implementa un pipeline de clasificación automática de asuntos administrativos por área, utilizando técnicas de Inteligencia Artificial y, en particular, modelos de lenguaje (LLM).

La arquitectura fue diseñada con los siguientes objetivos:

- Robustez ante redacciones diversas y casos no vistos.
- Simplicidad operativa y facilidad de mantenimiento.
- Separación clara entre experimentación y código productivo.
- Posibilidad de extender el sistema sin refactorizaciones mayores.

---

## Componentes principales

La arquitectura del proyecto se divide en cuatro bloques conceptuales:

1. Interfaz de entrada (CLI / sistema externo)
2. Preprocesamiento
3. Inferencia mediante modelo de lenguaje
4. Normalización y salida

Cada uno de estos bloques se implementa de forma desacoplada.

---

## Flujo del pipeline de clasificación

El flujo completo del sistema es el siguiente:

1. **Ingreso del asunto**
   - El sistema recibe un texto correspondiente al asunto de un trámite administrativo.
   - La entrada puede provenir de la línea de comandos (CLI) o de un sistema externo que integre el pipeline.

2. **Preprocesamiento**
   - Se realiza una normalización básica del texto:
     - eliminación de espacios redundantes,
     - limpieza de caracteres innecesarios,
     - estandarización mínima.
   - El objetivo de esta etapa es reducir ruido sin alterar el contenido semántico del asunto.

3. **Construcción del prompt**
   - Se construye un prompt que incluye:
     - una instrucción clara de clasificación,
     - el listado explícito de áreas administrativas posibles,
     - una breve descripción funcional de cada área,
     - el texto del asunto a clasificar.
   - El prompt fuerza al modelo a elegir una única área de un conjunto cerrado de etiquetas válidas.

4. **Inferencia con modelo de lenguaje**
   - El sistema realiza una llamada mínima y controlada a un modelo LLM.
   - Modelo primario:
     - **GPT-4.1-mini** (OpenAI).
   - En caso de error o indisponibilidad del modelo primario:
     - se utiliza un **modelo de fallback (DeepSeek)** vía OpenRouter.
   - La inferencia devuelve una predicción de área en formato texto.

5. **Normalización de la salida**
   - La salida del modelo se procesa para:
     - eliminar variaciones de formato,
     - asegurar coincidencia exacta con las etiquetas oficiales de área,
     - detectar respuestas inválidas o inesperadas.
   - Esta etapa garantiza consistencia y trazabilidad en la salida final.

6. **Salida del sistema**
   - El sistema devuelve el nombre del área administrativa asignada.
   - La salida está lista para ser:
     - registrada,
     - auditada,
     - o integrada en un sistema de gestión de trámites.

---

## Estrategia de fallback

Para aumentar la robustez operativa, el sistema implementa un mecanismo de fallback automático:

- Si la llamada al modelo primario falla por cualquier motivo
  (timeout, error de red, error de API),
- el pipeline intenta resolver la clasificación utilizando un modelo alternativo.

Esta estrategia permite:

- reducir puntos únicos de falla,
- mejorar la disponibilidad del sistema,
- mantener continuidad operativa.

---

## Relación con el bloque de experimentos

La arquitectura productiva surge directamente de los resultados del bloque experimental documentado en `experiments/`.

El recorrido experimental incluyó:

- reglas basadas en palabras clave,
- modelos clásicos de Machine Learning,
- embeddings y similitud semántica,
- y finalmente modelos de lenguaje.

La elección del enfoque LLM como núcleo del sistema se fundamenta en su mayor capacidad de generalización y en su mejor desempeño frente a casos ambiguos o no vistos durante el entrenamiento.

---

## Separación entre experimentación y producción

El proyecto mantiene una separación explícita entre:

- **Experimentación** (`experiments/`):
  - notebooks exploratorios,
  - evaluación comparativa de enfoques,
  - análisis de métricas y errores.

- **Producción** (`app/`):
  - pipeline de inferencia estable,
  - llamadas controladas a modelos,
  - manejo de configuración y fallback.

Esta separación facilita el mantenimiento, la auditoría del sistema y la evolución futura del proyecto.

---

## Consideraciones de diseño

- No se realiza entrenamiento de modelos en producción.
- La lógica de clasificación se controla principalmente mediante el diseño del prompt.
- La arquitectura es extensible a:
  - clasificación batch,
  - exposición mediante API,
  - incorporación de nuevos modelos o proveedores.

---

## Estado actual

En su versión actual (v0), el sistema:

- Implementa un pipeline de clasificación funcional de extremo a extremo.
- Utiliza un modelo LLM como núcleo de inferencia.
- Está listo para integración controlada y validación en entornos reales.
