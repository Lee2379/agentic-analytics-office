# Limitations and next experiments

## Current limitations

1. **No public LLM run:** the reproducible harness is deterministic and does not call the private production model.
2. **Private workspace evidence:** raw Slack screenshots cannot be published without exposing identifiers and operational context.
3. **Single live market snapshot:** the captured ranking is small, dynamic, and selection-biased.
4. **No single-agent baseline yet:** the repository evaluates the role pipeline but not its incremental benefit over one generalist prompt.
5. **Simple forecast:** linear trend is an interpretable baseline, not a production demand-forecasting model.
6. **Moving upstream image tag:** the observed live deployment used `latest`; production should pin a digest.
7. **Human approval remains external:** the harness models a QA gate but does not automate Slack approval decisions.

## Planned experiments

- Compare the seven-stage pipeline with a single-agent baseline on answer accuracy, revision rate, latency, and token cost.
- Add repeated public snapshots and quantify ranking volatility.
- Evaluate seasonal-naive, exponential-smoothing, and gradient-boosting forecast baselines.
- Capture fully synthetic Slack demonstrations in a dedicated demo workspace.
- Pin and attest the Hermes image, then record an SBOM and provenance metadata.
- Add failure injection for missing inputs, malformed tool output, and unavailable specialist profiles.
