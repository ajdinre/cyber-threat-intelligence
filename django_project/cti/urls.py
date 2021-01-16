from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cti-home'),
    path('upload/', views.upload, name='cti-upload'),
    path('uploadedfiles/', views.uploaded_files, name='cti-uploaded-files'),
    path('search/ip/', views.search_ip, name='cti-search-ip'),
    path('profile/', views.view_profile, name='cti-profile'),
    path('settings/', views.settings, name='cti-settings'),
    path('password/', views.change_password, name='cti-changepassword'),
    path('report/', views.report, name='cti-report'),
    path('fileinfo/', views.file_info, name='cti-file-info'),
]
