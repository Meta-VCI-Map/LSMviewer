from LSMviewer.common import *

DEBUG = True

ALLOWED_HOSTS = [
]

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

ROOT_URLCONF = PATH + '.urls'

WSGI_APPLICATION = PATH + '.wsgi.application'

#BASE_PATH = PATH