import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(AsyncWebsocketConsumer):
    # Connect to chat server
    async def connect(self):
        # Extracting the hub name from the URL route kwargs
        self.hub_name = self.scope['url_route']['kwargs']['hub_name']
        # Creating a group name for the hub
        self.hub_group_name = 'chat_%s' % self.hub_name

        # Adding the consumer to the group
        await self.channel_layer.group_add(
            self.hub_group_name,
            self.channel_name
        )
        # Accepting the Websocket connection
        await self.accept()

    # Disconnect from chat server
    async def disconnect(self):
        # Removing the consumer from the group
        await self.channel_layer.group_discard(
            self.hub_group_name,
            self.channel_name
        )