from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Jot, SubJot


# Create your views here.
class JotList(ListView):
  model = Jot
  context_object_name = 'jots'

class SubJotList(ListView):
  model = SubJot

class JotDetails(DetailView):
  model = Jot
  context_object_name = 'jot'