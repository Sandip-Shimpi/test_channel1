from django.shortcuts import render
from rest_framework.views import APIView
from . import models
from . import serializer
from rest_framework.response import Response
from datetime import datetime


# Create your views here.
class LatLong(APIView):
    def post(self, request):
        data=serializer.UserLatLongSerializer(data=request.data)
        if data.is_valid():
            data.save()
            print(datetime.now().time())
            return Response(data.data)
        else:
            return Response(data.errors)

    def get(self, request):
        d1 = models.Latlong.objects.all()
        print(d1)
        data=serializer.UserLatLongSerializer(d1, many=True)
        return Response(data.data)
        # else:
        #     return Response(data.errors)

class Users(APIView):
    def get(self, request):
        d1 = models.Groups.objects.all()
        print(d1)
        data=serializer.UsersSerializer(d1, many=True)
        return Response(data.data)