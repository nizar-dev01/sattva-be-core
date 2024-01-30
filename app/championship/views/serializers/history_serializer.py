from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import ChampionshipHistory


class ChampionshipHistorySerializer(ModelSerializer):
    """Serializer for ChampionshipHistory"""
    image = SerializerMethodField()
    class Meta:
        model = ChampionshipHistory
        fields = '__all__'
    
    def get_image(self, obj):
        """Return the image url"""
        if obj.image and obj.image.url:
            return obj.image.url
        return None