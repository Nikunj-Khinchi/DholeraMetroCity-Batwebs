from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'pages/index.html')

def blog_2(request):
    return render(request , 'pages/blog-2.html')

def resale(request):
    return render(request , 'pages/resale.html')