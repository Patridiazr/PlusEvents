from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.urls import path,include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'usuario', views.UsuarioViewSet)

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('formulario/',views.formulario,name='formulario'),
    path('formulario/crear_U',views.crear_U, name="crear_U"),
    path('administrador/',views.administrador,name='administrador'),
    path('calendario/',views.calendario,name='calendario'), 
    path('productos/',views.productos,name='productos'),
    path('contacto/',views.contacto,name='contacto'),
    path('login/iniciar', views.login_iniciar, name="iniciar"),    
    path('cerrarsesion', views.cerrar_session, name="cerrar_session"),
    path('api/', include(router.urls)),  
]