from django.db import models

class Cliente(models.Model):
    
    sexo_choices = (('hombre','Hombre'),('mujer','Mujer'),('no','Prefiero no responder'))
    
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    sexo = models.CharField(max_length=30, choices=sexo_choices)
    email = models.EmailField(max_length=255)