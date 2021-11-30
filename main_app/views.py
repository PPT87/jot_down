from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Jot, SubJot
from .forms import JotForm, SubJotForm
# from django.urls import reverse


# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def jots_index(request):
  jots = Jot.objects.filter(user=request.user)
  form = JotForm()
  context = {'jots': jots, 'form': form}
  return render(request, 'jots/index.html', context)

class jotCreate(LoginRequiredMixin, CreateView):
  model = Jot
  fields = ['title', 'complete'] 
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class subjotCreate(LoginRequiredMixin, CreateView):
  model = SubJot
  fields = ['title', 'complete']
  def form_valid(self, form):
    form.instance.jot_id = self.kwargs['jot_id']
    return super().form_valid(form)

@login_required
def deleteJot(request, jot_id):
    jot = Jot.objects.get(id=jot_id)
    jot.delete()
    return redirect('jots_index')

@login_required
def deletesubJot(request, jot_id, subjot_id):
  subjot = SubJot.objects.get(id=subjot_id)
  subjot.delete()
  return redirect('jots_detail', jot_id=jot_id)

@login_required
def deletecompleteJot(request):
  deletecomplete= Jot.objects.filter(complete__exact=True)
  deletecomplete.delete()
  return redirect('jots_index')

@login_required
def deletecompletesubJot(request, jot_id):
  if SubJot.objects.filter(complete__exact=True):
    deletecompletesub = SubJot.objects.filter(complete__exact=True)
    deletecompletesub.delete()
    return redirect('jots_details', jot_id=jot_id)
  else:
    return redirect('jots_details', jot_id=jot_id)

@login_required
def completeJot(request, jot_id):
  jot = Jot.objects.get(pk=jot_id)
  jot.complete = True
  jot.save()
  return redirect('jots_index')

@login_required
def incompleteJot(request, jot_id):
  jot = Jot.objects.get(pk=jot_id)
  jot.complete = False
  jot.save()
  return redirect('jots_index')

@login_required
def completesubJot(request, jot_id, subjot_id):
  subjot = SubJot.objects.get(id=subjot_id)
  subjot.complete = True
  subjot.save()
  return redirect('jots_detail', jot_id=jot_id)

@login_required
def incompletesubJot(request, jot_id, subjot_id):
  subjot = SubJot.objects.get(id=subjot_id)
  subjot.complete = False
  subjot.save()
  return redirect('jots_detail', jot_id=jot_id)

@login_required
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