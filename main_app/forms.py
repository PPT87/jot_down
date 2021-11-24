from django.forms import ModelForm
from .models import Task, SubTask

class TaskForm(ModelForm):  
  class Meta:
    model = Task
    fields = ['title', 'complete']

class SubTaskForm(ModelForm):
  class Meta:
    model = SubTask
    fields = ['title', 'complete']