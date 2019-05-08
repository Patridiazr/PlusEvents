from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('formulario/',views.formulario,name='formulario'),
    path('login/iniciar', views.login_iniciar, name="iniciar"),     
    path('cerrarsesion', views.cerrar_session, name="cerrar_session"),
]