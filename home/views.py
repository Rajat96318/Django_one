from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    # context is dictionary of variable jo send hoga website pe
    context = {
        "variable1" : "Rajat is noob",
        "variable2" : "I am noob",
    }
    # messages.success(request, "this is a test message")
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is dhsfjhdfgjxfn about page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")  # ye wala comma bhul k bhi mat lagana

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        address = request.POST.get('address','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, address=address, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been send!')
        return HttpResponseRedirect('contact','')
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")