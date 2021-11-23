from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task, SubTask
# from django.urls import reverse


# Create your views here.
class TaskList(ListView):
  model = Task
  context_object_name = 'tasks'

class TaskDetails(DetailView):
  model = Task
  context_object_name = 'task'

class TaskCreate(CreateView):
  model = Task
  fields = '__all__'
  success_url='/'

class SubTaskList(ListView):
  model = SubTask
  context_object_name = 'subtasks'