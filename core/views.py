from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required(login_url='/login/')
def evento (request, titulo_evento):
    try:
        eve = Evento.objects.get(titulo=titulo_evento)
        return HttpResponse(eve.local)
    except Evento.DoesNotExist:
        return HttpResponse('Não existe')

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")

        return redirect('/')

#    def index(request):
#    return redirect('/agenda/')
