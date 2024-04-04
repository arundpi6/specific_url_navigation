from django.urls import path
from Dhoni.views import *
app_name='Dhoni'
urlpatterns=[
    path('captain/',captain,name='captain'),
]