# dpv-areas

Sistema de clasificación automática de asuntos administrativos por área,
utilizando Inteligencia Artificial.

El proyecto implementa un pipeline de inferencia basado en modelos de lenguaje,
respaldado por un conjunto de experimentos comparativos documentados.

---

## Objetivo

Clasificar automáticamente el texto del asunto de un trámite administrativo
y asignarlo al área correspondiente dentro de una organización pública.

---

## Estructura del repositorio

```text
dpv-areas/
├── app/            # Código productivo del pipeline de inferencia
├── experiments/    # Notebooks de experimentación
├── results/        # Resultados de los experimentos
├── data/           # Descripción de datos (no versionados)
├── docs/           # Documentación técnica y metodológica
├── pyproject.toml  # Definición del proyecto y dependencias
└── README.md
```

## Entorno

El proyecto utiliza **uv** para la gestión de dependencias.

```bash
uv sync

Nada más por ahora. Lo vamos a mejorar después.

---

## 4.4 Test rápido: ¿el entorno funciona desde VS Code?

Abrí la terminal integrada de VS Code (`Ctrl + ñ`) y corré:

```bash
uv run python --version
