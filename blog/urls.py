from django.urls import path


from . import views


app_name = 'blog'

urlpatterns = [
    path("", views.index , name='index'),
    path('blog-2/' , views.blog_2 , name='blog-2'),
    path('resale-Booking-Status-Dholera-Metro-City/' , views.resale , name='resale-Booking-Status-Dholera-Metro-City')
 
]
