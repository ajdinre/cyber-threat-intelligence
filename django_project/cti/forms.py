from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile

CHOICES = [
    ('Country', 'Country'),
    ('City', 'City'),
    ('Region', 'Region'),
    ('Request method', 'Request method')
]

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

class AddressForm(forms.Form):
    address = forms.GenericIPAddressField(label='Address')

class StatisticsForm(forms.Form):
    parameter = forms.ChoiceField(label='Parameter', choices=CHOICES, widget=forms.Select())
    value = forms.CharField(label='Value')