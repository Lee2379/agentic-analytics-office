# Multi-Agent AI Analytics Office

**Language:** English | [日本語](README.ja.md)

[![CI](https://github.com/Lee2379/multi-agent-ai-analytics-office/actions/workflows/ci.yml/badge.svg)](https://github.com/Lee2379/multi-agent-ai-analytics-office/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-reproducible%20demo-2496ED?logo=docker&logoColor=white)
![Privacy](https://img.shields.io/badge/evidence-privacy--sanitized-176B3A)

**A role-based AI office for market research, data analysis, forecasting, review, and executive reporting—operated through Slack on the Hermes Agent runtime in Docker.**

This portfolio case study separates two things that are often mixed together:

1. **Operational evidence:** seven specialized Hermes profiles running in one bounded Docker deployment and serving work through Slack.
2. **Reproducible evaluation:** a deterministic, dependency-free Python harness that exercises the same role boundaries on synthetic data, produces an auditable trace, and is tested in CI.

No credentials, private messages, email/calendar data, workspace identifiers, or personal filesystem paths are published. Selected screenshots appear only as privacy-sanitized derivatives; the original private artifacts remain outside the repository.

## Executive summary

The prototype turns a general-purpose LLM runtime into a small virtual analytics office. A request is routed to agents with explicit responsibilities: data engineering, quantitative analysis, business interpretation, visualization, narrative, quality review, and final synthesis. Each stage emits a named artifact and a trace event instead of relying on an opaque group chat.

The live deployment demonstrated:

- seven isolated agent profiles with running gateways;
- Docker resource limits of 2 CPUs and 4 GiB memory;
- execution as the unprivileged `hermes` user;
- Slack delivery of a public-source market scan;
- role-specific work, including research, analysis, presentation generation, and operations support.

The public repository adds the missing engineering layer: deterministic data validation, leakage-safe holdout forecasting, artifact contracts, a QA gate, privacy scanning, tests, and a hardened offline container.

## Problem and design objectives

Market-research requests often combine source collection, data validation, quantitative analysis, interpretation, visualization, writing, and review in one unconstrained model interaction. That makes it difficult to identify where an error entered the workflow, which evidence supports a claim, or whether a final answer passed an independent check.

This project restructures that work around five design objectives:

1. **Role separation:** each specialist owns a bounded stage and an explicit output contract.
2. **Artifact-based handoffs:** metrics, charts, notes, verdicts, and reports move between stages as named artifacts rather than unstructured conversation history.
3. **Operational access:** Slack is the human-facing request and delivery surface; Hermes profiles provide specialist identities, policies, Skills, and tool access.
4. **Fail-closed review:** the final report is created only after data, forecast, chart, decision-note, and narrative checks pass.
5. **Reproducibility without disclosure:** the live deployment remains private, while a deterministic public harness reproduces the role sequence on synthetic data and emits reviewable outputs.

## Implementation model

The repository documents one system through two deliberately separate layers. Operational screenshots establish that the configured profiles were used in Docker and Slack; executable code establishes how the analytical contracts, evaluation logic, and QA gate behave. Neither layer is presented as a substitute for the other.

| Dimension | Live operational layer | Public reference layer |
|---|---|---|
| Runtime | Hermes Agent in one bounded Docker deployment | Python 3.11+ package and hardened offline container |
| Entry point | Slack mentions routed through profile gateways | `agentic-office run` CLI |
| Specialization | Seven Hermes profiles with profile-scoped identity, policy, Skills, and Slack configuration | Seven machine-readable contracts in [`config/agents.json`](config/agents.json) |
| Data access | Approved profile tools and optional MCP integrations | Synthetic CSV inputs; no network or external credentials |
| Coordination | Direct specialist routing for live work | Deterministic seven-stage artifact pipeline for evaluation |
| Outputs | Slack research reports and work products | JSON metrics and trace, SVG chart, Slack payload preview, executive report |
| Verification | Privacy-sanitized operational evidence with a digest register | Unit/integration tests, CI regeneration, privacy scan, and Docker build |

The detailed component model, configuration boundaries, and request paths are documented in [`docs/implementation.md`](docs/implementation.md).

## Operational evidence

The following evidence is organized by implementation layer: Docker profiles, Slack access controls, `SOUL.md` role policies, Skills, MCP, and live Slack work. The images are privacy-sanitized derivatives, not forensic originals. The underlying originals remain private and are linked to this case study by SHA-256 digest in the [evidence register](docs/evidence/evidence-register.md).

### Dockerized multi-profile runtime

![Sanitized Hermes profile registry showing the role-based deployment](assets/evidence/01-hermes-profile-registry-sanitized.png)

The runtime registry shows seven named specialist profiles with active gateways inside the Hermes deployment. Local paths and the account avatar are masked; free-form descriptions are normalized to public role labels.

![Read-only Docker check of per-profile Slack configuration](assets/evidence/05-docker-slack-profile-isolation-sanitized.png)

The read-only command executes inside `hermes-docker` and reports configuration presence without printing credential values. All seven profiles report bot/app configuration and an explicit user allowlist; open access is not configured. This supports profile-specific Slack configuration, but does not prove that the underlying token values are unique.

### `SOUL.md` role-policy separation

![Read-only metadata evidence for profile-specific SOUL.md files](assets/evidence/07-soul-policy-files-sanitized.png)

Each live profile has a `SOUL.md` file, and all seven files have distinct SHA-256 prefixes. The digests support separate policy artifacts; the public behavioral contracts are documented in [`config/agents.json`](config/agents.json), and enforcement remains a runtime claim rather than something the hashes alone can prove.

![Selected public excerpt from Oliver's SOUL.md role policy](assets/evidence/11-oliver-soul-policy-excerpt-sanitized.png)

The selected Oliver excerpt shows how a profile was given a concrete organizational role: head of strategic planning and researcher, with primary-source market reading and evidence-based decision support. This excerpt is intentionally public and contains no credentials. The complete policy, hidden instructions, and other profiles' policy bodies remain private.

### Skills and MCP integration

![Sanitized Hermes third-party skill installation and security scan](assets/evidence/06-skill-installation-sanitized.png)

The Skills workflow quarantines a third-party package, records source provenance, runs the Hermes security scan, shows the human confirmation step, and installs the reviewed files into the Oliver profile. A `SAFE` verdict is evidence of the recorded scan result, not a guarantee that third-party code is risk-free.

![Hermes MCP configuration with the credential value fully redacted](assets/evidence/04-mcp-integration-token-redacted.png)

The MCP screen shows the data-access integration surface used by the research workflow. The original credential value is completely covered by an opaque white mask. The live Slack report below is the separate evidence that a public-source research task produced a business result.

### Google Workspace capability discovery

![Sanitized GWS Gmail capability discovery in the configured environment](assets/evidence/09-gws-gmail-capability-sanitized.png)

The configured environment exposes the Google Workspace Gmail command surface for sending, triaging, replying, reading, and watching messages, together with an optional Model Armor sanitization parameter. The capture is a validation/help response because no Gmail subcommand was supplied. It confirms capability discovery, not successful OAuth authorization or mailbox retrieval; no message content or account identifier is displayed.

### Slack execution

<table>
  <tr>
    <td width="44%"><img src="assets/evidence/02-slack-multi-agent-sanitized.png" alt="Sanitized Slack thread showing multiple specialized agents responding" /></td>
    <td width="56%"><img src="assets/evidence/03-live-market-research-sanitized.png" alt="Sanitized live market-research result delivered through Slack" /></td>
  </tr>
  <tr>
    <td><strong>Multi-agent availability.</strong> A single request addresses the deployed specialist profiles in the shared Slack interface.</td>
    <td><strong>Business workload.</strong> A research specialist returns sourced pricing, discount, rating, and review aggregates from a live public ranking snapshot.</td>
  </tr>
</table>

![Sanitized Slack trace of Mia using role-specific skills and tools for presentation work](assets/evidence/08-slack-specialist-work-sanitized.png)

The two work captures show different specialists used for different assignments: Oliver for public-source market research and Mia for presentation generation with role-specific Skills and tools. They demonstrate multi-profile use in real Slack work; they do not establish autonomous agent-to-agent delegation.

Detailed evidence and claim boundaries: [Docker/Slack isolation](docs/evidence/docker-slack-isolation.md), [`SOUL.md` policy files](docs/evidence/soul-policy-files.md), [Skills supply chain](docs/evidence/skills-supply-chain.md), [MCP integration](docs/evidence/mcp-integration.md), [Google Workspace integration](docs/evidence/google-workspace-integration.md), [multi-agent Slack](docs/evidence/multi-agent-slack.md), [runtime metadata](docs/evidence/runtime-evidence.md), and [live workload](docs/evidence/live-workload.md).

## Architecture

```mermaid
%%{init: {"theme": "base", "themeVariables": {"fontSize": "18px", "fontFamily": "Arial, sans-serif", "lineColor": "#475569"}}}%%
flowchart TB
    U["Human request"] --> S["Slack gateway"]
    DATA["Public or synthetic data"]
    POLICY["Role and tool boundaries"]

    subgraph D["Hermes Agent runtime · Docker"]
      direction TB
      R["Role router"]

      subgraph ANALYSIS["Data and analysis"]
        direction LR
        SAM["Sam<br/>Data engineering"] --> ADA["Ada<br/>Quantitative analysis"] --> ETHAN["Ethan<br/>Business interpretation"]
      end

      subgraph DELIVERY["Communication and review"]
        direction LR
        MIA["Mia<br/>Visualization"] --> NOAH["Noah<br/>Narrative"] --> SOPHIE["Sophie<br/>QA and operations"]
      end

      OLIVER["Oliver<br/>Executive synthesis"]

      R --> SAM
      ETHAN --> MIA
      SOPHIE --> OLIVER
    end

    O["Slack delivery<br/>Report · metrics · execution trace"]

    S --> R
    DATA --> SAM
    POLICY --> R
    OLIVER --> O

    classDef input fill:#EFF6FF,stroke:#2563EB,color:#0F172A,stroke-width:2px;
    classDef gateway fill:#FFF7ED,stroke:#EA580C,color:#0F172A,stroke-width:2px;
    classDef router fill:#FAF5FF,stroke:#9333EA,color:#0F172A,stroke-width:2px;
    classDef agent fill:#ECFDF5,stroke:#059669,color:#0F172A,stroke-width:2px;
    classDef output fill:#FEF2F2,stroke:#DC2626,color:#0F172A,stroke-width:2px;

    class U,DATA,POLICY input;
    class S gateway;
    class R router;
    class SAM,ADA,ETHAN,MIA,NOAH,SOPHIE,OLIVER agent;
    class O output;
```

The live system supports direct routing to a specialist. The included offline harness models a full sequential handoff so the contracts and evaluation logic can be reviewed without access to private Slack or LLM credentials.

### Request paths

The live and public paths share the same role model but serve different verification purposes:

**Live specialist path**

1. A user mentions a named specialist in Slack.
2. That profile's gateway receives the event and applies profile-scoped configuration.
3. `SOUL.md` supplies the private role policy; installed Skills define reusable procedures and permitted tool use.
4. When the assignment requires external public data, the specialist can use an approved MCP integration.
5. The specialist returns the work product to the originating Slack thread.

**Public evaluation path**

1. The CLI loads synthetic product and chronological sales files.
2. Sam validates schema, values, uniqueness, and ordering before analysis starts.
3. Ada computes descriptive metrics and fits an interpretable trend on the training window only.
4. Ethan, Mia, and Noah independently produce decision notes, a portable chart, and a narrative from approved artifacts.
5. Sophie evaluates required controls and blocks finalization if any check fails.
6. Oliver emits the reviewed report and a Slack payload preview; the harness records every stage in `trace.json`.

The live prototype does not claim autonomous agent-to-agent delegation. Direct profile routing is operationally evidenced; the sequential public pipeline is an inspectable evaluation model of the intended handoffs.

### Hermes runtime primitives

| Primitive | Function in the live system | Public representation |
|---|---|---|
| Profile | Maintains one specialist identity and profile-scoped configuration/state within the shared runtime | Agent name, role, inputs, outputs, and reviewer in [`config/agents.json`](config/agents.json) |
| `SOUL.md` | Defines private persona, mission, decision boundaries, and response policy | Distinct file digests, one selected public excerpt, and non-sensitive behavioral contracts; complete policies are not published |
| Skill | Packages a reusable procedure and its tool instructions | Sanitized installation evidence and documented supply-chain boundary |
| MCP integration | Exposes an external data/tool adapter to an approved profile | Token-redacted configuration evidence and a separate Slack result capture |
| Slack gateway | Receives requests and returns profile responses in the work interface | Sanitized multi-profile and workload screenshots |
| Docker boundary | Hosts the shared Hermes runtime with bounded compute and no published service port or Docker socket | Secret-free deployment notes and an offline hardened Compose configuration |

This separation is intentional: configuration presence, policy hashes, and screenshots support narrowly stated operational claims, while public code and tests support reproducible engineering claims.

## Agent contracts

| Agent | Responsibility | Required output | Guardrail |
|---|---|---|---|
| Sam | Load and validate data | Data-quality summary | Stops on invalid or duplicated records |
| Ada | Compute market and forecast metrics | Quantitative metrics | No business claims without computed evidence |
| Ethan | Translate metrics into implications | Decision notes | Separates observation from recommendation |
| Mia | Render the analytical result | Portable SVG chart | Reads only approved aggregate metrics |
| Noah | Produce concise narrative | Draft summary | Must preserve figures and uncertainty |
| Sophie | Check completeness and consistency | QA verdict | Blocks finalization when required artifacts fail |
| Oliver | Synthesize the decision memo | Executive report | Uses only reviewed artifacts |

Machine-readable contracts are in [`config/agents.json`](config/agents.json).

## Live workload evidence

A sanitized production run analyzed a public men's-clothing ranking snapshot and delivered the result to Slack. The agent reported, for the visible top ten listings:

![Privacy-sanitized market-research result delivered to Slack](assets/evidence/03-live-market-research-sanitized.png)

- average price: **KRW 15,689**;
- median price: **KRW 12,210**;
- seven of ten listings at or below KRW 15,000;
- nine of ten listings displaying a discount;
- average displayed discount: **26.1%**;
- 1,067 combined reviews and a review-weighted rating of approximately **4.17/5**.

This is evidence of live task routing and delivery, not a population-level market estimate. The source was dynamic and the sample was rank-selected. The screenshot retains visible public product URLs as source context; the reproducible public dataset does not depend on them. See [`docs/evidence/live-workload.md`](docs/evidence/live-workload.md).

## Reproducible demo

The demo uses synthetic product and daily-sales data. It performs strict schema checks, computes descriptive market metrics, trains a linear trend only on the training window, evaluates on a chronological holdout, creates a seven-day forecast, and passes the artifacts through the seven agent contracts.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e .
agentic-office run \
  --products data/sample_products.csv \
  --sales data/sample_sales.csv \
  --output artifacts/local_run
```

Windows PowerShell activation:

```powershell
.venv\Scripts\Activate.ps1
```

Expected outputs:

```text
artifacts/local_run/
├── executive_report.md
├── forecast.svg
├── metrics.json
├── slack_payload.json
└── trace.json
```

Run the hardened offline demo:

```bash
docker compose up --build --abort-on-container-exit
```

The demo container runs as a non-root user, drops all Linux capabilities, sets `no-new-privileges`, uses a read-only root filesystem, and has no network dependency.

## Evaluation and quality gates

```bash
python -m unittest discover -s tests -v
python scripts/privacy_scan.py .
```

The CI workflow verifies:

- schema and data-quality rejection paths;
- chronological train/holdout separation;
- deterministic forecasting and report generation;
- completion of all seven role stages;
- QA-gate behavior;
- absence of common secrets, personal paths, private-network addresses, and email addresses.

Current deterministic benchmark results are recorded in [`docs/evaluation.md`](docs/evaluation.md). The committed output in [`artifacts/sample_run`](artifacts/sample_run) is regenerated and compared in CI.

### Reference benchmark

| Check | Committed result |
|---|---:|
| Valid synthetic product records | 15 |
| Chronological sales observations | 35 days |
| Training / holdout split | 28 / 7 days |
| Holdout MAE | 2.3831 units |
| Holdout RMSE | 2.7670 units |
| Holdout MAPE | 6.9532% |
| Seven-day projected demand | approximately 274 units |
| Workflow and QA status | 7/7 stages, passed |

These values are regression fixtures for the public harness, not production performance claims. The small synthetic dataset tests data contracts, temporal separation, artifact generation, and deterministic regeneration; it does not estimate general forecasting accuracy.

## Engineering decisions and trade-offs

- **Deterministic public harness:** no model call or network request is needed to reproduce the analytical result. This improves reviewability but does not reproduce private LLM reasoning.
- **Sequential public orchestration:** the reference workflow makes every handoff inspectable and testable. The live system can route directly to a specialist instead of executing the full chain for every request.
- **Chronological evaluation:** the final seven observations form the holdout and are excluded from fitting, preventing temporal leakage. The linear trend is deliberately interpretable and does not model seasonality, promotions, or causal effects.
- **Private operational state:** credentials, raw Slack history, `SOUL.md` bodies, sessions, and source screenshots stay outside Git. This limits external forensic verification, so public claims are scoped to sanitized evidence and recorded digests.
- **Artifact contracts over free-form coordination:** downstream roles consume approved outputs rather than unrestricted conversation context. This increases traceability at the cost of a more rigid workflow.
- **Upstream runtime boundary:** Hermes is consumed as a third-party runtime. The portfolio owns configuration, orchestration, evaluation, and evidence methodology—not the Hermes implementation itself.

## Privacy-preserving evidence policy

Raw screenshots are not evidence-safe: they can contain workspace labels, user display names, local paths, application IDs, or private operational context. Only ten reviewed derivatives are committed. Redaction uses opaque masks rather than blur, and each public derivative has its own SHA-256 digest in [`docs/evidence/evidence-register.md`](docs/evidence/evidence-register.md).

One supplied screenshot exposed an authentication token in a URL. The committed derivative covers the full credential value with an opaque white mask; the original is excluded from the repository and evidence chain. Redaction does not invalidate a leaked credential, so revocation and reissuance remain required.

## Contribution boundary

This project does **not** claim authorship of Hermes Agent, Slack, or the external data-access services. It uses the open-source [Hermes Agent](https://github.com/NousResearch/hermes-agent) runtime. My work in this case study is the role design, profile deployment, Docker operation, Slack workflow, deterministic evaluation harness, evidence methodology, privacy controls, and portfolio documentation.

No upstream Hermes source code is redistributed in this repository.

## Repository map

```text
config/                  Role contracts
data/                    Synthetic, non-identifying demo data
deployment/hermes/       Secret-free deployment notes and templates
docs/                     Architecture, evaluation, limitations, and evidence
assets/evidence/          Privacy-sanitized operational screenshots
scripts/                  Runtime evidence collector and privacy scanner
src/                      Deterministic analytics and orchestration harness
tests/                    Unit and integration tests
artifacts/sample_run/     Reproducible reference output
```

## Limitations

- The public harness is deterministic and does not call an LLM; it evaluates orchestration boundaries without exposing private model credentials.
- The live market scan is a single public ranking snapshot and is not statistically representative of the full market.
- Public screenshots are sanitized derivatives rather than forensic originals; private originals are available only for controlled interview review.
- The role sequence is evaluated; comparative experiments against a single-agent baseline remain future work.
- The live image was deployed from a moving `latest` tag. A production deployment should pin an immutable image digest.

## License

The original code and documentation in this repository are available under the [MIT License](LICENSE). Third-party products and trademarks remain the property of their respective owners.
