#!/usr/bin/env python3
"""Build the HubSpot API tube-style map.

~42 of HubSpot's APIs grouped onto 8 product lines covering CRM,
Engagements, Marketing, Commerce, CMS, and Platform/Developer surfaces.
"""

import sys
from pathlib import Path

sys.path.insert(0, "/Users/kinlane/GitHub/all/.claude/skills")
from _subway_engine import build_subway  # noqa: E402

ABBREV = {
    "Custom Objects":       "Custom Objects",
    "CRM Properties":       "Properties",
    "CRM Associations":     "Associations",
    "CRM Imports":          "Imports",
    "CRM Lists":            "Lists",
    "CRM Search":           "Search",
    "Marketing Email":      "Marketing Email",
    "Marketing Events":     "Mktg Events",
    "Analytics Events":     "Analytics Evt",
    "Custom Workflow Actions":"Workflow Actions",
    "Subscription Preferences":"Sub. Prefs",
    "CMS HubDB":            "HubDB",
    "CMS Pages":            "CMS Pages",
    "Communications":       "Communications",
    "Postal Mail":          "Postal Mail",
    "Calling Extensions":   "Calling Ext.",
    "Video Conferencing":   "Video Conf.",
}

LINES = [
    {
        "name": "CRM — Core",
        "color": "#FF7A59",  # HubSpot orange
        "stations": [
            ("Contacts",      (260, 195)),
            ("Companies",     (390, 175)),
            ("Deals",         (520, 165)),
            ("Tickets",       (650, 165)),
            ("Pipelines",     (780, 175)),
            ("Owners",        (910, 195)),
            ("Custom Objects",(1030, 220)),
        ],
    },
    {
        "name": "CRM — Tools",
        "color": "#0E9D6E",
        "stations": [
            ("CRM Properties",  (260, 290)),
            ("CRM Associations",(420, 270)),
            ("CRM Imports",     (590, 270)),
            ("CRM Lists",       (760, 270)),
            ("CRM Search",      (920, 290)),
        ],
    },
    {
        "name": "Engagements",
        "color": "#1E5BD0",
        "stations": [
            ("Calls",        (260, 380)),
            ("Notes",        (390, 405)),
            ("Meetings",     (520, 405)),
            ("Tasks",        (650, 405)),
            ("Emails",       (780, 405)),
            ("Communications",(920, 380)),
        ],
    },
    {
        "name": "Marketing",
        "color": "#C5318B",
        "stations": [
            ("Marketing Email",  (270, 480)),
            ("Marketing Events", (430, 460)),
            ("Forms",            (580, 460)),
            ("Analytics Events", (730, 460)),
            ("Conversations",    (870, 460)),
            ("Webhooks",         (1010, 480)),
        ],
    },
    {
        "name": "Commerce",
        "color": "#7B3FE4",
        "stations": [
            ("Products",      (270, 580)),
            ("Line Items",    (390, 555)),
            ("Quotes",        (510, 545)),
            ("Payments",      (630, 545)),
            ("Subscriptions", (750, 555)),
            ("Orders",        (870, 580)),
            ("Carts",         (990, 605)),
        ],
    },
    {
        "name": "CMS",
        "color": "#E68B1F",
        "stations": [
            ("CMS HubDB",   (260, 670)),
            ("CMS Pages",   (380, 645)),
            ("Domains",     (510, 645)),
            ("Source Code", (640, 645)),
            ("Authors",     (770, 645)),
            ("Posts",       (890, 670)),
        ],
    },
    {
        "name": "Workflows & Auth",
        "color": "#5A6275",
        "stations": [
            ("OAuth",                  (270, 760)),
            ("Workflows",              (430, 740)),
            ("Custom Workflow Actions",(610, 740)),
            ("Files",                  (790, 760)),
        ],
    },
    {
        "name": "Service & Settings",
        "color": "#B89719",
        # Closed quadrilateral at the bottom-right.
        "closed": True,
        "stations": [
            ("Calling Extensions",  (920, 670)),
            ("Video Conferencing",  (1010, 740)),
            ("Subscription Preferences",(920, 810)),
            ("Postal Mail",         (830, 740)),
        ],
    },
]

URL_OVERRIDES = {
    "Contacts":               "https://apis.apis.io/apis/hubspot/hubspot-contacts-api/",
    "Companies":              "https://apis.apis.io/apis/hubspot/hubspot-companies-api/",
    "Deals":                  "https://apis.apis.io/apis/hubspot/hubspot-deals-api/",
    "Tickets":                "https://apis.apis.io/apis/hubspot/hubspot-tickets-api/",
    "Pipelines":              "https://apis.apis.io/apis/hubspot/hubspot-pipelines-api/",
    "Owners":                 "https://apis.apis.io/apis/hubspot/hubspot-owners-api/",
    "Custom Objects":         "https://apis.apis.io/apis/hubspot/hubspot-custom-objects-api/",
    "CRM Properties":         "https://apis.apis.io/apis/hubspot/hubspot-crm-properties-api/",
    "CRM Associations":       "https://apis.apis.io/apis/hubspot/hubspot-crm-associations-api/",
    "CRM Imports":            "https://apis.apis.io/apis/hubspot/hubspot-crm-imports-api/",
    "CRM Lists":              "https://apis.apis.io/apis/hubspot/hubspot-crm-lists-api/",
    "CRM Search":             "https://apis.apis.io/apis/hubspot/hubspot-crm-search-api/",
    "Calls":                  "https://apis.apis.io/apis/hubspot/hubspot-engagement-calls-api/",
    "Notes":                  "https://apis.apis.io/apis/hubspot/hubspot-engagement-notes-api/",
    "Meetings":               "https://apis.apis.io/apis/hubspot/hubspot-engagement-meetings-api/",
    "Tasks":                  "https://apis.apis.io/apis/hubspot/hubspot-engagement-tasks-api/",
    "Emails":                 "https://apis.apis.io/apis/hubspot/hubspot-engagement-emails-api/",
    "Communications":         "https://apis.apis.io/apis/hubspot/hubspot-engagement-communications-api/",
    "Marketing Email":        "https://apis.apis.io/apis/hubspot/hubspot-marketing-email-api/",
    "Marketing Events":       "https://apis.apis.io/apis/hubspot/hubspot-marketing-events-api/",
    "Forms":                  "https://apis.apis.io/apis/hubspot/hubspot-forms-api/",
    "Analytics Events":       "https://apis.apis.io/apis/hubspot/hubspot-analytics-events-api/",
    "Conversations":          "https://apis.apis.io/apis/hubspot/hubspot-conversations-api/",
    "Webhooks":               "https://apis.apis.io/apis/hubspot/hubspot-webhooks-api/",
    "Products":               "https://apis.apis.io/apis/hubspot/hubspot-products-api/",
    "Line Items":             "https://apis.apis.io/apis/hubspot/hubspot-line-items-api/",
    "Quotes":                 "https://apis.apis.io/apis/hubspot/hubspot-quotes-api/",
    "Payments":               "https://apis.apis.io/apis/hubspot/hubspot-commerce-payments-api/",
    "Subscriptions":          "https://apis.apis.io/apis/hubspot/hubspot-commerce-subscriptions-api/",
    "Orders":                 "https://apis.apis.io/apis/hubspot/hubspot-orders-api/",
    "Carts":                  "https://apis.apis.io/apis/hubspot/hubspot-carts-api/",
    "CMS HubDB":              "https://apis.apis.io/apis/hubspot/hubspot-cms-hubdb-api/",
    "CMS Pages":              "https://apis.apis.io/apis/hubspot/hubspot-cms-pages-api/",
    "Domains":                "https://apis.apis.io/apis/hubspot/hubspot-domains-api/",
    "Source Code":            "https://apis.apis.io/apis/hubspot/hubspot-source-code-api/",
    "Authors":                "https://apis.apis.io/apis/hubspot/hubspot-authors-api/",
    "Posts":                  "https://apis.apis.io/apis/hubspot/hubspot-posts-api/",
    "OAuth":                  "https://apis.apis.io/apis/hubspot/hubspot-oauth-api/",
    "Workflows":              "https://apis.apis.io/apis/hubspot/hubspot-workflows-api/",
    "Custom Workflow Actions":"https://apis.apis.io/apis/hubspot/hubspot-custom-workflow-actions-api/",
    "Files":                  "https://apis.apis.io/apis/hubspot/hubspot-files-api/",
    "Calling Extensions":     "https://apis.apis.io/apis/hubspot/hubspot-calling-extensions-api/",
    "Video Conferencing":     "https://apis.apis.io/apis/hubspot/hubspot-video-conferencing-api/",
    "Subscription Preferences":"https://apis.apis.io/apis/hubspot/hubspot-subscription-preferences-api/",
    "Postal Mail":            "https://apis.apis.io/apis/hubspot/hubspot-engagement-postal-mail-api/",
}


def main():
    seen = set()
    n_unique = 0
    for ln in LINES:
        for (st, _) in ln["stations"]:
            if st not in seen:
                n_unique += 1
                seen.add(st)
    build_subway(
        title="The HubSpot API · Underground Map",
        subtitle=f"{n_unique} APIs · {len(LINES)} functional lines · click any station for the apis.io page",
        lines=LINES,
        abbrev=ABBREV,
        source_label="Source: hubspot/openapi/*.yml · github.com/api-evangelist/hubspot",
        out_dir=Path(__file__).resolve().parent,
        out_basename="hubspot-subway-map",
        provider_id="hubspot",
        station_url_overrides=URL_OVERRIDES,
    )


if __name__ == "__main__":
    main()
