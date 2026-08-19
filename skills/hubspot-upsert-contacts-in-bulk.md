---
name: Import or upsert HubSpot contacts in bulk
description: Load many contacts into HubSpot safely using the batch endpoints, deduplicating on email rather than on HubSpot object id.
api: openapi/hubspot-batch-api-openapi.yml
generated: '2026-08-13'
method: generated
source: openapi/hubspot-batch-api-openapi.yml, openapi/hubspot-contacts-api-openapi.yml, arazzo/hubspot-batch-import-contacts-workflow.yml, arazzo/hubspot-upsert-contact-workflow.yml
operations:
  - batchReadContacts
  - batchCreateContacts
  - batchUpdateContacts
  - searchContacts
---

# Import or upsert HubSpot contacts in bulk

Base URL: `https://api.hubapi.com`

## Why batch, not a loop

HubSpot's rate budget is per app per portal, and the secondly burst ceiling is
low relative to the daily ceiling. A loop of single `createContact` calls will
hit `429` long before it exhausts the daily quota. Batch endpoints move up to
100 objects per request, so a 10,000-contact import is ~100 requests instead of
10,000.

## Before you start

- `Authorization: Bearer <token>`; scope `crm.objects.contacts.write`.
- **No idempotency key exists.** Re-running `batchCreateContacts` on the same
  input creates duplicates. Deduplicate with `batchReadContacts` using
  `idProperty` before you write — that is the only replay protection HubSpot
  offers on this path.

## Steps

1. **Chunk your input into batches of 100.** This is the documented ceiling for
   the batch endpoints.

2. **Resolve which contacts already exist** — `batchReadContacts`
   `POST /crm/v3/objects/contacts/batch/read` with
   `{"idProperty": "email", "inputs": [{"id": "person@example.com"}, ...],
     "properties": ["email","firstname","lastname"]}`.
   Setting `idProperty` is what makes HubSpot match on the unique email property
   instead of the internal object id.

3. **Create the ones that came back missing** — `batchCreateContacts`
   `POST /crm/v3/objects/contacts/batch/create` with an `inputs` array of
   `{properties: {...}}`.

4. **Update the ones that already existed** — `batchUpdateContacts`
   `POST /crm/v3/objects/contacts/batch/update` with `inputs` of
   `{id, properties}`. Send only the properties you are changing.

5. **Verify anything ambiguous** — `searchContacts` for records that failed to
   resolve by email (blank email, or two records sharing one).

## Handling the response

- A batch that partially fails returns **`207 Multi-Status`** when multi-status
  error handling is enabled — the top-level call is a success and per-item
  outcomes live in the body. Parse the body; do not treat `2xx` as "all
  succeeded".
- `errors[].context.propertyName` identifies the offending field on a
  `VALIDATION_ERROR`.
- On `429`, back off and resume from the last confirmed chunk. Because there is
  no idempotency key, replaying a chunk you already committed will duplicate it —
  track committed chunks yourself.
- `524` means the request exceeded HubSpot's 100-second response limit; reduce
  the chunk size.

## Related

- `arazzo/hubspot-batch-import-contacts-workflow.yml`
- `arazzo/hubspot-upsert-contact-workflow.yml`
- `rate-limits/hubspot-rate-limits.yml`
- `conventions/hubspot-conventions.yml`
