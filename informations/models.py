from django.db import models
from datetime import datetime

class Information(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='info_photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title