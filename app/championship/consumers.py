from channels.consumer import AsyncConsumer
import json

class WSConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        group_name = "championship-info"
        await self.channel_layer.group_add(group_name, self.channel_name)
        await self.send({
            "type": "websocket.accept"
        })
        await self.channel_layer.group_send(group_name, {
            "type": "notify.push",
            "data": {
                "layer": "system",
                "kind": "connection",
                "data": {
                    "message": f"The connection has been established: {group_name}"
                }
            }
        })

    async def websocket_receive(self, event):
        """Receive message handler"""
        print("Received a message on websocket channel : ", event)
        # user = self.scope['user']
        # group_name = "notify_"+ user.username

        # await self.channel_layer.group_send(group_name, {
        #     "type": "notify.push",
        #     "data": {
        #         "layer": "application",
        #         "kind": "notification",
        #         "data": {
        #             "message": "The message reached the server."
        #         }
        #     },
        # })

    async def notify_push(self, event):
        """Send down to the client"""
        print("Sending data : ", event)
        await self.send({
            "type": "websocket.send",
            "text": json.dumps(event["data"])
        })
    
    async def websocket_disconnect(self, event):
        user=self.scope['user']
        group_name="notify_"+ user.username
        self.channel_layer.group_discard(group_name, self.channel_name)
