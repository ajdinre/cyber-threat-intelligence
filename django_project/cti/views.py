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
from  cti.neo4j.neo4j_classes import get_by_country_name
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
from cti.neo4j.neo4j_classes import get_nodes, get_requests_for_ip

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
        if form.is_valid():
            server_name = form['servername'].value()
            file = request.FILES['file']
            server_data = {'server_name': str(server_name), 'file_name': str(file)}
            instance = Apache_log(log_file=request.FILES['file'])
            instance.analyzed = False
            print("instance")
            print(instance.log_file)
            print(instance.analyzed)
            instance.save()
            analyzeThread = threading.Thread(target=analyze, args=(instance.log_file, server_data))
            analyzeThread.start()

            messages.success(request, 'File is saved.')
        else:
            messages.warning(request, 'An error has occured.')
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

                try:
                    if param == "Country":
                        data = IP.objects.filter(countryname=value)
                    elif param == "City":
                        data = IP.objects.filter(city=value)
                    elif param == "Region":
                        data = IP.objects.filter(region=value)
                    elif param == "Request method":
                        log_ip = Log_line.objects.filter(requestMethod=value).values_list('ip_address_id', flat=True).distinct()
                        data = IP.objects.filter(id__in=log_ip)
                    if not data:
                        raise IP.DoesNotExist
                    template = get_template('cti/statisticsReport.html')
                    context = {
                        "data" : data,
                        "parameter" : param,
                        "count" : data.count(),
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
                except(IP.DoesNotExist):
                    messages.warning(request, 'Invalid input.')
            else:
                address = form.cleaned_data['address']
                try:
                    data = IP.objects.get(address=address)
                    id = data.id
                    data_logs = Log_line.objects.filter(ip_address_id=id)
                    template = get_template('cti/viewReport.html')
                    context = {
                        "ip" : data,
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