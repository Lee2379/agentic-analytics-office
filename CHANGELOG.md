# Changelog

All notable changes to the public evaluation harness are documented here.

## Unreleased

- Localize the Japanese architecture diagram and refine the Japanese summary, implementation boundary, human-approval flow, and request-path explanations to match the English source semantics.
- Add an explicit human-in-the-loop approval gate to the English and Japanese architecture: QA evidence can be approved, returned through the role router for revision, or rejected with a recorded rationale before final synthesis and Slack delivery.
- Add a Supabase-backed agent data-operations case study covering schema contracts, role-separated ingestion, five-table reconciliation, human-reviewed data quality, auditable SQL analysis, deployed BI delivery, Kanban orchestration, scheduled execution, and approval-gated publication.
- Add eleven privacy-reviewed evidence derivatives and bind them to source/public SHA-256 records.
- Synchronize the English and Japanese README summaries and extend the architecture/implementation documentation with the database data plane and workflow control plane.
- Remove the duplicated standalone live-workload section from both READMEs; retain the stronger Slack evidence placement and the detailed evidence record.

## 1.1.0 — 2026-08-12

- Add a privacy-reviewed Japanese direct-evidence fact-check capture and synchronize the English/Japanese architecture, request-path, runtime-primitive, and evidence documentation.
- Load and validate the packaged seven-agent contract registry at runtime; reject duplicate or drifted public contracts.
- Record agent objectives, artifact contracts, and reviewers in the execution trace.
- Enforce canonical ISO dates and consecutive daily observations before temporal modeling.
- Represent MAPE as undefined when a holdout contains no non-zero actuals and report its eligible-observation count.
- Add a content-addressed run manifest for the two CSV inputs, executed contract registry, and five generated outputs.
- Compare all six regenerated reference artifacts in CI and verify internal Markdown links.
- Pin the offline Python base image by digest and smoke-test it with no network, a read-only root filesystem, no Linux capabilities, and `no-new-privileges`.

## 1.0.0 — 2026-08-09

- Initial public release of the deterministic seven-stage analytics harness, synthetic evaluation fixture, privacy controls, operational evidence register, and bilingual documentation.
