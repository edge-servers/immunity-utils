from django.conf import settings

ADMIN_SITE_CLASS = getattr(
    settings,
    'OPENWISP_ADMIN_SITE_CLASS',
    'immunity_utils.admin_theme.admin.ImmunityAdminSite',
)

OPENWISP_ADMIN_THEME_LINKS = getattr(settings, 'OPENWISP_ADMIN_THEME_LINKS', [])
OPENWISP_ADMIN_THEME_JS = getattr(settings, 'OPENWISP_ADMIN_THEME_JS', [])
ADMIN_DASHBOARD_ENABLED = getattr(settings, 'OPENWISP_ADMIN_DASHBOARD_ENABLED', True)

OPENWISP_EMAIL_TEMPLATE = getattr(
    settings,
    'OPENWISP_EMAIL_TEMPLATE',
    'immunity_utils/email_template.html',
)

OPENWISP_EMAIL_LOGO = getattr(
    settings,
    'OPENWISP_EMAIL_LOGO',
    'https://raw.githubusercontent.com/immunity/immunity-utils/master/immunity_utils/'
    'static/immunity-utils/images/immunity-logo.png',
)

OPENWISP_HTML_EMAIL = getattr(settings, 'OPENWISP_HTML_EMAIL', True)
AUTOCOMPLETE_FILTER_VIEW = getattr(
    settings,
    'OPENWISP_AUTOCOMPLETE_FILTER_VIEW',
    'immunity_utils.admin_theme.views.AutocompleteJsonView',
)
