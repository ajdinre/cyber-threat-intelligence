from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from rest_framework.schemas import get_schema_view
from rest_framework import routers

from cti import views as cti_views

#This code generates a REST api
router = routers.DefaultRouter()
router.register(r'user', cti_views.UserViewSet)
router.register(r'group', cti_views.GroupViewSet)
router.register(r'log', cti_views.ApacheLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cti.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='cti/login.html'), name='cti-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='cti/logout.html'), name='cti-logout'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #Documentation
    path('swagger-ui/', TemplateView.as_view(template_name='cti/swagger-ui.html', extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),
    path('openapi/', get_schema_view(title="Cyber Threat Intelligence", description="Api documentation for CTI project.", version="0.1.0-alpha"), name='openapi-schema')
]
