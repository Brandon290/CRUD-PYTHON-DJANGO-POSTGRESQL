from django.http import HttpResponse
from django.shortcuts import render
from django.http.request import QueryDict

from personas.models import Persona

# Create your views here.
def bienvenido(respuesta):
    return HttpResponse("hola mundo desde djnago")

def vistahtml(resquest):
    return render(resquest,'estudianteTdeA.html')

def admin(resquest):
    return render(resquest,'admin/')

def bienvenidohtml(request):
    no_persona_var = Persona.objects.count()
    personas = Persona.objects.all()
    DicMensajes={'msg1': 'Valor mensaje 1'}
    return render(request, 'estudianteTdeA.html', {'no_personas': no_persona_var,'personas':personas})

