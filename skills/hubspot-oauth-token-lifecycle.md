---
name: hubspot-oauth-token-lifecycle
title: Run the HubSpot OAuth token lifecycle
description: Exchange an authorization code, inspect the token, refresh it before expiry, and revoke it — the credential loop every HubSpot integration must implement.
api: openapi/hubspot-token-management-api-openapi.yml
generated: '2026-08-13'
method: generated
source: openapi/hubspot-token-management-api-openapi.yml, openapi/hubspot-access-tokens-api-openapi.yml, openapi/hubspot-refresh-tokens-api-openapi.yml, arazzo/hubspot-oauth-token-lifecycle-workflow.yml
operations:
  - 'post-/oauth/2026-09/token_/oauth/v3/token'
  - 'post-/oauth/2026-09/token/introspect_/oauth/v3/token/introspect'
  - 'post-/oauth/2026-09/token/introspect_/oauth/v3/token/introspect'
  - 'post-/oauth/2026-09/token/revoke_/oauth/v3/token/revoke'
x-remapped: '2026-10-12: operationIds repointed to the current refined specs (the original ids were renamed by refine-openapis)'
---

# Run the HubSpot OAuth token lifecycle

Base URL: `https://api.hubapi.com`

## The endpoints

- Authorize: `https://app.hubspot.com/oauth/authorize`
- Token: `https://api.hubapi.com/oauth/v1/token`
- Server metadata: `https://app.hubspot.com/.well-known/oauth-authorization-server`
  (RFC 8414, HTTP 200 — `code_challenge_methods_supported: ["S256"]`)

The MCP server is a **separate** authorization server:
`https://mcp.hubspot.com/.well-known/oauth-authorization-server`, issuer
`https://mcp.hubspot.com`. Do not send an MCP token to `api.hubapi.com` or the
reverse. See `mcp/hubspot-mcp.yml`.

## Steps

1. **Send the user to authorize.** Build the authorize URL with `client_id`,
   `redirect_uri`, the exact `scope` list your app needs, and a PKCE
   `code_challenge` using `S256`. Requesting a scope the account's tier does not
   include fails the install, so request optional scopes as optional.

2. **Exchange the code** — `post-/oauth/2026-09/token_/oauth/v3/token`
   `POST /oauth/v1/token` with `grant_type=authorization_code`, `client_id`,
   `client_secret`, `redirect_uri`, `code`. Content type is
   `application/x-www-form-urlencoded`, not JSON. Store `access_token`,
   `refresh_token` and `expires_in`.

3. **Inspect what you were granted** — `post-/oauth/2026-09/token/introspect_/oauth/v3/token/introspect`
   `GET /oauth/v1/access-tokens/{token}` returns the portal (hub) id, the app id,
   the user, and the scopes actually granted. Do not assume you got the scopes
   you asked for — read them back and store them.

4. **Refresh before expiry** — `post-/oauth/2026-09/token_/oauth/v3/token` again with
   `grant_type=refresh_token`. Refresh on a timer derived from `expires_in`, not
   on a `401`: refreshing reactively means every consumer sees one failure first.
   `post-/oauth/2026-09/token/introspect_/oauth/v3/token/introspect` (`GET /oauth/v1/refresh-tokens/{token}`) tells you
   what a stored refresh token still covers.

5. **Revoke on uninstall** — `post-/oauth/2026-09/token/revoke_/oauth/v3/token/revoke`
   `DELETE /oauth/v1/refresh-tokens/{token}`. Do this when a customer
   disconnects; leaving live refresh tokens for uninstalled portals is the
   failure mode that turns into a security finding.

## Handling the response

- A bad or reused authorization code returns `400` from the token endpoint.
- An expired or invalid access token returns `401` with
  `category: INVALID_AUTHENTICATION` and the header
  `x-hubspot-auth-failure: 401 Unauthorized` (observed live on 2026-08-13).
- `403` is a **scope** failure, not an auth failure — the token is valid.
  Re-authorize with the missing scope; retrying will never succeed.
- Never log `client_secret`, `refresh_token` or `access_token`.

## Related

- `arazzo/hubspot-oauth-token-lifecycle-workflow.yml`
- `authentication/hubspot-authentication.yml`
- `scopes/hubspot-scopes.yml`
- `well-known/hubspot-well-known.yml`
