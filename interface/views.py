from django.shortcuts import render

# Create your views here.

def interface (request):
    return render(request,'interface/interface.html')
