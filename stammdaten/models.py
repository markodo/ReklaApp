from django.db import models
from django.utils import timezone

# Create your models here.
class Firma(models.Model):
    firma_name = models.CharField(max_length=64)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.firma_name

class Kunde(models.Model):
    kunde_name = models.Charfield(max_length=64)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.kunde_name

class Lager(models.Model):
    kunde_name = models.ForeignKey(Kunde, on_delete=models.CASCADE)
    lager_name = models.Charfield(max_length=64)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.lager_name