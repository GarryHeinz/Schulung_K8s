# Coffee Haven

Coffee Haven ist eine produktionsnahe Referenzanwendung für einen Specialty-Coffee-Shop.
Die App basiert vollständig auf Flask, rendert serverseitige Seiten mit Tailwind CSS und hält Produktkatalog sowie Warenkorb im Speicher.

## Funktionsumfang

- Kuratierter Produktkatalog mit Gerätschaften, Bohnen und Zubehör
- Session-basierter Warenkorb inkl. Hinzufügen, Entfernen und Checkout-Fluss
- Responsive UI (Tailwind) mit komponierbaren Templates
- Health Endpoint für Observability/Monitoring

## Quick Start

```bash
uv sync --group dev        # App + Dev-Tools installieren
cp .env.example .env        # HOST/PORT/SECRET bei Bedarf anpassen
uv run flask --app app run  # http://localhost:8080
```

## Docker Workflow

```bash
docker build -t coffee-haven .
docker run -p 80:8080 coffee-haven
```

## Konfiguration

| Variable           | Default     | Beschreibung                              |
|--------------------|-------------|-------------------------------------------|
| `FLASK_ENV`        | `production`| Flask-Betriebsmodus                       |
| `FLASK_SECRET_KEY` | _leer_      | Signatur für Sessions                     |
| `HOST`             | `0.0.0.0`   | Bind-Adresse                              |
| `PORT`             | `8080`      | HTTP-Port                                 |

Konfigurationen können über `.env`, Container-Variablen oder Prozess-Manager gesetzt werden.

## Entwicklungsleitfaden

```bash
# Code-Qualität
uv run ruff check
uv run ruff format --check
uv run pyright

# Tests
uv run pytest
```

> Tipp: `uv run ruff format` ohne `--check` formatiert den Code automatisch.

### Projektstruktur

- `app/` – Flask Factory, Routen, Templates, statische Produktdaten
- `tests/` – Pytest-Suite mit Client-Fixtures & Session-Abdeckung
- `Dockerfile` – Produktionsimage (uv + Gunicorn)
- `pyproject.toml` – Metadaten & Tooling-Konfiguration

## Contribution Guidelines

1. Branch erstellen: `git checkout -b feature/awesome-change`
2. Feature + passende Tests implementieren
3. Sicherstellen, dass `uv run ruff check` und `uv run pytest` grün sind
4. Commit nach Conventional Commits, z. B. `feat: add cart badge`
5. Merge Request eröffnen und Reviewer zuweisen
