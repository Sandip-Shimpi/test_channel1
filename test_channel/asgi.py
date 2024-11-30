"""
ASGI config for test_channel project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
# from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack
from HHC_Chennal import routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_channel.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': 
        AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
    
    })

