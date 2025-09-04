from django.shortcuts import render, HttpResponse, redirect

from core.models import Evento

# Create your views here.

def evento (request, titulo_evento):
    try:
        eve = Evento.objects.get(titulo=titulo_evento)
        return HttpResponse(eve.local)
    except Evento.DoesNotExist:
        return HttpResponse('Não existe')

def lista_eventos(request):
    evento = Evento.objects.all
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)


#    def index(request):
#    return redirect('/agenda/')
