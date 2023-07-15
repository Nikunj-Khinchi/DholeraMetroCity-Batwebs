from django.urls import path


from . import views


app_name = 'download'

urlpatterns = [
    # path('', views.DholeraMetroCity , name='dholeraMetroCity'),
    # path('AboutUs/' , views.Aboutus , name='aboutUs'),
    path('', views.Download, name='download'),
    path('Brochure-DMC-5005/', views.Brochure_DMC_5005, name='Brochure-DMC-5005'),
    path('Brochure-DMC-5004/', views.Brochure_DMC_5004, name='Brochure-DMC-5004'),
    path('Brochure-DMC-5003/', views.Brochure_DMC_5003, name='Brochure-DMC-5003'),
    path('Brochure-DMC-5002/', views.Brochure_DMC_5002, name='Brochure-DMC-5002'),
    path('Brochure-DMC-5001/', views.Brochure_DMC_5001, name='Brochure-DMC-5001'),
    path('Brochure-DMC-4/', views.Brochure_DMC_4, name='Brochure-DMC-4'),
    path('Brochure-DMC-3/', views.Brochure_DMC_3, name='Brochure-DMC-3'),
    path('Brochure-DMC-2/', views.Brochure_DMC_2, name='Brochure-DMC-2'),
    path('Brochure-DMC-1/', views.Brochure_DMC_1, name='Brochure-DMC-1'),



    #   govt-circular
    path('Govt-Circular-for-Airport/', views.Govt_Circular_Airport,
         name='Govt-Circular-for-Airport'),

    path('Govt-Circular-for-Dholera_SIR/', views.Govt_Circular_Dholera,
         name='Govt-Circular-for-Dholera'),

    path('Dholera-SIR-RDA-Notification/', views.Dholera_SIR_RDA_Notification,
         name='Dholera-SIR-RDA-Notification'),

    # Final development Plan

    path('Final-Proposed-Land-Use-Plan/', views.Final_Proposed_Land_Use_Plan,
         name='Final-Proposed-Land-Use-Plan'),


    path('Dp-Report-1/', views.DP_Report_1, name='Dp-Report-1'),

    path('DP-Report-2-GDCR/', views.DP_Report_2_GDCR, name='DP-Report-2-GDCR'),

    path('DP-Sanction-Notification/', views.DP_Sanction_Notification,
         name='DP-Sanction-Notification'),

    path('General-Development-Control-Regulations/', views.General_Development_Control_Regulations,
         name='General-Development-Control-Regulations'),

    path('GDCR-Gujarati/', views.GDCR_Gujarati,
         name='GDCR-Gujarati'),

    path('DP-Gujarati-04062012/', views.DP_Gujarati_04062012,
         name='DP-Gujarati-04062012'),

    # Draft TP schema 3 & 4

    path('Publication-in-Gazette/', views.Publication_in_Gazette,
         name='Publication-in-Gazette'),

    path('Plan-2-OP-DTPS-3/', views.Plan_2_OP_Plan_DTPS_3, name='Plan-2-OP-DTPS-3'),

    path('Plan-3-OP-FP-Plan-DTPS-3', views.Plan_3_OP_FP_Plan_DTPS_3,
         name='Plan-3-OP-FP-Plan-DTPS-3'),

    path('Plan-3-FP-Plan-DTPS-4', views.Plan_3_FP_Plan_DTPS_4,
         name='Plan-3-FP-Plan-DTPS-4'),

    path('Plan-4-FP-Plan-DTPS-3', views.Plan_4_FP_Plan_DTPS_3,
         name='Plan-4-FP-Plan-DTPS-3'),


    path('Plan-4_OP-FP-Plan-DTPS-4', views.Plan_4_OP_FP_Plan_DTPS_4,
         name='Plan-4_OP-FP-Plan-DTPS-4'),

    path('DTPS-3-4-Notification', views.DTPS_3_4_Notification,
         name='DTPS-3-4-Notification'),

    path('DTPS-3-INDEX-PLAN', views.DTPS_3_INDEX_PLAN, name='DTPS-3-INDEX-PLAN'),

    path('DTPS-4-INDEX-PLAN', views.DTPS_4_INDEX_PLAN, name='DTPS-4-INDEX-PLAN'),


    # Draft TP Scheme 5 & 6

    path('DTPS-5-OP-Plan', views.DTPS_5_OP_PLAN, name='DTPS-5-OP-Plan'),


    path('DTPS-5-OP-FP-Plan', views.DTPS_5_OP_FP_PLAN, name='DTPS-5-OP-FP-Plan'),



    path('DTPS-5-FP-Plan', views.DTPS_5_FP_PLAN, name='DTPS-5-FP-Plan'),



    path('DTPS-6-OP-Plan', views.DTPS_6_OP_PLAN, name='DTPS-6-OP-Plan'),


    path('DTPS-6-FP-Plan', views.DTPS_6_FP_PLAN, name='DTPS-6-FP-Plan'),



    path('DTPS-6-OP-FP-Plan', views.DTPS_6_OP_FP_PLAN, name='DTPS-6-OP-FP-Plan'),


    path('DTPS-5-6-Notification', views.DTPS_5_6_Notification,
         name='DTPS-5-6-Notification'),


    path('DTPS-5-Index-Plan', views.DTPS_5_Index_Plan, name='DTPS-5-Index-Plan'),


    path('DTPS-6-Index-Plan', views.DTPS_6_Index_Plan, name='DTPS-6-Index-Plan'),



    # Sactioned DTPS 1-2-3


    path('OP-FP-Plan-DTPS-1', views.OP_FP_Plan_DTPS_1, name='OP-FP-Plan-DTPS-1'),


    path('OP-FP-Plan-DTPS-2', views.OP_FP_Plan_DTPS_2, name='OP-FP-Plan-DTPS-2'),

    path('OP-FP-Plan-DTPS-3', views.OP_FP_Plan_DTPS_3, name='OP-FP-Plan-DTPS-3'),

    path('FP-Plan-DTPS-1', views.FP_Plan_DTPS_1, name='FP-Plan-DTPS-1'),


    path('FP-Plan-DTPS-2', views.FP_Plan_DTPS_2, name='FP-Plan-DTPS-2'),

    path('FP-Plan-DTPS-3', views.FP_Plan_DTPS_3, name='FP-Plan-DTPS-3'),



    path('Notification-DTPS-1', views.Notification_DTPS_1,
         name='Notification-DTPS-1'),

    path('Notification-DTPS-2', views.Notification_DTPS_2,
         name='Notification-DTPS-2'),


    path('Notification-DTPS-3', views.Notification_DTPS_3,
         name='Notification-DTPS-3'),
    
    
    # Sir act 2009
    
    path('SIR-ACT-2009' , views.SIR_ACT_2009 , name='SIR-ACT-2009'),

]
