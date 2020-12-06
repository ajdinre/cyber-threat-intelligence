from django.db import models

class IP(models.Model):
    address = models.CharField(max_length=39, null=True)
    hostname = models.CharField(max_length=64, null=True)
    city = models.CharField(max_length=64, null=True)
    region = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=32, null=True)
    countryname = models.CharField(max_length=64, null=True)
    org = models.CharField(max_length=256, null=True)
    postal = models.CharField(max_length=16, null=True)
    timezone = models.CharField(max_length=32, null=True)
    latitude = models.CharField(max_length=32, null=True)
    longitude = models.CharField(max_length=32, null=True)

class Apache_log(models.Model):
    log_file = models.FileField()