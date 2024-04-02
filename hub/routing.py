from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<str: hub_name>/', consumers.ChatConsumers.as_asgi()),
]