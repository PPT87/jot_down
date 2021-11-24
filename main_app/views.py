from django.shortcuts import render, redirect
from .models import Task, SubTask
from .forms import TaskForm
# from django.urls import reverse


# Create your views here.
def task_list(request):
  tasks = Task.objects.all()

  form = TaskForm()

  if request.method == "POST":
    form = TaskForm(request.POST)
    if form.is_valid():
      form.save()
    return redirect('/')
  context = {'tasks':tasks, 'form':form}
  return render(request, 'jots/task_list.html', context)

def about(request):
  return render(request, 'about.html')