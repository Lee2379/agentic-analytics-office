# Deterministic benchmark

**Run date:** 2026-08-12<br>
**Python used for local verification:** 3.11.15<br>
**External dependencies:** none<br>
**Dataset:** synthetic 15-product assortment and 35 daily sales observations

## Test result

```text
Tests run: 12
Passed: 12
Failed: 0
```

Coverage includes data and agent-contract schema validation, public/package contract drift detection, duplicate rejection, canonical ISO date validation, continuous daily cadence, strict train/holdout separation, deterministic forecasting, zero-actual MAPE semantics, completion of all role stages, artifact hashing, and repository privacy scanning.

## Workflow result

| Metric | Result |
|---|---:|
| Role stages completed | 7 / 7 |
| Agent contract registry | v1.1; public/package copies matched |
| Valid product rows | 15 |
| Valid sales days | 35 |
| Duplicate SKUs | 0 |
| Duplicate dates | 0 |
| Consecutive daily cadence | passed |
| QA gate | passed |
| Hardened container smoke test | passed |

## Market summary

| Metric | Result |
|---|---:|
| Average price | KRW 22,766.67 |
| Median price | KRW 21,900 |
| Discounted product share | 93.33% |
| Average discount | 17.94% |
| Review-weighted rating | 4.233 / 5 |
| Total synthetic stock | 486 units |

## Forecast evaluation

The first 28 observations form the training window. The final seven observations form a strictly later holdout. No random split or holdout fitting is used.

| Metric | Result |
|---|---:|
| Train end | 2026-06-28 |
| Holdout start | 2026-06-29 |
| Training trend | +0.4745 units/day |
| Holdout MAE | 2.3831 units |
| Holdout RMSE | 2.7670 units |
| Holdout MAPE | 6.9532% |
| Non-zero actuals used by MAPE | 7 / 7 |
| Next-seven-day forecast | approximately 274 units |

These metrics validate the harness on one deliberately small synthetic dataset. They are not estimates of performance on a real production dataset.

## Reproducibility controls

The committed reference contains six generated files. CI regenerates the workflow from the two synthetic CSV inputs and the validated agent-contract registry, then requires exact normalized content equality for every output. `run_manifest.json` additionally records the package version, a deterministic run ID, input digests, output digests, and normalized byte counts. Internal Markdown links and all 24 reviewed evidence-image hashes are checked independently.

## Privacy scan

```text
privacy scan passed: no configured secret or personal-data patterns found
```

The scanner checks for common Slack credentials, credential-bearing URLs, email addresses, personal home paths, and private/Tailscale network addresses. It is a focused publication control, not a substitute for an enterprise secret-scanning platform.
