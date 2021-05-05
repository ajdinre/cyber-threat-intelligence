from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls import url

from rest_framework.schemas import get_schema_view
from rest_framework import routers
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from cti import views as cti_views

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




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
    #path('openapi/', get_schema_view(title="Cyber Threat Intelligence", description="Api documentation for CTI project.", version="0.1.0-alpha"), name='openapi-schema'),

    #drf-yasg
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),


    #REST
    path('log/upload', cti_views.FileUploadView.as_view()),
    path('ip', cti_views.IPView.as_view()),
    path('d3/links', cti_views.d3CreateLinks.as_view()),
    path('d3/nodes', cti_views.d3CreateNodes.as_view())


]
