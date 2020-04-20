from django.db import models
from django.conf import settings

class JourRendezVous(models.Model):
    number = models.IntegerField()
    day = models.DateField() 
    
class RendezVous(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    jour = models.ForeignKey(JourRendezVous, on_delete=models.CASCADE)