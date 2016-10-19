# -*- coding: utf-8 -*-
"""URLs and routing for REST API
"""

from rest_framework import routers

from . import views

#: The DRF Router object to use
ROUTER = routers.DefaultRouter()

# Views for "flowcells" app ---------------------------------------------------

ROUTER.register(r'sequencing_machines', views.SequencingMachineViewSet)
ROUTER.register(r'barcode_sets', views.BarcodeSetViewSet)
ROUTER.register(r'barcode_set_entries', views.BarcodeSetEntryViewSet)
ROUTER.register(r'flow_cells', views.FlowCellViewSet)
ROUTER.register(r'libraries', views.LibraryViewSet)

# Views for "threads" app -----------------------------------------------------

ROUTER.register(r'messages', views.MessageViewSet)
ROUTER.register(r'attachments', views.AttachmentViewSet)

# Views for "users" app -------------------------------------------------------

ROUTER.register(r'users', views.UserViewSet)
