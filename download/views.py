from django.shortcuts import render
from django.http import FileResponse, Http404
from django.conf import settings
import os
# Create your views here.


def Download(request):

    return render(request, "download-pages/Download.html")


def Brochure_DMC_5005(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-5005.pdf')
        # Specify the desired title here
        file_name = 'Brochure-Dholera-Metro-City-5005.pdf'

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_5004(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-5004.pdf')
        # Specify the desired title here
        file_name = 'Brochure-Dholera-Metro-City-5004.pdf'

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_5003(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-5003.pdf')
        # Specify the desired title here
        file_name = 'Brochure-Dholera-Metro-City-5003.pdf'

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_5002(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-5002.pdf')
        # Specify the desired title here
        file_name = 'Brochure-Dholera-Metro-City-5002.pdf'

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_5001(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-5001.pdf')
        # Specify the desired title here
        file_name = 'Brochure-Dholera-Metro-City-5001.pdf'

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_4(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-4.pdf')
        file_name = 'Brochure-Dholera-Metro-City-4.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_3(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-3.pdf')
        file_name = 'Brochure-Dholera-Metro-City-3.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_2(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-2.pdf')
        file_name = 'Brochure-Dholera-Metro-City-2.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Brochure_DMC_1(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/brochures/Brochure-Dholera-Metro-City-1.pdf')
        file_name = 'Brochure-Dholera-Metro-City-1.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


# govt circular


def Govt_Circular_Airport(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/govt-circular/Govt_Circular_for_Airport.pdf')
        file_name = 'Govt_Circular_for_Airport.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Govt_Circular_Dholera(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/govt-circular/Govt_Circular_for_Dholera_SIR.pdf')
        file_name = 'Govt_Circular_for_Dholera_SIR.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Dholera_SIR_RDA_Notification(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/govt-circular/Dholera_SIR_RDA_Notification.pdf')
        file_name = 'Dholera_SIR_RDA_Notification.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


# final development plans

def Final_Proposed_Land_Use_Plan(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/final-development-plan/Final_Proposed_Land_Use_Plan.pdf')
        file_name = 'Final_Proposed_Land_Use_Plan.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DP_Report_1(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/final-development-plan/DP_Report_1.pdf')
        file_name = 'DP_Report_1.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DP_Report_2_GDCR(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/final-development-plan/DP_Report_2_GDCR.pdf')
        file_name = 'DP_Report_2_GDCR.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DP_Sanction_Notification(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/final-development-plan/DP_Sanction_Notification.pdf')
        file_name = 'DP_Sanction_Notification.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def General_Development_Control_Regulations(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/final-development-plan/General_Development_Control_Regulations.pdf')
        # Specify the desired title here
        file_name = 'General_Development_Control_Regulations.pdf'

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def GDCR_Gujarati(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/final-development-plan/GDCR_Gujarati.pdf')
        file_name = 'GDCR_Gujarati.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DP_Gujarati_04062012(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/final-development-plan/DP_Gujarati_04062012.pdf')
        file_name = 'DP_Gujarati_04062012.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


# Draft TP Scheme 3 & 4

def Publication_in_Gazette(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/Publication-Gazette-TPS-3-4.pdf')
        file_name = 'Publication-Gazette-TPS-3-4.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Plan_2_OP_Plan_DTPS_3(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS-3-OP-PLAN.pdf')
        file_name = 'DTPS-3-OP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Plan_3_OP_FP_Plan_DTPS_3(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS-3-OP-FP-PLAN.pdf')
        file_name = 'DTPS-3-OP-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Plan_3_FP_Plan_DTPS_4(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS-3-FP-PLAN.pdf')
        file_name = 'DTPS-3-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Plan_4_FP_Plan_DTPS_3(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS-4-FP-PLAN.pdf')
        file_name = 'DTPS-4-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Plan_4_OP_FP_Plan_DTPS_4(request):

    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS-4-OP-FP-PLAN.pdf')
        file_name = 'DTPS-4-OP-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_3_4_Notification(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS_3-4_Notification.pdf')
        file_name = 'DTPS_3-4_Notification.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_3_INDEX_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS-3_INDEX-PLAN.pdf')
        file_name = 'DTPS-3_INDEX-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_4_INDEX_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/draft-TP-scheme-3&4/DTPS-4_INDEX-PLAN.pdf')
        file_name = 'DTPS-4_INDEX-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


# Draft TP Scheme 5 & 6


def DTPS_5_OP_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS-5-OP-PLAN.pdf')
        file_name = 'DTPS-5-OP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_5_OP_FP_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS-5-OP-FP-PLAN.pdf')
        file_name = 'DTPS-5-OP-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_5_FP_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS-5-FP-PLAN.pdf')
        file_name = 'DTPS-5-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_6_OP_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS-6-OP-PLAN.pdf')
        file_name = 'DTPS-6-OP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_6_FP_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS-6-FP-PLAN.pdf')
        file_name = 'DTPS-6-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_6_OP_FP_PLAN(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS-6-OP-FP-PLAN.pdf')
        file_name = 'DTPS-6-OP-FP-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_5_6_Notification(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS_5-6_Notification.pdf')
        file_name = 'DTPS_5-6_Notification.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_5_Index_Plan(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS_5_Index_Plan.pdf')
        file_name = 'DTPS_5_Index_Plan.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def DTPS_6_Index_Plan(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Draft-TP-Scheme-5&6/DTPS-6_INDEX-PLAN.pdf')
        file_name = 'DTPS-6_INDEX-PLAN.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


# Sactioned DTPS 1-2-3


def OP_FP_Plan_DTPS_1(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/OP-FP-Plan-DTPS-1.pdf')
        file_name = 'OP-FP-Plan-DTPS-1.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def FP_Plan_DTPS_1(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/FP-Plan-DTPS-1.pdf')
        file_name = 'FP-Plan-DTPS-1.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Notification_DTPS_1(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/Notification-DTPS-1.pdf')
        file_name = 'Notification-DTPS-1.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def OP_FP_Plan_DTPS_2(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/OP-FP-Plan-DTPS-2.pdf')
        file_name = 'OP-FP-Plan-DTPS-2.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def FP_Plan_DTPS_2(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/FP-Plan-DTPS-2.pdf')
        file_name = 'FP-Plan-DTPS-2.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Notification_DTPS_2(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/Notification-DTPS-2.pdf')
        file_name = 'Notification-DTPS-2.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def OP_FP_Plan_DTPS_3(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/OP-FP-Plan-DTPS-3.pdf')
        file_name = 'OP-FP-Plan-DTPS-3.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def FP_Plan_DTPS_3(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/FP-Plan-DTPS-3.pdf')
        file_name = 'FP-Plan-DTPS-3.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


def Notification_DTPS_3(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/Sactioned-DTPS-1-2-3/Notification-DTPS-3.pdf')
        file_name = 'Notification-DTPS-3.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404


# SIR ACT 2009

def SIR_ACT_2009(request):
    try:
        file_path = os.path.join(
            settings.BASE_DIR, 'download/static/pdf/SIR-Act-2009/SIR_Act_2009.pdf')
        file_name = 'SIR_Act_2009.pdf'  # Specify the desired title here

        response = FileResponse(open(file_path, 'rb'),
                                content_type='application/pdf')
        response['Content-Disposition'] = f'filename="{file_name}"'
        return response
    except FileNotFoundError:
        raise Http404
