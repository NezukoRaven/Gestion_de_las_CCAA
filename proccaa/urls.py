from django.urls import path
from proccaa import views


ccaa_urlpatterns = [
    path('ccaa_main/',views.ccaa_main,name="ccaa_main"),
    path('new_formpag/',views.new_formpag,name="new_formpag"), 
    path('new_form/',views.new_form,name="new_form"),  
]