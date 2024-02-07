from rest_framework.serializers import ModelSerializer, SerializerMethodField
 
from championship.models import Competition
from .team_serializer import TeamSerializer

from championship.models import Score
from .score_serializer import ScoreSerializer

class TeamCompetitionSerializer(TeamSerializer):
    """Serializer for Team in a competition"""
    scores = SerializerMethodField()
    wickets = SerializerMethodField()
    
    class Meta(TeamSerializer.Meta):
        model = TeamSerializer.Meta.model
        fields = '__all__'

    def get_scores(self, obj):
        score = Score.objects.all().get(team=obj, is_wicket=False)
        return score.points
    
    def get_wickets(self, obj):
        score = Score.objects.all().get(team=obj, is_wicket=True)
        return score.points

class CompetitionSerializer(ModelSerializer):
    """Serializer for Competition"""
    competitors = SerializerMethodField()
    winner = SerializerMethodField()
    class Meta:
        model = Competition
        fields = '__all__'

    def get_competitors(self, obj):
        """Serialize the Competitors"""
        return [
            TeamCompetitionSerializer(team).data for team in obj.competitors.all()
        ]

    def get_winner(self, obj):
        """Serialize the details of the winner"""
        if obj.winner is not None:
            winner = obj.winner
            serializer = TeamSerializer(winner)
            return serializer.data
        
        return None