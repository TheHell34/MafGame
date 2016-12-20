from django.db import models

# Create your models here.

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    name = models.IntegerField(max_length=255)
    dmg = models.BigIntegerField()
    armor = models.BigIntegerField()
    cost = models.BigIntegerField()