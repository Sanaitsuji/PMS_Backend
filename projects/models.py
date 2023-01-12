from django.db import models
from users.models import User

STATE_CHOICES = [
    ('borrador', 'Borrador'),
    ('en_progreso', 'En Progreso'),
    ('finalizado', 'Finalizado'),
    ('cancelado', 'Cancelado'),
]

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    leader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    description = models.TextField()
    methodology = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)