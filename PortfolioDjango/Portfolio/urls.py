"""
URL configuration for Portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
#Traer, importar cada def
from Portfolio.views import * #si no va el nombre de cada vista
from . import views

urlpatterns = [
    path('admin/', admin.site.urls), #Nombre de la funcion del archivo views
    path('', index, name = 'index'),   #Colocada como vista principal, HOME. En name indico el html al que va linkeado
    path('nosotros', nosotros, name = 'nosotros'),
    path('nosotreees', include('Perfiles.urls')),
    path('registrarPerfil/', registrarPerfil),
    path('eliminarP/<int:id>', eliminarP),
    path('edicionP/<int:id>', edicionP),
    path('editarP', editarP),
    path('skills', skills, name = 'skills'),
    path('contacto', contacto, name = 'contacto')
]



