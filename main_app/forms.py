from django import forms
from django.forms import ModelForm
from .models import Task, SubTask

class TaskForm(forms.ModelForm):  
  title = forms.CharField(max_length = 250, widget = forms.TextInput(attrs = {'class' : 'form-control','placeholder' : 'Jot Down New Item', 
        }
    )
)
  class Meta:
    model = Task
    fields = ['title']

class SubTaskForm(forms.ModelForm):
  class TaskForm(forms.ModelForm):  
    title = forms.CharField(max_length = 250, widget = forms.TextInput(attrs = {'class' : 'form-control','placeholder' : 'Jot Down New Item', 
        }
    )
)
  class Meta:
    model = SubTask
    fields = ['title']