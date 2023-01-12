from django.db import models
from user_stories.models import UserStories
from users.models import User

STATE_CHOICES = [
    ("borrador", "Borrador"),
    ('asignada', 'Asignada'),
    ('suspendida', 'Suspendida'),
    ('finalizada', 'Finalizada'),
    ('cancelada', 'Cancelada'),
]

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    user_story = models.ForeignKey(UserStories, on_delete=models.SET_NULL, null=True)
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    description = models.TextField()
    invested_time = models.FloatField()
    estimated_time = models.FloatField()
    remaining_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)