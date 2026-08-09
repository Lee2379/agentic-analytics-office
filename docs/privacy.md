# Privacy and publication model

## Public-data principle

The repository publishes only synthetic data, aggregate metrics, code, configuration templates, sanitized runtime metadata, and selected privacy-sanitized screenshot derivatives. It does not publish private email or calendar content, credentials, host paths, workspace names, application identifiers, or unreviewed raw screenshots.

## Evidence handling

1. Raw evidence remains outside the repository.
2. Only the minimum useful screenshots receive public derivatives.
3. Opaque masks replace sensitive pixels; blur is not accepted as redaction.
4. Free-form profile descriptions may be normalized when the change is disclosed beside the image.
5. Selected originals and every published derivative receive a SHA-256 digest in the evidence register.
6. A repository-wide text scanner blocks common secret and privacy patterns in CI; image review is manual because the scanner does not OCR binaries.
7. Private originals may be shown selectively during an interview, after rechecking the visible frame.

## Forbidden content

- `.env` or credential files;
- Slack bot/app tokens and OAuth credentials;
- authentication tokens embedded in URLs;
- email addresses and private messages;
- personal local filesystem paths;
- private, Tailscale, or internal network addresses;
- raw session history or model-provider metadata tied to a private account.

## Incident found during curation

One candidate screenshot contained a data-access token inside a configuration URL. Only a derivative with a fully opaque white mask over the credential value is published. The original is excluded. Revocation and reissuance are still required because redacting a screenshot does not invalidate the original credential.
