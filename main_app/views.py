from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView   
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Jot, SubJot
from .forms import JotForm, SubJotForm
# from django.urls import reverse


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def jots_index(request):
  jots = Jot.objects.filter(user=request.user)
  form = JotForm()
  context = {'jots': jots, 'form': form}
  return render(request, 'jots/index.html', context)

class jotCreate(CreateView):
  model = Jot
  fields = ['title', 'complete']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class subjotCreate(CreateView):
  model = SubJot
  fields = ['title', 'complete']
  def form_valid(self, form):
    form.instance.jot_id = self.kwargs['jot_id']
    return super().form_valid(form)

def deleteJot(request, jot_id):
    jot = Jot.objects.get(id=jot_id)
    jot.delete()
    return redirect('jots_index')


def jots_detail(request, jot_id):
  jot = Jot.objects.get(id=jot_id)
  subjot_form = SubJotForm()
  context = {'jot': jot, 'subjot_form': subjot_form}
  return render(request, 'jots/detail.html', context)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('jots_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)