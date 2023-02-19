from django.db import models

# Create your models here.
class Arduino(models.Model):
    id_arduino = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    permiso = models.CharField(max_length=10)