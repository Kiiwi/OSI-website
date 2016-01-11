# -*- coding: utf-8 -*-

from django.db import models
from django.utils.encoding import smart_str
from datetime import date


class Team(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Lag"

    def __str__(self):
        return self.name


class Player(models.Model):
    POSITION_CHOICES = (
        ("K", "Keeper"),
        ("B", "Back"),
        ("S", "Senter"),
        ("L", "Løper"),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    shirt_number = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    team = models.ForeignKey("Team")
    matches = models.ManyToManyField("Match", through="PlayerPoint")

    def total_goals(self):
        tot = 0
        for goal in PlayerPoint.objects.filter(player=self):
            tot += goal.goals
        return tot

    def total_assists(self):
        tot = 0
        for assist in PlayerPoint.objects.filter(player=self):
            tot += assist.assists
        return tot

    def total_penalty(self):
        tot = 0
        for penalty in PlayerPoint.objects.filter(player=self):
            tot += penalty.penalty_minutes
        return tot

    class Meta:
        verbose_name_plural = "Spillere"

    def __str__(self):
        return smart_str(self.team) + ' ' + smart_str(self.first_name) + ' ' + smart_str(self.last_name)


class Arena(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Arenaer"

    def __str__(self):
        return self.name


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches')
    away_team = models.ForeignKey(Team, related_name='away_matches')
    venue = models.ForeignKey(Arena)
    date = models.DateTimeField()

    class Meta:
        verbose_name_plural = "Kamper"

    @property
    def is_past_due(self):
        if date.today() < self.date.date():
            return True
        return False

    def __str__(self):
        return smart_str(self.home_team) + ' - ' + smart_str(self.away_team)


class Result(models.Model):
    match = models.OneToOneField(Match)
    score_hometeam = models.IntegerField()
    score_awayteam = models.IntegerField()

    class Meta:
        verbose_name_plural = "Resultater"

    def __str__(self):
        return smart_str(self.match) + '  ' + smart_str(self.score_hometeam) + ' - ' + smart_str(self.score_awayteam)


class PlayerPoint(models.Model):
    player = models.ForeignKey(Player, related_name="points")
    match = models.ForeignKey(Match)
    goals = models.IntegerField()
    assists = models.IntegerField()
    penalty_minutes = models.IntegerField()

    class Meta:
        verbose_name_plural = "Poeng"
        unique_together = ('player', 'match')

    def __str__(self):
        return smart_str(self.player) + ' ' + smart_str(self.goals) + ' ' + smart_str(self.assists) + ' ' + smart_str(
            self.penalty_minutes)


class Coach(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    team = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Trenere"