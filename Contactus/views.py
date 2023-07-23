import json
from django.shortcuts import render, redirect
from django.core.mail import send_mail,  EmailMessage
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

        subject = f'Inquiry by {name}'
        message = f'Name: {name}\n\nEmail: {email}\n\nPhone number: {mobile}\n\nPage: {page}'
        from_email = email  # Sender's email address
        recipient_list = [settings.EMAIL_HOST_USER]
        cc_list = ['ceo@dholerasir.co', 'it@dholerasir.co']

        email_message = EmailMessage(
            subject, message, from_email, recipient_list, cc=cc_list)
        email_message.send()

        from_email2 = settings.EMAIL_HOST_USER   # Sender's email address
        recipient_list2 = [email]

        subject2 = 'Dholera Metro City'
        message2 = f'Hello, {name}\nThankyou for contacting us we will reach you soon'

        send_mail(subject2, message2, from_email2, recipient_list2)

    return render(request, 'pages/inquiry.html')


def Site_visit(request):
    return render(request, 'pages/site-visit.html')


def NRI(request):
    return render(request, 'pages/NRI.html')


def Career(request):
    return render(request, 'pages/career.html')
