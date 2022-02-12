"""
Expansion of API-Endpoints for the CMS
"""
from django.urls import include, path

from .v3.events import events
from .v3.feedback import (
    page_feedback,
    search_result_feedback,
    region_feedback,
    offer_feedback,
    offer_list_feedback,
    event_list_feedback,
    event_feedback,
    poi_feedback,
    map_feedback,
    imprint_page_feedback,
    legacy_feedback_endpoint,
)
from .v3.imprint import imprint
from .v3.languages import languages
from .v3.locations import locations
from .v3.pages import pages, children, parents, single_page
from .v3.pdf_export import pdf_export
from .v3.push_notifications import sent_push_notifications
from .v3.regions import regions, liveregions, hiddenregions
from .v3.offers import offers


#: The namespace for this URL config (see :attr:`django.urls.ResolverMatch.app_name`)
app_name = "api"

content_api_urlpatterns = [
    path("pages/", pages, name="pages"),
    path("locations/", locations, name="locations"),
    path("events/", events, name="events"),
    path("page/", single_page, name="single_page"),
    path("post/", single_page, name="single_page"),
    path("children/", children, name="children"),
    path("parents/", parents, name="parents"),
    path("pdf/", pdf_export, name="pdf_export"),
    path(
        "sent_push_notifications/",
        sent_push_notifications,
        name="sent_push_notifications",
    ),
    path("imprint/", imprint, name="imprint"),
    path("disclaimer/", imprint, name="imprint"),
    path("offers/", offers, name="offers"),
    path("extras/", offers, name="offers"),
    path(
        "feedback/",
        include(
            [
                path(
                    "",
                    legacy_feedback_endpoint.legacy_feedback_endpoint,
                    name="legacy_feedback_endpoint",
                ),
                path(
                    "categories/",
                    region_feedback.region_feedback,
                    name="region_feedback",
                ),
                path("page/", page_feedback.page_feedback, name="page_feedback"),
                path(
                    "poi/",
                    poi_feedback.poi_feedback,
                    name="poi_feedback",
                ),
                path(
                    "event/",
                    event_feedback.event_feedback,
                    name="event_feedback",
                ),
                path(
                    "events/",
                    event_list_feedback.event_list_feedback,
                    name="event_list_feedback",
                ),
                path(
                    "imprint-page/",
                    imprint_page_feedback.imprint_page_feedback,
                    name="imprint_page_feedbacks",
                ),
                path(
                    "map/",
                    map_feedback.map_feedback,
                    name="map_feedback",
                ),
                path(
                    "search/",
                    search_result_feedback.search_result_feedback,
                    name="search_result_feedback",
                ),
                path(
                    "extras/",
                    offer_list_feedback.offer_list_feedback,
                    name="offer_list_feedback",
                ),
                path(
                    "offers/",
                    offer_list_feedback.offer_list_feedback,
                    name="offer_list_feedback",
                ),
                path("extra/", offer_feedback.offer_feedback, name="offer_feedback"),
                path("offer/", offer_feedback.offer_feedback, name="offer_feedback"),
            ]
        ),
    ),
]

region_api_urlpatterns = [
    path("", regions, name="regions"),
    path("live/", liveregions, name="regions_live"),
    path("hidden/", hiddenregions, name="regions_hidden"),
]

#: The url patterns of this module (see :doc:`topics/http/urls`)
urlpatterns = [
    path("api/regions/", include(region_api_urlpatterns)),
    path("wp-json/extensions/v3/sites/", include(region_api_urlpatterns)),
    path(
        "api/<slug:region_slug>/",
        include(
            [
                path("languages/", languages, name="languages"),
                path("offers/", offers, name="offers"),
                path("extras/", offers, name="offers"),
                path("<slug:language_slug>/", include(content_api_urlpatterns)),
            ]
        ),
    ),
    path(
        "<slug:region_slug>/",
        include(
            [
                path(
                    "de/wp-json/extensions/v3/languages/", languages, name="languages"
                ),
                path(
                    "<slug:language_slug>/wp-json/extensions/v3/",
                    include(content_api_urlpatterns),
                ),
            ]
        ),
    ),
]
