# HubSpot (hubspot)

HubSpot provides a full platform of marketing, sales, customer service, and CRM software plus the methodology, resources, and support to help businesses grow better.

**APIs.json:** [https://raw.githubusercontent.com/apis-json/artisanal/main/apis/hubspot.yml](https://raw.githubusercontent.com/apis-json/artisanal/main/apis/hubspot.yml)

## Scope

- **Position:** Consuming
- **Access:** 3rd-Party

## Tags

- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Operations
- Sales

## Timestamps

- **Created:** 2023/11/14
- **Modified:** 2026-05-19

## APIs

### HubSpot Domains API

These endpoints allow you to return information about the domains connected to a particular HubSpot CMS site. You can return data for a list of domains or specify a domain by ID.

- **Human URL:** [https://developers.hubspot.com/docs/api/overview](https://developers.hubspot.com/docs/api/overview)
- **Base URL:** `https://api.example.com`

#### Tags

- Domains

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/cms/domains)
- [OpenAPI](openapi/hubspot-domains-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/domains-api-domain-collection-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/domains-api-domain-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/domains-api-forward-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/domains-api-next-page-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/domains-api-domain-collection-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/domains-api-domain-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/domains-api-forward-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/domains-api-next-page-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/domains-api-domain-collection-response-example.json)
- [Code Examples](examples/domains-api-domain-example.json)
- [Code Examples](examples/domains-api-forward-paging-example.json)
- [Code Examples](examples/domains-api-next-page-example.json)

### HubSpot Source Code API

Endpoints for interacting with files in the CMS Developer File System. These files include HTML templates, CSS, JS, modules, and other assets which are used to create CMS content.

- **Human URL:** [https://developers.hubspot.com/docs/api/cms/source-code](https://developers.hubspot.com/docs/api/cms/source-code)
- **Base URL:** `https://api.example.com`

#### Tags

- Async
- Code
- Content
- Environments
- Extract
- Path
- Sources
- Status
- Task
- Validate

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/cms/source-code)
- [OpenAPI](openapi/hubspot-source-code-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/source-code-api-action-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/source-code-api-asset-file-metadata-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/source-code-api-file-extract-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/source-code-api-file-upload-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/source-code-api-task-locator-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/source-code-api-validation-error-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/source-code-api-validation-result-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/source-code-api-validation-warning-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-action-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-asset-file-metadata-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-file-extract-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-file-upload-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-task-locator-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-validation-error-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-validation-result-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/source-code-api-validation-warning-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/source-code-api-action-response-example.json)
- [Code Examples](examples/source-code-api-asset-file-metadata-example.json)
- [Code Examples](examples/source-code-api-file-extract-request-example.json)
- [Code Examples](examples/source-code-api-file-upload-request-example.json)
- [Code Examples](examples/source-code-api-task-locator-example.json)
- [Code Examples](examples/source-code-api-validation-error-example.json)
- [Code Examples](examples/source-code-api-validation-result-example.json)
- [Code Examples](examples/source-code-api-validation-warning-example.json)

### HubSpot Posts API

Use these endpoints for interacting with Blog Posts, Blog Authors, and Blog Tags.

- **Human URL:** [https://developers.hubspot.com/docs/api/cms/blog-post](https://developers.hubspot.com/docs/api/cms/blog-post)
- **Base URL:** `https://api.example.com`

#### Tags

- Archive
- Attach
- Batch
- Blog  Posts
- Blogs
- Clone
- Detach
- Draft
- Groups
- Language
- Live
- Multi
- Objects
- Posts
- Primary
- Read
- Reset
- Restore
- Revisions
- Schedules
- Set
- Variations

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/cms/blog-post)
- [OpenAPI](openapi/hubspot-blog-posts-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/blog-posts-api-attach-to-language-group-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-batch-input-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-batch-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-batch-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-batch-response-with-errors-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-blog-post-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-blog-post-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-blog-post-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-clone-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-create-language-variation-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-detach-from-language-group-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-paging-next-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-paging-previous-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-push-live-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-reset-draft-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-restore-previous-version-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-schedule-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-set-language-primary-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/blog-posts-api-version-history-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-attach-to-language-group-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-batch-input-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-batch-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-batch-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-batch-response-with-errors-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-blog-post-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-blog-post-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-blog-post-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-clone-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-create-language-variation-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-detach-from-language-group-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-paging-next-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-paging-previous-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-push-live-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-reset-draft-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-restore-previous-version-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-schedule-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-set-language-primary-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/blog-posts-api-version-history-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/blog-posts-api-attach-to-language-group-request-example.json)
- [Code Examples](examples/blog-posts-api-batch-input-example.json)
- [Code Examples](examples/blog-posts-api-batch-input-item-example.json)
- [Code Examples](examples/blog-posts-api-batch-response-example.json)
- [Code Examples](examples/blog-posts-api-batch-response-with-errors-example.json)
- [Code Examples](examples/blog-posts-api-blog-post-collection-example.json)
- [Code Examples](examples/blog-posts-api-blog-post-example.json)
- [Code Examples](examples/blog-posts-api-blog-post-input-example.json)
- [Code Examples](examples/blog-posts-api-clone-request-example.json)
- [Code Examples](examples/blog-posts-api-create-language-variation-request-example.json)
- [Code Examples](examples/blog-posts-api-detach-from-language-group-request-example.json)
- [Code Examples](examples/blog-posts-api-paging-example.json)
- [Code Examples](examples/blog-posts-api-paging-next-example.json)
- [Code Examples](examples/blog-posts-api-paging-previous-example.json)
- [Code Examples](examples/blog-posts-api-push-live-request-example.json)
- [Code Examples](examples/blog-posts-api-reset-draft-request-example.json)
- [Code Examples](examples/blog-posts-api-restore-previous-version-request-example.json)
- [Code Examples](examples/blog-posts-api-schedule-request-example.json)
- [Code Examples](examples/blog-posts-api-set-language-primary-request-example.json)
- [Code Examples](examples/blog-posts-api-version-history-example.json)

### HubSpot Authors API

Use the blog authors API to manage author information for your blog posts.

- **Human URL:** [https://developers.hubspot.com/docs/api/cms/blog-authors](https://developers.hubspot.com/docs/api/cms/blog-authors)
- **Base URL:** `https://api.example.com`

#### Tags

- Archive
- Attach
- Authors
- Batch
- Blogs
- Detach
- Groups
- Language
- Languages
- Multi
- Objects
- Primary
- Read
- Set
- Variations

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/cms/blog-authors)
- [OpenAPI](openapi/hubspot-authors-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/authors-api-attach-to-language-group-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-batch-archive-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-batch-input-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-batch-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-batch-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-batch-response-with-errors-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-blog-author-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-blog-author-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-blog-author-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-create-language-variation-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-detach-from-language-group-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-paging-next-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/authors-api-set-language-primary-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-attach-to-language-group-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-batch-archive-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-batch-input-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-batch-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-batch-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-batch-response-with-errors-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-blog-author-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-blog-author-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-blog-author-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-create-language-variation-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-detach-from-language-group-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-paging-next-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/authors-api-set-language-primary-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/authors-api-attach-to-language-group-request-example.json)
- [Code Examples](examples/authors-api-batch-archive-input-example.json)
- [Code Examples](examples/authors-api-batch-create-input-example.json)
- [Code Examples](examples/authors-api-batch-input-example.json)
- [Code Examples](examples/authors-api-batch-input-item-example.json)
- [Code Examples](examples/authors-api-batch-read-input-example.json)
- [Code Examples](examples/authors-api-batch-response-example.json)
- [Code Examples](examples/authors-api-batch-response-with-errors-example.json)
- [Code Examples](examples/authors-api-blog-author-collection-example.json)
- [Code Examples](examples/authors-api-blog-author-example.json)
- [Code Examples](examples/authors-api-blog-author-input-example.json)
- [Code Examples](examples/authors-api-create-language-variation-request-example.json)
- [Code Examples](examples/authors-api-detach-from-language-group-request-example.json)
- [Code Examples](examples/authors-api-paging-example.json)
- [Code Examples](examples/authors-api-paging-next-example.json)
- [Code Examples](examples/authors-api-set-language-primary-request-example.json)

### HubSpot URL Redirects API

URL redirects allow you to redirect traffic from a HubSpot-hosted page or blog post to any URL. You can also update URL redirects in bulk and use a flexible pattern redirect to dynamically update the structure of URLs.

- **Human URL:** [https://developers.hubspot.com/docs/api/cms/url-redirects](https://developers.hubspot.com/docs/api/cms/url-redirects)
- **Base URL:** `https://api.example.com`

#### Tags

- Redirects

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/cms/url-redirects)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CMS HubDB API

The HubDB API allows you to create, update, and delete HubDB data tables and their rows. HubDB tables can be used as data sources for dynamic CMS pages and are available in both draft and published versions.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/cms-hubdb-v3/guide](https://developers.hubspot.com/docs/api-reference/cms-hubdb-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CMS
- Content
- Data Tables
- HubDB

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/cms-hubdb-v3/guide)
- [OpenAPI](openapi/hubspot-cms-hubdb-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/cms-hubdb-api-collection-response-hub-dbrow-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-hubdb-api-collection-response-hub-dbtable-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-hubdb-api-hub-dbcolumn-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-hubdb-api-hub-dbrow-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-hubdb-api-hub-dbrow-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-hubdb-api-hub-dbtable-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-hubdb-api-hub-dbtable-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-hubdb-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-collection-response-hub-dbrow-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-collection-response-hub-dbtable-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-hub-dbcolumn-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-hub-dbrow-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-hub-dbrow-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-hub-dbtable-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-hub-dbtable-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-hubdb-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/cms-hubdb-api-collection-response-hub-dbrow-example.json)
- [Code Examples](examples/cms-hubdb-api-collection-response-hub-dbtable-example.json)
- [Code Examples](examples/cms-hubdb-api-hub-dbcolumn-example.json)
- [Code Examples](examples/cms-hubdb-api-hub-dbrow-create-request-example.json)
- [Code Examples](examples/cms-hubdb-api-hub-dbrow-example.json)
- [Code Examples](examples/cms-hubdb-api-hub-dbtable-create-request-example.json)
- [Code Examples](examples/cms-hubdb-api-hub-dbtable-example.json)
- [Code Examples](examples/cms-hubdb-api-paging-example.json)

### HubSpot CMS Pages API

The CMS Pages API provides endpoints for creating and managing site pages and landing pages hosted on HubSpot. You can create, retrieve, update, publish, and delete both site pages and landing pages programmatically.

- **Human URL:** [https://developers.hubspot.com/docs/api/cms/pages](https://developers.hubspot.com/docs/api/cms/pages)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CMS
- Landing Pages
- Pages
- Site Pages

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/cms/pages)
- [OpenAPI](openapi/hubspot-cms-pages-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/cms-pages-api-collection-response-page-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-pages-api-page-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-pages-api-page-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-pages-api-page-update-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/cms-pages-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-pages-api-collection-response-page-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-pages-api-page-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-pages-api-page-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-pages-api-page-update-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/cms-pages-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/cms-pages-api-collection-response-page-example.json)
- [Code Examples](examples/cms-pages-api-page-create-request-example.json)
- [Code Examples](examples/cms-pages-api-page-example.json)
- [Code Examples](examples/cms-pages-api-page-update-request-example.json)
- [Code Examples](examples/cms-pages-api-paging-example.json)

### HubSpot Contacts API

Contact records store information about individuals. The contacts endpoints allow you to manage contact data and sync it between HubSpot and other systems. You can create, retrieve, update, and delete contacts, as well as manage associations between contacts and other CRM objects.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/contacts](https://developers.hubspot.com/docs/api/crm/contacts)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Contacts
- CRM
- Records

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/contacts)
- [OpenAPI](openapi/hubspot-crm-contacts-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-contacts-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-batch-archive-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-batch-response-contact-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-collection-response-contact-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-contact-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-contacts-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-batch-archive-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-batch-response-contact-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-collection-response-contact-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-contact-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-contacts-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-contacts-api-association-example.json)
- [Code Examples](examples/crm-contacts-api-batch-archive-input-example.json)
- [Code Examples](examples/crm-contacts-api-batch-create-input-example.json)
- [Code Examples](examples/crm-contacts-api-batch-read-input-example.json)
- [Code Examples](examples/crm-contacts-api-batch-response-contact-example.json)
- [Code Examples](examples/crm-contacts-api-batch-update-input-example.json)
- [Code Examples](examples/crm-contacts-api-collection-response-association-example.json)
- [Code Examples](examples/crm-contacts-api-collection-response-contact-example.json)
- [Code Examples](examples/crm-contacts-api-contact-example.json)
- [Code Examples](examples/crm-contacts-api-filter-example.json)
- [Code Examples](examples/crm-contacts-api-filter-group-example.json)
- [Code Examples](examples/crm-contacts-api-paging-example.json)
- [Code Examples](examples/crm-contacts-api-search-request-example.json)
- [Code Examples](examples/crm-contacts-api-simple-public-object-input-example.json)

### HubSpot Companies API

Company records store data about businesses and organizations. The companies endpoints allow you to manage this data and sync it between HubSpot and other systems, including creating, retrieving, updating, and deleting company records and managing their associations.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/companies](https://developers.hubspot.com/docs/api/crm/companies)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Companies
- CRM
- Records

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/companies)
- [OpenAPI](openapi/hubspot-crm-companies-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-companies-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-batch-archive-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-batch-response-company-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-collection-response-company-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-company-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-companies-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-batch-archive-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-batch-response-company-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-collection-response-company-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-company-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-companies-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-companies-api-association-example.json)
- [Code Examples](examples/crm-companies-api-batch-archive-input-example.json)
- [Code Examples](examples/crm-companies-api-batch-create-input-example.json)
- [Code Examples](examples/crm-companies-api-batch-read-input-example.json)
- [Code Examples](examples/crm-companies-api-batch-response-company-example.json)
- [Code Examples](examples/crm-companies-api-batch-update-input-example.json)
- [Code Examples](examples/crm-companies-api-collection-response-association-example.json)
- [Code Examples](examples/crm-companies-api-collection-response-company-example.json)
- [Code Examples](examples/crm-companies-api-company-example.json)
- [Code Examples](examples/crm-companies-api-filter-example.json)
- [Code Examples](examples/crm-companies-api-filter-group-example.json)
- [Code Examples](examples/crm-companies-api-paging-example.json)
- [Code Examples](examples/crm-companies-api-search-request-example.json)
- [Code Examples](examples/crm-companies-api-simple-public-object-input-example.json)

### HubSpot Deals API

A deal stores data about an ongoing transaction or sales opportunity. The deals endpoints allow you to manage deal records and sync data between HubSpot and other systems, supporting the full lifecycle of sales opportunities through pipeline stages.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/deals](https://developers.hubspot.com/docs/api/crm/deals)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Deals
- Pipeline
- Sales

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/deals)
- [OpenAPI](openapi/hubspot-crm-deals-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-deals-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-batch-archive-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-batch-response-deal-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-collection-response-deal-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-deal-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-deals-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-batch-archive-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-batch-response-deal-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-collection-response-deal-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-deal-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-deals-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-deals-api-association-example.json)
- [Code Examples](examples/crm-deals-api-batch-archive-input-example.json)
- [Code Examples](examples/crm-deals-api-batch-create-input-example.json)
- [Code Examples](examples/crm-deals-api-batch-read-input-example.json)
- [Code Examples](examples/crm-deals-api-batch-response-deal-example.json)
- [Code Examples](examples/crm-deals-api-batch-update-input-example.json)
- [Code Examples](examples/crm-deals-api-collection-response-association-example.json)
- [Code Examples](examples/crm-deals-api-collection-response-deal-example.json)
- [Code Examples](examples/crm-deals-api-deal-example.json)
- [Code Examples](examples/crm-deals-api-filter-example.json)
- [Code Examples](examples/crm-deals-api-filter-group-example.json)
- [Code Examples](examples/crm-deals-api-paging-example.json)
- [Code Examples](examples/crm-deals-api-search-request-example.json)
- [Code Examples](examples/crm-deals-api-simple-public-object-input-example.json)

### HubSpot Tickets API

Tickets represent customer requests for help and are tracked through support pipelines until resolved. The tickets endpoints allow you to create, manage, and retrieve customer support ticket records and associate them with contacts, companies, and other CRM objects.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/tickets](https://developers.hubspot.com/docs/api/crm/tickets)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Customer Service
- Support
- Tickets

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/tickets)
- [OpenAPI](openapi/hubspot-crm-tickets-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-tickets-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-batch-archive-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-batch-response-ticket-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-collection-response-ticket-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-tickets-api-ticket-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-batch-archive-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-batch-response-ticket-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-collection-response-ticket-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-tickets-api-ticket-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-tickets-api-association-example.json)
- [Code Examples](examples/crm-tickets-api-batch-archive-input-example.json)
- [Code Examples](examples/crm-tickets-api-batch-create-input-example.json)
- [Code Examples](examples/crm-tickets-api-batch-read-input-example.json)
- [Code Examples](examples/crm-tickets-api-batch-response-ticket-example.json)
- [Code Examples](examples/crm-tickets-api-batch-update-input-example.json)
- [Code Examples](examples/crm-tickets-api-collection-response-association-example.json)
- [Code Examples](examples/crm-tickets-api-collection-response-ticket-example.json)
- [Code Examples](examples/crm-tickets-api-filter-example.json)
- [Code Examples](examples/crm-tickets-api-filter-group-example.json)
- [Code Examples](examples/crm-tickets-api-paging-example.json)
- [Code Examples](examples/crm-tickets-api-search-request-example.json)
- [Code Examples](examples/crm-tickets-api-simple-public-object-input-example.json)
- [Code Examples](examples/crm-tickets-api-ticket-example.json)

### HubSpot Pipelines API

Pipelines allow you to track records through defined stages in a process, such as sales deals or support tickets. The pipelines endpoints allow you to create, retrieve, update, and delete pipelines and pipeline stages for deals, tickets, and other object types.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/pipelines](https://developers.hubspot.com/docs/api/crm/pipelines)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Pipelines
- Sales
- Stages

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/pipelines)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Products API

Products represent the goods or services you sell in HubSpot. The products endpoints allow you to manage a product library which can be used to quickly add products to deals, generate quotes, and report on product performance.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/products](https://developers.hubspot.com/docs/api/crm/products)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Catalog
- Commerce
- CRM
- Products

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/products)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Line Items API

Line items are individual instances of products that are attached to a deal or quote. The line items endpoints allow you to create, retrieve, update, and delete line item records, enabling detailed product-level tracking on deals and quotes.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/line-items](https://developers.hubspot.com/docs/api/crm/line-items)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- CRM
- Line Items
- Products

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/line-items)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Quotes API

Quotes allow you to share pricing information with prospects and customers. The quotes endpoints allow you to create and manage quotes with associated line items, deals, and contacts, and support features like e-signatures and payment collection.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/quotes](https://developers.hubspot.com/docs/api/crm/quotes)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- CRM
- Quotes
- Sales

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/quotes)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CRM Properties API

The CRM properties endpoints allow you to manage custom properties and view default property details for any CRM object type. You can create, retrieve, update, and delete properties for contacts, companies, deals, tickets, and custom objects.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/properties](https://developers.hubspot.com/docs/api/crm/properties)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Custom Fields
- Properties

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/properties)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CRM Associations API

The associations endpoints allow you to manage relationships between CRM object records such as contacts, companies, deals, and tickets. You can create, retrieve, and delete associations with or without descriptive labels to represent different types of relationships.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/associations](https://developers.hubspot.com/docs/api/crm/associations)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Associations
- CRM
- Relationships

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/associations)
- [OpenAPI](openapi/hubspot-crm-associations-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-associations-api-association-definition-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-association-definition-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-association-label-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-association-label-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-association-result-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-association-type-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-association-type-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-batch-association-archive-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-batch-association-archive-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-batch-association-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-batch-association-create-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-batch-association-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-batch-association-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-create-association-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-create-label-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-object-reference-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-paging-next-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-associations-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-definition-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-definition-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-label-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-label-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-result-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-type-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-association-type-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-batch-association-archive-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-batch-association-archive-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-batch-association-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-batch-association-create-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-batch-association-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-batch-association-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-create-association-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-create-label-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-object-reference-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-paging-next-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-associations-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-associations-api-association-definition-collection-example.json)
- [Code Examples](examples/crm-associations-api-association-definition-example.json)
- [Code Examples](examples/crm-associations-api-association-example.json)
- [Code Examples](examples/crm-associations-api-association-label-collection-example.json)
- [Code Examples](examples/crm-associations-api-association-label-example.json)
- [Code Examples](examples/crm-associations-api-association-result-example.json)
- [Code Examples](examples/crm-associations-api-association-type-example.json)
- [Code Examples](examples/crm-associations-api-association-type-input-example.json)
- [Code Examples](examples/crm-associations-api-batch-association-archive-input-example.json)
- [Code Examples](examples/crm-associations-api-batch-association-archive-item-example.json)
- [Code Examples](examples/crm-associations-api-batch-association-create-input-example.json)
- [Code Examples](examples/crm-associations-api-batch-association-create-item-example.json)
- [Code Examples](examples/crm-associations-api-batch-association-read-input-example.json)
- [Code Examples](examples/crm-associations-api-batch-association-response-example.json)
- [Code Examples](examples/crm-associations-api-create-association-input-example.json)
- [Code Examples](examples/crm-associations-api-create-label-input-example.json)
- [Code Examples](examples/crm-associations-api-object-reference-example.json)
- [Code Examples](examples/crm-associations-api-paging-example.json)
- [Code Examples](examples/crm-associations-api-paging-next-example.json)

### HubSpot Owners API

The owners endpoints are used to retrieve the list of available owners for a HubSpot account. HubSpot uses owners to assign CRM object records to specific users, and owner IDs are used when setting record ownership through other CRM APIs.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/owners](https://developers.hubspot.com/docs/api/crm/owners)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Owners
- Users

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/owners)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CRM Imports API

The imports endpoints allow you to import contact, company, deal, and other CRM object data into a HubSpot account in bulk using CSV or Excel files. You can map file columns to HubSpot properties and track import status through the API.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/imports](https://developers.hubspot.com/docs/api/crm/imports)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Data
- Imports

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/imports)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CRM Lists API

The Lists API allows you to create and manage lists of CRM records based on static membership or dynamic filter criteria. Lists can be used to segment contacts, companies, and other CRM objects for marketing and sales operations.

- **Human URL:** [https://developers.hubspot.com/docs/reference/api/crm/lists](https://developers.hubspot.com/docs/reference/api/crm/lists)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Lists
- Segments

#### Properties

- [Documentation](https://developers.hubspot.com/docs/reference/api/crm/lists)
- [OpenAPI](openapi/hubspot-crm-lists-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-lists-api-collection-response-list-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-lists-api-collection-response-membership-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-lists-api-list-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-lists-api-list-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-lists-api-membership-change-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-lists-api-membership-change-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-lists-api-membership-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-lists-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-collection-response-list-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-collection-response-membership-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-list-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-list-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-membership-change-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-membership-change-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-membership-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-lists-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-lists-api-collection-response-list-example.json)
- [Code Examples](examples/crm-lists-api-collection-response-membership-example.json)
- [Code Examples](examples/crm-lists-api-list-create-request-example.json)
- [Code Examples](examples/crm-lists-api-list-example.json)
- [Code Examples](examples/crm-lists-api-membership-change-request-example.json)
- [Code Examples](examples/crm-lists-api-membership-change-response-example.json)
- [Code Examples](examples/crm-lists-api-membership-example.json)
- [Code Examples](examples/crm-lists-api-paging-example.json)

### HubSpot CRM Search API

The CRM Search API allows you to query and filter CRM objects using a flexible search interface. You can search across contacts, companies, deals, tickets, and other object types using filter groups, sorts, and pagination.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/search](https://developers.hubspot.com/docs/guides/api/crm/search)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Query
- Search

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/search)
- [OpenAPI](openapi/hubspot-crm-search-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-search-api-crmobject-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-search-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-search-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-search-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-search-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-search-api-search-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-search-api-sort-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-search-api-crmobject-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-search-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-search-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-search-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-search-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-search-api-search-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-search-api-sort-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-search-api-crmobject-example.json)
- [Code Examples](examples/crm-search-api-filter-example.json)
- [Code Examples](examples/crm-search-api-filter-group-example.json)
- [Code Examples](examples/crm-search-api-paging-example.json)
- [Code Examples](examples/crm-search-api-search-request-example.json)
- [Code Examples](examples/crm-search-api-search-response-example.json)
- [Code Examples](examples/crm-search-api-sort-example.json)

### HubSpot Custom Objects API

Custom objects allow you to define and create CRM object types that represent data unique to your business. The custom objects API allows you to define schemas, create records, manage properties, and associate custom objects with standard CRM objects like contacts and deals.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/crm-custom-objects-v3/guide](https://developers.hubspot.com/docs/api-reference/crm-custom-objects-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Custom Objects
- Schema

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/crm-custom-objects-v3/guide)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Commerce Payments API

The payments endpoints allow you to retrieve data about payment transactions processed through HubSpot Commerce. You can retrieve payment details, manage subscriptions, and access transaction history for commerce operations.

- **Human URL:** [https://developers.hubspot.com/docs/api/commerce/payments](https://developers.hubspot.com/docs/api/commerce/payments)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- Payments
- Transactions

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/commerce/payments)
- [OpenAPI](openapi/hubspot-commerce-payments-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/commerce-payments-api-association-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-association-result-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-association-type-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-archive-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-create-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-error-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-read-input-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-read-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-read-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-update-input-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-update-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-batch-update-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-commerce-payment-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-commerce-payment-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-commerce-payment-patch-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-commerce-payment-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-property-history-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-search-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-payments-api-sort-option-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-association-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-association-result-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-association-type-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-archive-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-create-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-error-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-read-input-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-read-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-read-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-update-input-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-update-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-batch-update-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-commerce-payment-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-commerce-payment-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-commerce-payment-patch-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-commerce-payment-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-property-history-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-search-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-payments-api-sort-option-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/commerce-payments-api-association-input-example.json)
- [Code Examples](examples/commerce-payments-api-association-result-example.json)
- [Code Examples](examples/commerce-payments-api-association-type-example.json)
- [Code Examples](examples/commerce-payments-api-batch-archive-request-example.json)
- [Code Examples](examples/commerce-payments-api-batch-create-request-example.json)
- [Code Examples](examples/commerce-payments-api-batch-create-response-example.json)
- [Code Examples](examples/commerce-payments-api-batch-error-example.json)
- [Code Examples](examples/commerce-payments-api-batch-read-input-item-example.json)
- [Code Examples](examples/commerce-payments-api-batch-read-request-example.json)
- [Code Examples](examples/commerce-payments-api-batch-read-response-example.json)
- [Code Examples](examples/commerce-payments-api-batch-update-input-item-example.json)
- [Code Examples](examples/commerce-payments-api-batch-update-request-example.json)
- [Code Examples](examples/commerce-payments-api-batch-update-response-example.json)
- [Code Examples](examples/commerce-payments-api-commerce-payment-collection-example.json)
- [Code Examples](examples/commerce-payments-api-commerce-payment-example.json)
- [Code Examples](examples/commerce-payments-api-commerce-payment-input-example.json)
- [Code Examples](examples/commerce-payments-api-commerce-payment-patch-example.json)
- [Code Examples](examples/commerce-payments-api-filter-example.json)
- [Code Examples](examples/commerce-payments-api-filter-group-example.json)
- [Code Examples](examples/commerce-payments-api-paging-example.json)
- [Code Examples](examples/commerce-payments-api-property-history-example.json)
- [Code Examples](examples/commerce-payments-api-search-request-example.json)
- [Code Examples](examples/commerce-payments-api-search-response-example.json)
- [Code Examples](examples/commerce-payments-api-sort-option-example.json)

### HubSpot Commerce Subscriptions API

The subscriptions API allows you to retrieve data about recurring subscription records in HubSpot Commerce. Subscriptions are created when a customer purchases a recurring product through HubSpot payments or a connected payment processor.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/commerce/subscriptions](https://developers.hubspot.com/docs/guides/api/crm/commerce/subscriptions)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- Recurring Revenue
- Subscriptions

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/commerce/subscriptions)
- [OpenAPI](openapi/hubspot-commerce-subscriptions-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/commerce-subscriptions-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-batch-response-subscription-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-collection-response-subscription-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/commerce-subscriptions-api-subscription-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-batch-response-subscription-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-collection-response-subscription-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/commerce-subscriptions-api-subscription-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/commerce-subscriptions-api-association-example.json)
- [Code Examples](examples/commerce-subscriptions-api-batch-create-input-example.json)
- [Code Examples](examples/commerce-subscriptions-api-batch-read-input-example.json)
- [Code Examples](examples/commerce-subscriptions-api-batch-response-subscription-example.json)
- [Code Examples](examples/commerce-subscriptions-api-batch-update-input-example.json)
- [Code Examples](examples/commerce-subscriptions-api-collection-response-association-example.json)
- [Code Examples](examples/commerce-subscriptions-api-collection-response-subscription-example.json)
- [Code Examples](examples/commerce-subscriptions-api-filter-example.json)
- [Code Examples](examples/commerce-subscriptions-api-filter-group-example.json)
- [Code Examples](examples/commerce-subscriptions-api-paging-example.json)
- [Code Examples](examples/commerce-subscriptions-api-search-request-example.json)
- [Code Examples](examples/commerce-subscriptions-api-simple-public-object-input-example.json)
- [Code Examples](examples/commerce-subscriptions-api-subscription-example.json)

### HubSpot OAuth API

The OAuth API allows you to manage OAuth access tokens for public applications. You can generate, refresh, retrieve metadata for, and delete OAuth tokens to provide secure, scoped API access for HubSpot integrations.

- **Human URL:** [https://developers.hubspot.com/docs/api/oauth/tokens](https://developers.hubspot.com/docs/api/oauth/tokens)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Access Tokens
- Authentication
- OAuth

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/oauth/tokens)
- [OpenAPI](openapi/hubspot-oauth-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/oauth-api-access-token-metadata-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/oauth-api-refresh-token-metadata-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/oauth-api-token-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/oauth-api-token-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/oauth-api-access-token-metadata-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/oauth-api-refresh-token-metadata-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/oauth-api-token-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/oauth-api-token-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/oauth-api-access-token-metadata-example.json)
- [Code Examples](examples/oauth-api-refresh-token-metadata-example.json)
- [Code Examples](examples/oauth-api-token-request-example.json)
- [Code Examples](examples/oauth-api-token-response-example.json)

### HubSpot Analytics Events API

Custom events allow you to track advanced user activity via a JavaScript or HTTP API. The events API enables you to send custom event occurrences, define event schemas, and retrieve historical event data associated with CRM records.

- **Human URL:** [https://developers.hubspot.com/docs/api/analytics/events](https://developers.hubspot.com/docs/api/analytics/events)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Analytics
- Events
- Tracking

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/analytics/events)
- [OpenAPI](openapi/hubspot-analytics-events-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/analytics-events-api-event-instance-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/analytics-events-api-event-instance-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/analytics-events-api-event-type-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/analytics-events-api-paging-next-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/analytics-events-api-paging-previous-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/analytics-events-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/analytics-events-api-event-instance-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/analytics-events-api-event-instance-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/analytics-events-api-event-type-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/analytics-events-api-paging-next-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/analytics-events-api-paging-previous-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/analytics-events-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/analytics-events-api-event-instance-collection-example.json)
- [Code Examples](examples/analytics-events-api-event-instance-example.json)
- [Code Examples](examples/analytics-events-api-event-type-collection-example.json)
- [Code Examples](examples/analytics-events-api-paging-example.json)
- [Code Examples](examples/analytics-events-api-paging-next-example.json)
- [Code Examples](examples/analytics-events-api-paging-previous-example.json)

### HubSpot Marketing Email API

The marketing emails API allows you to programmatically create, update, and retrieve details about marketing emails in HubSpot. You can manage email campaigns, retrieve email performance statistics, and automate email content management workflows.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/marketing-marketing-emails-v3/guide](https://developers.hubspot.com/docs/api-reference/marketing-marketing-emails-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Campaigns
- Email
- Marketing

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/marketing-marketing-emails-v3/guide)
- [OpenAPI](openapi/hubspot-marketing-emal-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/marketing-emal-api-email-message-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-next-page-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-smtp-token-collection-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-smtp-token-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-smtp-token-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-smtp-token-with-password-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-transactional-email-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/marketing-emal-api-transactional-email-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-email-message-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-next-page-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-smtp-token-collection-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-smtp-token-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-smtp-token-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-smtp-token-with-password-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-transactional-email-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/marketing-emal-api-transactional-email-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/marketing-emal-api-email-message-example.json)
- [Code Examples](examples/marketing-emal-api-next-page-example.json)
- [Code Examples](examples/marketing-emal-api-paging-example.json)
- [Code Examples](examples/marketing-emal-api-smtp-token-collection-response-example.json)
- [Code Examples](examples/marketing-emal-api-smtp-token-create-request-example.json)
- [Code Examples](examples/marketing-emal-api-smtp-token-example.json)
- [Code Examples](examples/marketing-emal-api-smtp-token-with-password-example.json)
- [Code Examples](examples/marketing-emal-api-transactional-email-request-example.json)
- [Code Examples](examples/marketing-emal-api-transactional-email-response-example.json)

### HubSpot Marketing Events API

Marketing events are CRM objects that enable you to track marketing activities such as webinars along with the contacts who registered and attended. The marketing events API supports creating and managing events, tracking attendance, and accessing participation analytics.

- **Human URL:** [https://developers.hubspot.com/docs/api/marketing/marketing-events](https://developers.hubspot.com/docs/api/marketing/marketing-events)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Events
- Marketing
- Webinars

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/marketing/marketing-events)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Forms API

The forms endpoints allow you to create and manage HubSpot forms used for capturing lead information. Supported form types include HubSpot native forms, captured external forms, flow forms, and blog comment forms.

- **Human URL:** [https://developers.hubspot.com/docs/api/marketing/forms](https://developers.hubspot.com/docs/api/marketing/forms)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Forms
- Lead Capture
- Marketing

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/marketing/forms)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Conversations API

The conversations API enables management of inboxes, channels, threads, and messages within HubSpot's conversations system. You can retrieve conversation data, update thread statuses, send messages, and access contact-specific conversation history.

- **Human URL:** [https://developers.hubspot.com/docs/api/conversations/conversations](https://developers.hubspot.com/docs/api/conversations/conversations)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Conversations
- Inbox
- Messaging

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/conversations/conversations)
- [OpenAPI](openapi/hubspot-conversations-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/conversations-api-actor-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-actor-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-attachment-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-channel-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-channel-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-inbox-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-inbox-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-message-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-message-recipient-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-message-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-message-status-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-paging-next-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-send-message-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-thread-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-thread-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/conversations-api-update-thread-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-actor-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-actor-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-attachment-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-channel-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-channel-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-inbox-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-inbox-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-message-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-message-recipient-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-message-status-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-message-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-paging-next-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-send-message-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-thread-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-thread-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/conversations-api-update-thread-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/conversations-api-actor-collection-example.json)
- [Code Examples](examples/conversations-api-actor-example.json)
- [Code Examples](examples/conversations-api-attachment-example.json)
- [Code Examples](examples/conversations-api-channel-collection-example.json)
- [Code Examples](examples/conversations-api-channel-example.json)
- [Code Examples](examples/conversations-api-inbox-collection-example.json)
- [Code Examples](examples/conversations-api-inbox-example.json)
- [Code Examples](examples/conversations-api-message-collection-example.json)
- [Code Examples](examples/conversations-api-message-example.json)
- [Code Examples](examples/conversations-api-message-recipient-example.json)
- [Code Examples](examples/conversations-api-message-status-example.json)
- [Code Examples](examples/conversations-api-paging-example.json)
- [Code Examples](examples/conversations-api-paging-next-example.json)
- [Code Examples](examples/conversations-api-send-message-request-example.json)
- [Code Examples](examples/conversations-api-thread-collection-example.json)
- [Code Examples](examples/conversations-api-thread-example.json)
- [Code Examples](examples/conversations-api-update-thread-request-example.json)

### HubSpot Engagement Calls API

The calls endpoints allow you to log and manage call engagement records within HubSpot CRM. You can create call records, associate them with contacts and deals, retrieve call data, and manage call recordings and transcripts.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/calls](https://developers.hubspot.com/docs/api/crm/calls)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Activities
- Calls
- Engagements

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/calls)
- [OpenAPI](openapi/hubspot-engagement-calls-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/engagement-calls-api-association-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-association-type-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-archive-calls-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-calls-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-create-calls-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-error-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-read-calls-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-update-calls-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-call-collection-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-call-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-call-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-call-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-call-search-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-call-update-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-gdpr-delete-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-next-page-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-property-history-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-calls-api-sort-option-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-association-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-association-type-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-archive-calls-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-calls-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-create-calls-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-error-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-read-calls-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-update-calls-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-call-collection-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-call-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-call-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-call-search-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-call-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-call-update-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-gdpr-delete-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-next-page-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-property-history-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-calls-api-sort-option-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/engagement-calls-api-association-input-example.json)
- [Code Examples](examples/engagement-calls-api-association-type-example.json)
- [Code Examples](examples/engagement-calls-api-batch-archive-calls-request-example.json)
- [Code Examples](examples/engagement-calls-api-batch-calls-response-example.json)
- [Code Examples](examples/engagement-calls-api-batch-create-calls-request-example.json)
- [Code Examples](examples/engagement-calls-api-batch-error-example.json)
- [Code Examples](examples/engagement-calls-api-batch-read-calls-request-example.json)
- [Code Examples](examples/engagement-calls-api-batch-read-input-example.json)
- [Code Examples](examples/engagement-calls-api-batch-update-calls-request-example.json)
- [Code Examples](examples/engagement-calls-api-batch-update-input-example.json)
- [Code Examples](examples/engagement-calls-api-call-collection-response-example.json)
- [Code Examples](examples/engagement-calls-api-call-create-request-example.json)
- [Code Examples](examples/engagement-calls-api-call-example.json)
- [Code Examples](examples/engagement-calls-api-call-search-request-example.json)
- [Code Examples](examples/engagement-calls-api-call-search-response-example.json)
- [Code Examples](examples/engagement-calls-api-call-update-request-example.json)
- [Code Examples](examples/engagement-calls-api-filter-example.json)
- [Code Examples](examples/engagement-calls-api-filter-group-example.json)
- [Code Examples](examples/engagement-calls-api-gdpr-delete-request-example.json)
- [Code Examples](examples/engagement-calls-api-next-page-example.json)
- [Code Examples](examples/engagement-calls-api-paging-example.json)
- [Code Examples](examples/engagement-calls-api-property-history-example.json)
- [Code Examples](examples/engagement-calls-api-sort-option-example.json)

### HubSpot Engagement Notes API

The notes endpoints allow you to create and manage note engagement records in HubSpot CRM. Notes can be associated with contacts, companies, deals, and tickets to capture important information and activity history.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/notes](https://developers.hubspot.com/docs/api/crm/notes)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Activities
- Engagements
- Notes

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/notes)
- [OpenAPI](openapi/hubspot-engagement-notes-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/engagement-notes-association-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-association-type-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-archive-notes-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-create-notes-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-error-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-notes-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-read-notes-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-batch-update-notes-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-gdpr-delete-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-next-page-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-note-collection-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-note-create-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-note-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-note-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-note-search-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-note-update-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-property-history-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-notes-sort-option-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-association-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-association-type-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-archive-notes-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-create-notes-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-error-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-notes-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-read-notes-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-batch-update-notes-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-gdpr-delete-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-next-page-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-note-collection-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-note-create-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-note-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-note-search-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-note-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-note-update-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-property-history-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-notes-sort-option-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/engagement-notes-association-input-example.json)
- [Code Examples](examples/engagement-notes-association-type-example.json)
- [Code Examples](examples/engagement-notes-batch-archive-notes-request-example.json)
- [Code Examples](examples/engagement-notes-batch-create-notes-request-example.json)
- [Code Examples](examples/engagement-notes-batch-error-example.json)
- [Code Examples](examples/engagement-notes-batch-notes-response-example.json)
- [Code Examples](examples/engagement-notes-batch-read-input-example.json)
- [Code Examples](examples/engagement-notes-batch-read-notes-request-example.json)
- [Code Examples](examples/engagement-notes-batch-update-input-example.json)
- [Code Examples](examples/engagement-notes-batch-update-notes-request-example.json)
- [Code Examples](examples/engagement-notes-filter-example.json)
- [Code Examples](examples/engagement-notes-filter-group-example.json)
- [Code Examples](examples/engagement-notes-gdpr-delete-request-example.json)
- [Code Examples](examples/engagement-notes-next-page-example.json)
- [Code Examples](examples/engagement-notes-note-collection-response-example.json)
- [Code Examples](examples/engagement-notes-note-create-request-example.json)
- [Code Examples](examples/engagement-notes-note-example.json)
- [Code Examples](examples/engagement-notes-note-search-request-example.json)
- [Code Examples](examples/engagement-notes-note-search-response-example.json)
- [Code Examples](examples/engagement-notes-note-update-request-example.json)
- [Code Examples](examples/engagement-notes-paging-example.json)
- [Code Examples](examples/engagement-notes-property-history-example.json)
- [Code Examples](examples/engagement-notes-sort-option-example.json)

### HubSpot Engagement Meetings API

The meetings endpoints allow you to log and manage meeting engagement records in HubSpot CRM. You can create meeting records, associate them with contacts and companies, and retrieve meeting details and outcomes.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/meetings](https://developers.hubspot.com/docs/api/crm/meetings)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Activities
- Engagements
- Meetings

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/meetings)
- [OpenAPI](openapi/hubspot-engagement-meetings-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/engagement-meetings-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-batch-response-meeting-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-collection-response-meeting-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-meeting-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-meetings-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-batch-response-meeting-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-collection-response-meeting-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-meeting-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-meetings-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/engagement-meetings-api-association-example.json)
- [Code Examples](examples/engagement-meetings-api-batch-create-input-example.json)
- [Code Examples](examples/engagement-meetings-api-batch-read-input-example.json)
- [Code Examples](examples/engagement-meetings-api-batch-response-meeting-example.json)
- [Code Examples](examples/engagement-meetings-api-batch-update-input-example.json)
- [Code Examples](examples/engagement-meetings-api-collection-response-association-example.json)
- [Code Examples](examples/engagement-meetings-api-collection-response-meeting-example.json)
- [Code Examples](examples/engagement-meetings-api-filter-example.json)
- [Code Examples](examples/engagement-meetings-api-filter-group-example.json)
- [Code Examples](examples/engagement-meetings-api-meeting-example.json)
- [Code Examples](examples/engagement-meetings-api-paging-example.json)
- [Code Examples](examples/engagement-meetings-api-search-request-example.json)
- [Code Examples](examples/engagement-meetings-api-simple-public-object-input-example.json)

### HubSpot Engagement Tasks API

The tasks endpoints allow you to create and manage task engagement records in HubSpot CRM. Tasks represent to-do items that can be assigned to users and associated with contacts, companies, and deals to track follow-up actions.

- **Human URL:** [https://developers.hubspot.com/docs/api/crm/tasks](https://developers.hubspot.com/docs/api/crm/tasks)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Activities
- Engagements
- Tasks

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/crm/tasks)
- [OpenAPI](openapi/hubspot-engagement-tasks-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/engagement-tasks-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-batch-response-task-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-collection-response-task-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-tasks-api-task-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-batch-response-task-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-collection-response-task-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-tasks-api-task-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/engagement-tasks-api-association-example.json)
- [Code Examples](examples/engagement-tasks-api-batch-create-input-example.json)
- [Code Examples](examples/engagement-tasks-api-batch-read-input-example.json)
- [Code Examples](examples/engagement-tasks-api-batch-response-task-example.json)
- [Code Examples](examples/engagement-tasks-api-batch-update-input-example.json)
- [Code Examples](examples/engagement-tasks-api-collection-response-association-example.json)
- [Code Examples](examples/engagement-tasks-api-collection-response-task-example.json)
- [Code Examples](examples/engagement-tasks-api-filter-example.json)
- [Code Examples](examples/engagement-tasks-api-filter-group-example.json)
- [Code Examples](examples/engagement-tasks-api-paging-example.json)
- [Code Examples](examples/engagement-tasks-api-search-request-example.json)
- [Code Examples](examples/engagement-tasks-api-simple-public-object-input-example.json)
- [Code Examples](examples/engagement-tasks-api-task-example.json)

### HubSpot Engagement Emails API

The emails engagement API allows you to log and manage email activity records on CRM records in HubSpot. You can create email engagement records to track sent emails, associate them with contacts and deals, and retrieve email activity history.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/crm-emails-v3/guide](https://developers.hubspot.com/docs/api-reference/crm-emails-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Activities
- Emails
- Engagements

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/crm-emails-v3/guide)
- [OpenAPI](openapi/hubspot-engagement-emails-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/engagement-emails-api-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-batch-create-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-batch-read-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-batch-response-email-engagement-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-batch-update-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-collection-response-association-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-collection-response-email-engagement-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-email-engagement-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-filter-group-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-filter-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/engagement-emails-api-simple-public-object-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-batch-create-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-batch-read-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-batch-response-email-engagement-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-batch-update-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-collection-response-association-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-collection-response-email-engagement-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-email-engagement-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-filter-group-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-filter-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-search-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/engagement-emails-api-simple-public-object-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/engagement-emails-api-association-example.json)
- [Code Examples](examples/engagement-emails-api-batch-create-input-example.json)
- [Code Examples](examples/engagement-emails-api-batch-read-input-example.json)
- [Code Examples](examples/engagement-emails-api-batch-response-email-engagement-example.json)
- [Code Examples](examples/engagement-emails-api-batch-update-input-example.json)
- [Code Examples](examples/engagement-emails-api-collection-response-association-example.json)
- [Code Examples](examples/engagement-emails-api-collection-response-email-engagement-example.json)
- [Code Examples](examples/engagement-emails-api-email-engagement-example.json)
- [Code Examples](examples/engagement-emails-api-filter-example.json)
- [Code Examples](examples/engagement-emails-api-filter-group-example.json)
- [Code Examples](examples/engagement-emails-api-paging-example.json)
- [Code Examples](examples/engagement-emails-api-search-request-example.json)
- [Code Examples](examples/engagement-emails-api-simple-public-object-input-example.json)

### HubSpot Custom Workflow Actions API

Custom workflow actions allow you to extend HubSpot workflows by creating reusable actions that can be installed by HubSpot users. The custom workflow actions API allows you to define, manage, and retrieve custom action definitions for use in HubSpot automation workflows.

- **Human URL:** [https://developers.hubspot.com/docs/api/automation/custom-workflow-actions](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Automation
- Custom Actions
- Workflows

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/automation/custom-workflow-actions)
- [OpenAPI](openapi/hubspot-custom-workflow-actions-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-definition-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-definition-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-definition-patch-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-definition-revision-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-definition-revision-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-definition-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-function-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-function-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-function-reference-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-function-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-action-labels-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-batch-callback-completion-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-batch-callback-error-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-batch-callback-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-batch-callback-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-callback-completion-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-field-option-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-field-type-definition-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-input-field-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-object-request-options-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-output-field-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/custom-workflow-actions-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-definition-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-definition-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-definition-patch-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-definition-revision-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-definition-revision-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-definition-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-function-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-function-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-function-reference-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-function-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-action-labels-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-batch-callback-completion-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-batch-callback-error-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-batch-callback-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-batch-callback-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-callback-completion-request-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-field-option-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-field-type-definition-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-input-field-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-object-request-options-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-output-field-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/custom-workflow-actions-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/custom-workflow-actions-api-action-definition-collection-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-definition-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-definition-input-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-definition-patch-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-definition-revision-collection-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-definition-revision-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-function-collection-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-function-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-function-input-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-function-reference-example.json)
- [Code Examples](examples/custom-workflow-actions-api-action-labels-example.json)
- [Code Examples](examples/custom-workflow-actions-api-batch-callback-completion-request-example.json)
- [Code Examples](examples/custom-workflow-actions-api-batch-callback-error-example.json)
- [Code Examples](examples/custom-workflow-actions-api-batch-callback-input-example.json)
- [Code Examples](examples/custom-workflow-actions-api-batch-callback-response-example.json)
- [Code Examples](examples/custom-workflow-actions-api-callback-completion-request-example.json)
- [Code Examples](examples/custom-workflow-actions-api-field-option-example.json)
- [Code Examples](examples/custom-workflow-actions-api-field-type-definition-example.json)
- [Code Examples](examples/custom-workflow-actions-api-input-field-example.json)
- [Code Examples](examples/custom-workflow-actions-api-object-request-options-example.json)
- [Code Examples](examples/custom-workflow-actions-api-output-field-example.json)
- [Code Examples](examples/custom-workflow-actions-api-paging-example.json)

### HubSpot Workflows API

The workflows API allows you to programmatically create, retrieve, update, and delete HubSpot automation workflows. You can manage workflow definitions and automate business processes across CRM objects and marketing activities.

- **Human URL:** [https://developers.hubspot.com/docs/api/automation/workflows](https://developers.hubspot.com/docs/api/automation/workflows)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Automation
- Operations
- Workflows

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/automation/workflows)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Webhooks API

The webhooks API allows you to subscribe to events occurring in a HubSpot account, receiving real-time notifications when CRM objects or conversations are created, updated, or deleted. You can configure subscriptions, manage webhook settings, and validate incoming webhook payloads.

- **Human URL:** [https://developers.hubspot.com/docs/api/webhooks](https://developers.hubspot.com/docs/api/webhooks)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Events
- Integrations
- Webhooks

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api/webhooks)
- [AsyncAPI](asyncapi/hubspot-webhooks-asyncapi.yml) — [AsyncAPI Specification](https://www.asyncapi.com/docs/reference/specification/latest)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CRM Feature Flags API

The feature flags API allows public app developers to manage feature flags for their HubSpot app installations. Feature flags can be used to control the rollout of new functionality to specific accounts or user segments.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/crm-public-app-feature-flags-v3-v3/guide](https://developers.hubspot.com/docs/api-reference/crm-public-app-feature-flags-v3-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- App Management
- CRM
- Feature Flags

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/crm-public-app-feature-flags-v3-v3/guide)
- [OpenAPI](openapi/hubspot-crm-feature-flags-api-openapi.yml) — [OpenAPI Specification](https://spec.openapis.org/oas/latest.html)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [JSON Schema](json-schema/crm-feature-flags-api-batch-delete-input-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-batch-delete-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-batch-error-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-batch-portal-flag-state-input-item-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-batch-portal-flag-state-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-batch-portal-flag-state-response-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-batch-portal-flag-state-response-with-errors-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-feature-flag-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-feature-flag-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-flag-state-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-paging-next-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-paging-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-portal-flag-state-collection-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-portal-flag-state-input-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/crm-feature-flags-api-portal-flag-state-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-batch-delete-input-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-batch-delete-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-batch-error-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-batch-portal-flag-state-input-item-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-batch-portal-flag-state-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-batch-portal-flag-state-response-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-batch-portal-flag-state-response-with-errors-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-feature-flag-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-feature-flag-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-flag-state-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-paging-next-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-paging-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-portal-flag-state-collection-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-portal-flag-state-input-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-structure/crm-feature-flags-api-portal-flag-state-structure.json) — [JSON Schema](https://json-schema.org/specification)
- [Code Examples](examples/crm-feature-flags-api-batch-delete-input-example.json)
- [Code Examples](examples/crm-feature-flags-api-batch-delete-input-item-example.json)
- [Code Examples](examples/crm-feature-flags-api-batch-error-example.json)
- [Code Examples](examples/crm-feature-flags-api-batch-portal-flag-state-input-example.json)
- [Code Examples](examples/crm-feature-flags-api-batch-portal-flag-state-input-item-example.json)
- [Code Examples](examples/crm-feature-flags-api-batch-portal-flag-state-response-example.json)
- [Code Examples](examples/crm-feature-flags-api-batch-portal-flag-state-response-with-errors-example.json)
- [Code Examples](examples/crm-feature-flags-api-feature-flag-example.json)
- [Code Examples](examples/crm-feature-flags-api-feature-flag-input-example.json)
- [Code Examples](examples/crm-feature-flags-api-flag-state-example.json)
- [Code Examples](examples/crm-feature-flags-api-paging-example.json)
- [Code Examples](examples/crm-feature-flags-api-paging-next-example.json)
- [Code Examples](examples/crm-feature-flags-api-portal-flag-state-collection-example.json)
- [Code Examples](examples/crm-feature-flags-api-portal-flag-state-example.json)
- [Code Examples](examples/crm-feature-flags-api-portal-flag-state-input-example.json)

### HubSpot Settings User Provisioning API

The user provisioning API allows you to create and manage users in a HubSpot account along with their roles, permissions, and team assignments. You can add, retrieve, update, and remove users programmatically for account administration.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/settings-user-provisioning-v3/guide](https://developers.hubspot.com/docs/api-reference/settings-user-provisioning-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Settings
- Teams
- Users

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/settings-user-provisioning-v3/guide)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Blog Tags API

The blog tags API allows you to create, manage, and organize blog post tags in HubSpot CMS. Tags help organize blog content and improve discoverability. You can create, retrieve, update, and delete tags, as well as manage multi-language tag variants.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/cms/blogs/blog-tags](https://developers.hubspot.com/docs/guides/api/cms/blogs/blog-tags)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Blogs
- CMS

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/cms/blogs/blog-tags)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CMS Site Search API

The site search API allows you to search the content of HubSpot-hosted sites, including site pages, blog posts, landing pages, and knowledge articles. You can build custom site search experiences and access indexed data for documents with ranking customization and filtering.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/cms/site-search](https://developers.hubspot.com/docs/guides/api/cms/site-search)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CMS
- Content
- Search

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/cms/site-search)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot CMS Content Audit API

The CMS content audit API allows you to query audit logs of CMS changes that occurred within your HubSpot account. You can filter and sort on content object changes by type, time period, or HubSpot user ID to track content change history.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/cms/content-audit](https://developers.hubspot.com/docs/guides/api/cms/content-audit)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Audit
- CMS
- Content
- Logs

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/cms/content-audit)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Files API

The files API allows you to upload, manage, and organize files in HubSpot's file manager. You can upload files, organize them into folders, control file accessibility and privacy settings, retrieve file details, and attach files to CRM records.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/library/files](https://developers.hubspot.com/docs/guides/api/library/files)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Files
- Storage
- Uploads

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/library/files)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Feedback Submissions API

The feedback submissions API allows you to retrieve survey response data from HubSpot surveys including NPS, CSAT, CES, and custom surveys. This is a read-only API that provides access to existing survey responses and their associated properties.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/objects/feedback-submissions](https://developers.hubspot.com/docs/guides/api/crm/objects/feedback-submissions)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Feedback
- Surveys

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/objects/feedback-submissions)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Leads API

The leads API enables you to manage lead records in HubSpot. Leads are contacts or companies that are potential customers who have shown interest in your products or services. You can create, retrieve, update, and delete lead records and manage their associations with contacts and other CRM objects.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/objects/leads](https://developers.hubspot.com/docs/guides/api/crm/objects/leads)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Leads
- Sales

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/objects/leads)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Goals API

The goals API enables you to sync user-specific sales and service team quotas between HubSpot and external systems. Goals are used to create user-specific quotas based on templates provided by HubSpot, and can be retrieved, created, updated, and deleted through the API.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/objects/goals](https://developers.hubspot.com/docs/guides/api/crm/objects/goals)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Goals
- Quotas

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/objects/goals)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Orders API

The orders API enables you to create and manage ecommerce order data in HubSpot. You can create orders, manage associations to contacts, line items, payments, and invoices, and track fulfillment progress using customizable pipelines and stages.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/commerce/orders](https://developers.hubspot.com/docs/guides/api/crm/commerce/orders)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- Ecommerce
- Orders

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/commerce/orders)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Carts API

The carts API enables you to create and manage ecommerce cart data in HubSpot. You can sync cart information between HubSpot and external ecommerce platforms, manage cart properties like pricing and currency, and associate carts with contacts, line items, and orders.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/commerce/carts](https://developers.hubspot.com/docs/guides/api/crm/commerce/carts)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Carts
- Commerce
- Ecommerce

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/commerce/carts)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Invoices API

The invoices API allows you to create, manage, retrieve, and delete invoices used for billing customers. Invoices progress through draft, open, paid, and voided statuses, and can be configured with digital payment collection via HubSpot Payments or Stripe.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/commerce/invoices](https://developers.hubspot.com/docs/guides/api/crm/commerce/invoices)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Billing
- Commerce
- Invoices

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/commerce/invoices)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Taxes API

The taxes API enables you to create and associate tax objects as part of the pricing details for quotes and invoices. Taxes are used in conjunction with discounts and fees when determining pricing totals, with taxes applied last in the calculation sequence.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/commerce/taxes](https://developers.hubspot.com/docs/guides/api/crm/commerce/taxes)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- Pricing
- Taxes

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/commerce/taxes)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Fees API

The fees API allows you to create and manage fees that can be included in invoices and legacy quotes. Fees support fixed dollar amounts or percentage-based values and are used alongside discounts and taxes when determining pricing totals.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/commerce/fees](https://developers.hubspot.com/docs/guides/api/crm/commerce/fees)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- Fees
- Pricing

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/commerce/fees)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Discounts API

The discounts API enables you to create and associate discounts as part of the pricing details for quotes. Discounts work alongside fees and taxes in the quote pricing workflow, being applied first in the calculation sequence.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/commerce/discounts](https://developers.hubspot.com/docs/guides/api/crm/commerce/discounts)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Commerce
- Discounts
- Pricing

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/commerce/discounts)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Engagement Communications API

The communications API allows you to log WhatsApp, LinkedIn, or SMS messages to CRM record timelines. You can create, retrieve, update, and manage message engagement records and associate them with contacts, companies, and other CRM objects.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/engagements/communications](https://developers.hubspot.com/docs/guides/api/crm/engagements/communications)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Communications
- Engagements
- Messaging
- SMS
- WhatsApp

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/engagements/communications)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Engagement Postal Mail API

The postal mail engagement API allows you to log postal mail sent to or received from contacts or companies on their CRM records. You can create, retrieve, update, and delete postal mail engagement records and associate them with contacts, companies, deals, and tickets.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/engagements/postal-mail](https://developers.hubspot.com/docs/guides/api/crm/engagements/postal-mail)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Activities
- Engagements
- Postal Mail

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/engagements/postal-mail)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Transactional Email API

The transactional email API enables sending template-based transactional emails through HubSpot using the Single Send API and managing SMTP tokens. You can send emails for commerce receipts, account updates, and other essential business transactions over a dedicated IP address.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/marketing-transactional-single-send-v3/guide](https://developers.hubspot.com/docs/api-reference/marketing-transactional-single-send-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Marketing
- SMTP
- Transactional Email

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/marketing-transactional-single-send-v3/guide)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Subscription Preferences API

The subscription preferences API allows you to manage email subscription details for contacts in your account. You can retrieve subscription types, check contact preferences, subscribe or unsubscribe contacts, manage global opt-outs, and perform bulk operations on subscription statuses.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/marketing/subscriptions](https://developers.hubspot.com/docs/guides/api/marketing/subscriptions)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Email Preferences
- Marketing
- Subscriptions

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/marketing/subscriptions)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Timeline Events API

The timeline events API enables technology partners to send custom event data from external systems into HubSpot for display on CRM record activity timelines. You can create event templates, define custom tokens, configure display templates, and associate events with CRM records.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/extensions/timeline](https://developers.hubspot.com/docs/guides/api/crm/extensions/timeline)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Events
- Extensions
- Timeline

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/extensions/timeline)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Calling Extensions API

The calling extensions SDK enables apps to provide a custom calling option to HubSpot users directly from CRM records. The SDK facilitates bidirectional communication between calling applications and HubSpot, including call event messaging and automatic engagement record creation.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/extensions/calling-sdk](https://developers.hubspot.com/docs/guides/api/crm/extensions/calling-sdk)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Calling
- CRM
- Extensions
- SDK

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/extensions/calling-sdk)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Video Conferencing API

The video conferencing API enables you to integrate custom video conferencing solutions into HubSpot's meeting creation workflow. You can configure webhook notifications for meeting creation, updates, and deletion, and provide conference link details directly in meeting invitations.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/crm/extensions/video-conferencing](https://developers.hubspot.com/docs/guides/api/crm/extensions/video-conferencing)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- CRM
- Extensions
- Meetings
- Video Conferencing

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/crm/extensions/video-conferencing)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Account Information API

The account information API provides account configuration and usage data for HubSpot accounts. You can retrieve account details including portal ID, time zone, currency settings, and data center location, as well as monitor daily API call consumption.

- **Human URL:** [https://developers.hubspot.com/docs/api-reference/account-account-info-v3/guide](https://developers.hubspot.com/docs/api-reference/account-account-info-v3/guide)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Account
- Configuration
- Settings

#### Properties

- [Documentation](https://developers.hubspot.com/docs/api-reference/account-account-info-v3/guide)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Business Units API

The business units (brands) API provides information about brands tied to a HubSpot user. You can retrieve brand data including brand name, ID, and logo metadata for brands associated with a specific user account.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/settings/business-units-api](https://developers.hubspot.com/docs/guides/api/settings/business-units-api)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Brands
- Business Units
- Settings

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/settings/business-units-api)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

### HubSpot Currencies API

The currencies API allows you to manage the currencies used in your HubSpot account. You can set your account's company currency, create additional currencies, update exchange rates, and configure automatic exchange rate updates for multi-currency operations.

- **Human URL:** [https://developers.hubspot.com/docs/guides/api/settings/currencies](https://developers.hubspot.com/docs/guides/api/settings/currencies)
- **Base URL:** `https://api.hubapi.com`

#### Tags

- Currencies
- Exchange Rates
- Settings

#### Properties

- [Documentation](https://developers.hubspot.com/docs/guides/api/settings/currencies)
- [Postman Collection](collections/hubspot-analytics-events-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-analytics-events-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-authors-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-authors-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-blog-posts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-blog-posts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-hubdb-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-hubdb-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-cms-pages-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-cms-pages-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-payments-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-payments-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-commerce-subscriptions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-commerce-subscriptions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-conversations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-conversations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-associations-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-associations-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-companies-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-companies-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-contacts-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-contacts-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-deals-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-deals-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-feature-flags-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-feature-flags-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-lists-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-lists-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-search-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-search-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-crm-tickets-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-crm-tickets-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-custom-workflow-actions-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-custom-workflow-actions-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-domains-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-domains-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-calls-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-calls-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-emails-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-emails-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-meetings-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-meetings-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-notes.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-notes.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-engagement-tasks-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-engagement-tasks-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-marketing-emal-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-marketing-emal-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-oauth-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-oauth-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)
- [Postman Collection](collections/hubspot-source-code-api.postman_collection.json) — [Postman Collection 2.1](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- [Open Collection](collections/hubspot-source-code-api.opencollection.json) — [Open Collection 1.0](https://schema.opencollection.com/opencollection/v1.0.0.json)

## Common Properties

- [Arazzo Workflows](arazzo/) — [Arazzo Specification](https://spec.openapis.org/arazzo/latest.html)
- [LinkedIn](https://www.linkedin.com/company/hubspot)
- [API Reference](https://api.hubspot.com/api-catalog-public/v1/apis)
- [Portal](https://developers.hubspot.com/)
- [Documentation](https://developers.hubspot.com/docs/api/overview)
- [Changelog](https://developers.hubspot.com/changelog)
- [Support](https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers)
- [Support](https://developers.hubspot.com/slack)
- [Blog](https://developers.hubspot.com/blog)
- [Newsletter](https://offers.hubspot.com/developer-newsletter-signup)
- [Events](https://www.hubspot.com/developer-community-events)
- [Integrations](https://ecosystem.hubspot.com/marketplace/apps)
- [Privacy Policy](https://legal.hubspot.com/privacy-policy)
- [Terms of Service](https://legal.hubspot.com/terms-of-service)
- [Getting Started](https://developers.hubspot.com/docs/getting-started/overview)
- [Documentation](https://developers.hubspot.com/docs/guides/api)
- [Documentation](https://developers.hubspot.com/docs/reference/api/overview)
- [Login](https://app.hubspot.com/login)
- [Contact](https://offers.hubspot.com/crm-platform-demo)
- [Documentation](https://www.hubspot.com/our-story)
- [Blog](https://blog.hubspot.com/)
- [Security](https://legal.hubspot.com/security)
- [Partners](https://www.hubspot.com/partners/affiliates)
- [Partners](https://www.hubspot.com/partners)
- [Pricing](https://www.hubspot.com/pricing/marketing/enterprise)
- [Showcase](https://www.hubspot.com/case-studies)
- [Features](undefined)
- [Use Cases](undefined)
- [Sign Up](https://app.hubspot.com/signup/developers)
- [Authentication](https://developers.hubspot.com/docs/api/intro-to-auth)
- [Rate Limits](https://developers.hubspot.com/docs/guides/apps/api-usage/usage-details)
- [Status Page](https://status.hubspot.com)
- [Support](https://community.hubspot.com/t5/APIs-Integrations/bd-p/integrations)
- [GitHub Organization](https://github.com/HubSpot)
- [GitHub Repository](https://github.com/HubSpot/HubSpot-public-api-spec-collection)
- [SDK](https://developers.hubspot.com/docs/api/client-libraries)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/hubspot)
- [Resources](https://www.postman.com/hubspot/hubspot-public-api-workspace/overview)
- [Resources](https://developers.hubspot.com/developer-tools)
- [API Reference](https://developers.hubspot.com/apisbytier)
- [JSON Schema](json-schema/hubspot-crm-object-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON Schema](json-schema/hubspot-crm-search-request-schema.json) — [JSON Schema](https://json-schema.org/specification)
- [JSON-LD](json-ld/hubspot-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [Integrations](undefined)
- [SDK](https://pypi.org/project/hubspot-api-client/)
- [SDK](https://www.npmjs.com/package/@hubspot/api-client)
- [SDK](https://rubygems.org/gems/hubspot-api-client)
- [SDK](https://packagist.org/packages/hubspot/api-client)
- [C L I](https://www.npmjs.com/package/@hubspot/cli)
- [GitHub Repository](https://github.com/HubSpot/mcp-server)
- [SDK](https://github.com/HubSpot/calling-extensions-sdk)
- [JSON-LD](json-ld/hubspot-analytics-events-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-authors-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-blog-posts-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-cms-hubdb-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-cms-pages-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-commerce-payments-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-commerce-subscriptions-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-conversations-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-associations-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-companies-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-contacts-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-deals-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-feature-flags-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-lists-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-search-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-crm-tickets-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-custom-workflow-actions-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-domains-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-calls-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-emails-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-meetings-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-association-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-batch-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-filter-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-gdpr-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-next-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-note-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-paging-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-property-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-notes-sort-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-engagement-tasks-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-marketing-emal-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-oauth-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [JSON-LD](json-ld/hubspot-source-code-api-context.jsonld) — [JSON-LD](https://www.w3.org/TR/json-ld11/)
- [Documentation](rules/hubspot-spectral-rules.yml)
- [Documentation](vocabulary/hubspot-vocabulary.yaml)
- [Documentation](capabilities/automation-and-integration.yaml)
- [Documentation](capabilities/commerce-operations.yaml)
- [Documentation](capabilities/content-management.yaml)
- [Documentation](capabilities/crm-management.yaml)
- [Documentation](capabilities/marketing-automation.yaml)
- [Documentation](capabilities/sales-engagement.yaml)
- [Documentation](capabilities/shared/analytics-events-api.yaml)
- [Documentation](capabilities/shared/authors-api.yaml)
- [Documentation](capabilities/shared/blog-posts-api.yaml)
- [Documentation](capabilities/shared/cms-hubdb-api.yaml)
- [Documentation](capabilities/shared/cms-pages-api.yaml)
- [Documentation](capabilities/shared/commerce-payments-api.yaml)
- [Documentation](capabilities/shared/commerce-subscriptions-api.yaml)
- [Documentation](capabilities/shared/conversations-api.yaml)
- [Documentation](capabilities/shared/crm-associations-api.yaml)
- [Documentation](capabilities/shared/crm-companies-api.yaml)
- [Documentation](capabilities/shared/crm-contacts-api.yaml)
- [Documentation](capabilities/shared/crm-deals-api.yaml)
- [Documentation](capabilities/shared/crm-feature-flags-api.yaml)
- [Documentation](capabilities/shared/crm-lists-api.yaml)
- [Documentation](capabilities/shared/crm-search-api.yaml)
- [Documentation](capabilities/shared/crm-tickets-api.yaml)
- [Documentation](capabilities/shared/custom-workflow-actions-api.yaml)
- [Documentation](capabilities/shared/domains-api.yaml)
- [Documentation](capabilities/shared/engagement-calls-api.yaml)
- [Documentation](capabilities/shared/engagement-emails-api.yaml)
- [Documentation](capabilities/shared/engagement-meetings-api.yaml)
- [Documentation](capabilities/shared/engagement-notes.yaml)
- [Documentation](capabilities/shared/engagement-tasks-api.yaml)
- [Documentation](capabilities/shared/marketing-emal-api.yaml)
- [Documentation](capabilities/shared/oauth-api.yaml)
- [Documentation](capabilities/shared/source-code-api.yaml)
- [M C P Server](https://github.com/HubSpot/mcp-server)
- [Agent Skill](https://github.com/HubSpot/noc-skills)

## Maintainers

**FN:** Kin Lane
**Email:** kin@apievangelist.com
**URL:** http://apievangelist.com
