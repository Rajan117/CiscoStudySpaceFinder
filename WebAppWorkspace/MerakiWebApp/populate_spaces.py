import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MerakiWebApp.settings')

import django

django.setup()

from MerakiApp.models import StudySpace, Device


def populate():
    spaces = [{'name': 'Cafe', 'noise': 80, 'light': 76, 'people': 44},
              {'name': '1stFloor', 'noise': 68, 'light': 70, 'people': 28},
              {'name': '2ndFloor', 'noise': 50, 'light': 68, 'people': 24},
              {'name': '3rdFloor', 'noise': 30, 'light': 60, 'people': 12}]

    devices = [{'location_tag': '4thFloor', 'type': 'camera', 'model': 'MV12WE', 'serial': 'Q2FV-VVUW-VZAY', 'net_ID': 'L_620933798623712533', 'name': '4thFloorPrinterCamera'},
               {'location_tag': '1stFloor', 'type': 'camera', 'model': 'MV12WE', 'serial': 'Q2FV-TCTG-39M5',
                'net_ID': 'L_620933798623712533', 'name': '1stFloorCafeCamera'},
               {'location_tag': '1stFloor', 'type': 'temp', 'model': 'MT10', 'serial': 'Q3CA-B6TD-L2BA',
                'net_ID': 'L_620933798623712533', 'name': '1stFloorStairsTempSenso'},
               {'location_tag': '2ndFloor', 'type': 'temp', 'model': 'MT10', 'serial': 'Q3CA-QHTC-BSK5',
                'net_ID': 'L_620933798623712533', 'name': '2ndFloorResearchRoomTempSensor'}]

    for space in spaces:
        s = add_space(space['name'], space['noise'], space['light'], space['people'])

    for device in devices:
        d = add_device(device['location_tag'], device['type'], device['model'], device['serial'], device['net_ID'], device['name'])





def add_space(name, noise, light, people):
    s = StudySpace.objects.get_or_create(name=name)[0]
    s.avg_noise_level = noise
    s.avg_light_level = light
    s.people = people
    s.save()
    return s

def add_device(location_tag, type, model, serial, net_ID, name):
    d = Device.objects.get_or_create(serial=serial)[0]
    d.location_tag = location_tag
    d.type = type
    d.model = model
    d.serial = serial
    d.net_ID = net_ID
    d.name = name
    d.save()
    return d


if __name__ == '__main__':
    print("Staring Django population script...")
    populate()