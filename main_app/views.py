from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Task, SubTask
from .forms import TaskForm, SubTaskForm
# from django.urls import reverse


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def jots_index(request):
  tasks = Task.objects.filter(user=request.user)
  form = TaskForm()
  context = {'tasks': tasks, 'form': form}
  return render(request, 'jots/index.html', context)

def jotCreate(request):
  form = TaskForm(request.POST)
  if form.is_valid():
    form.save()
  return redirect('jots_index')

def deleteJot(request, id):
    task = Task.objects.get(pk = id)
    task.delete()
    return redirect('jots_index')

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

def jots_detail(request, jot_id):
  task = Task.objects.get(id=jot_id)
  return render(request, 'jots/detail.html', { 'task': task })