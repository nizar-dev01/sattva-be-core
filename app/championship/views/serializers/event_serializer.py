from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Event


class EventSerializer(ModelSerializer):
    """Serializer for Event"""
    image = SerializerMethodField()
    class Meta:
        model = Event
        fields = '__all__'
    
    def get_image(self, obj):
        """Return the image url"""
        if obj.image and obj.image.url:
            return obj.image.url
        return None