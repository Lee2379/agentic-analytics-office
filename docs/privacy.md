# Privacy and publication model

## Public-data principle

The repository publishes only synthetic data, aggregate metrics, code, configuration templates, and sanitized runtime metadata. It does not publish raw Slack messages, private email or calendar content, credentials, host paths, workspace names, or application identifiers.

## Evidence handling

1. Raw evidence remains outside the repository.
2. A minimal sanitized narrative records only facts needed to support the claim.
3. Selected originals receive a SHA-256 digest in the evidence register.
4. A repository-wide scanner blocks common secret and privacy patterns in CI.
5. Private originals may be shown selectively during an interview, after rechecking the visible frame.

## Forbidden content

- `.env` or credential files;
- Slack bot/app tokens and OAuth credentials;
- authentication tokens embedded in URLs;
- email addresses and private messages;
- personal local filesystem paths;
- private, Tailscale, or internal network addresses;
- raw session history or model-provider metadata tied to a private account.

## Incident found during curation

One candidate screenshot contained a data-access token inside a configuration URL. It is excluded. Revocation and reissuance are recommended because redacting a screenshot does not invalidate the original credential.
