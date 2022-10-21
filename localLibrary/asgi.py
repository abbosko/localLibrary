"""
ASGI config for localLibrary project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/

a standard for Python asynchronous web apps and servers to 
communicate with each other. ASGI is the asynchronous successor 
to WSGI and provides a standard for both asynchronous and 
synchronous Python app
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'localLibrary.settings')

application = get_asgi_application()
