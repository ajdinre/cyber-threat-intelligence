from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Count
from .forms import UploadFileForm, EditProfileForm, AddressForm, StatisticsForm
from cti.models import IP
from cti.models import Log_line
from cti.neo4j.neo4j_classes import create_node
from .models import Apache_log
from .log_analyzer import analyze
from  cti.neo4j.neo4j_classes import get_count_of_ip
from  cti.neo4j.neo4j_classes import get_Top_countries_by_ip
from  cti.neo4j.neo4j_classes import get_by_ip
from  cti.neo4j.neo4j_classes import get_by_country_code
# ne postoji više from  cti.neo4j.neo4j_classes import get_by_country_name
from  cti.neo4j.neo4j_classes import get_by_city
from  cti.neo4j.neo4j_classes import get_by_org
from  cti.neo4j.neo4j_classes import get_by_region
from  cti.neo4j.neo4j_classes import get_by_timezone
from  cti.neo4j.neo4j_classes import get_by_postal
import threading
import os
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.template.loader import get_template
from .pdf_generator import render_to_pdf
from cti.neo4j.neo4j_classes import get_nodes, get_requests_for_ip, get_ips_with_request_method

# TEST IMPORTS
from django.utils.deconstruct import deconstructible
from django.template.defaultfilters import filesizeformat
#import validator.py
@login_required
def home(request):
    # Get top countries by IP
    TopCountriesByIP = get_Top_countries_by_ip()
    # Number of IPs
    numberOfIPs = get_count_of_ip()
    # Number of Requests
    numberOfRequests = Log_line.objects.count()
    # Number of Files
    numberOfFiles = Apache_log.objects.count()
    # print(numberOfRequests)
    return render(request, 'cti/home.html', {'TopCountriesByIP': TopCountriesByIP, 'numberOfIPs': numberOfIPs, 'numberOfRequests': numberOfRequests, 'numberOfFiles': numberOfFiles})

@login_required
def uploaded_files(request):
    file_list = Apache_log.objects.all()
    path="media"
    return render(request, 'cti/uploaded_files.html', {'files': file_list})

@login_required
def search_ip(request):
    query = request.GET.get('searchInput') 
    # TODO: make a switch for every option then repeat query code based on that
    
    if (query != None):
        requestTag = request.GET.get('searchCategory')
        if (requestTag =='ipAddress'):
            ips = get_by_ip(query)
            
        elif (requestTag =='countryCode'):
            ips = get_by_country_code(query)

        elif (requestTag =='countryName'):
            ips = get_by_country_name(query)

        elif (requestTag =='hostname'):
            ips = IP.objects.filter(hostname__contains=query)

        elif (requestTag =='city'):
            ips = get_by_city(query)

        elif (requestTag =='region'):
            ips = get_by_region(query)

        elif (requestTag =='org'):
            ips = get_by_org(query)

        elif (requestTag =='postal'):
            ips = get_by_postal(query)

        elif (requestTag =='timezone'):
            ips = get_by_timezone(query)
              

    else:
        ips = None

    path="search/ip"
    return render(request, 'cti/search_ips.html', {'ips': ips})


@login_required
def upload(request):
    if request.method == 'GET':
        return render(request, 'cti/upload.html')
    elif request.method == 'POST':

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
    return render(request, 'cti/upload.html', {'form': form})

@login_required
def settings(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('cti-profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'cti/settings.html', args)

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'cti/profile.html', args)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('cti-profile'))
        else:
            return redirect(reverse('cti-changepassword'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'cti/change_password.html', args)

@login_required
def report(request):
    if request.method == 'POST':
        if 'htmlST' in request.POST or 'pdfST' in request.POST:
            form = StatisticsForm(request.POST)
        else:
            form = AddressForm(request.POST)
        if form.is_valid():
            if 'htmlST' in request.POST or 'pdfST' in request.POST:
                param = form.cleaned_data['parameter']
                value = form.cleaned_data['value']

                if param == "Country":
                    data = get_nodes("IP", { "country" : value })
                elif param == "City":
                    data = get_nodes("IP", { "city" : value })
                elif param == "Region":
                    data = get_nodes("IP", { "region" : value })
                elif param == "Request method":
                    data_res = get_ips_with_request_method(value)
                    data = []
                    for ip in data_res:
                        data.append(ip['a'])
                if not data:
                    messages.warning(request, 'No data found.')
                    return HttpResponseRedirect("")
                template = get_template('cti/statisticsReport.html')
                context = {
                    "data" : data,
                    "parameter" : param,
                    "count" : len(data),
                    "value" : value,
                }

                html = template.render(context)
                if 'htmlST' in request.POST:
                    return HttpResponse(html)

                pdf = render_to_pdf('cti/statisticsReport.html', context)
                if pdf:
                    response = HttpResponse(pdf, content_type='application/pdf')
                    content = "attachment; filename='Report.pdf'"
                    download = request.GET.get("download")
                    response['Content-Disposition'] = content
                    return response
                return HttpResponse("Not found")
            else:
                address = form.cleaned_data['address']
                try:
                    data = get_nodes("IP", {"ip_address" : address })
                    data_logs_res = get_requests_for_ip(address)
                    template = get_template('cti/viewReport.html')
                    if not data:
                        messages.warning(request, 'Could not find the requested IP address.')
                        return HttpResponseRedirect("")

                    data_logs = []
                    for log in data_logs_res:
                        data_logs.append(log['b'])
                    context = {
                        "ip" : data[0],
                        "ip_log" : data_logs,
                    }

                    html = template.render(context)
                    if 'htmlIP' in request.POST:
                        return HttpResponse(html)

                    pdf = render_to_pdf('cti/viewReport.html', context)
                    if pdf:
                        response = HttpResponse(pdf, content_type='application/pdf')
                        content = "attachment; filename='Report.pdf'"
                        download = request.GET.get("download")
                        response['Content-Disposition'] = content
                        return response
                    return HttpResponse("Not found")

                except(IP.DoesNotExist):
                    messages.warning(request, 'IP address not found.')

    return render(request, 'cti/report.html', {'form' : AddressForm(), 'formST' : StatisticsForm()})

@login_required
def file_info(request):
    file_id = request.POST.get('file_id')
    if file_id != None:
        file_data = Apache_log.objects.filter(id=file_id).first()
        context = {
            'file' : file_data
        }

        pdf = render_to_pdf('cti/file_info.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            content = "attachment; filename='FileInformation.pdf'"
            download = request.GET.get("download")
            response['Content-Disposition'] = content
            return response
    return HttpResponse("Not found")