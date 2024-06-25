import logging

from django.conf import settings
from django.contrib import admin
from django.shortcuts import render
from django.urls import path
from django.utils.module_loading import import_string
from django.utils.translation import gettext_lazy as _

from ..metric_collection.helper import MetricCollectionAdminSiteHelper
from . import settings as app_settings
from .dashboard import get_dashboard_context
from .system_info import (
    get_enabled_immunity_modules,
    get_immunity_version,
    get_os_details,
)

logger = logging.getLogger(__name__)


class ImmunityAdminSite(admin.AdminSite):
    # <title>
    site_title = getattr(settings, 'IMMUNITY
_ADMIN_SITE_TITLE', 'Immunity Admin')
    # h1 text
    site_header = getattr(settings, 'IMMUNITY
_ADMIN_SITE_HEADER', 'Immunity')
    # text at the top of the admin index page
    index_title = _(
        getattr(settings, 'IMMUNITY
_ADMIN_INDEX_TITLE', 'Network Administration')
    )
    enable_nav_sidebar = False
    metric_collection = MetricCollectionAdminSiteHelper

    def index(self, request, extra_context=None):
        if app_settings.ADMIN_DASHBOARD_ENABLED:
            context = get_dashboard_context(request)
        else:
            context = {'dashboard_enabled': False}
        self.metric_collection.show_consent_info(request)
        return super().index(request, extra_context=context)

    def immunity_info(self, request, *args, **kwargs):
        context = {
            'enabled_immunity_modules': get_enabled_immunity_modules(),
            'system_info': get_os_details(),
            'immunity_version': get_immunity_version(),
            'title': _('System Information'),
            'site_title': self.site_title,
        }
        self.metric_collection.manage_form(request, context)
        return render(request, 'admin/immunity_info.html', context)

    def get_urls(self):
        autocomplete_view = import_string(app_settings.AUTOCOMPLETE_FILTER_VIEW)
        return [
            path(
                'ow-auto-filter/',
                self.admin_view(autocomplete_view.as_view(admin_site=self)),
                name='ow-auto-filter',
            ),
            path(
                'immunity-system-info/',
                self.admin_view(self.immunity_info),
                name='ow-info',
            ),
        ] + super().get_urls()


def immunity_admin(site_url=None):  # pragma: no cover
    """
    immunity_admin function is deprecated
    """
    logger.warning(
        'WARNING! Calling immunity_utils.admin_theme.admin.immunity_admin() '
        'is not necessary anymore and is therefore deprecated.\nThis function '
        'will be removed in future versions of immunity-utils and therefore '
        'it is recommended to remove any reference to it.\n'
    )
