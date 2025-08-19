# Ejercicio 1 — Transcripción + NER (ES)

**Objetivo.** Transcribimos audios en español con Whisper y extraemos entidades (PER/ORG/LOC/MISC) con `MMG/xlm-roberta-large-ner-spanish`.
**Notebook principal:** `notebooks/ej1_transcripcion.ipynb`

## Datos (no incluidos en el ZIP)
Copiar los audios en: `data/audio/` (formatos: wav, mp3, m4a, flac, ogg).

## Salidas
- `outputs/json/`  → JSON por audio + `resultados_global.json`
- `outputs/csv/`   → resúmenes tabulares (si se generan)
- `outputs/figures/` → figuras opcionales (si se generan)

## Entrega
- Exportar el notebook a **PDF** y guardarlo en `outputs/docs/`.
- Exportar opcionalmente a **.py** y colocarlo en `scripts/`.

## Requisitos (Colab o local)
- `ffmpeg`, `openai-whisper`, `transformers`, `torch` (y aceleración si hay GPU).
