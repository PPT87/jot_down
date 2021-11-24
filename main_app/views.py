from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import Task, SubTask
from .forms import TaskForm
# from django.urls import reverse


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def task_list(request):
  tasks = Task.objects.all()

  form = TaskForm()

  if request.method == "POST":
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('/jots')
  context = {'tasks':tasks, 'form':form}
  return render(request, 'jots/task_list.html', context)

def about(request):
  return render(request, 'about.html')