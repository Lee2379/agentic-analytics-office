# Security policy

## Reporting

Please do not open a public issue containing credentials, private workspace data, or personal information. Use GitHub's private vulnerability-reporting feature when enabled.

## Repository guarantees

- Demo data is synthetic.
- No live credential is required to run the tests or offline workflow.
- CI runs `scripts/privacy_scan.py` before accepting changes.
- Raw operational screenshots are not stored in Git.

## Credential response

If a credential is ever committed:

1. revoke and reissue it immediately;
2. remove it from the current tree and Git history;
3. audit access logs where available;
4. document the incident without reproducing the secret;
5. rerun the repository privacy scan.
