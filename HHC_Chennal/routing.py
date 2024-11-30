from django.urls import path
from .consumers import *


websocket_urlpatterns = [
    path('ws/test/', test_api.as_asgi()),
    path('ws/test/<demo>', test_api1.as_asgi()),
    # path('ws/test/<chat_room>', test_api.as_asgi()),
    # path(r'ws/chat/(?P<source_room_name>\w+)/(?P<target_room_name>\w+)/$', test_api.as_asgi())
]