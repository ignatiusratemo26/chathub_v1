import os

from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import hub.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chathub.settings')

#modified
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        hub.routing.websocket_urlpatterns
    )
})
