# Ejercicio 4 — Clustering de flores (ResNet50 → PCA → KMeans)
Este proyecto tiene como objetivo **agrupar 500 imágenes de flores en 5 grupos** según sus características visuales.  
Para ello utilizamos una red neuronal convolucional **ResNet50** preentrenada para extraer vectores de características, reducimos la dimensionalidad con **PCA** y aplicamos un algoritmo de **clustering KMeans** para generar los grupos.

**Datos (no incluidos en el ZIP):** colocar imágenes en `data/flores/` (formatos JPG/PNG).
**Modo trabajo:** `USE_DRIVE=True`, `RUN_MODELING=True` para generar artefactos.
**Modo entrega:** `USE_DRIVE=False`, `RUN_MODELING=False` para cargar artefactos desde `outputs/`.

**Salidas:**
- `outputs/csv/`     → features index, etiquetas de KMeans, métricas básicas.
- `outputs/models/`  → `pca.pkl`, `kmeans_k5.pkl`.
- `outputs/figures/` → varianza PCA, scatter 2D, mosaicos por cluster.
