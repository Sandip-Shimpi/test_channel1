from django.db import models

# Create your models here.
class Latlong(models.Model):
	location_id = models.AutoField(primary_key=True)
	location_name=models.CharField(max_length=200, blank=True, null=True)
	Latitude=models.FloatField(null=True)
	Longitude=models.FloatField(null=True)
	
class Groups(models.Model):
    p_id = models.AutoField(primary_key = True)
    p_name = models.CharField(max_length=250, null=True)
    is_active = models.BooleanField(default=True)
    group_name=models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.group_name