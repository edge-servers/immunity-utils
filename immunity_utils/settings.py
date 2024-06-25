from django.conf import settings

EXTENDED_APPS = getattr(settings, 'EXTENDED_APPS', [])

# API settings
API_DOCS = getattr(settings, 'IMMUNITY
_API_DOCS', True)
API_INFO = getattr(
    settings,
    'IMMUNITY
_API_INFO',
    {
        'title': 'Immunity API',
        'default_version': 'v1',
        'description': 'Immunity REST API',
    },
)

CELERY_HARD_TIME_LIMIT = getattr(settings, 'IMMUNITY
_CELERY_HARD_TIME_LIMIT', 120)
CELERY_SOFT_TIME_LIMIT = getattr(settings, 'IMMUNITY
_CELERY_SOFT_TIME_LIMIT', 30)
