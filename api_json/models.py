from django.db import models

# Create your models here.
class Arduino(models.Model):
    id_arduino = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200)
    permiso = models.BooleanField(default=False )

    def __str__(self):
        return f"{self.name} - {self.id_arduino}"


'F1000000F1E30000F1E3A500F1E3A51B'