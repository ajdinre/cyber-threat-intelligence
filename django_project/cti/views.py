from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from django.contrib import messages

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def home(request):
    return render(request, 'cti/home.html')


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
            messages.success(request, 'Datoteka je spremljena. (Treba implementirati funkciju koja sprema datoteku na file system)')  # <-
        else:
            messages.warning(request, 'Desila se greška molimo pokušaje ponovno.')
    else:
        form = UploadFileForm()
    return render(request, 'cti/upload.html', {'form': form})
