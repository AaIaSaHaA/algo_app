from django.shortcuts import render
from . models import Developer_Info

# Create your views here.
def home (request):
    return render(request,'page/home.html')

def about (request):
    post = Developer_Info.objects.all()
    return render(request,'page/about.html', {'post':post})