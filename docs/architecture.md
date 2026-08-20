# Architecture and design decisions

## System boundary

The live prototype uses one Docker container as the runtime boundary. Hermes profiles provide separate identities, prompts, skills, sessions, and Slack gateways. The profiles share the upstream runtime but are treated as distinct workers by the routing layer.

The public repository does not copy private profile directories. Instead, `config/agents.json` defines a portable contract for each role, and the Python harness evaluates those contracts without an LLM or network connection.

## Why role-based decomposition

A single agent can produce an answer quickly, but it also combines data handling, analysis, interpretation, presentation, and review in one opaque step. This design separates those responsibilities so that:

- invalid inputs fail before analysis;
- numerical artifacts can be inspected independently of prose;
- visualization consumes aggregates instead of raw operational data;
- a human reviewer can approve finalization, request revision through the role router, or reject publication with a recorded rationale;
- the final report has a traceable lineage.

## Artifact flow

| Stage | Producer | Input | Output |
|---|---|---|---|
| 1 | Sam | CSV files | Validated records and data-quality counts |
| 2 | Ada | Validated records | Market summary and chronological forecast |
| 3 | Ethan | Quantitative metrics | Evidence-linked decision notes |
| 4 | Mia | Forecast series | Portable SVG figure |
| 5 | Noah | Metrics and notes | Concise narrative draft |
| 6 | Sophie | All artifacts | Pass/fail QA verdict |
| Control gate | Human reviewer in the live workflow; deterministic gate in the public harness | QA verdict and reviewed artifacts | Approve, revise, or reject decision |
| 7 | Oliver | Reviewed artifacts | Executive report and Slack payload |

The human-in-the-loop gate is deliberately outside the Docker agent runtime. A revision returns to the role router, a rejection blocks publication and records the reason, and only approval permits executive synthesis and Slack delivery. For reproducible, non-interactive CI, the public harness models the same boundary as a deterministic blocking gate rather than pretending to automate a human decision.

## Database-backed operating loop

The live Supabase case adds a durable data plane and an explicit control plane to the role model:

- Oliver collects approved source records into a fixed file contract;
- Ethan validates and stages the batch;
- Sam loads and reconciles records transactionally;
- Supabase/PostgreSQL enforces types, nullability, key structure, and selected domain checks;
- Ada performs read-only SQL analysis against an approved view and retains the executed SQL;
- Noah drafts the report only after the analysis artifact is available;
- Sam publishes only after the validation/approval gate passes; and
- the scheduler and Kanban state machine preserve execution order and escalate blocked work to a human.

The database is not used as unconstrained agent memory. It is a governed system of record behind bounded role and task contracts. The captured implementation is scheduled batch automation rather than a streaming system. See the [Supabase-backed agent data operations case study](case-studies/supabase-agent-data-operations.md).

## Evaluation boundary

The offline harness is deliberately deterministic. It is not presented as a replacement for the live LLM agents; it is a test double for the data contracts and handoff logic. This makes CI repeatable and prevents portfolio reviewers from needing paid APIs or private Slack access.

## Deployment hardening

The offline Docker demo uses:

- a dedicated non-root user;
- a read-only root filesystem;
- `cap_drop: [ALL]`;
- `no-new-privileges:true`;
- no externally published port;
- no credential or network requirement.

The historical live deployment used a moving image tag. Pinning an immutable digest is a documented production improvement.
