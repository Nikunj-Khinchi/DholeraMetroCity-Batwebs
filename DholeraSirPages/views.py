from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
    return render(request , 'dholera/dholeraSir.html')

def connectivity(request):
    return render(request , 'dholera/connectivity.html')





def image_view(request, image_name):
    if image_name == 'Road-Connectivity':
         image_path = os.path.join( settings.BASE_DIR, 'DholeraSirPages/static/dholeraSir-images/Conectivity/thumbnail/ways/Road_Connectivity_dholera_SIR.jpg')
    elif image_name =='Rail-Connectivity':
         image_path = os.path.join( settings.BASE_DIR, 'DholeraSirPages/static/dholeraSir-images/Conectivity/thumbnail/ways/Rail_Connectivity_dholera_SIR.jpg')
    elif image_name =='Air-Connectivity':
         image_path = os.path.join( settings.BASE_DIR, 'DholeraSirPages/static/dholeraSir-images/Conectivity/thumbnail/ways/Air_Connectivity_dholera_SIR.jpg')
    elif image_name =='Sea-Connectivity':
         image_path = os.path.join( settings.BASE_DIR, 'DholeraSirPages/static/dholeraSir-images/Conectivity/thumbnail/ways/Sea_Connectivity_dholera_SIR.jpg')
         
         
    with open(image_path, 'rb') as f:
        return HttpResponse(f.read(), content_type="image/jpeg")
    
    
    
def projects(request):
    return render(request , 'dholera/projects.html')

def AirPort(request):
    return render(request , 'dholera/dholera-Airport.html')

def Solar_plant(request):
    return render(request , 'dholera/solar-plant.html')

def Metro(request):
    return render(request , 'dholera/metro.html')

def Express(request):
    return render(request , 'dholera/express-way.html')

def MegaProjects(request):
    return render(request , 'dholera/mega-projects.html') 

def PhotoGallery(request):
    
    image_range = range(1, 36)  # Generate a range from 1 to 20
    context = {'image_range': image_range}
    return render(request , 'dholera/photo-gallery.html' , context) 

def RuCoProjects(request):
    return render(request , 'dholera/running-completedProjects.html')  

def CurrentStatus(request):
    return render(request , 'dholera/current-status.html')

def DMIC(request):
    return render(request ,  'dholera/DMIC.html')

def DFC(request):
    return render(request, 'dholera/DFC.html')

def GIDB(request):
    return render(request , 'dholera/GIDB.html')

def DRDA(request):
    return render(request , 'dholera/D-RDA.html')
    