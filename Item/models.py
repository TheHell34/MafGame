from django.db import models

# Create your models here.
from Type.models import Type


class Unit(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.IntegerField(max_length=255)
    desc = models.TextField()
    cost = models.BigIntegerField()
    type = models.ForeignKey(Type)
    value = models.BigIntegerField()
