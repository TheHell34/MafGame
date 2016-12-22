from django.db import models


# Create your models here.
class building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    perhour = models.BigIntegerField()
    cost = models.BigIntegerField()
    multiplier = models.FloatField()
    requiredxp = models.BigIntegerField()

    def buy(self, player):
        player.money = player.money - self.cost
        player.save()
        return player.money
