from django.urls import path


from . import views


app_name = 'NewsApps'

urlpatterns = [
    path('' , views.index , name='index')
]
