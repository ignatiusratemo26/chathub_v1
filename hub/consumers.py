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
    
    # Defining a method to handle incoming WebSocket messages
    async def receive(self, text_data):
        # Parsing the incoming JSON-formatted text data into a Python dictionary
        data = json.load(text_data)
        # Extracting the 'message', 'username', and 'hub' data from the parsed dictionary
        message = data['message']   # Extracting the message content
        username = data['username'] # Extracting the username of the sender
        hub = data['hub']           # Extracting the hub information

        await self.channel_layer.group_send(
            self.hub_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'hub': hub,
            }
        )
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        hub = event['hub']

        await self.send(text_data= json.dumps({
            'message': message,
            'username': username,
            'hub': hub,
        }))