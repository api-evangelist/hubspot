# Programmatic API Onboarding — HubSpot

A single-file, zero-dependency Node.js (18+) CLI that reproduces SoundCloud's
`sc-api-auth.mjs` pattern for HubSpot: register an application / obtain credentials
programmatically instead of clicking through a dashboard, so agents and developers
can onboard at the command line.

- Script: [`hubspot-api-auth.mjs`](hubspot-api-auth.mjs)
- Run `node hubspot-api-auth.mjs --help` for usage and the required environment variables.
- Story / rationale: https://apievangelist.com/2026/08/25/hubspot-oauth-but-create-the-app-by-hand/

Part of the API Evangelist "Programmatic API Onboarding for the Agentic Moment" series.
