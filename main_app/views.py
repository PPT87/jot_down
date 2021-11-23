from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Jot, SubJot


# Create your views here.
class JotList(ListView):
  model = Jot
  context_object_name = 'jots'

class SubJotList(ListView):
  model = SubJot