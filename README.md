# 7bots-mvp

Multi-agent platform that extracts a traceable ArchiMate As-Is model from legacy system evidence.

MVP scope is Phase 1 of the architecture design: evidence → agent-extracted model → git commit → human PR review → viewable model. Single tenant, single system. No Phase 2/3/4, no UML/C4 projection.

## Stack

| Concern  | Choice                          |
| -------- | ------------------------------- |
| Backend  | Python 3.12, FastAPI            |
| Agents   | deepagents (LangGraph)          |
| Database | PostgreSQL, SQLAlchemy, Alembic |
| Frontend | React, Vite, TypeScript         |
| LLM      | Anthropic Claude API            |
| Tracing  | LangSmith                       |

Each of these is a swap seam, not a permanent commitment. See the architecture design for the provider abstractions they sit behind.

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Docker. Python 3.12 is installed by uv automatically.

```
cp .env.example .env
uv sync
uv run pre-commit install
docker compose up -d
uv run poe db-check
```

If `db-check` reports `user: app`, `superuser: False`, `can_create_tables: True`, setup is done.

## Commands

```
uv run poe lint       # ruff check + black --check
uv run poe format     # ruff --fix + black
uv run poe db-check   # verify the app can reach Postgres
```

`make lint` and `make format` also work if you have make.

## Database

Postgres runs in Docker. `docker-compose.yml` reads the `POSTGRES_*` variables from `.env`; the app
connects with `DATABASE_URL`, so the two must agree.

`postgres` is the superuser, for administration only. The app connects as `app`, which is
unprivileged and can only create tables in schema `public`.

```
docker compose up -d      # start
docker compose down       # stop, keep data
docker compose down -v    # stop and destroy data
```

Role creation only runs on an empty data directory, so changing `POSTGRES_APP_PASSWORD` takes effect
only after `docker compose down -v`.

## Layout

```
agents/     Deep Agents runtime: subagents, skills, shared schemas
backend/    FastAPI app, data layer, git and PR automation
frontend/   React model viewer
```

This is the engineering repo. The ArchiMate model output lives in a separate GitHub repo created in task A3.

## Secrets

`.env` is git-ignored. Never commit real credentials; add new variables to `.env.example` as placeholders instead.

_AI-generated_
