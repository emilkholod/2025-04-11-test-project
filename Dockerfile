ARG WORKDIR="/app"

# --- Builder image ---

FROM python:3.12-alpine AS builder

ARG WORKDIR

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR "${WORKDIR}"

RUN pip install --no-cache-dir poetry==2.1.1 \
    && poetry config virtualenvs.in-project true

COPY pyproject.toml poetry.lock ./

ARG ENV=prod
RUN if [ "$ENV" = "dev" ]; then \
        poetry install --no-root; \
    else \
        poetry install --without dev --no-root; \
    fi

# --- Target image ---

FROM python:3.12-alpine

ARG WORKDIR

USER nobody

WORKDIR "${WORKDIR}"

COPY --from=builder "${WORKDIR}" .

COPY ./src/ ./src
COPY ./raw_data/ ./raw_data

ENV PYTHONPATH="/app/src"
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000
CMD ["python", "-m", "freelancer_analyzer_app"]
