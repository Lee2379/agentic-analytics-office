# Skills and supply-chain evidence

![Sanitized Hermes skill-installation trace](../../assets/evidence/06-skill-installation-sanitized.png)

## Supported claim

The Hermes Skills workflow fetched a third-party `brightdata-guide` skill, placed it in quarantine, recorded upstream provenance and a source hash, ran the configured security scanner, required confirmation, and installed `SKILL.md` plus its reference files into the Oliver profile.

## Boundary

The screenshot records a `SAFE` scanner verdict and `ALLOWED` decision at that point in time. Automated scanning cannot guarantee that external instructions or scripts are risk-free. Production use should additionally pin an immutable source revision, review installed files, and re-scan changes.

## Sanitization

The personal shell prompt was replaced with `[HOST]$`. Public upstream URLs and the recorded source hash remain visible because they support provenance review.
