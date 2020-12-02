from django.shortcuts import render


def home(request):
    return render(request, 'cti/home.html')

def upload(request):
    return render(request, 'cti/upload.html')

