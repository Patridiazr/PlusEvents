from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request,'index.html')
def login(request):
    return render (request,'login.html',{})
def formulario(request):
    return render(request, 'formulario.html', {})



#LOGIN
def login_iniciar(request):
    username = request.POST.get('email', '')
    password = request.POST.get('contrasenia', '')
    user = authenticate(request, username=username, password=password)
    print(username, password)
    if user is not None:
        auth_login(request, user)
        return HttpResponse('<script>alert("Inicio de sesión correcto.");'+
                            ' window.location.href="/";</script>')
    else:
        return HttpResponse('<script>alert("Ocurrió un error, intenta nuevamente..."); ' +
                            'window.location.href="/login/";</script>')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required(login_url='/login/')
def cerrar_session(request):
    logout(request)
    return HttpResponse('<script>alert("Cierre de sesión correcto.");'+
                        ' window.location.href="/";</script>')