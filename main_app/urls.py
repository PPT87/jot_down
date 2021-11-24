from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('jots/', views.task_list, name='tasks'),
  path('about/', views.about, name='about'),
]