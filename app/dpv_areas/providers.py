

from __future__ import annotations

import os
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI

from .prompt_builder import build_classification_prompt, get_area_labels

load_dotenv()

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

def _openai_primary_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Falta OPENAI_API_KEY en el entorno (.env).")
    return OpenAI(api_key=api_key)

def _openrouter_fallback_client() -> OpenAI:
    # Podés llamarla DEEPSEEK_API_KEY o OPENROUTER_API_KEY; acá soporte ambas
    api_key = os.getenv("OPENROUTER_API_KEY") or os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Falta OPENROUTER_API_KEY o DEEPSEEK_API_KEY en el entorno (.env).")
    return OpenAI(api_key=api_key, base_url=OPENROUTER_BASE_URL)

def _normalize_area_output(raw: str) -> str:
    area_labels = get_area_labels()
    cleaned = raw.upper().replace('"', "").strip()

    # Intento 1: coincidencia por inclusión
    for area in area_labels:
        if area in cleaned:
            return area

    # Intento 2: coincidencia exacta (ignorando mayúsculas)
    for area in area_labels:
        if cleaned == area.upper():
            return area

    # Si no matchea, devuelvo lo que vino para inspección
    return raw

def _classify_with_client(asunto_texto: str, client: OpenAI, model_name: str) -> str:
    prompt = build_classification_prompt(asunto_texto)
    response = client.responses.create(
        model=model_name,
        input=prompt,
    )

    try:
        raw = response.output[0].content[0].text.strip()
    except Exception as e:
        raise RuntimeError(f"Error al parsear la respuesta del modelo: {e}") from e

    return _normalize_area_output(raw)

def classify_asunto_llm(
    asunto_texto: str,
    primary_model: str = "gpt-4.1-mini",
    fallback_model: str = "deepseek/deepseek-chat",
) -> str:
    """
    Producción:
    - Primario: OpenAI GPT-4.1-mini
    - Fallback: DeepSeek vía OpenRouter (modelo configurable)
    """
    primary = _openai_primary_client()
    try:
        return _classify_with_client(asunto_texto, primary, primary_model)
    except Exception:
        fallback = _openrouter_fallback_client()
        return _classify_with_client(asunto_texto, fallback, fallback_model)
