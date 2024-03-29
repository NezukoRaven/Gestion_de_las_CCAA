"""Gestion_de_las_CCAA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from proccaa.urls import ccaa_urlpatterns
from django.conf.urls.static import static
from core.urls import core_urlpatterns

urlpatterns = [
    path('',include(core_urlpatterns)),
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    path('ccaa_main/', include(ccaa_urlpatterns)),
    path('accounts/', include('django.contrib.auth.urls')),
]
