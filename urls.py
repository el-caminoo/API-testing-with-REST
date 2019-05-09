from django.urls import path
from .views import *

urlpatterns = [
    path('api', StudentView.as_view(), name='studentView'),

]
