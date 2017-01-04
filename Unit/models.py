from django.db import models

# Create your models here.

class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    dmg = models.BigIntegerField()
    armor = models.BigIntegerField()
    cost = models.BigIntegerField()
    carry = models.BigIntegerField()

    def buy(self, player, amount):
        pu = player_Unit.objects.get(player_id=player, unit_id=self)
        if player.money >= (self.cost * amount):
            player.money -= (self.cost * amount)
            pu.amount += amount
            player.save()
            pu.save()

    @staticmethod
    def attack(attacker, defender):
        attack_power = attacker.armor
        defend_armor = defender.armor
        carry = 0
        attacker_units = player_Unit.objects.all().filter(player_id=attacker)
        defender_units = player_Unit.objects.all().filter(player_id=defender)
        for unit in attacker_units:
            attack_power += (unit.unit_id.dmg * unit.amount)
            carry += (unit.unit_id.carry * unit.amount)
        for unit in defender_units:
            defend_armor += (unit.unit_id.armor * unit.amount)
        if attack_power > defend_armor:
            money = defe
            return "attacker wins"

        else:
            return "defender wins"

    def __str__(self):
        return self.name

class player_Unit(models.Model):
    id = models.AutoField(primary_key=True)
    player_id = models.ForeignKey('Player.player')
    unit_id = models.ForeignKey(Unit)
    amount = models.BigIntegerField()