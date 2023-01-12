from django.db import models
from projects.models import Project
from users.models import User

STATE_CHOICES = [
    ("borrador", "Borrador"),
    ('asignada', 'Asignada'),
    ('suspendida', 'Suspendida'),
    ('finalizada', 'Finalizada'),
    ('cancelada', 'Cancelada'),
]

# Create your models here.
class UserStories(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True)
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    description = models.TextField()
    weight = models.IntegerField()
    estimated_time = models.FloatField()
    total_time = models.FloatField()
    sprint = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)