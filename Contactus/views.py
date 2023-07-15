import json
from django.shortcuts import render , redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
def index(request):
    pass

def Inquiry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        page = request.POST.get('current_url')

        subject = 'Inquiry by ' + name
        message = f'Name: {name}\n\nEmail: {email}\n\nPhone number: {mobile}\n\nPage: {page}'
        from_email = (email)  # Sender's email address
        recipient_list = [settings.EMAIL_HOST_USER]  # Recipient's email address (Nikunj's email)

        send_mail(subject, message, from_email, recipient_list)

      
        
    return render(request, 'pages/inquiry.html')

def Site_visit(request):
    return render(request , 'pages/site-visit.html')

def NRI(request):
    return render(request, 'pages/NRI.html')

def Career(request):
    return render(request, 'pages/career.html')