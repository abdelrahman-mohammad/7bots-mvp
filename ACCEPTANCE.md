# Phase 1 acceptance run

The MVP's definition of done. Automated checks run with `uv run poe accept shiptrack`; the rest are observed by hand because they involve a human reviewer.

## Steps

1. `docker compose up -d`, then `uv run poe serve` and `npm run dev` in `frontend/`.
2. Open the app and press **Run ingestion**. Do not run the orchestrator from a script; the trigger has to come from the UI.
3. Watch the status move through `queued`, `running`, `succeeded`. The job row shows the LangSmith run id.
4. Review the PR that opens on the model repo, read its description, and merge it through GitHub's own UI.
5. Deliver the merge webhook so `artifact_versions` flips to `approved`.
6. Open the elements screen and the versions screen.
7. Run `uv run poe accept shiptrack`.

## Definition of done

| # | Check | How it is verified |
| --- | --- | --- |
| 1 | Ingestion triggered via the UI, not a script | By hand, step 2 |
| 2 | All 5 subagents produce schema-valid, evidence-cited elements | `accept`, checks 1 to 3 |
| 3 | Reconciler merges the intentional duplicate, keeping both evidence sources | See "known deviations" |
| 4 | Validator flags the intentional invalid reference and halts progression to PR | See "known deviations" |
| 5 | A clean run opens a PR with an accurate, human-readable description | By hand, step 4 |
| 6 | A human merges the PR through GitHub's UI | By hand, step 4 |
| 7 | Webhook flips `artifact_versions` to approved, no manual DB edits | `accept`, approval check |
| 8 | Model viewer shows merged elements by layer with working evidence links | By hand, step 6 |
| 9 | Version screen shows the approved version linked to the correct PR | By hand, step 6 |
| 10 | The run is a connected trace in LangSmith | `accept`, run id check |

## Known deviations

**Checks 3 and 4 cannot be met as written, because upstream subagents are better than the fixture expected.**

J1 planted a near-duplicate host so F1 would have something to merge. E4 recognises `shipdb-primary` in the Terraform and `SHIPDB PRIMARY` in the CMDB as one machine and writes a single element citing both files. The duplicate is resolved during extraction, so F1 receives nothing to merge. Its merge path is proven by unit test on exactly that pair instead.

J1 also planted a reference to a Legacy Invoicing Gateway that no other evidence describes, so the validator would reject a dangling relationship. E5 refuses to invent the id and logs the refusal to `rejected.md`, so the validator never sees a broken reference. F2's rejection path is proven by injecting one by hand.

Both traps work. They are caught one stage earlier than the referral doc anticipated.

## Open findings

**The pipeline never verifies that evidence is real.** F2 checks archimate types and relationship pairs. The verbatim-excerpt check lives in `agents/element_check.py` and only runs from the `poe *-check` scripts, which the orchestrator does not call. A run therefore can, and did, merge an element whose excerpt is quoted from the wrong line: `nightly-scan-archive-job` cites `cmdb-export.csv:4` when its excerpt is on line 5. The quote is real; the line number is not. A reviewer following the evidence link lands in the wrong place.

**A model can be merged with an unresolved conflict.** F1 flagged that a business `BusinessService` and an application `ApplicationService` had both been given the id `consignment-booking-service`. The PR was merged without resolving it. `model_element_index.id` is the primary key, so the two rows collapse into one and one element disappears from the viewer: 34 indexed against 35 files on main. The reconciler behaved correctly by flagging rather than guessing. The gate that failed was human.
