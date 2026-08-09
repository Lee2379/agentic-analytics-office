# Docker and per-profile Slack configuration

![Read-only Docker check of per-profile Slack configuration](../../assets/evidence/05-docker-slack-profile-isolation-sanitized.png)

## Supported claim

The check ran inside the `hermes-docker` container and inspected configuration presence for Ada, Ethan, Mia, Noah, Oliver, Sam, and Sophie. Every profile reported:

- Slack bot configuration present;
- Slack app configuration present;
- a user allowlist configured;
- no open-access flag configured.

The command intentionally reports only `set`, `configured`, or `not_configured`; it does not print credential or user-ID values.

## Boundary

This evidence supports seven profile-specific configuration paths in one Docker runtime. It does not prove that token values are unique, valid, or currently accepted by Slack. The profile registry and Slack work captures provide the separate runtime and delivery evidence.

## Sanitization

The personal host prompt was replaced with `[HOST]$`. No credential value was present in the source or derivative.
