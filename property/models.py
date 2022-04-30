from django.db import models


class Property(models.Model):
    location = models.CharField(max_length=70, blank=False, default='')
    latittude = models.DecimalField(max_digits=10,decimal_places=2,blank=False, default=0)
    longitude = models.DecimalField(max_digits=10,decimal_places=2,blank=False, default=0)
