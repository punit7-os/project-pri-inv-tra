import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_desc = models.CharField(max_length=400)

    def __str__(self):
        return self.service_title
