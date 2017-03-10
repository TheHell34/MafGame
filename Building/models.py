from django.db import models
from Player.models import player

# Create your models here.

def generate_money():
    players = player.objects.all()
    for p in players:
        pb = player_building.objects.filter(player_id=p)
        for building in pb:
            p.money += building.perminute
        p.save()


class building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    perminute = models.BigIntegerField()
    cost = models.BigIntegerField()
    multiplier = models.FloatField()
    requiredxp = models.BigIntegerField()

    def upgrade(self, player):
        pb = player_building.objects.get(player_id=player, building_id=self)
        if player.money >= pb.cost:
            player.money -= pb.cost
            pb.level += 1
            pb.cost *= self.multiplier
            pb.perminute += self.perminute
            player.save()
            pb.save()
        else:
            return False

    def __str__(self):
        return self.name

class player_building(models.Model):
    id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey(player)
    building_id = models.ForeignKey(building)
    level = models.IntegerField()
    perminute = models.BigIntegerField()
    cost = models.BigIntegerField()






