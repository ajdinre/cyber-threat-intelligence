from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cti-home'),
    path('upload/', views.upload, name='cti-upload'),
    path('test_sql/', views.test_sql, name='cti-test-sql')
]
