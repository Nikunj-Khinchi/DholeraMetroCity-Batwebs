from django.urls import path


from . import views


app_name = 'consultancy'

urlpatterns = [
    path("", views.index, name="index"),
    path("Live-Booking-Status-lily-dholera-residential-township", views.Lily_DRT , name='Live-Booking-Status-lily-dholera-residential-township'),
    path("Live-Booking-Status-rose-dholera-residential-township", views.Rose_DRT , name='Live-Booking-Status-rose-dholera-residential-township'),
    path("Live-Booking-Status-lotus-dholera-residential-township", views.Lotus_DRT , name='Live-Booking-Status-lotus-dholera-residential-township'),
    path("Live-Booking-Status-lotus-commercial-hub", views.Lotus_DCH , name='Live-Booking-Status-lotus-commercial-hub'),
    path("Live-Booking-Status-lotus-industrial-park", views.Lotus_DIP , name='Live-Booking-Status-lotus-industrial-park'),
    path("Live-Booking-Status-rose-industrial-park", views.Rose_DIP , name='Live-Booking-Status-rose-industrial-park'),
    path("Live-Booking-Status-lily-industrial-park", views.Lily_DIP , name='Live-Booking-Status-lily-industrial-park'),
    path("Live-Booking-Status-orchid-industrial-park", views.Orchid_DIP , name='Live-Booking-Status-orchid-industrial-park'),
    path("Live-Booking-Status-rose-logistics-park", views.Rose_DLP , name='Live-Booking-Status-rose-logistics-park'),
   
 
]
