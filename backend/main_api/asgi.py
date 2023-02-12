"""
ASGI config for main_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from main_api.routing import web_socket_url_patterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main_api.settings')
application = ProtocolTypeRouter({
    'http':
    get_asgi_application(),
    'websocket':
    AuthMiddlewareStack(URLRouter(web_socket_url_patterns))
})
