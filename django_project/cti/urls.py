from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cti-home'),
    path('upload/', views.upload, name='cti-upload'),
    path('uploadedfiles/', views.uploaded_files, name='cti-uploaded-files'),
]
