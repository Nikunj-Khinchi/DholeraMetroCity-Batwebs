from django.urls import path


from . import views


app_name = 'PhotoGallery'

urlpatterns = [
    
    path('' , views.index , name='index'),
    path('Investor-Visit/' , views.Investors , name='Investor-Visit'),
    path('Investor-Feedback/' , views.Feedback , name='Investor-Feedback'),
    path('DMC-Site-Progress/' , views.DMCSite , name='DMC-Site-Progress'),
    path('photo-gallery-Dholera-Metro-City/' , views.Dholera_images , name='photo-gallery-Dholera-Metro-City'),
    path('photo-gallery-summit-2017/' , views.Summit_2017 , name='photo-gallery-summit-2017'),
    path('photo-gallery-summit-2018/' , views.Summit_2018 , name='photo-gallery-summit-2018'),
    path('Video-Gallery/' , views.VideoGallery , name='Video-Gallery'),
]
