from django.db import models
from Player.models import player

# Create your models here.

class building(models.Model):
    building_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    perhour = models.BigIntegerField()
    cost = models.BigIntegerField()
    multiplier = models.FloatField()
    requiredxp = models.BigIntegerField()

    def generate_money(self, player):
        player.money += self.perhour
        player.save()

    def upgrade(self, player):
        pb = player_building.objects.get(player_id=player, building_id=self)
        if player.money >= pb.cost:
            player.money -= pb.cost
            pb.level += 1
            pb.cost *= self.multiplier
            pb.perhour += self.perhour
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
    perhour = models.BigIntegerField()
    cost = models.BigIntegerField()






