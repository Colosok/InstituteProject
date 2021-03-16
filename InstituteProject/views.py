from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.db.models import F


class IndexView(generic.TemplateView):
    template_name = 'InstituteProject/index.html'
