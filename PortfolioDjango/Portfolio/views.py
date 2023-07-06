from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.template import loader
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views.generic import ListView
from Perfiles.models import Perfil
import datetime

def index(request):
    return render(request,'index.html')

def nosotros(request):
    return render(request,'nosotros.html')

def nosotreees(request):
    #perfilesL = Perfil.objects.all().order_by('nombre')
    #return render(request,'nosotreees.html', {"perfiles": perfilesL})
    data = {
        'perfiles':'perfilesListados',
    }

    return render(request, 'nosotreees.html', data)

class PerfilListView(ListView):
    model = Perfil
    template_name = 'nosotreees.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        print(context)
        return context
    
def registrarPerfil(request):
    nombre = request.POST['nombreP']
    telefono = request.POST['telefonoP']
    email = request.POST['emailP']
    domicilio = request.POST['domicilioP']
    perfil = Perfil.objects.create(nombre=nombre, telefono=telefono, email=email, domicilio=domicilio)
    
    return redirect('registrarPerfil')
    
def eliminarP(request,id):
    perfil=Perfil.objects.get(id=id)
    perfil.delete()
    return redirect('/')

def edicionP(request,id):
    perfil=Perfil.objects.get(id=id)
    data = {
        'titulo' : 'Edicion de Perfil',
        'perfil' : Perfil
    }
    return render(request, 'editarP.html', data)
    
def skills(request):
    return render(request,'skills.html')

def contacto(request):
    return render(request,'contacto.html')

def editarP(request, id):
    id = int(request.POST['idPE'])
    nombre = request.POST['nombrePE']
    telefono = request.POST['telefonoPE']
    email = request.POST['emailPE']
    domicilio = request.POST['domicilioPE']
    
    perfil = Perfil.objects.get(id=id)
    perfil.nombre = nombre
    perfil.telefono = telefono
    perfil.email = email
    perfil.domicilio = domicilio
    perfil.save()
    return redirect('')

