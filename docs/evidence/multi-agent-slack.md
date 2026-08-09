# Multi-agent Slack evidence

![Privacy-sanitized Slack thread showing multiple agents](../../assets/evidence/02-slack-multi-agent-sanitized.png)

## Supported claim

The live Slack interface could address multiple separately named Hermes profiles and receive role-aware responses in one thread. This supports deployment and channel-integration claims.

## Sanitization

- the human requester's display name is replaced with `[REQUESTER]`;
- the requester avatar is covered with an opaque neutral mask;
- agent names and visible responses remain available for review.

## Boundary

This lightweight availability check does not establish that the agents autonomously delegated work to one another. The reproducible harness demonstrates the sequential handoff contract; the screenshot demonstrates live multi-profile accessibility through Slack.
