from django.db import models

# Create your models here.


class IP(models.Model):
    ip_adress = models.CharField(max_length=20)
