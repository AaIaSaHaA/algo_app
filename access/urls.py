from unicodedata import name
from django.urls import path
from manage import main
from . import views

urlpatterns = [
    path('note/', views.note, name='note'),
    path('algorithm_guess/', views.algorithm_guess, name='algorithm_guess'),
    path('result/', views.result, name='result'),
    path('error/', views.error, name='error'),
]
