# Architecture and design decisions

## System boundary

The live prototype uses one Docker container as the runtime boundary. Hermes profiles provide separate identities, prompts, skills, sessions, and Slack gateways. The profiles share the upstream runtime but are treated as distinct workers by the routing layer.

The public repository does not copy private profile directories. Instead, `config/agents.json` defines a portable contract for each role, and the Python harness evaluates those contracts without an LLM or network connection.

## Why role-based decomposition

A single agent can produce an answer quickly, but it also combines data handling, analysis, interpretation, presentation, and review in one opaque step. This design separates those responsibilities so that:

- invalid inputs fail before analysis;
- numerical artifacts can be inspected independently of prose;
- visualization consumes aggregates instead of raw operational data;
- the reviewer can block finalization;
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
| 7 | Oliver | Reviewed artifacts | Executive report and Slack payload |

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
