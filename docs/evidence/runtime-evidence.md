# Sanitized runtime evidence

**Collection date:** 2026-08-09<br>
**Scope:** read-only metadata from the local Hermes Docker deployment<br>
**Credential values read:** no<br>
**Private profile prompts or sessions read:** no

## Container

| Control | Observed value |
|---|---|
| Image | `nousresearch/hermes-agent:latest` |
| State | running |
| Restart policy | `unless-stopped` |
| Memory limit | 4,294,967,296 bytes (4 GiB) |
| CPU limit | 2,000,000,000 NanoCPUs (2 CPUs) |
| Published ports | none |
| Mounted destinations | `/opt/data` only |
| Docker socket mounted | no |
| Evidence command identity | `uid=1000(hermes) gid=1000(hermes)` |

The moving image tag is reported as observed, not recommended. A production version should use a tested immutable digest.

## Runtime versions

```text
Hermes Agent v0.20.0 (2026.8.3)
Python 3.13.5
OpenAI SDK 2.24.0
```

## Analytics-office profiles

| Profile | Gateway | Model | Skills reported | Profile policy file |
|---|---|---|---:|---|
| Ada | running | `gpt-5.6-sol` | 81 | present |
| Ethan | running | `gpt-5.6-sol` | 79 | present |
| Mia | running | `gpt-5.6-sol` | 81 | present |
| Noah | running | `gpt-5.6-sol` | 79 | present |
| Oliver | running | `gpt-5.6-sol` | 80 | present |
| Sam | running | `gpt-5.6-sol` | 79 | present |
| Sophie | running | `gpt-5.6-sol` | 81 | present |

The collector used only `hermes --version`, `id`, `hermes profile list`, `hermes profile show <name>`, and selected `docker inspect --format` fields. It did not print environment variables, Slack identifiers, profile contents, messages, or host mount sources.
