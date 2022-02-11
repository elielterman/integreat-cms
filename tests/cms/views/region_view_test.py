from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group as Role

from integreat_cms.cms.models import Region, Language, LanguageTreeNode

from .view_test import ViewTest
from .view_test_utils import generate_test_functions


region_views = [
    "analytics",
    "app_size",
    "dashboard",
    "media",
    "mediacenter_directory_path",
    "mediacenter_get_directory_content",
    "new_region_user",
    "region_feedback",
    "region_users",
    "statistics",
    "translation_coverage",
    "user_settings",
]

region_language_views = [
    "archived_pages",
    "archived_pois",
    "edit_imprint",
    "events",
    "events_archived",
    "new_event",
    "new_page",
    "new_poi",
    "new_push_notification",
    "pages",
    "pois",
    "push_notifications",
]


class RegionViewTest(ViewTest):
    """
    This test checks whether all region views return status code 200.
    """

    def setUp(self):
        region = Region.objects.create(slug="test_region", statistics_enabled=True)
        language = Language.objects.create(
            slug="te-st", native_name="test_language", english_name="test_language"
        )
        LanguageTreeNode.add_root(language=language, region=region)
        user = get_user_model().objects.create_user("region_user")
        user.regions.add(region)
        user.save()
        Role.objects.get(name="MANAGEMENT").user_set.add(user)
        self.client.force_login(user)

    generate_test_functions(
        class_variables=vars(),
        views=region_views,
        kwargs={"region_slug": "test_region"},
    )

    generate_test_functions(
        class_variables=vars(),
        views=region_language_views,
        kwargs={"region_slug": "test_region", "language_slug": "te-st"},
    )