from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Member


class MemberSerializer(ModelSerializer):
    """Serializer for Member"""
    image = SerializerMethodField()
    class Meta:
        model = Member
        fields = '__all__'
    
    def get_image(self, obj):
        """Return the image url"""
        if obj.image and obj.image.url:
            return obj.image.url
        return None