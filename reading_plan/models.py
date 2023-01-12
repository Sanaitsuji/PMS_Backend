from django.db import models

def technologyFile(instance, filename):
    return '/'.join( ['reading_plan/technology_images', filename] )

# Create your models here.
class Technology(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    used_by = models.CharField(max_length=200)
    draw = models.ImageField(
        upload_to=technologyFile,
        max_length=254, blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

class CharacterHated(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class CharacterLoved(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UnimpressiveSections(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)