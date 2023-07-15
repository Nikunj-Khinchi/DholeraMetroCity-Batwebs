from django.urls import path


from . import views


app_name = 'Contactus'

urlpatterns = [
    path("", views.index, name="index"),
    path("inquiry-now/", views.Inquiry, name="inquiry-now"),
    path('site-visit', views.Site_visit , name='site-visit'),
    path('NRI' , views.NRI , name='NRI'),
    path('Career' , views.Career , name='Career'),
    
 
]