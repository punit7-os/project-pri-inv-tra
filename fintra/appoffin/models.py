import datetime
from django.db import models
from django.utils import timezone
# Create your models here.
class Service(models.Model):
    service_title = models.CharField(max_length=100)
    service_desc = models.CharField(max_length=400)
    logos = models.ImageField(upload_to="finance/services_logos", default="")

    def __str__(self):
        return self.service_title
    
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    u_fname = models.CharField(max_length=23)
    u_lname = models.CharField(max_length=23)
    u_email = models.EmailField(unique=True, blank=False)
    u_mob = models.IntegerField()
    u_pass = models.CharField(max_length=23)    
    
    def __str__(self):
        return self.u_fname
