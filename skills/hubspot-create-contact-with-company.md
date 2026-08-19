---
name: Create a HubSpot contact and link it to a company
description: Create a CRM contact, create or find its company, and associate the two, using HubSpot's REST API with OAuth or a private-app token.
api: openapi/hubspot-contacts-api-openapi.yml
generated: '2026-08-13'
method: generated
source: openapi/hubspot-contacts-api-openapi.yml, openapi/hubspot-companies-api-openapi.yml, openapi/hubspot-associations-api-openapi.yml, arazzo/hubspot-create-contact-with-company-workflow.yml
operations:
  - searchContacts
  - createContact
  - searchCompanies
  - createCompany
  - createContactAssociation
---

# Create a HubSpot contact and link it to a company

Base URL: `https://api.hubapi.com`

## Before you start

- Authenticate with `Authorization: Bearer <token>` — either an OAuth 2.0 access
  token (authorize `https://app.hubspot.com/oauth/authorize`, token
  `https://api.hubapi.com/oauth/v1/token`) or a private-app access token. There is
  no separate test host: a sandbox is a different HubSpot account, not a
  different base URL.
- Required scopes: `crm.objects.contacts.write` and `crm.objects.companies.write`.
  See `scopes/hubspot-scopes.yml`.
- **There is no idempotency key.** HubSpot publishes no `Idempotency-Key`
  contract, so a retried `createContact` creates a SECOND contact. Search first
  (step 1) and treat that search as your deduplication, or use the batch upsert
  path with `idProperty: email`. See `conventions/hubspot-conventions.yml`.

## Steps

1. **Look for an existing contact** — `searchContacts`
   `POST /crm/v3/objects/contacts/search` with a `filterGroups` filter on
   `email` using operator `EQ`. If `results` is non-empty, skip step 2 and reuse
   `results[0].id`.

2. **Create the contact** — `createContact`
   `POST /crm/v3/objects/contacts` with a `properties` object
   (`email`, `firstname`, `lastname`, `phone`). Keep the returned `id`.

3. **Look for the company** — `searchCompanies`
   `POST /crm/v3/objects/companies/search` filtering on `domain` with `EQ`.

4. **Create the company if it is missing** — `createCompany`
   `POST /crm/v3/objects/companies` with `properties.name` and
   `properties.domain`. Keep the returned `id`.

5. **Associate them** — `createContactAssociation`
   HubSpot does not store the link as a field on either object; it is a typed
   edge created through the Associations API. Use the contact id from step 1/2 as
   the from-object and the company id from step 3/4 as the to-object.

## Handling the response

- Success on create is `201`; reads are `200`.
- Errors are `application/json` with
  `{status, message, category, correlationId, errors[]}` — **not** RFC 9457
  problem+json. Log `correlationId` (also returned as the
  `x-hubspot-correlation-id` response header) on every failure.
- `400` with `category: VALIDATION_ERROR` means a property value is invalid or a
  required property is missing; `errors[].context.propertyName` names the field.
- `403` means the token is valid but the app lacks a scope — do not retry, fix
  the scope.
- `429` means the per-app-per-portal budget is exhausted. Back off and read
  `X-HubSpot-RateLimit-Daily-Remaining` /
  `X-HubSpot-RateLimit-Secondly-Remaining`.
- `423` means a data sync is running — retry after 2+ seconds.

## Related

- `arazzo/hubspot-create-contact-with-company-workflow.yml` — the runnable workflow
- `errors/hubspot-problem-types.yml`
- `data-model/hubspot-data-model.yml`
