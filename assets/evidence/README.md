# Published evidence images

These files are privacy-sanitized derivatives prepared for the public portfolio. They are not forensic originals.

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

Binary images require manual visual review. The repository privacy scanner does not claim OCR coverage.

`manifest.json` records each reviewed derivative's byte length and SHA-256 digest. CI runs `scripts/verify_evidence_images.py` so later image changes cannot silently replace the approved set.
