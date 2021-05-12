from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cti-home'),
    path('upload/', views.upload, name='cti-upload'),
    path('user/me/', views.current_user, name='cti-current-user'),
    
]
