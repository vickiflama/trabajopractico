from django.contrib import admin
from .models import Perfil
# Register your models here.


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display=('id','nombre')
    list_display_links = ('nombre',)
#admin.site.register(Perfil)
#admin.site.register(Perfil, PerfilAdmin)