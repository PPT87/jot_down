from django.urls import path
from . import views

urlpatterns = [
  path('about/', views.about, name='about'),
  path('accounts/signup/', views.signup, name='signup'),
  path('', views.Home.as_view(), name='home'),
  path('jots/', views.jots_index, name='jots_index'),
  path('jots/<int:jot_id>/', views.jots_detail, name='jots_detail'),
  path('jots/create/', views.jotCreate.as_view(), name="jot_create"),
  path('jots/<int:jot_id>/createsubjot/', views.subjotCreate.as_view(), name="subjot_create"),
  path('jots/delete/<int:jot_id>', views.deleteJot, name="jot_delete"),
  path('jots/<int:jot_id>/complete', views.completeJot, name="jot_complete"),
  path('jots/<int:jot_id>/completesubjot', views.completesubJot, name="subjot_complete")

]