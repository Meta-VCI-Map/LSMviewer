from LSMviewer.common import *

DEBUG = False

ALLOWED_HOSTS = [
  'metavcimap.org',
  'www.metavcimap.org',
]

ROOT_URLCONF = PATH + '.LSMviewer.urls'

WSGI_APPLICATION = PATH + '.LSMviewer.wsgi.application'

# HTTPS SETTINGS
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_SSL_REDIRECT = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

STATIC_ROOT = '/home/deb117379/domains/metavcimap.org/public_html/static'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/home/deb117379/logs/lsmviewer.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

BASE_PATH = PATH