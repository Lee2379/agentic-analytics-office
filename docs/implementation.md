# System implementation

## Scope

Agentic Analytics Office is a configuration, orchestration, and evaluation layer built on the third-party Hermes Agent runtime. The live prototype uses Hermes profiles and Slack gateways inside Docker. The public repository does not redistribute Hermes, private profile directories, credentials, raw messages, or private policy text.

The implementation is documented through two evidence classes:

- **Operational evidence** establishes that seven configured specialist profiles, Slack connectivity, Skills, MCP integration, and business tasks existed in the live prototype.
- **Reproducible evidence** establishes how the public role contracts, data validation, chronological evaluation, artifact handoffs, QA gate, and reporting logic execute.

Keeping these classes separate prevents a screenshot from being treated as reproducible code and prevents a deterministic test harness from being presented as proof of a private live deployment.

## Live deployment topology

The prototype ran one Hermes Agent image as a shared Docker runtime. Within that runtime, seven profiles represented distinct job functions:

| Profile | Operational responsibility |
|---|---|
| Sam | Data ingestion and validation |
| Ada | Quantitative analysis and forecasting |
| Ethan | Business interpretation |
| Mia | Visualization and presentation production |
| Noah | Narrative editing |
| Sophie | Quality review and operations support |
| Oliver | Research and executive synthesis |

Profiles are separate specialist identities within one upstream runtime; they are not seven independently built model services. Each profile can maintain profile-scoped configuration, policy, Skills, sessions, and Slack gateway settings. The public evidence confirms profile presence, running gateways, policy-file separation, and configuration status without exposing the underlying values.

The observed container controls include bounded CPU and memory, an unprivileged runtime identity, no mounted Docker socket, and no published service port. These are deployment properties of the captured prototype, not a general security claim about every Hermes installation.

## Role and policy layer

### Profiles

A profile is the primary isolation and routing unit in the live design. A Slack app identity is associated with a specialist profile, allowing a user to address a specific function instead of sending every request to one general-purpose assistant.

The public repository mirrors only the non-sensitive portion of that design in [`../config/agents.json`](../config/agents.json): role name, allowed inputs, required outputs, and reviewer. Live credentials and runtime state are excluded.

### `SOUL.md`

Each profile has a private `SOUL.md` policy artifact that defines its mission, behavior, and boundaries. Publishing those files would disclose operational instructions, so the repository provides two narrower forms of evidence:

1. read-only metadata and distinct SHA-256 prefixes showing separate policy files existed; and
2. public behavioral contracts that describe the expected role without reproducing the private prompt.

The digest evidence establishes file distinction, not behavioral enforcement. Runtime behavior must be evaluated separately through traces, outputs, and controlled tests.

## Capability layer

### Skills

Hermes Skills package reusable procedures and tool instructions. In the prototype, Skills supported role-specific work such as research workflows and presentation production. Related procedures can be grouped into bundles so a multi-step workplace routine can be invoked consistently from Slack.

External Skills are treated as supply-chain inputs. The recorded installation flow quarantined the package, captured source provenance, ran the platform scan, and required human confirmation. A scan result narrows risk; it does not prove that third-party instructions are safe. Credentials belong in profile-scoped environment configuration and must never be embedded in Skill files.

### MCP

Model Context Protocol integrations provide adapters to external data and tools. The prototype configured a public-web data integration for the research profile. The portfolio separates three claims:

- the configuration screenshot shows that the MCP integration surface was configured;
- the credential value is fully redacted and is not present in Git history;
- the Slack workload capture separately shows a sourced market-research result delivered to the user.

This avoids treating configuration alone as proof of successful business execution.

## Slack request and delivery flow

The live interaction model is specialist-directed:

```text
Slack request
  -> profile-specific gateway
  -> profile policy and role boundary
  -> approved Skill / tool / optional MCP adapter
  -> specialist work product
  -> originating Slack thread
```

Two captured assignments document different operational paths:

- Oliver produced a public-source men's-clothing ranking snapshot with price, discount, rating, and review aggregates.
- Mia used role-specific Skills and tools to generate presentation material from a design-system specification.

The captures establish multi-profile use through one work interface. They do not establish autonomous delegation between profiles, continuous unattended operation, or population-level validity of the market sample.

## Public analytical reference

The executable repository implements an offline, dependency-free reference pipeline:

```text
synthetic CSV inputs
  -> Sam: validation
  -> Ada: descriptive analysis and chronological forecast evaluation
  -> Ethan: metric-linked decision notes
  -> Mia: portable SVG forecast chart
  -> Noah: figure-preserving narrative
  -> Sophie: required-artifact and consistency checks
  -> Oliver: reviewed report and Slack payload preview
```

### Input contracts

Product records require identifiers, category and brand labels, selling and list prices, ratings, review counts, and stock. Sales records require date, units, and revenue. Validation rejects missing columns, invalid numeric ranges, duplicate identifiers or dates, empty categorical fields, unsorted observations, and insufficient history.

Analysis does not begin when validation fails.

### Temporal evaluation

The baseline holds out the final seven daily observations. Model fitting uses only the preceding 28 observations; holdout predictions are then scored with MAE, RMSE, and MAPE. The code asserts that the training end precedes the holdout start. After evaluation, a full-history linear trend generates the next seven dates for the reference forecast.

The method is intentionally simple and inspectable. It is a contract and leakage test, not a production demand-forecasting model.

### Artifact lineage

Every completed stage appends a structured event containing:

- sequence number;
- specialist and role;
- stage name and status;
- named input and output artifacts; and
- checks performed at that boundary.

The final `trace.json` therefore records the route by which the report was produced. `metrics.json` contains data-quality, market, forecast, QA, and workflow fields. `forecast.svg`, `executive_report.md`, and `slack_payload.json` are generated from those approved values.

### QA gate

Sophie checks five prerequisites before Oliver can finalize the report:

1. data validation passed;
2. the forecast holdout occurs strictly after the training window;
3. the forecast chart exists;
4. decision notes were produced; and
5. the narrative is non-empty.

A failed prerequisite raises an error and prevents final report generation. The gate validates required artifacts and internal sequencing; it is not a substitute for statistical, domain, or human review.

## Reproducibility and verification

The public workflow requires no API key and makes no network request. A reviewer can run it directly or through the hardened Compose service. CI executes the test suite, regenerates the reference artifacts, compares them with the committed sample run, performs the privacy scan, verifies evidence-image hashes, and builds the Docker image.

The synthetic fixture contains 15 products and 35 chronological sales observations. The committed run completes all seven stages and passes the QA gate. Exact evaluation values and limitations are recorded in [`evaluation.md`](evaluation.md).

## Information excluded from the repository

The following materials are intentionally unavailable in the public project:

- Slack bot and app credentials;
- MCP authentication material;
- raw Slack workspace screenshots and message history;
- profile `.env` files and session state;
- private `SOUL.md` contents;
- personal filesystem paths, workspace identifiers, email/calendar data, and private network addresses; and
- original unredacted evidence files.

Only reviewed screenshot derivatives are committed. Their hashes and claim boundaries are recorded in [`evidence/evidence-register.md`](evidence/evidence-register.md).

## Ownership boundary

Hermes Agent, Slack, and external data services are third-party systems. The original work in this repository consists of the specialist role model, profile deployment design, Slack operating workflow, public analytics harness, validation and forecast logic, artifact contracts, QA gate, evidence sanitization, privacy scanning, tests, and documentation.
