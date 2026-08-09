# Privacy-preserving evidence register

Raw screenshots are intentionally not committed. They contain workspace labels, user display names, local filesystem paths, or private operational context. This register separately records selected private originals and the reviewed public derivatives.

Original digests allow the owner to show during a controlled interview that a presented private artifact is the same fixed file referenced here. Public-derivative digests make the committed visual set reproducible at the byte level. Neither digest turns a sanitized derivative into forensic proof.

| ID | Private artifact | Classification | Bytes | SHA-256 |
|---|---|---|---:|---|
| E-001 | Seven Hermes profiles visible and gateways running | private operational UI | 143,823 | `ed1e9e8ba7b6700e21f75a53dd0b9665e5e4eca8037bfe6cbaff374c7df984c8` |
| E-002 | Public-source market research delivered to Slack | private workspace evidence | 572,208 | `1f08c72c3f30c429d9908b008a136c4f731b1657cd7fdc9f11c9426ca8e397ea` |
| E-003 | Specialist presentation-generation task trace | private workspace evidence | 333,821 | `6b94acdf698e23eec9aad1d580b08ef2efa147b59ff8fd6336e5876b82feee66` |
| E-004 | Generated design-system deliverable preview | low-sensitivity deliverable | 155,748 | `8beee0cf3bcbb095c0175dad9b2268a50d24cee63c1d73c947690ce72803fc74` |
| E-005 | Multi-profile response thread in Slack | private workspace evidence | 303,516 | `c9e0e2ba2ca3e39a96c05a7cea9c51a614f0443a3244d9f0f81f0859dd500912` |

## Published derivatives

| ID | Public artifact | Sanitization | Bytes | SHA-256 |
|---|---|---|---:|---|
| P-001 | `assets/evidence/01-hermes-profile-registry-sanitized.png` | local paths/account avatar masked; role descriptions normalized | 1,158,418 | `f0b62fcbd04c2d6788125be8f0eef555c95391609268af4bc0702921c34401ef` |
| P-002 | `assets/evidence/02-slack-multi-agent-sanitized.png` | requester name/avatar masked | 1,218,939 | `6dfd1f2bd52572653743fc9f77887296cb9ed537bc80c2f4788c2bcc2ec3bfb9` |
| P-003 | `assets/evidence/03-live-market-research-sanitized.png` | workspace/requester identity masked | 1,510,376 | `1e166cecd24b7f3f8f26060fcc1c627a6f33caf715e3d1b1e5ad73e3de6cdd23` |
| P-004 | `assets/evidence/04-mcp-integration-token-redacted.png` | full credential value covered by opaque white mask; account avatar masked | 1,126,794 | `24fef86b7c6fba9e3e67edd0c840ea8f8a7f7aec6b8e539377a5b74c8120ac73` |

## Explicit exclusions

- Slack API application inventory screens: workspace and application identifiers.
- Environment-file editor screens: unsafe precedent even when visible values appear blank.
- Morning brief screens: potential email, calendar, or task information.
- Unredacted local profile screens containing personal filesystem names.
- The original data-access configuration screen containing an authentication token in a URL.

The exposed data-access token must be revoked and reissued. Its original screenshot is not hashed here because a credential-bearing source must not become part of the portfolio evidence chain; only P-004 is published.
