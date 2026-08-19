---
name: Advance a HubSpot deal and log the activity
description: Move a deal through its pipeline stage and log the call, meeting or note that justified the move, so the CRM record explains itself.
api: openapi/hubspot-deals-api-openapi.yml
generated: '2026-08-13'
method: generated
source: openapi/hubspot-deals-api-openapi.yml, openapi/hubspot-basic-operations-api-openapi.yml, openapi/hubspot-meetings-api-openapi.yml, arazzo/hubspot-advance-deal-stage-workflow.yml, arazzo/hubspot-log-meeting-on-deal-workflow.yml
operations:
  - searchDeals
  - getDeal
  - updateDeal
  - createNote
  - createCall
  - createMeeting
  - createObjectAssociation
---

# Advance a HubSpot deal and log the activity

Base URL: `https://api.hubapi.com`

## Before you start

- `Authorization: Bearer <token>`; scopes `crm.objects.deals.write` and, for the
  engagement, `crm.objects.notes.write` / `crm.objects.calls.write` /
  `crm.objects.meetings.write`.
- A deal stage is a property value (`dealstage`) whose allowed values come from
  the pipeline the deal belongs to. Read the deal first — writing a stage id
  from a different pipeline is the most common `VALIDATION_ERROR` on this flow.

## Steps

1. **Find the deal** — `searchDeals`
   `POST /crm/v3/objects/deals/search`, filtering on `dealname`, `hs_object_id`
   or a custom external-id property.

2. **Read its current state** — `getDeal`
   `GET /crm/v3/objects/deals/{dealId}` requesting
   `properties=dealstage,pipeline,amount,closedate`. Confirm the target stage
   belongs to the returned `pipeline`.

3. **Move the stage** — `updateDeal`
   `PATCH /crm/v3/objects/deals/{dealId}` with
   `{"properties": {"dealstage": "<stage id>"}}`. Send only the properties you
   are changing; a PATCH with a full property bag will overwrite fields other
   systems own.

4. **Log the activity** — one of `createNote`, `createCall` or `createMeeting`.
   Set the engagement timestamp property so the activity lands on the timeline at
   the right moment, not at ingest time.

5. **Attach the activity to the deal** — `createObjectAssociation`
   The engagement is a separate CRM object. Until you associate it, it does not
   appear on the deal record. This step is not optional and is the one most
   often skipped.

## Handling the response

- `updateDeal` returns `200` with the updated object.
- `400` / `VALIDATION_ERROR` on `dealstage` almost always means the stage id
  belongs to another pipeline — re-read step 2.
- `404` means the deal id does not exist **in this portal**. A sandbox and a
  production account have different ids for the same logical record.
- Log `x-hubspot-correlation-id` from every failed response.

## Related

- `arazzo/hubspot-advance-deal-stage-workflow.yml`
- `arazzo/hubspot-log-meeting-on-deal-workflow.yml`
- `data-model/hubspot-data-model.yml` — why associations, not foreign keys
