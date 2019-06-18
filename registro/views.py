from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Usuario, Servicio

#import de api
from rest_framework import viewsets
from .serializer import UsuarioSerializer
from .serializer import ServicioSerializer


# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    return render (request,'login.html',{})
def formulario(request):
    return render(request, 'formulario.html', {})
def administrador(request):
    usuario = Usuario.objects.all()
    servicio = Servicio.objects.all()
    contexto = {'usuario':usuario,'servicio':servicio}
    return render(request, 'administrador.html',contexto)
def contacto(request):
    return render(request, 'contacto.html', {})
def productos(request):
    servicio = Servicio.objects.all()
    contexto = {'servicio':servicio}
    return render(request, 'productos.html',contexto)
def calendario(request):
    return render(request, 'calendario.html', {})
def regservicio(request):
    return render(request, 'regservicio.html',)
    

#Crear Usuarios
def crear_U(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    usuario = Usuario(username=username, password=password)
    usu = User(username=username, password=password)
    usuario.save()
    usu.save()
    return redirect('login')


#CREAR SERVICIOS
def crear_S(request):
    nombre = request.POST.get('nombre','')
    descripcion = request.POST.get('descripcion','')
    servicio = Servicio(nombre=nombre, descripcion=descripcion)
    servicio.save()
    # HttpResponse('<h4>Servicio agregado con exito</>')
    return redirect('regservicio')

#LOGIN
def login_iniciar(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto.");'+
                            ' window.location.href="/administrador/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); ' +
                            'window.location.href="/login/";</script>')

#Eliminar usuario
def eliminar_u(request,id_usu):
    u = Usuario.objects.get(id=id_usu)
    u.delete()
    return redirect('administrador')



def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto.");'+
                        ' window.location.href="/login/";</script>')

#Serialyzer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer