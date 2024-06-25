from django.conf import settings

ADMIN_SITE_CLASS = getattr(
    settings,
    'IMMUNITY
_ADMIN_SITE_CLASS',
    'immunity_utils.admin_theme.admin.ImmunityAdminSite',
)

IMMUNITY
_ADMIN_THEME_LINKS = getattr(settings, 'IMMUNITY
_ADMIN_THEME_LINKS', [])
IMMUNITY
_ADMIN_THEME_JS = getattr(settings, 'IMMUNITY
_ADMIN_THEME_JS', [])
ADMIN_DASHBOARD_ENABLED = getattr(settings, 'IMMUNITY
_ADMIN_DASHBOARD_ENABLED', True)

IMMUNITY
_EMAIL_TEMPLATE = getattr(
    settings,
    'IMMUNITY
_EMAIL_TEMPLATE',
    'immunity_utils/email_template.html',
)

IMMUNITY
_EMAIL_LOGO = getattr(
    settings,
    'IMMUNITY
_EMAIL_LOGO',
    'https://raw.githubusercontent.com/immunity/immunity-utils/master/immunity_utils/'
    'static/immunity-utils/images/immunity-logo.png',
)

IMMUNITY
_HTML_EMAIL = getattr(settings, 'IMMUNITY
_HTML_EMAIL', True)
AUTOCOMPLETE_FILTER_VIEW = getattr(
    settings,
    'IMMUNITY
_AUTOCOMPLETE_FILTER_VIEW',
    'immunity_utils.admin_theme.views.AutocompleteJsonView',
)
