from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Task, SubTask
from .forms import TaskForm
# from django.urls import reverse


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def jots_index(request):
  tasks = Task.objects.filter(user=request.user)
  return render(request, 'jots/index.html', {'tasks': tasks})

def about(request):
  return render(request, 'about.html')

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