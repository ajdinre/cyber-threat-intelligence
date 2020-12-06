from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.contrib import messages
from cti.models import IP
from .models import Apache_log
from .log_analyzer import analyze

def home(request):
    return render(request, 'cti/home.html')


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

def test_sql(request):
    ips = IP.objects.all
    return render(request, 'cti/test_sql.html', {'ips': ips})

