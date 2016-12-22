from django.db import models

# Create your models here.
class player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    money = models.BigIntegerField()
    xp = models.BigIntegerField()
    health = models.IntegerField()
    armor = models.IntegerField()
    registered = models.DateTimeField('auto_now_add=True')