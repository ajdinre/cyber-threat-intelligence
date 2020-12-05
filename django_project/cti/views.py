from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def home(request):
    return render(request, 'cti/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account was created! You can now log in!')
            return redirect('cti-login')
    else:
        form = UserRegisterForm()
    return render(request, 'cti/register.html', {'form': form})


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
