# Profile-specific `SOUL.md` policy files

![Sanitized collector output for seven SOUL.md files](../../assets/evidence/07-soul-policy-files-sanitized.png)

## Collection method

A read-only Docker command checked the file size and SHA-256 digest of each profile's `SOUL.md`. It did not print file contents, inspect credentials, or modify the container.

## Supported claim

- all seven specialist profiles have a `SOUL.md` policy file;
- all seven recorded digest prefixes are distinct;
- the policy artifacts are therefore not one identical file copied across every role at the time of collection.

## Boundary

Hashes establish file identity, not behavioral enforcement. The private policy bodies remain outside the repository. [`config/agents.json`](../../config/agents.json) is the public, machine-readable contract derived for portfolio review; it is not presented as a byte-for-byte copy of the private `SOUL.md` files.
