from django.db import models

# Create your models here.
class Building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    perhour = models.BigIntegerField()
    cost = models.BigIntegerField()
    multipleir = models.FloatField()
    requiredxp = models.BigIntegerField()
