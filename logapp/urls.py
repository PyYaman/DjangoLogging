from django.urls import path
from .views import *

urlpatterns = [
    path('view/', StudentView.as_view()),
]