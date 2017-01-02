from django.db import models

# Create your models here.

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dmg = models.BigIntegerField()
    armor = models.BigIntegerField()
    cost = models.BigIntegerField()
    carry = models.BigIntegerField()

    def attack(self):
        pass

    def defend(self):
        pass

    def calc(self):
        pass

    def __str__(self):
        return self.name

class player_Unit(models.Model):
    id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey('Player.player')
    unit_id = models.ForeignKey(Unit)
    amount = models.BigIntegerField()