# MCP integration evidence

![Hermes MCP configuration with the authentication token fully redacted](../../assets/evidence/04-mcp-integration-token-redacted.png)

## Supported claim

The Hermes deployment exposed an MCP configuration workflow for connecting an approved public-data service. This image demonstrates the integration surface, not successful data retrieval by itself; the delivered Slack market report provides the separate workload evidence.

## Sanitization and incident response

The original screenshot contained an authentication token embedded in the URL. The committed derivative covers the complete token value with an opaque white mask and labels it `[REDACTED]`. The original is not committed or hashed into the public evidence chain.

Masking protects the portfolio image but does not revoke the credential. The token must still be revoked and reissued before any further use.
