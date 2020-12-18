from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from cti.models import IP
from .models import Apache_log
from .log_analyzer import analyze
import threading
import os 

@login_required
def home(request):
    return render(request, 'cti/home.html')

@login_required
def uploaded_files(request):
    file_list = Apache_log.objects.all()
    path="media"
    return render(request, 'cti/uploaded_files.html', {'files': file_list})

@login_required
def search_ip(request):
    query = request.GET.get('ip') 
    if (query != None):
        ips = IP.objects.filter(address__contains=query)
    else:
        ips = None

    path="search/ip"
    return render(request, 'cti/search_ips.html', {'ips': ips})


@login_required
def upload(request):
    if request.method == 'GET':
        return render(request, 'cti/upload.html')
    elif request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            instance = Apache_log(log_file=request.FILES['file'])
            instance.save()
            analyzeThread = threading.Thread(target=analyze, args=(instance.log_file,))
            analyzeThread.start()

            messages.success(request, 'File is saved.')
        else:
            messages.warning(request, 'An error has occured.')
    else:
        form = UploadFileForm()
    return render(request, 'cti/upload.html', {'form': form})
