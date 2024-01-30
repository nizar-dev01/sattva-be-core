
from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from championship.views import (
    ChampionshipViewset,
    EventViewset,
    TeamViewset,
    CompanyViewset,
    MemberViewset,
    CompetitionViewset,
    ScoreViewset,
    ChampionshipHistoryViewset
)

router_v1 = DefaultRouter()
router_v1.register('championships', ChampionshipViewset, basename='championship')
router_v1.register('events', EventViewset, basename='event')
router_v1.register('teams', TeamViewset, basename='team')
router_v1.register('companies', CompanyViewset, basename='company')
router_v1.register('members', MemberViewset, basename='member')
router_v1.register('competitions', CompetitionViewset, basename='competition')
router_v1.register('scores', ScoreViewset, basename='score')
router_v1.register('championship-history', ChampionshipHistoryViewset, basename='championship-history')

app_name = "api"

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
