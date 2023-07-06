from django.db import models

# Create your models here.

class Perfil(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField(max_length=40)
    domicilio = models.CharField(max_length=100)
    
    
    def __str__(self):
        texto = "({0}) ({1}) ({2}) ({3})"
        return texto.format(self.nombre, self.telefono, self.email, self.domicilio)