# Demo evidence set

A fictional legacy system used as the fixture for Epics E to J, so every developer gets the same results.

The system is **ShipTrack**, a consignment tracking platform run by a freight company since 2009. Its system id is `shiptrack`, so extracted elements belong under `systems/shiptrack/as-is/<layer>/`.

`EVIDENCE_PATH` points at `evidence/`, which the agent sees mounted read-only at `/evidence/`. This README sits one level above it on purpose: it says what the fixture is designed to catch, so a subagent that could read it would be reading the answer key.

## Folders

| Folder         | Read by                 | Content                                            |
| -------------- | ----------------------- | -------------------------------------------------- |
| `motivation/`  | strategy-analyst (E1)   | A compliance memo about a failed audit             |
| `strategy/`    | strategy-analyst (E1)   | A platform plan                                    |
| `business/`    | business-analyst (E2)   | An operations handbook and an interview transcript |
| `code/`        | code-analyzer (E3)      | Two services and the database schema               |
| `infra/`       | infra-analyzer (E4)     | A Terraform snippet and a CMDB export              |
| `integration/` | integration-mapper (E5) | An OpenAPI spec and an integrations document       |

## Intentional edge cases

**Near-duplicate element, for the reconciler (F1).** The same two hosts are named twice. Terraform calls them `shipdb-primary` and `shiptrack-app-01`, the CMDB export calls them `SHIPDB PRIMARY` and `SHIPTRACK APP 01`. One subagent reading both files should produce two Node elements per machine, and the reconciler should merge them. A softer one: the handbook says "dispatch team", the interview says "dispatch desk".

**Invalid reference, for the validator (F2) and the integration mapper (E5).** `integration/integrations.md` says the Booking API posts invoice events to a Legacy Invoicing Gateway (INVGW). Nothing else describes INVGW, so no subagent will have produced an element for it. A relationship pointing at INVGW must fail validation with a clear error instead of being written as a broken reference.
