from django import forms
from django.forms import ModelForm
from .models import Jot, SubJot

class JotForm(forms.ModelForm):  
  title = forms.CharField(max_length = 250, widget = forms.TextInput(attrs = {'class' : 'form-control','placeholder' : 'Jot Down New Item', 
        }
    )
)
  class Meta:
    model = Jot
    fields = ['title']

class SubJotForm(forms.ModelForm):
  class JotForm(forms.ModelForm):  
    title = forms.CharField(max_length = 250, widget = forms.TextInput(attrs = {'class' : 'form-control','placeholder' : 'Jot Down New Item', 
        }
    )
)
  class Meta:
    model = SubJot
    fields = ['title']