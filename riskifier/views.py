# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView
from .models import RiskifierData


# Create your views here.
class ViewPageHome(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'home.html', context=None)

class ViewPageStart(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'start.html', context=None)

class ViewPageQuestionnaire(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'questionnaire.html', context=None)

class ViewPageResult(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'result.html', context=None)

class ViewPageFormular(TemplateView):
    def get(self, request, **kwargs):
        formulars = RiskifierData.objects.all()
        return render(request, 'formular.html', {'formulars': formulars})
