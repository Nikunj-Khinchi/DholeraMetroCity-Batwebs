from django.urls import path


from . import views


app_name = 'core'

urlpatterns = [
    path('', views.DholeraMetroCity , name='dholeraMetroCity'),
    # path('AboutUs/' , views.Aboutus , name='aboutUs'),
    # path('Download/' , views.Download , name='download'),
    # path('Download/Brochure-DMC-5005/', views.Brochure_DMC_5005, name='Brochure-DMC-5005'),
    path('RERA/' , views.RERA , name='RERA'),
    path('Project-Land/'  , views.Project_Land , name='Project-Land'),
    path('Terms&Conditions/' , views.termConditions , name='Terms&Conditions'),
    path('Shipping-Policy/' , views.shipping , name='Shipping-Policy'),
    path('refund-cancellation-policy/' , views.RCpolicy , name='refund-cancellation-policy'),
    
      
]