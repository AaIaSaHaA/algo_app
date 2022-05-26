from django.shortcuts import render
from . models import Teacher_Info

# Create your views here.
def home (request):
    return render(request,'page/home.html')

def about (request):
    post = Teacher_Info.objects.all()
    return render(request,'page/about.html', {'post':post})