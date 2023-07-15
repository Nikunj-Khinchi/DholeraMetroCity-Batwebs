from django.urls import path


from . import views


app_name = 'ourProject'

urlpatterns = [
    
    path('' , views.project_5006 , name='index'),
    path('Live-Booking-Status-DMC-5006/' , views.project_5006 , name='Live-Booking-Status-DMC-5006'),
    path('Live-Booking-Status-DMC-5005/' , views.project_5005 , name='Live-Booking-Status-DMC-5005'),
    path('Live-Booking-Status-DMC-5004/' , views.project_5004 , name='Live-Booking-Status-DMC-5004'),
    path('Live-Booking-Status-DMC-5003/' , views.project_5003 , name='Live-Booking-Status-DMC-5003'),
    path('Live-Booking-Status-DMC-5002/' , views.project_5002 , name='Live-Booking-Status-DMC-5002'),
    path('Live-Booking-Status-DMC-5001/' , views.project_5001 , name='Live-Booking-Status-DMC-5001'),
    path('Live-Booking-Status-DMC-4/' , views.project_4, name='Live-Booking-Status-DMC-4'),
    path('Live-Booking-Status-DMC-3/' , views.project_3, name='Live-Booking-Status-DMC-3'),
    path('Live-Booking-Status-DMC-2/' , views.project_2, name='Live-Booking-Status-DMC-2'),
    path('Live-Booking-Status-DMC-1/' , views.project_1, name='Live-Booking-Status-DMC-1'),
    
    
    
    
   
]
