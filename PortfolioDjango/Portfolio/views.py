from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.template import loader
from django.shortcuts import render
from django.views.generic import TemplateView
import datetime

def inicio(request):
    return render(request,'index.html',{'nombre':'Analia'})

def nosotros(request):
    return render(request,'nosotros.html')

def skills(request):
    return render(request,'skills.html')

def contacto(request):
    return render(request,'contacto.html')

