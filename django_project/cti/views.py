from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from django.db.models import Count
from .forms import UploadFileForm, EditProfileForm, AddressForm, StatisticsForm
from cti.models import IP, Log_line
from .models import Apache_log
from .log_analyzer import analyze
from cti.neo4j.neo4j_classes import create_node, get_count_of_ip, get_Top_countries_by_ip, get_by_ip, get_by_country_code, get_by_city, get_by_org, get_by_region, get_by_timezone, get_by_postal, get_nodes, get_requests_for_ip, get_ips_with_request_method
from django.urls import reverse
from django.template.loader import get_template
from .pdf_generator import render_to_pdf

from cti.serializers import UserSerializer, GroupSerializer, ApacheLogSerializer

from rest_framework import viewsets, mixins, permissions, status, views
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework.response import Response

import threading
import os

# Testing rest api

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def current_user(request):
    user_id = request._user._wrapped.id
    user = User.objects.get(pk=user_id)
    print(vars(user))
    serializer_class = UserSerializer(user, context={'request': request})
    print(vars(serializer_class))

    return Response(serializer_class.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class ApacheLogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows files to be viewed or edited.
    """
    queryset = Apache_log.objects.all()
    serializer_class = ApacheLogSerializer
    http_method_names = ['get']
    permission_classes = [permissions.IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')
class FileUploadView(views.APIView):
    #permission_classes = [permissions.IsAuthenticated]

    #TODO: ovo ne mogu testirati bez Angulara

    parser_classes = [MultiPartParser]
    @csrf_exempt
    def post(self, request, format=None):
        file = request.FILES['file']
        server_name = request.data['servername']

        server_data = {'server_name': str(server_name), 'file_name': str(file)}

        # save the file
        instance = Apache_log(log_file=request.FILES['file'])
        instance.analyzed = False
        instance.save()

        #start analyzing
        analyzeThread = threading.Thread(target=analyze, args=(instance.log_file, server_data))
        analyzeThread.start()

        return Response(status=204)

class IPView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        ip_list = ''
        print(ip_list)
        return Response(ip_list)




# TEST IMPORTS
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat

@login_required
def home(request):
    return render(request, 'cti/home.html')


def upload(request):
    if request.method == 'POST':

        form = UploadFileForm(request.POST, request.FILES)
        #TODO: 
        #   Check if file is empty DONE
        #   Check if file isn't too big in size DONE
        #   Check if file is in right format DONE
        
        if form.is_valid():
            #PROVJERA FILE TYPE-A: PRIHVAĆAMO SAMO TEXT FILE I LOG FILE
            
            server_name = form['servername'].value()
            file = request.FILES['file']
            print(str(file.content_type))
            #print('^^^^^OVO JE FILE TYPE ^^^^^^^')

            if file.content_type == 'application/octet-stream' or file.content_type == 'text/plain':
                #TODO: FIND A PLACE FOR MAX SIZE VARIABLE (DECIDE MAX SIZE TOO)
                Num_of_MBs = 40
                MaxsizeinMBs= 1024*1024*Num_of_MBs

                if file.size < MaxsizeinMBs:

                    #server_data = {'server_name': str(server_name), 'file_name': str(file)}
                    server_data = {'server_name': str(server_name)}
                    instance = Apache_log(log_file=request.FILES['file'])
                    instance.analyzed = False
                    #print("instance")
                    #print(instance.log_file)
                    #print(instance.analyzed)
                    instance.save()
                    analyzeThread = threading.Thread(target=analyze, args=(instance.log_file, server_data))
                    analyzeThread.start()

                    messages.success(request, 'File is saved.')
                else:
                    messages.warning(request,'File is too big! Allowed size is '+str(Num_of_MBs)+'MBs, your file is: '+str(file.size//(1024*1024))+'MBs.')
                    form = UploadFileForm()
                
            else:
                messages.warning(request, 'File is not an apache log or a text file!')
                

                form = UploadFileForm()
                #print(file)
                #print(file.values)
                #print(vars(file))
                #print(file.size)
        else:   #One or more file upload checks was not satisfied
            
            #   Check if file is empty!
            #print(str(form.errors))
            if form.has_error('file'):
                messages.warning(request,'File is empty!')
            
    else:
        form = UploadFileForm()
    return render(request, 'cti/home.html', {'form': form})

