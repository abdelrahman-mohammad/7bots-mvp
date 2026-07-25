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

Requires [uv](https://docs.astral.sh/uv/). Python 3.12 is installed by uv automatically.

```
uv sync
uv run pre-commit install
cp .env.example .env
```

## Commands

```
uv run poe lint      # ruff check + black --check
uv run poe format    # ruff --fix + black
```

`make lint` and `make format` also work if you have make.

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
