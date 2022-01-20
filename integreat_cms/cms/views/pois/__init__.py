"""
This package contains all views related to POIs (points of interest)
"""
from .poi_view import POIView
from .poi_actions import (
    view_poi,
    archive_poi,
    restore_poi,
    delete_poi,
    automatic_translation,
)
from .poi_list_view import POIListView
