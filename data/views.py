# -*- coding: utf-8 -*-
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render_to_response, RequestContext, render

from .models import Player
from .models import Match
from .models import Result
from .models import Coach


def home(request):
    return render_to_response("index.html", locals(),
                              context_instance=RequestContext(request))


def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


class D1(ListView):
    context_object_name = "players"
    template_name = "d1.html"

    queryset = Player.objects.filter(team__name='D1')

    def get_context_data(self, **kwargs):
        context = super(D1, self).get_context_data(**kwargs)
        team = 'D1'
        context["team"] = team
        context["coach"] = Coach.objects.filter(team=team)
        context["matches"] = Match.objects.filter(Q(home_team__name=team) | Q(away_team__name=team))
        context["results"] = Result.objects.filter(Q(match__home_team__name=team) | Q(match__away_team__name=team))
        return context


class D2(ListView):
    context_object_name = "players"
    template_name = "d2.html"

    queryset = Player.objects.filter(team__name='D2')

    def get_context_data(self, **kwargs):
        context = super(D2, self).get_context_data(**kwargs)
        team = 'D2'
        context["team"] = team
        context["coach"] = Coach.objects.filter(team=team)
        context["matches"] = Match.objects.filter(Q(home_team__name=team) | Q(away_team__name=team))
        context["results"] = Result.objects.filter(Q(match__home_team__name=team) | Q(match__away_team__name=team))
        return context


class H1(ListView):
    context_object_name = "players"
    template_name = "h1.html"

    queryset = Player.objects.filter(team__name='H1')

    def get_context_data(self, **kwargs):
        context = super(H1, self).get_context_data(**kwargs)
        team = 'H1'
        context["team"] = team
        context["coach"] = Coach.objects.filter(team=team)
        context["matches"] = Match.objects.filter(Q(home_team__name=team) | Q(away_team__name=team))
        context["results"] = Result.objects.filter(Q(match__home_team__name=team) | Q(match__away_team__name=team))
        return context


class H2(ListView):
    context_object_name = "players"
    template_name = "h2.html"

    queryset = Player.objects.filter(team__name='H2')

    def get_context_data(self, **kwargs):
        context = super(H2, self).get_context_data(**kwargs)
        team = 'H2'
        context["team"] = team
        context["coach"] = Coach.objects.filter(team=team)
        context["matches"] = Match.objects.filter(Q(home_team__name=team) | Q(away_team__name=team))
        context["results"] = Result.objects.filter(Q(match__home_team__name=team) | Q(match__away_team__name=team))
        return context
