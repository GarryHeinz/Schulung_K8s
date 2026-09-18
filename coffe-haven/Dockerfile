FROM ghcr.io/astral-sh/uv:0.9.24-python3.12-alpine AS builder

WORKDIR /app

RUN apk add --no-cache build-base

COPY pyproject.toml ./
RUN uv sync --no-dev --python /usr/local/bin/python \
    && rm -rf /root/.cache

FROM ghcr.io/astral-sh/uv:0.9.24-python3.12-alpine

WORKDIR /app
RUN adduser -D -u 1000 appuser
COPY --from=builder /app/.venv /app/.venv

COPY app /app/app
COPY pyproject.toml README.md /app/
RUN chown -R appuser:appuser /app

USER appuser

ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/app/.venv
ENV PATH=/app/.venv/bin:${PATH}

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app.__init__:create_app()"]
