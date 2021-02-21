from django.db import models
from django.utils import timezone

# Create your models here.
class Reklamation(models.Model):
    reklamation_name = models.CharField(max_length=64)
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.firma_name