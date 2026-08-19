---
name: Receive and process HubSpot webhook events
description: Consume HubSpot's CRM webhook deliveries safely — verify the signature, treat the payload as a notification rather than data, and re-read the object before acting.
api: asyncapi/hubspot-webhooks-asyncapi.yml
generated: '2026-08-13'
method: generated
source: asyncapi/hubspot-webhooks-asyncapi.yml, openapi/hubspot-contacts-api-openapi.yml, openapi/hubspot-deals-api-openapi.yml
operations:
  - getContact
  - getCompany
  - getDeal
  - getTicket
---

# Receive and process HubSpot webhook events

Event surface: `asyncapi/hubspot-webhooks-asyncapi.yml` (AsyncAPI 2.6.0)
Management API base URL: `https://api.hubapi.com`

## The shape of the contract

HubSpot delivers HTTP POSTs to a target URL you register on the app. Deliveries
are **batched** — one request body carries an array of event objects, each with
`subscriptionType` (e.g. `contact.creation`, `contact.propertyChange`,
`deal.propertyChange`), `objectId`, `portalId`, `occurredAt`, `eventId` and,
for property changes, `propertyName` and `propertyValue`.

Subscription types cover contacts, companies, deals, tickets and conversations.
The channel list in the AsyncAPI document is authoritative for this repo.

## Steps

1. **Return 200 fast.** Acknowledge the delivery before you do any work.
   HubSpot retries on a non-2xx, and slow handlers become duplicate deliveries.

2. **Verify the request signature** before trusting anything in the body. An
   unverified webhook endpoint is an unauthenticated write path into your system.

3. **Deduplicate on `eventId`.** Delivery is at-least-once. Because HubSpot's
   REST API has **no idempotency key** (see
   `conventions/hubspot-conventions.yml`), a duplicated event that triggers a
   write will create a duplicate record unless you dedupe here.

4. **Sort by `occurredAt` within a batch.** Events for one object can arrive in
   the same body out of order; applying them in delivery order can leave you with
   an older value.

5. **Re-read the object before acting** — `getContact`, `getCompany`, `getDeal`,
   `getTicket`. The payload tells you an object *changed*; it is not a
   trustworthy snapshot of the object's current state. Fetch the record and act
   on what the API returns.

6. **Back off on `429` while re-reading.** A burst of webhook events becomes a
   burst of reads against the same per-app-per-portal budget your foreground
   traffic uses.

## Handling failures

- Errors from the re-read follow the standard envelope
  `{status, message, category, correlationId, errors[]}`; keep
  `correlationId` alongside `eventId` in your logs so a HubSpot support ticket
  can join the two.
- `404` on re-read is normal and expected — the object may have been deleted
  between the event and your fetch. Treat it as a terminal outcome, not an error.

## Related

- `asyncapi/hubspot-webhooks-asyncapi.yml`
- `errors/hubspot-problem-types.yml`
- `rate-limits/hubspot-rate-limits.yml`
