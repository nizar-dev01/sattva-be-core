from drf_spectacular.utils import extend_schema

from championship.models import Championship
from .serializers import ChampionshipSerializer
from .base_common import BaseViewSet

@extend_schema(tags=['Championship'])
class ChampionshipViewset(BaseViewSet):
    """Manage the CRUD operations of Championship"""
    queryset = Championship.objects.all()
    serializer_class = ChampionshipSerializer