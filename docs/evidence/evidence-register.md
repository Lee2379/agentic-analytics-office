# Privacy-preserving evidence register

The raw screenshots are intentionally not committed. They contain workspace labels, user display names, local filesystem paths, or private operational context. This register records only a description, classification, byte length, and SHA-256 digest of selected originals.

The digests allow the owner to show during a private interview that a presented original is the same fixed artifact referenced here. They do not make the private evidence independently verifiable by a public reader.

| ID | Private artifact | Classification | Bytes | SHA-256 |
|---|---|---|---:|---|
| E-001 | Seven Hermes profiles visible and gateways running | private operational UI | 143,823 | `ed1e9e8ba7b6700e21f75a53dd0b9665e5e4eca8037bfe6cbaff374c7df984c8` |
| E-002 | Public-source market research delivered to Slack | private workspace evidence | 572,208 | `1f08c72c3f30c429d9908b008a136c4f731b1657cd7fdc9f11c9426ca8e397ea` |
| E-003 | Specialist presentation-generation task trace | private workspace evidence | 333,821 | `6b94acdf698e23eec9aad1d580b08ef2efa147b59ff8fd6336e5876b82feee66` |
| E-004 | Generated design-system deliverable preview | low-sensitivity deliverable | 155,748 | `8beee0cf3bcbb095c0175dad9b2268a50d24cee63c1d73c947690ce72803fc74` |

## Explicit exclusions

- Slack API application inventory screens: workspace and application identifiers.
- Environment-file editor screens: unsafe precedent even when visible values appear blank.
- Morning brief screens: potential email, calendar, or task information.
- Local URLs and profile screens containing personal filesystem names.
- Data-access configuration screen containing an authentication token in a URL.

The exposed data-access token must be revoked and reissued. The screenshot containing it is not hashed here because it must not become part of the portfolio evidence chain.
