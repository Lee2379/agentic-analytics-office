# Google Workspace Gmail capability

![Sanitized GWS Gmail capability discovery](../../assets/evidence/09-gws-gmail-capability-sanitized.png)

## Supported claim

The configured environment recognized the `gws gmail` command and exposed operations for sending, triaging, replying to, forwarding, reading, and watching Gmail messages. The help response also displayed a `--sanitize` option for processing API responses through a Model Armor template.

This establishes that the Google Workspace Gmail capability surface was installed and discoverable in the operating environment.

## Boundary

The command was invoked without a required Gmail subcommand and returned a validation/help response. The capture does **not** prove:

- successful OAuth authorization;
- mailbox access;
- granted permission scopes;
- a completed Gmail API call; or
- successful Model Armor processing.

No email address, message, thread, label, OAuth token, project identifier, or mailbox content is displayed. A future non-sensitive health check should record authorization state and a minimal API success result without returning personal data.

## Sanitization

The personal shell prompt was covered with an opaque background-colored mask. The `gws gmail` command and original help output were otherwise preserved. No generative image editing was used.
