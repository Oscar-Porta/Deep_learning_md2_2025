# Ejercicio 2 — Predicción de consumo de gas (t+1 a t+7)

**Objetivo.** Predecir el consumo de gas a 7 días combinando lags del consumo e información meteorológica.
**Notebook principal:** `notebooks/ej2_prediccion.ipynb`

## Cómo ejecutar
1. Colocamos los ficheros CSV de entrada en `ej2_prediccion_gas/data/raw/`:
   - `Consumption.csv`
   - `Meteorological_data_anon.csv`
2. Ejecutamos el notebook en orden: integración de datos, ACF/PACF y selección de lags, creación de ventanas supervisadas y entrenamiento de modelos (base y extendido).
3. Los resultados se guardan en `outputs/`.

## Entradas
- `data/raw/`: CSV originales (consumo y meteorología).

## Salidas
- `data/processed/`: datos integrados y limpios.
- `outputs/figures/`: gráficos (estacionalidad, ACF/PACF, etc.).
- `outputs/csv/`: métricas (MAE, RMSE) y tablas auxiliares.
- `outputs/models/`: modelos entrenados en formato Keras/TensorFlow.

## Notas (Anexo 11)
- Variables de calendario: día de la semana, fin de semana y festivos **nacionales** (sin autonómicos).
## Requisitos
- Google Colab (o Python 3.10+)
- `pandas`, `numpy`, `matplotlib`, `statsmodels`, `scikit-learn`
- `tensorflow` / `keras`
