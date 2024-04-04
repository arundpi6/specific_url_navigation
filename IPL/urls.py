from django.urls import path
from IPL.views import *
app_name='IPL'
urlpatterns=[
    path('csk_team/',csk_team,name='csk_team'),
]