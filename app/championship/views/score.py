from drf_spectacular.utils import extend_schema

from championship.models import Score
from .serializers import ScoreSerializer
from .base_common import BaseViewSetSkeleton

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Score'])
class ScoreViewset(BaseViewSetSkeleton):
    """Manage the CRUD operations of Score"""
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer