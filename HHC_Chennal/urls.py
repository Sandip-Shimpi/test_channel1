from django.urls import path
from .views import * 

urlpatterns = [
    path('locations',LatLong.as_view() ),
    path('users',Users.as_view() )
    ]