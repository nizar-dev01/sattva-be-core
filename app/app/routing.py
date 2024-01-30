from django.urls import re_path

from championship import consumers

websocket_urlpatterns = [
    re_path(r"ws/championship/(?P<room_name>\w+)/$", consumers.WSConsumer.as_asgi()),
]