from django.shortcuts import render
from .models import Contact
#from django.http import HttpResponse
#from .models import Contact

# Create your views here.
def contact (request):
    if request.method == 'POST':
        #Get data from the form
        v_name = request.POST.get('name')
        v_email = request.POST.get('email')
        v_subject = request.POST.get('subject')
        v_message = request.POST.get('message')

        #Send the data to DB (models)
        v_contact = Contact(name=v_name, email=v_email, subject=v_subject, message=v_message)
        v_contact.save()

        return render(request,'user/Thank.html')
    else:
        return render(request,'user/contact.html')