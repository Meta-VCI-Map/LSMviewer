"""
WSGI config for LSMviewer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

try:
    '''Development'''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LSMviewer.settings')
except:
    '''Deployment'''
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LSMviewer.LSMviewer.deployment_settings')

application = get_wsgi_application()
