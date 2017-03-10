from django.db import models

# Create your models here.


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    desc = models.TextField()
    cost = models.BigIntegerField()
    value = models.BigIntegerField()
