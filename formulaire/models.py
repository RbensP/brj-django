from django.db import models
from django.conf import settings
from datetime import datetime

class Formulaire(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    state = models.CharField(max_length=25)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    time_life = models.CharField(max_length=255)
    date_created = models.DateTimeField(default=datetime.now) 
    pdf = models.URLField(max_length=255, blank=True) 