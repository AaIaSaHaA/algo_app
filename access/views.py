from django.shortcuts import render
from . models import Note

# Create your views here.
def note (request):
    post = Note.objects.all()
    return render(request,'access/note.html', {'post':post})