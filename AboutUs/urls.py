from django.urls import path , include


from . import views 


app_name = 'AboutUs'

urlpatterns = [
    # path('', views.DholeraMetroCity , name='dholeraMetroCity'),
    path("__reload__/", include("django_browser_reload.urls")),
    
    path('' , views.about , name='about'),
    path('privacy/' , views.privacy, name='privacy'),
      path('site-map/' , views.sitemap, name='site-map'),
]