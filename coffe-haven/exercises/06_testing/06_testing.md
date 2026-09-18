# Testing

Ziel dieser Übung ist es, Unit-Tests in unsere Pipeline zu integrieren.

## Aufgaben

1. Schreibe den Pipeline Step für die Unittests mit pytest
2. Korrigiere den Code bei Fehlern

## Zusatzaufgaben

Exportiere die Testergebnisse als JUnit XML Report, damit diese in der GitLab UI angezeigt werden können.

### Für Fortgeschrittene

Füge einen Coverage Report hinzu, der die Testabdeckung anzeigt. Zur Berechnung der Testabdeckung kannst du die Python Bibliothek [pytest-cov](https://pypi.org/project/pytest-cov/) verwenden. Diese muss allerdings vorher als dependency in der `pyproject.toml` hinzugefügt werden.

## Hinweise

- Folgendes Docker Image kann in den Jobs verwendet werden, um `uv` und Python zur Verfügung zu haben:

    ```yaml
    image: ghcr.io/astral-sh/uv:0.9.24-python3.10-alpine
    ```

- pytest ist in unserer pyproject.toml bereits vorkonfiguriert und kann daher direkt aufgerufen werden
  - Der einfache Befehl zum Ausführen der Tests lautet:

      ```bash
      uv run pytest
      ```

- Verwende die Flag `--junit-xml=filename` in Kombination mit dem `junit` Report Artifakt für eine Ausgabe des Reports in der GitLab UI
- Um in der Zusatzaufgabe die Testabdeckung zu messen, kannst du die folgenden Flags verwenden (pytest-cov muss vorher in der pyproject.toml als dependency hinzugefügt werden):

    ```bash
    uv run pytest --cov --cov-report=xml:<pfad-zur-datei>.xml
    ```
