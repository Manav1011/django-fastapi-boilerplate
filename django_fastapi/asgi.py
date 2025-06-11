"""
ASGI config for django_fastapi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_fastapi.settings')
import django
django.setup()

from django_fastapi.fastapi_setup import get_fastapi_application
from starlette.applications import Starlette
from starlette.routing import Mount



application = get_asgi_application()
fastapi_application = get_fastapi_application()

# Combined ASGI app
application = Starlette(routes=[
    Mount("/api", app=fastapi_application),      # FastAPI served at /api/*
    Mount("/", app=application),          # Django served at /
])