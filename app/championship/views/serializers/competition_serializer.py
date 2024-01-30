from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Competition


class CompetitionSerializer(ModelSerializer):
    """Serializer for Competition"""
    image = SerializerMethodField()
    class Meta:
        model = Competition
        fields = '__all__'