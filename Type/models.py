from django.db import models

# Create your models here.

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)