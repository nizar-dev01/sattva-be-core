from drf_spectacular.utils import extend_schema

from championship.models import ChampionshipHistory
from .serializers import ChampionshipHistorySerializer
from .base_common import BaseViewSet

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['ChampionshipHistory'])
class ChampionshipHistoryViewset(BaseViewSet):
    """Manage the CRUD operations of ChampionshipHistory"""
    queryset = ChampionshipHistory.objects.all()
    serializer_class = ChampionshipHistorySerializer