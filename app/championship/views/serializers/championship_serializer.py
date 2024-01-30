from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Championship


class ChampionshipSerializer(ModelSerializer):
    """Serializer for Championship"""
    image = SerializerMethodField()
    class Meta:
        model = Championship
        fields = '__all__'
    
    def get_image(self, obj):
        """Return the image url"""
        if obj.image and obj.image.url:
            return obj.image.url
        return None