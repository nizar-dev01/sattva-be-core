from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Team


class TeamSerializer(ModelSerializer):
    """Serializer for Team"""
    image = SerializerMethodField()
    class Meta:
        model = Team
        fields = '__all__'
    
    def get_image(self, obj):
        """Return the image url"""
        if obj.image and obj.image.url:
            return obj.image.url
        return None