# HHC_Chennal/tasks.py
from celery import shared_task
from .models import Latlong  # Import your Location model
from channels.db import database_sync_to_async

@database_sync_to_async
def saveloc(user, latitude, longitude):
#     print
     return Latlong.objects.create(location_name=user,Latitude=latitude,Longitude=longitude)

@shared_task
def save_location(user, latitude, longitude):
#    print(user,latitude,longitude)
     print('hellow')
     return saveloc(user, latitude, longitude)
     
