# Ejercicio 5 — Efecto de características estructurales sobre la rentabilidad operativa

Este proyecto analiza el impacto de variables estructurales (país, sector, tamaño, año) sobre la rentabilidad operativa (`EBITDA_Ingresos_netos`),
construye un modelo predictivo (árbol de regresión) y estima el efecto causal (CATE) de `Leverage alto vs bajo`, controlando por observables.

**Notebook principal:** notebooks/Ej5_finanzas.ipynb, abrelo para ejecutar el flujo completo del ejercicio siguiendo las instrucciones.
**Datos (no incluidos):** coloca el fichero de datos en `data/raw/` (CSV o Excel).
**Modo trabajo:** `USE_DRIVE=True`, `RUN_MODELING=True` para generar artefactos.
**Modo entrega:** `USE_DRIVE=False`, `RUN_MODELING=False` para cargar artefactos desde `outputs/`.

**Estructura:**
- `data/raw/`       → datos originales
- `data/processed/` → datos limpios / transformados
- `outputs/csv/`    → tablas de resultados (métricas, importancias, CATE, etc.)
- `outputs/figures/`→ gráficos (EDA, árbol, subgrupos)
- `outputs/models/` → modelos guardados (árbol, preprocesamiento)
- `docs/`           → documentación auxiliar

**Notas:**
- El árbol predictivo usará `country`, `year`, `sector`, `size`, `total_assets`, `Solvencia`, `Leverage`.
- Para CATE definiremos `Leverage alto` vs `bajo` y estimaremos efectos heterogéneos por subgrupos.
