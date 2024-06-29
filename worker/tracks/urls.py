from django.urls import include, path
from .views import *


urlpatterns = [
    path('hit/', get_request, name='get request')
]