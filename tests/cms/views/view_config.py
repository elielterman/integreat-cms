"""
This modules contains the config for the view tests
"""
from django.conf import settings
from django.urls import reverse

from ...conftest import (
    ALL_ROLES,
    EDITOR,
    MANAGEMENT,
    MUNICIPALITY_TEAM,
    PRIV_STAFF_ROLES,
    REGION_ROLES,
    ROLES,
    ROOT,
    STAFF_ROLES,
)

#: This list contains the config for all views
#: Each element is a tuple which consists of two elements: A list of view configs and the keyword arguments that are
#: identical for all views in this list. Each view config item consists of the name of the view, the list of roles that
#: are allowed to access that view and optionally post data that is sent with the request. The post data can either be
#: a dict to send form data or a string to send JSON.
VIEWS = [
    (
        [
            ("api:regions", ALL_ROLES),
            ("api:regions_live", ALL_ROLES),
            ("api:regions_hidden", ALL_ROLES),
            ("public:login_mfa", ALL_ROLES),
            ("sitemap:index", ALL_ROLES),
            ("admin_dashboard", STAFF_ROLES),
            ("admin_feedback", STAFF_ROLES),
            ("languages", STAFF_ROLES),
            ("media_admin", STAFF_ROLES),
            ("mediacenter_directory_path", STAFF_ROLES),
            ("mediacenter_get_directory_content", STAFF_ROLES),
            ("new_language", STAFF_ROLES),
            ("new_offertemplate", STAFF_ROLES),
            ("new_organization", STAFF_ROLES),
            ("new_region", STAFF_ROLES),
            ("new_role", [ROOT]),
            ("new_user", STAFF_ROLES),
            ("offertemplates", STAFF_ROLES),
            ("organizations", STAFF_ROLES),
            ("regions", STAFF_ROLES),
            ("roles", [ROOT]),
            ("user_settings", STAFF_ROLES),
            ("authenticate_modify_mfa", STAFF_ROLES),
            ("users", STAFF_ROLES),
        ],
        # The kwargs for these views
        {},
    ),
    (
        [
            ("api:languages", ALL_ROLES),
            ("analytics", ROLES),
            ("dashboard", ROLES),
            ("language_tree", STAFF_ROLES),
            ("media", ROLES),
            ("mediacenter_directory_path", ROLES),
            ("mediacenter_get_directory_content", ROLES),
            ("new_language_tree_node", STAFF_ROLES),
            ("new_region_user", STAFF_ROLES + [MANAGEMENT]),
            (
                "new_region_user",
                PRIV_STAFF_ROLES + [MANAGEMENT],
                {"username": "new_username", "email": "new@email.address", "role": 1},
            ),
            ("region_feedback", STAFF_ROLES + [MANAGEMENT]),
            ("region_users", STAFF_ROLES + [MANAGEMENT]),
            ("translation_coverage", ROLES),
            ("user_settings", ROLES),
            ("authenticate_modify_mfa", ROLES),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg"},
    ),
    (
        [
            ("api:languages", ALL_ROLES),
            ("analytics", STAFF_ROLES),
            ("dashboard", STAFF_ROLES),
            ("language_tree", STAFF_ROLES),
            ("media", STAFF_ROLES),
            ("mediacenter_directory_path", STAFF_ROLES),
            ("mediacenter_get_directory_content", STAFF_ROLES),
            ("new_language_tree_node", STAFF_ROLES),
            ("new_region_user", STAFF_ROLES),
            (
                "new_region_user",
                PRIV_STAFF_ROLES,
                {"username": "new_username", "email": "new@email.address", "role": 1},
            ),
            ("region_feedback", STAFF_ROLES),
            ("region_users", STAFF_ROLES),
            ("translation_coverage", STAFF_ROLES),
            ("user_settings", STAFF_ROLES),
            ("authenticate_modify_mfa", STAFF_ROLES),
        ],
        # The kwargs for these views
        {"region_slug": "nurnberg"},
    ),
    (
        [
            ("api:pages", ALL_ROLES),
            ("api:pdf_export", ALL_ROLES),
            ("api:sent_push_notifications", ALL_ROLES),
            (
                "api:legacy_feedback_endpoint",
                ALL_ROLES,
                {
                    "permalink": "/augsburg/de/willkommen",
                    "comment": "Cool page!",
                    "rating": "up",
                    "category": "Inhalte",
                },
            ),
            (
                "api:legacy_feedback_endpoint",
                ALL_ROLES,
                {
                    "permalink": "/augsburg/de/willkommen",
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:legacy_feedback_endpoint",
                ALL_ROLES,
                {
                    "permalink": "/augsburg/de/events/test-veranstaltung",
                    "comment": "Cool event!",
                    "rating": "up",
                    "category": "Inhalte",
                },
            ),
            (
                "api:legacy_feedback_endpoint",
                ALL_ROLES,
                {
                    "permalink": "/augsburg/de/events/test-veranstaltung",
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:region_feedback",
                ALL_ROLES,
                {"comment": "Cool region!", "rating": "up", "category": "Inhalte"},
            ),
            (
                "api:region_feedback",
                ALL_ROLES,
                {
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:page_feedback",
                ALL_ROLES,
                {
                    "slug": "willkommen",
                    "comment": "Cool page!",
                    "rating": "up",
                    "category": "Inhalte",
                },
            ),
            (
                "api:page_feedback",
                ALL_ROLES,
                {
                    "slug": "willkommen",
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:poi_feedback",
                ALL_ROLES,
                {
                    "slug": "test-ort",
                    "comment": "Cool POI!",
                    "rating": "up",
                    "category": "Inhalte",
                },
            ),
            (
                "api:poi_feedback",
                ALL_ROLES,
                {
                    "slug": "test-ort",
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:event_feedback",
                ALL_ROLES,
                {
                    "slug": "test-veranstaltung",
                    "comment": "Cool event!",
                    "rating": "up",
                    "category": "Inhalte",
                },
            ),
            (
                "api:event_feedback",
                ALL_ROLES,
                {
                    "slug": "test-veranstaltung",
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:event_list_feedback",
                ALL_ROLES,
                {"comment": "Cool events!", "rating": "up", "category": "Inhalte"},
            ),
            (
                "api:event_list_feedback",
                ALL_ROLES,
                {
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:imprint_page_feedbacks",
                ALL_ROLES,
                {"comment": "Cool imprint!", "rating": "up", "category": "Inhalte"},
            ),
            (
                "api:imprint_page_feedbacks",
                ALL_ROLES,
                {
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:map_feedback",
                ALL_ROLES,
                {"comment": "Cool map!", "rating": "up", "category": "Inhalte"},
            ),
            (
                "api:map_feedback",
                ALL_ROLES,
                {
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:search_result_feedback",
                ALL_ROLES,
                {
                    "query": "search query",
                    "comment": "Cool search results!",
                    "rating": "up",
                    "category": "Inhalte",
                },
            ),
            (
                "api:search_result_feedback",
                ALL_ROLES,
                {
                    "query": "search query",
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:offer_list_feedback",
                ALL_ROLES,
                {"comment": "Cool offers!", "rating": "up", "category": "Inhalte"},
            ),
            (
                "api:offer_list_feedback",
                ALL_ROLES,
                {
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            (
                "api:offer_feedback",
                ALL_ROLES,
                {
                    "slug": "sprungbrett",
                    "comment": "Cool offer!",
                    "rating": "up",
                    "category": "Inhalte",
                },
            ),
            (
                "api:offer_feedback",
                ALL_ROLES,
                {
                    "slug": "sprungbrett",
                    "comment": "Strange bug!",
                    "rating": "down",
                    "category": "Technisches Feedback",
                },
            ),
            ("sitemap:region_language", ALL_ROLES),
            ("archived_pages", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            ("archived_pois", ROLES),
            ("edit_imprint", STAFF_ROLES + [MANAGEMENT]),
            (
                "edit_imprint",
                PRIV_STAFF_ROLES + [MANAGEMENT],
                {"title": "imprint", "submit_draft": True},
            ),
            ("events", ROLES),
            ("events_archived", ROLES),
            ("new_event", ROLES),
            (
                "new_event",
                PRIV_STAFF_ROLES + REGION_ROLES,
                {
                    "title": "new event",
                    "start_date": "2030-01-01",
                    "end_date": "2030-01-01",
                    "is_all_day": True,
                    "submit_draft": True,
                },
            ),
            ("new_page", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            (
                "new_page",
                PRIV_STAFF_ROLES + [MANAGEMENT, EDITOR],
                {
                    "title": "new page",
                    "mirrored_page_region": "",
                    "_ref_node_id": 1,
                    "_position": "first-child",
                    "submit_draft": True,
                },
            ),
            ("new_poi", ROLES),
            (
                "new_poi",
                PRIV_STAFF_ROLES + REGION_ROLES,
                {
                    "title": "new poi",
                    "short_description": "short description",
                    "address": "Test-Straße 5",
                    "postcode": "54321",
                    "city": "Augsburg",
                    "country": "Deutschland",
                    "longitude": 1,
                    "latitude": 1,
                    "submit_draft": True,
                },
            ),
            ("new_push_notification", STAFF_ROLES + [MANAGEMENT]),
            ("pages", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            ("pois", ROLES),
            ("push_notifications", STAFF_ROLES + [MANAGEMENT]),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "language_slug": "de"},
    ),
    (
        [
            ("api:pages", ALL_ROLES),
            ("api:pdf_export", ALL_ROLES),
            ("api:sent_push_notifications", ALL_ROLES),
            ("archived_pages", STAFF_ROLES),
            ("archived_pois", STAFF_ROLES),
            ("edit_imprint", STAFF_ROLES),
            (
                "edit_imprint",
                PRIV_STAFF_ROLES,
                {"title": "imprint", "submit_draft": True},
            ),
            ("events", STAFF_ROLES),
            ("events_archived", STAFF_ROLES),
            ("new_event", STAFF_ROLES),
            (
                "new_event",
                PRIV_STAFF_ROLES,
                {
                    "title": "new event",
                    "start_date": "2030-01-01",
                    "end_date": "2030-01-01",
                    "is_all_day": True,
                    "submit_draft": True,
                },
            ),
            ("new_page", STAFF_ROLES),
            (
                "new_page",
                PRIV_STAFF_ROLES,
                {
                    "title": "new page",
                    "mirrored_page_region": "",
                    "_ref_node_id": 7,
                    "_position": "first-child",
                    "submit_draft": True,
                },
            ),
            ("new_poi", STAFF_ROLES),
            (
                "new_poi",
                PRIV_STAFF_ROLES,
                {
                    "title": "new poi",
                    "short_description": "short description",
                    "address": "Test-Straße 5",
                    "postcode": "54321",
                    "city": "Augsburg",
                    "country": "Deutschland",
                    "longitude": 1,
                    "latitude": 1,
                    "submit_draft": True,
                },
            ),
            ("new_push_notification", STAFF_ROLES),
            ("pages", STAFF_ROLES),
            ("pois", STAFF_ROLES),
            ("push_notifications", STAFF_ROLES),
        ],
        # The kwargs for these views
        {"region_slug": "nurnberg", "language_slug": "de"},
    ),
    (
        [
            ("edit_region", STAFF_ROLES),
            (
                "edit_region",
                PRIV_STAFF_ROLES,
                {
                    "administrative_division": "CITY",
                    "name": "Augsburg",
                    "admin_mail": "augsburg@example.com",
                    "postal_code": "86150",
                    "status": "ACTIVE",
                    "longitude": 1,
                    "latitude": 1,
                },
            ),
        ],
        # The kwargs for these views
        {"slug": "augsburg"},
    ),
    (
        [
            ("edit_language", STAFF_ROLES),
            (
                "edit_language",
                PRIV_STAFF_ROLES,
                {
                    "native_name": "New name",
                    "english_name": "German",
                    "slug": "de",
                    "bcp47_tag": "de-de",
                    "text_direction": "LEFT_TO_RIGHT",
                    "table_of_contents": "Inhaltsverzeichnis",
                    "primary_country_code": "de",
                },
            ),
        ],
        # The kwargs for these views
        {"slug": "de"},
    ),
    (
        [("edit_user", STAFF_ROLES)],
        # The kwargs for these views
        {"user_id": 1},
    ),
    (
        [("edit_role", [ROOT])],
        # The kwargs for these views
        {"role_id": 1},
    ),
    (
        [("edit_offertemplate", STAFF_ROLES)],
        # The kwargs for these views
        {"slug": "ihk-lehrstellenboerse"},
    ),
    (
        [("linkcheck", ROLES)],
        # The kwargs for these views
        {"region_slug": "augsburg", "link_filter": "valid"},
    ),
    (
        [("linkcheck", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "link_filter": "valid"},
    ),
    (
        [("linkcheck", ROLES)],
        # The kwargs for these views
        {"region_slug": "augsburg", "link_filter": "unchecked"},
    ),
    (
        [("linkcheck", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "link_filter": "unchecked"},
    ),
    (
        [("linkcheck", ROLES)],
        # The kwargs for these views
        {"region_slug": "augsburg", "link_filter": "ignored"},
    ),
    (
        [("linkcheck", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "link_filter": "ignored"},
    ),
    (
        [("linkcheck", ROLES)],
        # The kwargs for these views
        {"region_slug": "augsburg", "link_filter": "invalid"},
    ),
    (
        [("linkcheck", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "link_filter": "invalid"},
    ),
    (
        [("get_page_order_table_ajax", STAFF_ROLES + [MANAGEMENT, EDITOR])],
        # The kwargs for these views
        {"region_slug": "augsburg", "parent_id": 1},
    ),
    (
        [("get_page_order_table_ajax", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "parent_id": 7},
    ),
    (
        [("get_page_order_table_ajax", STAFF_ROLES + [MANAGEMENT, EDITOR])],
        # The kwargs for these views
        {"region_slug": "augsburg", "parent_id": 1, "page_id": 2},
    ),
    (
        [("get_page_order_table_ajax", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "parent_id": 7, "page_id": 8},
    ),
    (
        [("get_page_order_table_ajax", STAFF_ROLES + [MANAGEMENT, EDITOR])],
        # The kwargs for these views
        {"region_slug": "augsburg", "page_id": 2},
    ),
    (
        [("get_page_order_table_ajax", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "page_id": 8},
    ),
    (
        [("get_page_children_ajax", STAFF_ROLES + [MANAGEMENT, EDITOR])],
        # The kwargs for these views
        {
            "region_slug": "augsburg",
            "language_slug": "de",
            "tree_id": 2,
            "lft": 1,
            "rgt": 12,
            "depth": 1,
        },
    ),
    (
        [("get_page_children_ajax", STAFF_ROLES)],
        # The kwargs for these views
        {
            "region_slug": "nurnberg",
            "language_slug": "de",
            "tree_id": 1,
            "lft": 1,
            "rgt": 14,
            "depth": 1,
        },
    ),
    (
        [
            ("view_page", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            ("edit_page", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            ("edit_page", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            (
                "edit_page",
                PRIV_STAFF_ROLES + [MANAGEMENT, EDITOR],
                {
                    "title": "new title",
                    "mirrored_page_region": "",
                    "_ref_node_id": 21,
                    "_position": "first-child",
                    "submit_draft": True,
                },
            ),
            ("sbs_edit_page", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            ("page_revisions", STAFF_ROLES + [MANAGEMENT, EDITOR]),
            (
                "archive_page",
                PRIV_STAFF_ROLES + [MANAGEMENT, EDITOR],
                {"post_data": True},
            ),
            (
                "restore_page",
                PRIV_STAFF_ROLES + [MANAGEMENT, EDITOR],
                {"post_data": True},
            ),
            ("delete_page", [ROOT, MUNICIPALITY_TEAM], {"post_data": True}),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "language_slug": "en", "page_id": 1},
    ),
    (
        [
            ("view_page", STAFF_ROLES),
            ("edit_page", STAFF_ROLES),
            ("sbs_edit_page", STAFF_ROLES),
            ("page_revisions", STAFF_ROLES),
            ("archive_page", PRIV_STAFF_ROLES, {"post_data": True}),
            ("restore_page", PRIV_STAFF_ROLES, {"post_data": True}),
            ("delete_page", [ROOT, MUNICIPALITY_TEAM], {"post_data": True}),
        ],
        # The kwargs for these views
        {"region_slug": "nurnberg", "language_slug": "en", "page_id": 7},
    ),
    (
        [("move_page", PRIV_STAFF_ROLES + [MANAGEMENT, EDITOR], {"post_data": True})],
        # The kwargs for these views
        {
            "region_slug": "augsburg",
            "language_slug": "en",
            "page_id": 1,
            "target_id": 21,
            "position": "first-child",
        },
    ),
    (
        [("page_revisions", STAFF_ROLES + [MANAGEMENT, EDITOR])],
        # The kwargs for these views
        {
            "region_slug": "augsburg",
            "language_slug": "de",
            "page_id": 1,
            "selected_revision": 1,
        },
    ),
    (
        [
            ("edit_event", ROLES),
            (
                "edit_event",
                PRIV_STAFF_ROLES + REGION_ROLES,
                {
                    "title": "new title",
                    "start_date": "2030-01-01",
                    "end_date": "2030-01-01",
                    "is_all_day": True,
                    "submit_draft": True,
                },
            ),
            ("archive_event", PRIV_STAFF_ROLES + REGION_ROLES, {"post_data": True}),
            ("restore_event", PRIV_STAFF_ROLES + REGION_ROLES, {"post_data": True}),
            ("delete_event", PRIV_STAFF_ROLES, {"post_data": True}),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "language_slug": "de", "event_id": 1},
    ),
    (
        [
            ("edit_poi", ROLES),
            (
                "edit_poi",
                PRIV_STAFF_ROLES + REGION_ROLES,
                {
                    "title": "new title",
                    "short_description": "short description",
                    "address": "Test-Straße 5",
                    "postcode": "54321",
                    "city": "Augsburg",
                    "country": "Deutschland",
                    "longitude": 1,
                    "latitude": 1,
                    "submit_draft": True,
                },
            ),
            ("archive_poi", PRIV_STAFF_ROLES + REGION_ROLES, {"post_data": True}),
            ("restore_poi", PRIV_STAFF_ROLES + REGION_ROLES, {"post_data": True}),
            ("delete_poi", [ROOT, MUNICIPALITY_TEAM], {"post_data": True}),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "language_slug": "de", "poi_id": 4},
    ),
    (
        [
            ("edit_language_tree_node", STAFF_ROLES),
            ("edit_language_tree_node", PRIV_STAFF_ROLES, {"language": 3, "parent": 2}),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "language_tree_node_id": 3},
    ),
    (
        [
            ("edit_region_user", STAFF_ROLES + [MANAGEMENT]),
            (
                "edit_region_user",
                PRIV_STAFF_ROLES + [MANAGEMENT],
                {"username": "new_username", "email": "new@email.address", "role": 1},
            ),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "user_id": 2},
    ),
    (
        [("edit_region_user", STAFF_ROLES)],
        # The kwargs for these views
        {"region_slug": "nurnberg", "user_id": 2},
    ),
    (
        [("dismiss_tutorial", ROLES, {"post_data": True})],
        # The kwargs for these views
        {"region_slug": "augsburg", "slug": "page-tree"},
    ),
    (
        [
            (
                "cancel_translation_process_ajax",
                PRIV_STAFF_ROLES + [MANAGEMENT, EDITOR],
                {"post_data": True},
            )
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "language_slug": "en", "page_id": 1},
    ),
]

#: In order for these views to be used as parameters, we have to flatten the nested structure
PARAMETRIZED_VIEWS = [
    (view_name, kwargs, post_data[0] if post_data else {}, roles)
    for view_conf, kwargs in VIEWS
    for view_name, roles, *post_data in view_conf
]

#: This list contains the config for all views which should check whether they correctly redirect to another url
REDIRECT_VIEWS = [
    (
        [
            ("public:login", ROLES, settings.LOGIN_REDIRECT_URL),
            ("public:password_reset", ROLES, settings.LOGIN_REDIRECT_URL),
            ("public:wiki_redirect", ALL_ROLES, settings.WIKI_URL),
            ("get_mfa_challenge", STAFF_ROLES, reverse("authenticate_modify_mfa")),
            ("register_new_mfa_key", STAFF_ROLES, reverse("authenticate_modify_mfa")),
        ],
        # The kwargs for these views
        {},
    ),
    (
        [
            (
                "statistics",
                ROLES,
                reverse("dashboard", kwargs={"region_slug": "augsburg"}),
            ),
            (
                "get_mfa_challenge",
                ROLES,
                reverse("authenticate_modify_mfa", kwargs={"region_slug": "augsburg"}),
            ),
            (
                "register_new_mfa_key",
                ROLES,
                reverse("authenticate_modify_mfa", kwargs={"region_slug": "augsburg"}),
            ),
            (
                "linkcheck_landing",
                STAFF_ROLES,
                reverse(
                    "linkcheck",
                    kwargs={"region_slug": "augsburg", "link_filter": "invalid"},
                ),
            ),
        ],
        # The kwargs for these views
        {"region_slug": "augsburg"},
    ),
    (
        [
            (
                "sbs_edit_page",
                STAFF_ROLES + [MANAGEMENT, EDITOR],
                reverse(
                    "edit_page",
                    kwargs={
                        "region_slug": "augsburg",
                        "language_slug": "de",
                        "page_id": 1,
                    },
                ),
            )
        ],
        # The kwargs for these views
        {"region_slug": "augsburg", "language_slug": "de", "page_id": 1},
    ),
    (
        [
            (
                "public:expand_page_translation_id",
                ALL_ROLES,
                "https://integreat.app/augsburg/de/willkommen/",
            )
        ],
        # The kwargs for these views
        {"short_url_id": 1},
    ),
]

#: In order for these views to be used as parameters, we have to flatten the nested structure
PARAMETRIZED_REDIRECT_VIEWS = [
    (view_name, kwargs, roles, target)
    for view_conf, kwargs in REDIRECT_VIEWS
    for view_name, roles, target in view_conf
]

#: Public views that only work for anonymous users
PARAMETRIZED_PUBLIC_VIEWS = [
    ("public:login", {}),
    ("public:login_mfa", {}),
    ("public:password_reset", {}),
    ("public:password_reset", {"email": "root@root.root"}),
]