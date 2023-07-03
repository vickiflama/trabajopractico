from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

def curso(request):
    fecha= datetime.datetime.now()
    return render(request,"curso.html",{"now":fecha})

def inicio(request):
    return render(request,'index.html',{'nombre':'Analia'})

def nosotros(request):
    return render(request,'nosotros.html')

def skills(request):
    return render(request,'skills.html')

def contacto(request):
    return render(request,'contacto.html')

def saludo(request):
    
    """nombre= "Juan"
    apellido= "Perez"
    fecha= datetime.datetime.now()
    lista=["Curso 1","Curso 2","Curso 3","Curso 4"]
    arch=open("C:/Users/Usuario/Documents/Python2023/trabajopractico-main/Portfolio/templates/plantilla.html")
    plt=Template(arch.read())
    arch.close()
    ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "now":fecha, "lista":lista})
    documento=plt.render(ctx)    """
    nombre= "Juan"
    apellido= "Perez"
    fecha= datetime.datetime.now()
    lista=["Curso 1","Curso 2","Curso 3","Curso 4"]
    return render(request,"plantilla.html",{"nombre_persona":nombre, "apellido_persona":apellido, "now":fecha, "lista":lista})

def saludo_html(request):
    documento="""<html><body><h1>Hola a todos!</h1><body></html>"""
    
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta luego!")

def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha: %s </h1><body></html>"""%fecha_actual
    return HttpResponse(documento)
