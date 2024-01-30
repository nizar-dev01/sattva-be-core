from drf_spectacular.utils import extend_schema

from championship.models import Member
from .serializers import MemberSerializer
from .base_common import BaseViewSet

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Member'])
class MemberViewset(BaseViewSet):
    """Manage the CRUD operations of Member"""
    queryset = Member.objects.all()
    serializer_class = MemberSerializer