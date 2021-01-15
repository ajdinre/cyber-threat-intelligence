from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MinLengthValidator, int_list_validator


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
    created = models.DateTimeField(auto_now_add=True)
    analyzed = models.BooleanField(null=False, default=False)

class Server_attack(models.Model):
    server_name = models.CharField(max_length=32, null=False)
    filehash = models.CharField(max_length=64, null=False)

class Log_line(models.Model):
    ip_address = models.ForeignKey(
        IP, on_delete=models.CASCADE)
    timestamp = models.CharField(max_length=32, null=True) #treba stavit u timestamp a ne string
    requestMethod = models.CharField(max_length=7, null=True)
    path = models.CharField(max_length=512, null=True)
    httpVersion = models.CharField(max_length=32, null=True)
    response = models.CharField(max_length=32, null=True)
    sizeInBytes = models.CharField(max_length=32, null=True)


class UserProfile(models.Model):

    CONFIDENTIAL = 'CF'
    SECRET = 'S'
    TOP_SECRET = 'TS'

    SECURITY_LEVEL = (
        (CONFIDENTIAL, 'Confidential'),
        (SECRET, 'Secret'),
        (TOP_SECRET, 'Top Secret'),
    )
 
    security = models.CharField(
        max_length=2,
        choices=SECURITY_LEVEL,
        
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_image', blank=True)
    phone_no = models.CharField(max_length=13,
    validators=[int_list_validator(sep=''),MinLengthValidator(10),], 
    default='385')
    address = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=50, default='')
    employee_status = models.CharField(max_length=150, default='')
    
    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)