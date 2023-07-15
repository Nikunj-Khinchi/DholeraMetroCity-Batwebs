from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request , "pages/aboutUs.html")

def privacy(request):
    return render(request , "pages/privacyPolicy.html")

def sitemap(request):
    return render(request , "pages\Sitemap.html")