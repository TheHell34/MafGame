from django.db import models

# Create your models here.
from django.utils import timezone

import Building
from Unit.models import Unit, player_Unit


class player(models.Model):
    player_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=50)
    money = models.BigIntegerField()
    xp = models.BigIntegerField()
    health = models.IntegerField()
    armor = models.IntegerField()
    registered = models.DateTimeField()

    @staticmethod
    def register(name, password):
        player.objects.create(name=name, password=password, money=100, xp=0, health=100, armor=0, registered=timezone.now())
        p = player.objects.get(name=name)
        units = Unit.objects.all()
        buildings = Building.models.building.objects.all()
        for unit in units:
            player_Unit.objects.create(player_id=p, unit_id=unit, amount=0)
        for b in buildings:
            Building.models.player_building.objects.create(player_id=p, building_id=b, level=0, perhour=0, cost=b.cost)

    #for testing only
    def give_money(self, amount):
        self.money += amount
        self.save()

    def __str__(self):
        return self.name