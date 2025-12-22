# Experimentos

Este directorio contiene los experimentos realizados para evaluar distintos
enfoques de clasificación automática de asuntos administrativos por área.

El objetivo del bloque experimental fue comparar métodos heurísticos,
modelos de Machine Learning clásico y enfoques basados en representaciones
semánticas y modelos de lenguaje, con el fin de seleccionar una solución
robusta para su uso en producción.

---

## Convenciones generales

- Cada notebook representa un experimento independiente.
- Los datos reales no se incluyen en el repositorio por motivos de
  confidencialidad.
- Los resultados generados por los experimentos (métricas, matrices de
  confusión, ejemplos de errores) se almacenan en el directorio `results/`.
- Los notebooks reflejan el proceso real de experimentación y no fueron
  reescritos con fines cosméticos.

---

## Experimentos incluidos

### 1. Clasificación basada en reglas y palabras clave  
**Notebook:** `Clasif_palabra_claves.ipynb`

Enfoque heurístico inicial basado en la detección de palabras clave asociadas
a cada área administrativa.

- Ventajas: simplicidad, interpretabilidad, bajo costo computacional.
- Limitaciones: alta dependencia de la redacción exacta y baja capacidad de
  generalización.

Este experimento se utilizó como **baseline inicial** y punto de partida del
análisis.

---

### 2. Clasificación mediante embeddings y similitud coseno  
**Notebook:** `OpenAI_Embeddings_Small.ipynb`

Enfoque no supervisado basado en representaciones vectoriales semánticas
(*embeddings*) y similitud coseno entre asuntos y descripciones de áreas.

- Mejora respecto a métodos léxicos (keywords, TF-IDF).
- No requiere entrenamiento supervisado.
- Sensible a la calidad de las descripciones de las áreas.

Este experimento introdujo el uso de espacios semánticos compartidos y sirvió
como paso intermedio hacia enfoques más avanzados.

---

### 3. Clasificación supervisada con embeddings + Regresión Logística  
**Notebook:** `ML_EmbeddingsOpenAI_RegresionLogistica.ipynb`

Enfoque supervisado que combina embeddings de OpenAI como representación del
texto con un clasificador de Regresión Logística.

- Captura semántica más rica que TF-IDF.
- Entrenamiento rápido y modelo simple.
- Requiere retraining ante cambios en el dominio o en las áreas.

Este experimento permitió evaluar el potencial de soluciones supervisadas
modernas basadas en embeddings.

---

### 4. Regresión Logística con optimización de hiperparámetros  
**Notebook:** `ML_RegresionLogistica_GridSearchCV.ipynb`

Baseline supervisado clásico utilizando Regresión Logística optimizada mediante
GridSearchCV.

- Modelo interpretable y reproducible.
- Buen desempeño en escenarios controlados.
- Capacidad limitada para generalizar a redacciones no vistas.

Sirve como referencia directa frente a modelos más complejos.

---

### 5. XGBoost con GridSearchCV  
**Notebook:** `ML_XGB_GridSearchCV.ipynb`

Modelo supervisado no lineal avanzado entrenado sobre representaciones
vectoriales del texto, con ajuste de hiperparámetros.

- Buen desempeño en clases frecuentes.
- Capacidad para modelar relaciones no lineales.
- Dependencia fuerte de la distribución del dataset y necesidad de retraining.

Este experimento establece un límite superior razonable para el desempeño de
Machine Learning clásico supervisado en este dominio.

---

### 6. Clasificación con modelos de lenguaje (LLM)  
**Notebook:** `API_OpenAI_gtp4-mini.ipynb`

Experimento basado en el uso de un modelo de lenguaje (GPT-4.1-mini) para la
clasificación directa de asuntos administrativos mediante un prompt diseñado
con descripciones funcionales por área.

- Alta capacidad de generalización.
- Menor dependencia de ingeniería de features.
- Flexibilidad ante redacciones ambiguas o no vistas.

Este enfoque fue seleccionado como **solución final para producción** y dio
origen al pipeline implementado en el directorio `app/`.

---

## Conclusión del bloque experimental

El recorrido experimental muestra una progresión clara:
- Reglas (keywords)
- Embeddings + similitud
- ML supervisado (Regresión Logística, XGBoost)
- Modelos de Lenguaje (LLM)
  
Si bien los modelos clásicos ofrecen resultados competitivos en escenarios
controlados, los enfoques basados en modelos de lenguaje demostraron mayor
robustez y capacidad de generalización para el dominio real del problema,
motivando su adopción como solución productiva.




