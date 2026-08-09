# Hermes deployment notes

This directory documents the live runtime boundary without publishing private Hermes state. It does not contain copied profile directories, sessions, tokens, or upstream source code.

## Observed topology

- one Docker container running Hermes Agent;
- seven analytics-office profiles: Ada, Ethan, Mia, Noah, Oliver, Sam, and Sophie;
- one Slack gateway per specialist profile;
- profile-specific policy and skill state persisted under the container data volume;
- no published container port and no Docker socket mount.

## Safe verification

Run the collector from the repository root:

```bash
./scripts/collect_runtime_evidence.sh
```

The collector prints version, unprivileged identity, selected container controls, and profile summaries. It never reads `.env`, `SOUL.md`, session history, messages, or host mount sources.

## Secret configuration

Use `env.example` only as a variable-name reference. Create real profile credentials through the Hermes setup flow or a secret manager. Never commit the populated file.

## Reproducibility note

The observed image was `nousresearch/hermes-agent:latest`. Before production use, replace the moving tag with a tested immutable digest and document the exact Hermes version.
