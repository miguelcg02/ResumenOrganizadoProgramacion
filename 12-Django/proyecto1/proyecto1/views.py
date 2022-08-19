from datetime import datetime
from django.http import HttpResponse #Importacion para los request
from django.shortcuts import render
import datetime

def saludo(request): #Primera vista, con un request en el primer parametro 
    return render(request, 'miplantilla.html', {"nombre":"Miguel", "apellido":"Calvache"} )

def despedida(request):
    return HttpResponse("Chao")

def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    return HttpResponse(f'fecha y hora actual: {fecha_actual}')

def calculaEdad(request,edad,agno):
    periodo=agno-2022
    edadFuruta=edad+periodo
    documento = f"En el año {agno} tendrás {edadFuruta} años"
    return HttpResponse(documento)