# main.py — FastAPI para Ej2 (predicción 7 días)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from pathlib import Path
import json, joblib
import numpy as np
import pandas as pd
import tensorflow as tf

app = FastAPI(title="Ej2 — Predicción 7 días (lags + meteo + calendario)")

# === Carga de artefactos ===
ARTS = Path(".")
model = tf.keras.models.load_model(ARTS / "ej2_model_lags_meteo_cal.keras")
scaler_num = joblib.load(ARTS / "ej2_scaler_num.pkl")
feat_cols  = json.loads((ARTS / "ej2_feat_cols.json").read_text(encoding="utf-8"))
num_cols   = json.loads((ARTS / "ej2_num_cols.json").read_text(encoding="utf-8"))
cat_cols   = json.loads((ARTS / "ej2_cat_cols.json").read_text(encoding="utf-8"))

# Comprobaciones básicas
assert set(num_cols).issubset(feat_cols), "num_cols no está incluido en feat_cols"
assert set(cat_cols).issubset(feat_cols), "cat_cols no está incluido en feat_cols"

class PredictPayload(BaseModel):
    # Enviar un diccionario con las features: acepta mayúsc/minúsculas indiferentes
    features: Dict[str, Any]

def _norm_keys(d: Dict[str, Any]) -> Dict[str, Any]:
    # normaliza claves a minúsculas y quita espacios
    return {str(k).strip().lower(): v for k, v in d.items()}

@app.get("/")
def root():
    return {"ok": True, "message": "API viva. Ir a /docs para Swagger."}

@app.post("/predict")
def predict(payload: PredictPayload):
    # 1) normalizar claves
    feats_in = _norm_keys(payload.features)

    # 2) validar que todas las numéricas existen
    missing_num = [c for c in num_cols if c.lower() not in feats_in]
    if missing_num:
        raise HTTPException(status_code=400, detail=f"Faltan numéricas requeridas: {missing_num}")

    # 3) construir fila 1xN en el orden exacto de feat_cols
    row = {}
    for c in feat_cols:
        lc = c.lower()
        if lc in feats_in:
            row[c] = feats_in[lc]
        else:
            # si falta una categórica (dummy), la rellenamos a 0
            if c in cat_cols:
                row[c] = 0
            else:
                raise HTTPException(status_code=400, detail=f"Falta la columna requerida: {c}")

    df = pd.DataFrame([row], columns=feat_cols)

    # 4) escalar solo numéricas con el scaler guardado
    df_num = df[num_cols].astype(float)
    df_cat = df[cat_cols].astype(float)

    df_num_s = pd.DataFrame(scaler_num.transform(df_num), columns=num_cols)
    X = np.hstack([df_num_s.values, df_cat.values]).astype(np.float32)

    # 5) predecir (7 valores)
    y_hat = model.predict(X, verbose=0)[0].tolist()

    return {"ok": True, "horizon": 7, "y_hat": [float(v) for v in y_hat]}