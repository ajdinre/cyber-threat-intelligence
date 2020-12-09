from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from cti.models import IP

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def home(request):
    return render(request, 'cti/home.html')


@login_required
def upload(request):
    if request.method == 'GET':
        return render(request, 'cti/upload.html')
    elif request.method == 'POST':
        print(request)
        print(request.FILES)
        form = UploadFileForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            #handle_uploaded_file(request.FILES['file'])
            messages.success(request, 'File saved. (Treba implementirati funkciju koja sprema datoteku na file system)')  # <-
        else:
            messages.warning(request, 'Oops. Something went wrong, please try again.')
    else:
        form = UploadFileForm()
    return render(request, 'cti/upload.html', {'form': form})
