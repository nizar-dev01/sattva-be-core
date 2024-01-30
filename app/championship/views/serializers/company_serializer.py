from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Company


class CompanySerializer(ModelSerializer):
    """Serializer for Company"""
    image = SerializerMethodField()
    class Meta:
        model = Company
        fields = '__all__'
    
    def get_image(self, obj):
        """Return the image url"""
        if obj.image and obj.image.url:
            return obj.image.url
        return None