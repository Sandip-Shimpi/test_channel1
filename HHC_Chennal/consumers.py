import json
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer

# class test_api(AsyncWebsocketConsumer):
#     async def connect(self):
# #         # if self.scope['url_route']['kwargs']['demo']:
# #         # print(self.scope, 'self.scopeself.scope''''''')
# #         # self.source_room_name = self.scope['url_route']['kwargs']['demo']
# #         # else:self.source_room_name =''
#         # data=str(self.source_room_name)
# #         # self.source_room_name=data[:2]
# #         # self.to=data[2:]
#         print('connected')
#         await self.channel_layer.group_add(
#             "location_group",
#             # f"location_group{self.source_room_name}",
#             self.channel_name
#         )
# #         # data=[[ 28.55108, 77.26913 ],[ 28.55106, 77.26906 ],[ 28.55105, 77.26897 ],[ 28.55101, 77.26872 ],[ 28.55099, 77.26849 ],[ 28.55097, 77.26831 ],[ 28.55093, 77.26794 ],[ 28.55089, 77.2676 ],[ 28.55123, 77.26756 ],[ 28.55145, 77.26758 ],[ 28.55168, 77.26758 ],[ 28.55175, 77.26759 ],[ 28.55177, 77.26755 ],[ 28.55179, 77.26753 ],[ 28.55108, 77.26913 ],[ 28.55106, 77.26906 ],[ 28.55105, 77.26897 ],[ 28.55101, 77.26872 ],[ 28.55099, 77.26849 ],[ 28.55097, 77.26831 ],[ 28.55093, 77.26794 ],[ 28.55089, 77.2676 ],[ 28.55123, 77.26756 ],[ 28.55145, 77.26758 ],[ 28.55168, 77.26758 ],[ 28.55175, 77.26759 ],[ 28.55177, 77.26755 ],[ 28.55179, 77.26753 ]]
        
#         await self.accept()
# #         # for i in data:
# #         #     await self.send(text_data=str(i))
# #         #     # await asyncio.sleep(0.5)  

#     async def receive(self, text_data=None, bytes_data=None):
#         if text_data:
# #             # Parse the incoming JSON message
#             print(text_data, 'datassss')
# #             # print(bytes_data, 'datassss')
#             data = json.loads(text_data)
# #             # data = text_data
#             print(data['text_data'], 'dataa.....')#[18.12134523,78.23451234]
#             message=[]
#             data1=data['text_data'].split(',')
#             for data in data1:
# #                 print(data)
#                 dd=data.replace(' ','').replace('[','').replace(']','')
#                 print(dd)
#                 message.append(dd)
#             # message = data.get('text_data', '')
#             print(message,';;;')
#             # response = await self.send_message(data)
# #             # print(message, ';message')
#             if data:
#                 await self.channel_layer.group_send(
#                     "location_group",
#                     {
#                         'type': 'send_message',
#                         'data':message 
#                     }
#                 )   
# #                 # Send the response from the internal API back to the client
#             # await self.send(text_data=json.dumps({
#             #         'internal_api_response': response
#             #     }))
# #             # Send the message back to the client
# #             # await self.send(text_data=message)

# #             # Send the message 10 times with a 500ms delay
# #         # for i in range(40):
# #         #     await self.send(text_data=str(i))
# #             # await asyncio.sleep(0.1)  # Asynchronous sleep for 500ms

#     async def send_message(self, data=[]):
#         if data: 
#             # await self.send(text_data=data)
#             # print(data,'yes got ')
#             await self.send(text_data=json.dumps(data))
# #             # print(json.dumps(data),'text_data=json.dumps(data)')

    

#     async def disconnect(self, close_code):
#         print('disconnected')
#         await self.channel_layer.group_discard(
# #             # f"location_group{self.source_room_name}",
#             "location_group",
#             self.channel_name
#         )
# from django.shortcuts import get_object_or_404
# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Get the room names from the URL
#         self.source_room_name = self.scope['url_route']['kwargs']['source_room_name']
#         self.target_room_name = self.scope['url_route']['kwargs']['target_room_name']
        
#         # self.chatroom = get_object_or_404(ChatGroup, group_name=self.chatroom_name)
#         # Create unique group names based on the room names
#         self.source_room_group_name = f'chat_{self.source_room_name}'
#         self.target_room_group_name = f'chat_{self.target_room_name}'

#         # Add the channel to the source group
#         await self.channel_layer.group_add(
#             self.source_room_group_name,
#             self.channel_name
#         )

#         # Accept the WebSocket connection
#         await self.accept()

#     async def disconnect(self, close_code):
#         # Remove the channel from the source group
#         await self.channel_layer.group_discard(
#             self.source_room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         # Receive a message from the WebSocket
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Forward the message from the source group to the target group
#         await self.channel_layer.group_send(
#             self.target_room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     async def chat_message(self, event):
#         # Receive a message from the group and send it to the WebSocket
#         message = event['message']
        
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class test_api(AsyncWebsocketConsumer):
#     async def connect(self):
#         # Determine room name and group from URL
#         self.room_name = self.scope['url_route']['kwargs']['demo']
#         self.group_name = f"location_group_{self.room_name}"
#         print(f'Connected to {self.group_name}')

#         # Add the WebSocket to the group
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )

#         await self.accept()

#     async def receive(self, text_data=None, bytes_data=None):
#         if text_data:
#             # Parse the incoming message
#             message_data = text_data.split(',')
#             message = [data.split(':')[1].strip() for data in message_data]

#             print(f'Received message: {message} in {self.group_name}')

#             # Determine the target group (forwarding logic)
#             # if self.room_name == '1213':
#             #     target_group = "location_group_1312"
#             # elif self.room_name == '1312':
#             #     target_group = "location_group_1213"
#             # else:
#             #     target_group = None

#             # Send the message to the target group if determined
#             # for i in range(3000):
#             #     if self.group_name:
#             #         await self.channel_layer.group_send(
#             #             self.group_name,
#             #             {
#             #                 'type': 'send_message',
#             #                 # 'data': message
#             #                 'data': i
#             #             }
#             #         ) 
#             # await asyncio.sleep(0.4)  # Asynchronous sleep for 500ms
                
#         for number in range(1, 120):  # Adjust range as needed
#             await self.send(text_data=str(number))
#             await asyncio.sleep(0.1)
#     async def send_message(self, event):
#         # Send the forwarded message to WebSocket
#         data = event['data']
#         print(f'Sending message: {data} to {self.group_name}')
#         await self.send(text_data=json.dumps(data))

#     async def disconnect(self, close_code):
#         # Remove from group on disconnect
#         print(f'Disconnected from {self.group_name}')
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )
import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class test_api(AsyncWebsocketConsumer):
#     async def connect(self):
#         print('connected')
        
#         # Adding the current WebSocket connection to the group
#         await self.channel_layer.group_add(
#             "location_group",
#             self.channel_name
#         )
#         await self.accept()

#     async def receive(self, text_data=None, bytes_data=None):
#         if text_data:
#             # print(text_data, 'datassss')
#             data = json.loads(text_data)
#             print(data['text_data'], 'dataa.....') #[18.12134523,78.23451234]
            
#             message = []
#             data1 = data['text_data'].split(',')
#             for data in data1:
#                 dd = data.replace(' ', '').replace('[', '').replace(']', '')
#                 message.append(dd)
#             # message=data1
#             # print(data1, ';;;')
#             print(message, ';;;')

#             if message:
#                 await self.channel_layer.group_send(
#                     "location_group",
#                     {
#                         'type': 'send_message',
#                         'data': message 
#                     }
#                 )

#     async def send_message(self, event):
#         data = event['data']
#         if data:
#             await self.send(text_data=json.dumps(data))

#     async def disconnect(self, close_code):
#         print('disconnected')
#         await self.channel_layer.group_discard(
#             "location_group",
#             self.channel_name
#         )


# class test_api1(AsyncWebsocketConsumer):
#     async def connect(self):

#         self.room_name = self.scope['url_route']['kwargs']['demo']
#         self.group_name = f"{self.room_name}"
#         # print('connected')
#         print(f'Connected to {self.group_name}')
        
#         # Adding the current WebSocket connection to the group
#         await self.channel_layer.group_add(
#             self.group_name,
#             self.channel_name
#         )
#         await self.accept()

#     async def receive(self, text_data=None, bytes_data=None):
#         if text_data:
#             # print(text_data, 'datassss')
#             data = json.loads(text_data)
#             # print(data['text_data'], 'dataa.....') #[18.12134523,78.23451234]
            
#             message = []
#             data1 = data['text_data'].split(',')
#             for data in data1:
#                 dd = data.replace(' ', '').replace('[', '').replace(']', '').replace('Lat:', '').replace('Lon:', '')
#                 message.append(dd)
#             # message=data1
#             # print(data1, ';;;')
#             message.append(self.group_name)
#             print(message, ';;;')

#             if message:
#                 await self.channel_layer.group_send(
#                     self.group_name,
#                     {
#                         'type': 'send_message',
#                         'data': message 
#                     }
#                 )

#     async def send_message(self, event):
#         data = event['data']
#         if data:
#             await self.send(text_data=json.dumps(data))

#     async def disconnect(self, close_code):
#         print('disconnected')
#         await self.channel_layer.group_discard(
#             self.group_name,
#             self.channel_name
#         )




###################################################################################################################
###################################################################################################################
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import save_location  # Import the Celery task

class test_api(AsyncWebsocketConsumer):
    async def connect(self):
        print('connected')
        await self.channel_layer.group_add("location_group", self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)
            print(data['text_data'], 'dataa.....')  # Example: [18.12134523,78.23451234]

            message = []
            data1 = data['text_data'].split(',')
            for data in data1:
                dd = data.replace(' ', '').replace('[', '').replace(']', '')
                message.append(dd)

            print(message, ';;;')

            if message:
                # Extract latitude and longitude from the message
                if len(message) >= 2:
                    latitude = message[0]
                    longitude = message[1]
                    user = data.get('user', 'anonymous')  # Extract user or default to 'anonymous'
                    
                    # Call the Celery task to save the location
                    save_location.delay(user, latitude, longitude)

                await self.channel_layer.group_send(
                    "location_group",
                    {
                        'type': 'send_message',
                        'data': message
                    }
                )

    async def send_message(self, event):
        data = event['data']
        if data:
            await self.send(text_data=json.dumps(data))

    async def disconnect(self, close_code):
        print('disconnected')
        await self.channel_layer.group_discard("location_group", self.channel_name)

class test_api1(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['demo']
        self.group_name = f"{self.room_name}"
        print(f'Connected to {self.group_name}')
        
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def receive(self, text_data=None, bytes_data=None):
        if text_data:
            data = json.loads(text_data)

            message = []
            data1 = data['text_data'].split(',')
            for data in data1:
                dd = data.replace(' ', '').replace('[', '').replace(']', '').replace('Lat:', '').replace('Lon:', '')
                message.append(dd)

            message.append(self.group_name)
            print(message, ';;;')

            if message:
                # Extract latitude and longitude from the message
                if len(message) >= 2:
                    latitude = message[0]
                    longitude = message[1]
                    # user = data.get('user', 'anonymous')  # Extract user or default to 'anonymous'
                    user = self.group_name
                    # Call the Celery task to save the location
                    # print(user, latitude,longitude , '#############')
                    save_location.delay(user, latitude, longitude)
                    # await save_location(user, latitude, longitude)

                await self.channel_layer.group_send(
                    self.group_name,
                    {
                        'type': 'send_message',
                        'data': message
                    }
                )

    async def send_message(self, event):
        data = event['data']
        if data:
            await self.send(text_data=json.dumps(data))

    async def disconnect(self, close_code):
        print('disconnected')
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
