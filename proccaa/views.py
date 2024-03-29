from random import seed
from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from registration.models import Profile
from proccaa.models import FormPago, Informe, Usuario, Ver_informe

from xml.etree.ElementTree import QName
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import (
api_view, authentication_classes, permission_classes)
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
#from colaboradores.models import colaborador2, Asistencia2, Liquidaciones2
from django.db.models import Q
from registration.models import Profile

#------------------------------------------------------------#

def ccaa_main(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ccaa/ccaa_main.html'
    return render(request,template_name,{'profile':profile})

#----------------------Formulario------------------------#
@login_required
def new_formpag(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ccaa/formpag_add.html'
    return render(request,template_name,{'profile':profile})

@login_required
def new_form(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        carrera = request.POST.get('carrera')
        sede = request.POST.get('sede')
        nivel = request.POST.get('nivel')
        periodo = request.POST.get('periodo')
        año = str(request.POST.get('año'))
        reunion_1 = str(request.POST.get('reunion_1'))
        reunion_1_link = request.POST.get('reunion_1_link')
        reunion_2 = str(request.POST.get('reunion_2'))
        reunion_2_link = request.POST.get('reunion_2_link')
        reunion_3 = str(request.POST.get('reunion_3'))
        reunion_3_link = request.POST.get('reunion_3_link')
        if carrera == '' or sede == '' or nivel == '' or periodo == '' or año == '' or reunion_1 == '' or reunion_1_link == '' or reunion_2 == '' or reunion_2_link == '' or reunion_3 == '' or reunion_3_link == '':
            messages.add_message(request, messages.INFO, 'Debes ingresar toda la información')
            return redirect('new_formpag')
        else:
            pago_save= FormPago(
                carrera= carrera,
                sede = sede,
                nivel = nivel,
                periodo = periodo,
                año = año,
                reunion_1 = reunion_1,
                reunion_1_link = reunion_1_link,
                reunion_2 = reunion_2,
                reunion_2_link = reunion_2_link,
                reunion_3 = reunion_3,
                reunion_3_link = reunion_3_link,
                )
            pago_save.save()
        messages.add_message(request, messages.INFO, 'Orden ingresada con éxito')
        return redirect('ccaa_main')
    else:
        messages.add_message(request, messages.INFO, 'Error en el método de envío')
        return redirect('check_group_main')              

def ver_form_ant(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    form_data = FormPago.objects.all()
    template_name = 'ccaa/ver_form_ant/ver_inf_ant.html'
    return render(request,template_name,{'profile':profile, 'form_data':form_data})

def ver_form(request, id):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    form_data = FormPago.objects.get(pk=id)
    template_name = 'ccaa/ver_form_ant/ver_inf.html'
    return render(request,template_name,{'profile':profile, 'form_data':form_data})

def guardar_informe(request):
    if request.method == 'POST':
        metodologias = request.POST.get('metodologias')
        capacitaciones = request.POST.get('capacitaciones')
        actividades = request.POST.get('actividades')
        otros = request.POST.get('otros')
        objetivo = request.POST.get('objetivo')
        estrategia = request.POST.get('estrategia')
        respuesta2 = request.POST.get('respuesta2')
        respuesta3 = request.POST.get('respuesta3')
        respuesta4 = request.POST.get('respuesta4')

        if metodologias == '' or capacitaciones == '' or actividades == '' or otros == '':
            return redirect('ccaa_main')
        
        informe_save = Informe(
            metodologias =metodologias,
            capacitaciones = capacitaciones,
            actividades = actividades,
            otros = otros,
            objetivo= objetivo,
            estrategia= estrategia,
            respuesta2= respuesta2,
            respuesta3= respuesta3,
            respuesta4= respuesta4,
        )
        informe_save.save()
        return redirect('ccaa_main')

def informe_de_cierre(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'ccaa/crear_informe.html'
    return render(request,template_name,{'profile':profile})

'''class crear_informePDF(View):
    def get(self,request,*args,**kwargs):
        informes = Informe.objects.filter()
        data={
            'informes':informes
        }
        template_name = 'ccaa/crear_informe.html'
        pdf= renderizar_pdf(template_name,data)
        return HttpResponse(pdf, content_type='application/pdf')'''

def VerInforme(request):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    captura = Ver_informe.objects.all()
    template_name = 'ccaa/informes_anteriores.html'
    return render(request,template_name,{'profile':profile, 'captura':captura})

def VerInformeAnterior(request,id):
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    vinf = Ver_informe.objects.filter(verinforme=id)
    captura_data = Informe.objects.get(pk=1)
    template_name = 'ccaa/ver_informes_anteriores.html'
    return render(request,template_name,{'profile':profile, 'captura_data':captura_data})
