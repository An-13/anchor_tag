from django.urls import path
from app2.views import *
app_name='HL'

urlpatterns = [
    path('Webtech/',Webtech,name='Webtech'),
    path('Bootstrap/',Bootstrap,name='Bootstrap'),
]