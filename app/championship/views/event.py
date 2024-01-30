from drf_spectacular.utils import extend_schema

from championship.models import Event
from .serializers import EventSerializer
from .base_common import BaseViewSet

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Event'])
class EventViewset(BaseViewSet):
    """Manage the CRUD operations of Event"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer