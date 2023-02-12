from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import asyncio


class ChallengeConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['challenge_id']
        self.room_group_name = 'room_%s' % self.room_name
        # Add the client to a group
        await self.channel_layer.group_add(self.room_group_name,
                                           self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Remove the client from the group
        await self.channel_layer.group_discard(self.room_group_name,
                                               self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json.get('action')

        if action == "finish":
            finished = text_data_json.get('finished')
            # Broadcast the update to the group
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "finish_update",
                "finished": finished,
            })

        if action == "start":
            start = text_data_json.get("start")
            await self.channel_layer.group_send(self.room_group_name, {
                "type": "start_update",
                "start": start,
            })

    async def finish_update(self, event):
        finished = event.get('finished')
        # Send the update to the client
        await self.send(text_data=json.dumps({
            "finished": finished,
        }))

    async def start_update(self, event):
        start = event.get('start')
        # Send the update to the client
        await self.send(text_data=json.dumps({
            "start": start,
        }))