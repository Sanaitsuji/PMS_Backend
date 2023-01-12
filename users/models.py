from django.db import models

STATE_CHOICES = [
    ('activo', 'Activo'),
    ('inactivo', 'Inactivo'),
]

# Create your models here.
#Parametrización de los campos del formulario.
class User(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=100)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)