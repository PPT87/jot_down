from django.urls import path
from . views import JotList, JotDetails

urlpatterns = [
    path('', JotList.as_view(), name='jots'),
    path('jot/<int:pk>/', JotDetails.as_view(), name='jot')
]