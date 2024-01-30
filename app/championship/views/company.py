from drf_spectacular.utils import extend_schema

from championship.models import Company
from .serializers import CompanySerializer
from .base_common import BaseViewSet

from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Company'])
class CompanyViewset(BaseViewSet):
    """Manage the CRUD operations of Company"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer