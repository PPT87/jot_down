from django.urls import path
from . views import JotList

urlpatterns = [
    path('', JotList.as_view(), name='jots'),
]