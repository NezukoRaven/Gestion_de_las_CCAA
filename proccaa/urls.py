from django.urls import path
from proccaa import views


ccaa_urlpatterns = [
    path('ccaa_main/',views.ccaa_main,name="ccaa_main"),
    path('new_formpag/',views.new_formpag,name="new_formpag"), 
    path('new_form/',views.new_form,name="new_form"),
    path('ver_form_ant/',views.ver_form_ant,name="ver_form_ant"),
    path('ver_form/<id>/',views.ver_form,name="ver_form"),
   # path('crear_informe/',views.crear_informePDF.as_view(),name="crear_informe"), En proceso - crea un pdf.
    path('guardar_informe/',views.guardar_informe,name="guardar_informe"),
    path('informe_de_cierre/',views.informe_de_cierre,name="informe_de_cierre"),
]