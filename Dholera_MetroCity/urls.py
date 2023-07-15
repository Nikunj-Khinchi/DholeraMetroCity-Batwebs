"""
URL configuration for Dholera_MetroCity project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path , include





urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
     path("" , include('core.urls')),
     path("about us/" , include('AboutUs.urls')),
    path('Download/' , include('download.urls')),
    path('Dholera-Sir/' , include('DholeraSirPages.urls')),
    path('News/' , include('NewsApps.urls')),
    path('Photo-Gallery/' , include('PhotoGallery.urls')),
    path('Blogs/', include("blog.urls")),
    path('OurProjects/' , include('ourProject.urls')),
    path('Consultancy/' , include('consultancy.urls')),
    path('Contact-Us/' , include('Contactus.urls')),
    #  path("about/" , include('core.urls'))
]
