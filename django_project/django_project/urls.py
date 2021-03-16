"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from cti import views as cti_views
from rest_framework import routers



# django-rest-framework stuff
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view


router = routers.DefaultRouter()
router.register(r'users', cti_views.UserViewSet)
router.register(r'groups', cti_views.GroupViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cti.urls')),
    #path('home/', auth_views.LoginView.as_view(template_name='cti/home.html'), name='cti-home'),
    path('login/', auth_views.LoginView.as_view(template_name='cti/login.html'), name='cti-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cti/logout.html'), name='cti-logout'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger-ui/', TemplateView.as_view(template_name='cti/swagger-ui.html', extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),
    path('openapi/', get_schema_view(
        title="Cyber Threat Intelligence",
        description="Api documentation for CTI project.",
        version="0.1.0-alpha"
    ), name='openapi-schema')
]
