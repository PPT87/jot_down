from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('jots/', views.jots_index, name='jots_index'),
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('jots/<int:jot_id>/', views.jots_detail, name='jots_detail'),
  path('jots/create', views.jotCreate, name="jot_create")
]