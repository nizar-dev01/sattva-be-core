from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import action
from rest_framework.serializers import Serializer

class StoryImageSerializer(Serializer):
    """Serializer for uploading images to stories."""
    class Meta:
        fields = ("image",)


class BaseViewSetSkeleton(ModelViewSet):
    """Manage the CRUD operations of Championship.
        This module will help us decide which events belong to which championship
    """
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication, SessionAuthentication)

class BaseViewSet(BaseViewSetSkeleton):
    @action(methods=["POST"], detail=True, url_path="upload-image")
    def upload_image(self, request, id=None):
        """Upload image"""
        if not request.user.is_authenticated:
            raise AuthenticationFailed("Authentication credentials were not provided.")