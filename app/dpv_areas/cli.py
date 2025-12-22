from __future__ import annotations

import json
import typer

from .inference_pipeline import classify_one

app = typer.Typer(help="dpv-areas: clasificador de asuntos administrativos")


@app.command()
def classify(asunto: str = typer.Option(..., "--asunto", "-a")):
    result = classify_one(asunto)
    typer.echo(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    app()
