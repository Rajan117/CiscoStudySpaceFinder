from django.shortcuts import render
from django.http import HttpResponse
import requests
from MerakiApp.models import StudySpace, Device
from MerakiApp.forms import StudySpaceForm
from django.shortcuts import redirect
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

ORG_ID = "1112354"

NET_ID = "L_620933798623712533"

payload = {}

headers = {'X-Cisco-Meraki-API-Key': '6fa78caf241818bea416c8f2bacec3511fa7063c'}


def user_dashboard(request):

    context_dict = {'boldmessage': "Study space information unavailable at this time."}

    context_dict['StudySpaces'] = StudySpace.objects.all()

    if request.method == 'GET':
        order_type = request.GET.get('order_options', False)

        if order_type == 'People':
            context_dict['StudySpaces'] = StudySpace.objects.order_by('people')

        elif order_type == 'Noise':
            context_dict['StudySpaces'] = StudySpace.objects.order_by('avg_noise_level')

        elif order_type == 'Light':
            context_dict['StudySpaces'] = StudySpace.objects.order_by('avg_light_level')

        context_dict['order_type'] = order_type

    return render(request, 'MerakiWebApp/user-dashboard.html', context=context_dict)


def user_search(request):
    results = []

    context_dict = {}
    results = StudySpace.objects.all()

    show_results = False

    if request.method == 'POST':

        query = request.GET.get('search', None)

        query_noise_max = request.POST.get('max_noise', None)
        query_noise_min = request.POST.get('min_noise', None)

        query_light_max = request.POST.get('max_light', None)
        query_light_min = request.POST.get('min_light', None)

        query_people_max = request.POST.get('max_people', None)
        query_people_min = request.POST.get('min_people', None)

        if query:
            show_results = True
            results = results.filter(Q(name__icontains=query))
            context_dict['name'] = query

        if query_noise_max and int(query_noise_max) > 0:
            show_results = True
            results = results.filter(avg_noise_level__lte=query_noise_max).filter(avg_noise_level__gte=query_noise_min)

        if query_light_max and int(query_light_max) > 0:
            show_results = True
            results = results.filter(avg_light_level__lte=query_light_max).filter(avg_light_level__gte=query_light_min)

        if query_people_max and int(query_people_max) > 0:
            show_results = True
            results = results.filter(people__lte=query_people_max).filter(people__gte=query_people_min)

        if show_results:
            context_dict['results'] = results


    return render(request, 'MerakiWebApp/user-search.html', context=context_dict)


def user_results(request):
    context_dict = {}

    url = "https://api.meraki.com/api/v1/networks/L_566327653141843049/devices"

    device_list = requests.request("GET", url, headers=headers, data=payload)

    context_dict['devices'] = device_list

    return render(request, 'MerakiWebApp/user-results.html', context=context_dict)

def admin_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)
                return redirect(reverse('MerakiApp:admin-dashboard'))

            else:

                return HttpResponse('That account is disabled.')

        else:

            return HttpResponse('Invalid credentials')

    else:

        return render(request, 'MerakiWebApp/admin-login.html')

@login_required
def admin_device(request, device_slug):

    context_dict = {}

    try:
        device = Device.objects.get(slug=device_slug)
        context_dict['device'] = device
    except Device.DoesNotExist:
        context_dict['device'] = None

    return render(request, 'MerakiWebApp/admin-device.html', context=context_dict)




@login_required
def admin_dashboard(request):
    # url = ("https://api.meraki.com/api/v1/organizations/" + ORG_ID + "/networks")

    #url = ("https://api.meraki.com/api/v1/networks/" + NET_ID + "/devices")

    # url = "https://api.meraki.com/api/v1/networks/" + NET_ID + "/devices/Q2FV-VVUW-VZAY"

    #netlist = requests.request("GET", url, headers=headers, data=payload)

    devices = Device.objects.all()

    context_dict = {'locations': Device.objects.all().values_list('location_tag', flat=True).distinct(),
                    'types': Device.objects.all().values_list('device_type', flat=True).distinct(), 'devices': devices}

    if request.method == 'GET':
        location = request.GET.get('location_options', False)

        types = request.GET.getlist('types')

        if types:
            for device_type in types:
                devices = devices.filter(device_type=device_type)
                print(devices)

        if location and location != "Unselected":
            devices = devices.filter(location_tag=location)

        context_dict['devices'] = devices

    return render(request, 'MerakiWebApp/admin-dashboard.html', context=context_dict)

@login_required
def admin_alerts(request):

    return render(request, 'MerakiWebApp/admin-alerts.html')
