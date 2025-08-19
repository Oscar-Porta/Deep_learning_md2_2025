# Ejercicio 3 — Clasificación de imágenes (ardilla, caballo, vaca)

**Objetivo.** Entrenamos 3 CNN con la misma arquitectura cambiando solo el optimizador (Adam, SGD, RMSprop), comparamos métricas y evaluamos en test (matriz de confusión + 5 predicciones).

## Datos (no incluidos en el ZIP)
Colocar la carpeta `animales/` en `data/animales/` con:
- `train/{ardilla,caballo,vaca}`
- `validation/{ardilla,caballo,vaca}`
- `test/{ardilla,caballo,vaca}`

## Salidas
- `outputs/models/`  → modelos `.keras`
- `outputs/csv/`     → histories y comparativa
- `outputs/figures/` → curvas, matriz, muestras

## Modo entrega
- En el notebook: `RUN_TRAINING = False` y `RECALC_TEST = False` para cargar artefactos ya guardados.
