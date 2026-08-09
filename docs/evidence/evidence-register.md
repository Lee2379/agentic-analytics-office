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
| E-006 | Docker check of seven profiles' Slack configuration presence | private terminal evidence | 163,454 | `9f98045ac55c54b648e58ff9fab7ab03d6b2e46dfa404c71567556adb321af93` |
| E-007 | Hermes skill quarantine, scan, and installation trace | private terminal evidence | 322,050 | `3f0a2f1866c4f1fb09aebec188fdba72117373e5f72783ae4023a3b5b4d1cfd2` |
| E-008 | GWS Gmail capability and validation/help response | private terminal evidence | 295,366 | `b405a7298a47bad57def924897d75f7b3fa867f51622e4ff6d8c47889d85845a` |
| E-009 | Oliver `SOUL.md` strategic-planning persona excerpt | selected policy UI | 163,040 | `c0daed16b668e1aa821fe56228621f1e1caa649df51bbbef308a65a2a7675175` |

## Published derivatives

| ID | Public artifact | Sanitization | Bytes | SHA-256 |
|---|---|---|---:|---|
| P-001 | `assets/evidence/01-hermes-profile-registry-sanitized.png` | local paths/account avatar masked; role descriptions normalized | 1,158,418 | `f0b62fcbd04c2d6788125be8f0eef555c95391609268af4bc0702921c34401ef` |
| P-002 | `assets/evidence/02-slack-multi-agent-sanitized.png` | requester name/avatar masked | 1,218,939 | `6dfd1f2bd52572653743fc9f77887296cb9ed537bc80c2f4788c2bcc2ec3bfb9` |
| P-003 | `assets/evidence/03-live-market-research-sanitized.png` | workspace/requester/private channel masked | 1,631,029 | `a206cb5ba774fca288925beea09976f049251cfd3391e8394fd7f1def3414411` |
| P-004 | `assets/evidence/04-mcp-integration-token-redacted.png` | full credential value covered by opaque white mask; account avatar masked | 1,126,794 | `24fef86b7c6fba9e3e67edd0c840ea8f8a7f7aec6b8e539377a5b74c8120ac73` |
| P-005 | `assets/evidence/05-docker-slack-profile-isolation-sanitized.png` | personal host prompt replaced; no credential values displayed | 1,280,149 | `3cf3c69ac94d11317837dae52c1995d59a7124ef1f3c829d7ae90217cc157744` |
| P-006 | `assets/evidence/06-skill-installation-sanitized.png` | personal shell prompt replaced | 1,431,361 | `85214a64c2dd540aed2dc321bccbc75ad9a64d356e82296e6548207b6a7db385` |
| P-007 | `assets/evidence/07-soul-policy-files-sanitized.png` | generated from read-only Docker metadata; no policy body displayed | 70,897 | `4e64aca814e8c2be9af10153891565cd58b4d113c305a7cfe8aa573fc9184f0b` |
| P-008 | `assets/evidence/08-slack-specialist-work-sanitized.png` | requester identity and personal paths masked | 1,324,338 | `b1368e37b2138c09f9784db478555933a20e14035b9b293ba541df936f839dcb` |
| P-009 | `assets/evidence/09-gws-gmail-capability-sanitized.png` | personal shell prompt covered; no mailbox content displayed | 244,770 | `0b622a915fdd50425d536ec11f1545f219c10b2f3ec0355ac2b595d4b864d0fc` |
| P-010 | `assets/evidence/11-oliver-soul-policy-excerpt-sanitized.png` | selected non-secret role-policy excerpt approved for publication; original pixels preserved | 139,189 | `ead7ad39ee156a572bd474f87cb7997fd838f3757f3d8618fbba704425fde278` |

## Explicit exclusions

- Slack API application inventory screens: workspace and application identifiers.
- Environment-file editor screens: unsafe precedent even when visible values appear blank.
- Screens containing actual email, calendar, task, or personal morning-brief content.
- Unredacted local profile screens containing personal filesystem names.
- The original data-access configuration screen containing an authentication token in a URL.

The exposed data-access token must be revoked and reissued. Its original screenshot is not hashed here because a credential-bearing source must not become part of the portfolio evidence chain; only P-004 is published.
