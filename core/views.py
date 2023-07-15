from django.shortcuts import render , redirect
from django.http import FileResponse, Http404
from django.conf import settings
import os

from django.core.mail import send_mail

# Create your views here.


def DholeraMetroCity(request):
   

    return render(request, "core/index.html")


def Download(request):

    return render(request, "core/Download.html")


# def Brochure_DMC_5005(request):
#     file_path = os.path.join(settings.BASE_DIR, 'core/static/images/pdf/Brochure-Dholera-Metro-City-5005.pdf')
#     file_name = 'Brochure-Dholera-Metro-City-5005.pdf'  # Specify the desired title here

#     response = FileResponse(open(file_path, 'rb'), content_type='application/pdf')
#     response['Content-Disposition'] = f'filename="{file_name}"'
#     return response


def RERA(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'core/static/images/RERA/rera-certificate-dholera-metro-city.pdf')
        # Specify the desired title here
        file_name = 'rera-certificate-dholera-metro-city.pdf'

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Project_Land(request):
    return render(request, 'core/project-land.html')


def termConditions(request):
    return render(request, 'core/term-conditions.html')


def shipping(request):
    return render(request, 'core/shipping.html')


def RCpolicy(request):
    return render(request, 'core/R_C-policy.html')
