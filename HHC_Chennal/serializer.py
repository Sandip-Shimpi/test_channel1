from rest_framework import serializers
from . import models


class UserLatLongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Latlong
        fields = ['location_id','Latitude','Longitude']

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Groups
        fields = ['p_id','p_name','group_name']
