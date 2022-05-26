from unicodedata import name
from django.urls import path
from manage import main
from . import views

urlpatterns = [
    path('contact',views.contact,name='contact'),
] 