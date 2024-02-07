from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Score


class ScoreSerializer(ModelSerializer):
    """Serializer for Score"""
    class Meta:
        model = Score
        fields = '__all__'
