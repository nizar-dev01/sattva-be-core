from django.contrib import admin

from championship.models import Championship, Event, Team, Company, Member, Competition, Score, ChampionshipHistory

from .championship_admin import ChampionshipAdmin
from .event_admin import EventAdmin
from .team_admin import TeamAdmin
from .company_admin import CompanyAdmin
from .member_admin import MemberAdmin
from .competition_admin import CompetitionAdmin
from .score_admin import ScoreAdmin
from .history_admin import HistoryAdmin

admin.site.register(Championship, ChampionshipAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Team, TeamAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Competition, CompetitionAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(ChampionshipHistory, HistoryAdmin)
