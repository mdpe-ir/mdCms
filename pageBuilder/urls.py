from django.urls import path
from .views import *

app_name = 'pageBuilder'
urlpatterns = [
    path('', index, name='home'),
]
