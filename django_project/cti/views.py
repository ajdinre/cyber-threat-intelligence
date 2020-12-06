from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from cti.models import IP
from .models import Apache_log
from .log_analyzer import analyze

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
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Apache_log(log_file=request.FILES['file'])
            instance.save()
            print(instance.log_file) #ime fajla
            analyze(instance.log_file)

            messages.success(request, 'File is saved.')
        else:
            messages.warning(request, 'An error has occured.')
    else:
        form = UploadFileForm()
    return render(request, 'cti/upload.html', {'form': form})
