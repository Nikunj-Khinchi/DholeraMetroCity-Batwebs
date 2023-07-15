from django.urls import path , include


from . import views 


app_name = 'DholeraSirPages'

urlpatterns = [
    path('', views.index , name='index'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('Connectivtiy/' , views.connectivity , name='Connectivity'),
    path('Connectivtiy/<str:image_name>.jpg', views.image_view, name='image_view'),
    path('Dholera-Sir-Projects' , views.projects , name='Dholera-Sir-Projects'),
    path("Dholera-International-Airport/", views.AirPort, name="Dholera-International-Airport"),
    path('Dholera-solar-power-plant/' , views.Solar_plant , name='Dholera-solar-power-plant'),
    path('Dholera-metro-rail-project/' , views.Metro , name='Dholera-metro-rail-project'),
    path('ahmedabad-dholera-six-lane-expressway/' , views.Express , name='ahmedabad-dholera-six-lane-expressway'),
    path('Mega-Projects' , views.MegaProjects , name='Mega-Projects'),
    path('Dholera-Sir-Work-Progress' , views.PhotoGallery , name='Dholera-Sir-Work-Progress'),
    path('Dholera-sir-projects-update', views.RuCoProjects , name='Dholera-sir-projects-update' ),
    path('Dholera-Sir-Current-Status', views.CurrentStatus , name='Dholera-Sir-Current-Status' ),
    path('DMIC-Projects' , views.DMIC , name='DMIC-Projects'),
    path('DFC-Projects' , views.DFC , name='DFC-Projects'),
    path('GIDB' , views.GIDB , name='GIDB'),
    path('D-RDA' , views.DRDA , name='D-RDA')
    
]