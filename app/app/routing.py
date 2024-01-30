from django.urls import re_path

from championship import consumers

websocket_urlpatterns = [
    re_path("ws/championship-info/", consumers.WSConsumer.as_asgi()),
]