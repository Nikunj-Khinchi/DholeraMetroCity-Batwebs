from django.shortcuts import render

# Create your views here.
def index(request):
    pass

def Lily_DRT(request):    
    return render(request , 'pages/Lily-DRT.html')


def Rose_DRT(request):    
    return render(request , 'pages/Rose-DRT.html')

def Lotus_DRT(request):    
    return render(request , 'pages/Lotus-DRT.html')


def Lotus_DCH(request):    
    return render(request , 'pages/Lotus-DCH.html')

def Lotus_DIP(request):    
    return render(request , 'pages/Lotus-DIP.html')


def Rose_DIP(request):    
    return render(request , 'pages/Rose-DIP.html')

def Lily_DIP(request):    
    return render(request , 'pages/Lily-DIP.html')

def Orchid_DIP(request):    
    return render(request , 'pages/Orchid-DIP.html')


def Rose_DLP(request):    
    return render(request , 'pages/Rose-DLP.html')