from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path('ws/<str:hub_name>/', consumers.ChatConsumer.as_asgi()),
]