from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Jot


# Create your views here.
class JotList(ListView):
  model = Jot