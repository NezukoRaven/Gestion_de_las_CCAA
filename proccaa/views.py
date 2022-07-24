from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
#from registration.models import Profile
from proccaa.models import Usuario

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

