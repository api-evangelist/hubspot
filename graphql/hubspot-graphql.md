# HubSpot GraphQL

## Description

HubSpot does not currently offer a public GraphQL API. All platform capabilities are exposed through a
comprehensive set of REST APIs covering CRM objects (Contacts, Companies, Deals, Tickets), Marketing
(Email, Forms, Landing Pages, Blog), Commerce (Payments, Quotes, Line Items), and platform utilities
(Properties, Associations, Owners, Lists, Workflows).

The schema provided alongside this document (`hubspot-schema.graphql`) is a **conceptual SDL** derived
from HubSpot's published REST data model. It faithfully maps field names and types documented in the
official OpenAPI specifications to GraphQL types, making it useful for:

- Understanding HubSpot's CRM data model at a glance
- Generating client-side type definitions for GraphQL tooling applied to the REST responses
- Evaluating a future HubSpot GraphQL layer built on top of the existing REST surface

## Endpoint

No GraphQL endpoint is currently available.

A probe against `https://api.hubapi.com/graphql` returns HTTP 404.

## Authentication

HubSpot REST APIs (and any future GraphQL layer) use OAuth 2.0 or Private App Access Tokens:

- **Private App Token**: Include as `Authorization: Bearer <token>` header.
- **OAuth 2.0**: Standard three-legged flow; exchange code for access + refresh tokens at
  `https://api.hubapi.com/oauth/v1/token`.

Scopes are defined per product area (e.g. `crm.objects.contacts.read`, `crm.objects.deals.write`).

## Notes

- Source: HubSpot Developer Documentation — https://developers.hubspot.com/docs/api/overview
- REST API catalog: https://api.hubspot.com/api-catalog-public/v1/apis
- The schema covers 24 core types drawn from the CRM, CMS, Commerce, and Marketing surface areas.
- Field lists reflect the default properties returned by HubSpot REST responses; custom properties are
  supported at runtime but cannot be enumerated statically.
- Association types between objects (Contact-Company, Deal-Contact, etc.) are modelled as object-typed
  fields and lists, matching HubSpot's Associations v4 data model.
