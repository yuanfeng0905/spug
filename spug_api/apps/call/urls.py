from django.urls import path

from .views import *

urlpatterns = [
    path('hello', TestView.as_view()),
]
