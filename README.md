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

## What you need first

| Tool | Why |
| --- | --- |
| [uv](https://docs.astral.sh/uv/) | Python dependencies. Installs Python 3.12 itself |
| Docker Desktop | Runs Postgres. It has to actually be running, not just installed |
| Node 20+ | Frontend |
| git | Both repos |

## Setup

The agents write their output into a **second repository**, checked out next to this one. Clone both:

```
git clone https://github.com/<account>/7bots-mvp.git
git clone https://github.com/<account>/7bots-archimate.git
```

You should end up with `7bots-mvp/` and `7bots-archimate/` as siblings, because `MODEL_REPO_PATH` defaults to `../7bots-archimate`.

Then, from `7bots-mvp/`:

```
cp .env.example .env          # fill it in, see the table below
uv sync
uv run pre-commit install
docker compose up -d
uv run poe db-check
uv run alembic upgrade head   # creates the tables
uv run poe seed shiptrack ShipTrack
```

`db-check` should report `user: app`, `superuser: False`, `can_create_tables: True`.

That last step is easy to miss and the error it prevents does not name the real problem. Four tables have a foreign key to `legacy_systems`, so triggering a run for a system with no row there fails with a foreign key violation.

Frontend, from `frontend/`:

```
npm install
cp .env.example .env          # VITE_API_KEY must match API_KEY
```

## Environment variables

| Variable | Where to get it |
| --- | --- |
| `POSTGRES_*` | Make them up. `docker-compose.yml` reads them to build the container |
| `DATABASE_URL` | Must agree with the `POSTGRES_*` values above |
| `ANTHROPIC_API_KEY` | [console.anthropic.com](https://console.anthropic.com), API keys |
| `LANGSMITH_API_KEY` | [smith.langchain.com](https://smith.langchain.com), Settings then API keys |
| `LANGSMITH_TRACING` | `true`, otherwise runs are not traced |
| `LANGSMITH_PROJECT` | Any name. Groups your runs in the LangSmith UI |
| `GITHUB_TOKEN` | GitHub, Settings, Developer settings, **fine-grained** personal access token scoped to the model repo, with **Contents: read and write** and **Pull requests: read and write** |
| `GITHUB_MODEL_REPO` | `<account>/7bots-archimate` |
| `MODEL_REPO_PATH` | `../7bots-archimate` |
| `EVIDENCE_PATH` | `./test-fixtures/evidence` |
| `GITHUB_WEBHOOK_SECRET` | Generate one with `python -c "import secrets; print(secrets.token_hex(20))"`. Use the same value when registering the webhook on GitHub |
| `API_KEY` | Generate one the same way. The frontend sends it as `X-API-Key` |
| `FRONTEND_ORIGIN` | `http://localhost:5173`. Without it the browser blocks every API call |

In `frontend/.env`, `VITE_API_KEY` has to equal `API_KEY`, and the two repo URLs build the links back to GitHub in the model viewer.

## Running it

Two terminals:

```
uv run poe serve              # API on :8000, docs at /docs
cd frontend && npm run dev    # UI on :5173
```

## Commands

```
uv run poe lint       # ruff check + black --check
uv run poe format     # ruff --fix + black
uv run poe test       # pytest, needs Postgres up
uv run poe db-check   # verify the app can reach Postgres
uv run poe seed       # create a legacy_systems row
uv run poe serve      # run the API
uv run poe ingest     # run the whole pipeline from the terminal
uv run poe accept     # the Phase 1 acceptance checks
```

Individual pipeline stages, useful when debugging one subagent:

```
uv run poe strategy-check     # E1, motivation and strategy
uv run poe business-check     # E2
uv run poe code-check         # E3
uv run poe infra-check        # E4
uv run poe integration-check  # E5, relationships
uv run poe reconcile          # F1
uv run poe validate           # F2
```

Each `*-check` runs its subagent **twice** and prints the element count difference, because reproducibility is part of those tasks' definition of done. They also wipe their own layer directories first, so run them in order if you want a complete model.

## The acceptance flow

[ACCEPTANCE.md](ACCEPTANCE.md) is the end-to-end run: trigger from the UI, review and merge the PR yourself, confirm the webhook approves it, then look at the model in the viewer. Run it once after setup to prove your environment works.

A full run takes about six minutes and makes five subagent calls plus reconciliation, so it is not free.

## How the pieces fit

```
test-fixtures/evidence/   the input, mounted read-only at /evidence/
        |  E1-E5 subagents
../7bots-archimate/       the output, a separate git repo
        |  F1 reconcile, F2 validate
        |  G1 branch and push, G2 open PR
   human review on GitHub
        |  G3 webhook
   Postgres index, REST API, model viewer
```

## Layout

```
agents/     Deep Agents runtime: subagents, skills, shared schemas
backend/    FastAPI app, data layer, git and PR automation
frontend/   React model viewer
```

## Database

Postgres runs in Docker. `docker-compose.yml` reads the `POSTGRES_*` variables from `.env`; the app connects with `DATABASE_URL`, so the two must agree.

`postgres` is the superuser, for administration only. The app connects as `app`, which is unprivileged and can only create tables in schema `public`.

```
docker compose up -d      # start
docker compose down       # stop, keep data
docker compose down -v    # stop and destroy data
```

Role creation only runs on an empty data directory, so changing `POSTGRES_APP_PASSWORD` takes effect only after `docker compose down -v`. After that you need `alembic upgrade head` and `poe seed` again.

## Known gaps

The webhook has to reach your machine for an approval to register. On localhost it cannot, so merging a PR does not flip `artifact_versions` to `approved` until you either expose the port or deliver the payload yourself. Anything merged without a delivered webhook shows as `pending` in the viewer even though GitHub says merged.

## Secrets

`.env` is git-ignored. Never commit real credentials; add new variables to `.env.example` as placeholders instead.
