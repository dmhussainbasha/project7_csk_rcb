from csk.views import *
from django.urls import path
app_name='abc'
urlpatterns=[
    path('msd/',msd,name='msd'),
     path('raina/',raina,name='raina'),
]