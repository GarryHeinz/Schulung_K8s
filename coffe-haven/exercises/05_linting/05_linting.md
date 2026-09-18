# Linting

Ziel dieser Übung ist es, Linting in unsere Pipeline zu integrieren.

## Aufgaben

1. Schreibe einen Linting-Step in deiner Pipeline, welcher den Python-Quellcode überprüft
2. Überprüfe das Ergebnis und passe den Code ggf. an.

## Zusatzaufgabe

Generiere einen Linting-Report und speichere diesen als Artefakt in der Pipeline.

## Hinweise

- `uv` ist ein Python package manager, der in diesem Projekt verwendet wird.
    Dieser ist bereits über die `pyproject.toml` Datei konfiguriert und über ihn kann `ruff` ausgeführt werden.
- Um `ruff` auszuführen, kannst du folgenden Befehl verwenden:

    ```bash
    uv run ruff check
    ```

- Die Flag `--output-format=junit` kann verwendet werden, um den Report im JUnit Format zu generieren.

- Folgendes Docker Image kann in den Jobs verwendet werden, um `uv` und Python zur Verfügung zu haben:

    ```yaml
    image: ghcr.io/astral-sh/uv:0.9.24-python3.10-alpine
    ```

- Genaueres findest du [hier](https://docs.astral.sh/uv/guides/integration/gitlab/)
