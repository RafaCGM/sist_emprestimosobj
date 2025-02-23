from django.urls import path
from .views import *

urlpatterns = [

    # USUARIO/AUTENTICAÇÃO EXPRESS
    path('login_express/', view_login_express, name='login_express'),
    path('registro_express/', view_registro_express, name='registro_express'),

]