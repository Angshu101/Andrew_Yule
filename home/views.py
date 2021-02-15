from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
def index(request):
    context={
        'variable':"WOW YOU ARE SO GREAT"
    }
    return render(request,'index.html',context)

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        messages.success(request, 'Your Info Has been Saved')
    return render(request,'contact.html')