from django.urls import path
from .views import *

urlpatterns = [
    path('', view_home, name='home'),
    path('login/', view_login, name='login'),

    path('perfil/', view_perfil, name='perfil')
    # path('exemplo/', view_Json, name='Json'),
]