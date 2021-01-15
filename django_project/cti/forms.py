from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile

class UploadFileForm(forms.Form):
    #title = forms.CharField(max_length=50)
    file = forms.FileField()


class EditProfileForm(UserChangeForm):
    
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
        )
