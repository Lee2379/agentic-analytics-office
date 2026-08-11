# Published evidence images

These files are privacy-reviewed captures prepared for the public portfolio. The set contains sanitized derivatives and low-sensitivity captures approved without pixel edits; neither category is treated as a forensic original.

| File | Purpose | Public edits |
|---|---|---|
| `01-hermes-profile-registry-sanitized.png` | Deployment overview | local paths and account avatar masked; role descriptions normalized |
| `02-slack-multi-agent-sanitized.png` | Multi-profile Slack availability | requester name and avatar masked |
| `03-live-market-research-sanitized.png` | Real business workload | workspace, requester identity, and private channel label masked |
| `04-mcp-integration-token-redacted.png` | MCP configuration surface | full token value covered by an opaque white mask; account avatar masked |
| `05-docker-slack-profile-isolation-sanitized.png` | Docker/per-profile Slack configuration | personal host prompt replaced; no credential values displayed |
| `06-skill-installation-sanitized.png` | Skills provenance and scan workflow | personal shell prompt replaced |
| `07-soul-policy-files-sanitized.png` | Profile-specific policy metadata | generated from read-only collector output; no policy body displayed |
| `08-slack-specialist-work-sanitized.png` | Specialist presentation task in Slack | requester identity and personal paths masked |
| `09-gws-gmail-capability-sanitized.png` | Google Workspace Gmail capability discovery | personal shell prompt covered; no mailbox data displayed |
| `11-oliver-soul-policy-excerpt-sanitized.png` | Selected Oliver role-policy example | approved non-secret excerpt; original pixels preserved |
| `12-oliver-analysis-charter-request-sanitized.png` | Bounded retail-analysis planning request | requester name, avatar, and timestamp covered with opaque white masks |
| `13-oliver-analysis-charter-result-sanitized.png` | Oliver file-backed charter execution | already-redacted private path segment re-covered with an opaque white mask |
| `15-magma-design-system-deliverable-sanitized.png` | Generated design-system PDF preview | metadata-normalized copy; no private identifier or credential observed in the published frame |
| `16-obsidian-raw-source-ingestion.png` | Source-addressed Obsidian research corpus | no pixel edits; public source provenance retained |
| `17-oliver-librarian-workflow.png` | Librarian routing and duplicate-task suppression | no pixel edits; generic vault identifiers retained |
| `18-structured-concept-page.png` | Typed concept, confidence, provenance, and relations | no pixel edits; public source provenance retained |
| `19-evidence-linked-synthesis.png` | Multi-source synthesis artifact | no pixel edits; vault-relative provenance retained |
| `20-fact-check-english.png` | English claim review | no pixel edits; citation markers retained |
| `21-fact-check-japanese.png` | Japanese claim review | no pixel edits; citation markers retained |
| `22-japanese-corrections-and-sources.png` | Japanese corrections and source traceability | no pixel edits; public source URLs retained |
| `23-agent-generated-market-report-deck.png` | Fifteen-slide market-report overview | no pixel edits; portfolio deliverable retained |
| `24-fact-interpretation-question-slide.png` | Decision-hygiene presentation slide | no pixel edits; portfolio deliverable retained |
| `25-source-register-slide.png` | Presentation source appendix | no pixel edits; public source URLs retained |
| `26-trilingual-correction-diff.png` | English, Korean, and Japanese corrections | no pixel edits; multilingual review output retained |

Binary images require manual visual review. The repository privacy scanner does not claim OCR coverage.

`manifest.json` records each reviewed capture's byte length and SHA-256 digest. CI runs `scripts/verify_evidence_images.py` so later image changes cannot silently replace the approved set.
