from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from user.models import Notification
import json


class NotificationConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Get the user tag from the URL route
        user_tag = self.scope['url_route']['kwargs']['usertag']

        # Replace any '$' signs with underscores in the user tag
        group_name = user_tag.replace('$', '_')

        # Subscribe the WebSocket connection to the user's group
        await self.channel_layer.group_add(group_name, self.channel_name)

        # Accept the WebSocket connection
        await self.accept()

    async def receive(self, text_data):
        # Parse the JSON message
        text_data_json = json.loads(text_data)

        # Extract the message data
        from_user = text_data_json['from_user']
        message = text_data_json['message']
        recipients = text_data_json['recipients']
        url = text_data_json['url']

        create_notification = database_sync_to_async(
            Notification.objects.create)
        await create_notification(from_user=from_user,
                                  message=message,
                                  sent_to=recipients,
                                  url=url)

        # Send the message to the appropriate recipients
        for recipient in recipients:
            # Replace any '$' signs with underscores in the recipient group name
            group_name = recipient.replace('$', '_')
            await self.channel_layer.group_send(
                group_name, {
                    'type': 'notification_message',
                    'from_user': from_user,
                    'message': message,
                    'url': url
                })

    async def notification_message(self, event):
        # Send the message to the WebSocket connection
        await self.send(text_data=json.dumps({
            'from_user': event['from_user'],
            'message': event['message']
        }))

    async def disconnect(self, close_code):
        # Get the user tag from the URL route
        user_tag = self.scope['url_route']['kwargs']['usertag']

        # Replace any '$' signs with underscores in the user tag
        group_name = user_tag.replace('$', '_')

        # Unsubscribe the WebSocket connection from the user's group
        await self.channel_layer.group_discard(group_name, self.channel_name)
