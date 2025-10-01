"""
WSGI config para flight_manager.
Este archivo sirve como punto de entrada para servidores WSGI como Gunicorn.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flight_manager.settings')

application = get_wsgi_application()
