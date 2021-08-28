import json
from channels.generic.websocket import WebsocketConsumer
from .views import respond_to_websockets
from asgiref.sync import async_to_sync
from .models import Audit


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        self.user = self.scope["user"]

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        response = respond_to_websockets({'text' : message})
        # Auditing Users Clicks and Updating Counts
        audit, created = Audit.objects.get_or_create(
            user = self.user,
            defaults={ 'user' : self.user},
        )
        audit.update_counts(message)

        self.send(text_data=json.dumps({
            'message': response['text']
        }))
