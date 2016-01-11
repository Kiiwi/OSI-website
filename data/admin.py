from django.contrib import admin

from .models import Team
from .models import Player
from .models import Match
from .models import PlayerPoint
from .models import Result
from .models import Arena
from .models import Coach


class PlayerAdmin(admin.ModelAdmin):
    class Meta:
        model = Player

admin.site.register(Player, PlayerAdmin)


class MatchAdmin(admin.ModelAdmin):
    class Meta:
        model = Match

admin.site.register(Match, MatchAdmin)


class PointAdmin(admin.ModelAdmin):
    class Meta:
        model = PlayerPoint

admin.site.register(PlayerPoint, PointAdmin)


class ResultAdmin(admin.ModelAdmin):
    class Meta:
        model = Result

admin.site.register(Result, ResultAdmin)


class TeamAdmin(admin.ModelAdmin):
    class Meta:
        model = Team

admin.site.register(Team, TeamAdmin)


class ArenaAdmin(admin.ModelAdmin):
    class Meta:
        model = Arena

admin.site.register(Arena, ArenaAdmin)


class CoachAdmin(admin.ModelAdmin):
    class Meta:
        model = Coach

admin.site.register(Coach, CoachAdmin)