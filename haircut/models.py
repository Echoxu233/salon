from django.db import models

# Create your models here.
class Order(models.Model):
     barber = models.CharField(max_length=180, null=True, blank=True)
     customer = models.CharField(max_length=180, null=True, blank=True)
     time = models.CharField(max_length=180, null=True, blank=True)