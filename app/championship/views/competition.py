from drf_spectacular.utils import extend_schema

from championship.models import Competition
from .serializers import CompetitionSerializer
from .base_common import BaseViewSetSkeleton

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Competition'])
class CompetitionViewset(BaseViewSetSkeleton):
    """Manage the CRUD operations of Competition"""
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer