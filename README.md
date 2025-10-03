Repositorio de la evaluación del módulo Minería de Datos II. Reúne cinco ejercicios prácticos de deep learning y text mining con una puesta a punto portable (Colab o local) y artefactos guardados en outputs/.

Nota GenAI: usamos Whisper (modelo fundacional) para transcripción de audio; el resto son modelos discriminativos (clasificación, series temporales y clustering).

Contenido
	•	ej1_transcripcion — ASR con Whisper + NER en español (XLM-R).
	•	ej2_prediccion_gas — Predicción t+1…t+7 con lags, meteo y calendario (Keras).
	•	ej3_clasificacion_animales — CNN desde cero; comparación de optimizadores (Adam/SGD/RMSprop).
	•	ej4_clustering_flores — Feature extraction con ResNet50, PCA y KMeans (5 clústeres).
	•	ej5_finanzas_causal_predictivo — (prototipo) análisis/forecast con enfoque causal-predictivo.

Ejecución rápida
	1.	Abrimos el cuaderno en notebooks/ del ejercicio.
	2.	Ajustamos las banderas iniciales: USE_DRIVE (Drive vs. local) y RUN_MODELING (reentrenar vs. cargar artefactos).
	3.	Colocamos los datos en data/… según el README de cada ejercicio (los datasets no se incluyen).
	4.	Ejecutamos en orden; las salidas se guardan en outputs/{csv, figures, models}.

Requisitos (principales)

Python 3.10+, TensorFlow/Keras, scikit-learn, pandas, numpy, matplotlib; según el ejercicio: transformers, openai-whisper (+ ffmpeg), statsmodels, holidays.
