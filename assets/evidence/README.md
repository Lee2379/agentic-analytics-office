# Published evidence images

These files are privacy-sanitized derivatives prepared for the public portfolio. They are not forensic originals.

| File | Purpose | Public edits |
|---|---|---|
| `01-hermes-profile-registry-sanitized.png` | Deployment overview | local paths and account avatar masked; role descriptions normalized |
| `02-slack-multi-agent-sanitized.png` | Multi-profile Slack availability | requester name and avatar masked |
| `03-live-market-research-sanitized.png` | Real business workload | workspace and requester identity masked |
| `04-mcp-integration-token-redacted.png` | MCP configuration surface | full token value covered by an opaque white mask; account avatar masked |

Binary images require manual visual review. The repository privacy scanner does not claim OCR coverage.

`manifest.json` records each reviewed derivative's byte length and SHA-256 digest. CI runs `scripts/verify_evidence_images.py` so later image changes cannot silently replace the approved set.
