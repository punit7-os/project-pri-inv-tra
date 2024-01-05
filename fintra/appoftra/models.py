from django.db import models

# Create your models here.
class Package(models.Model):
    package_title = models.CharField(max_length=100)
    package_desc = models.CharField(max_length=400)
    logos = models.ImageField(upload_to="packages/packages_logos", default="")

    def __str__(self):
        return self.package_title