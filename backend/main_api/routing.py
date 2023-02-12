from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from um_challenge.routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    "http":
    get_asgi_application(),
    "websocket":
    AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(websocket_urlpatterns))),
    # Just HTTP for now. (We can add other protocols later.)
})
""" web_socket_url_patterns = [
    path("ws/test/", consumers.TestConsumer.as_view()),
] """