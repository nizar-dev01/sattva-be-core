from drf_spectacular.utils import extend_schema

from championship.models import Team
from .serializers import TeamSerializer
from .base_common import BaseViewSet

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Team'])
class TeamViewset(BaseViewSet):
    """Manage the CRUD operations of Team"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer