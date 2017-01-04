from django.db import models
from Player.models import player
from Building.models import player_building

# Create your models here.

class gang(models.Model):

    class weapon(models.Model):
        weapon_id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=255)
        cost = models.BigIntegerField()
        capacity = models.IntegerField

        def buy(self, player):
            player.money -= self.cost
            self.register_weapon(player)
            player.save()

        def register_weapon(self, p):
            gang_items.objects.create(player_id=p, weapon_id=self, cost=self.cost)
            pw = gang_items.objects.get(player_id=p, weapon_id=self)
            pw.save()

        def upgrade(self, player):
            pw = gang_items.objects.get(player_id=player, weapon_id=self)
            if player.money >= pw.cost:
                player.money -= pw.cost
                pw.weapon_level += 1
                pw.capacity += 5
                player.save()
                pw.save()
            else:
                return False

    class member(models.Model):
        member_id = models.AutoField(primary_key=True)
        member_name = models.CharField(max_length=255)
        amount = models.IntegerField()

        def find_recruits(self, player):
            player.money -= self.cost
            self.recruit(player)
            player.save()

        def recruit(self, p):
            gang_items.objects.create(player_id=p, member_id=self, cost=self.cost)
            pm = gang_items.objects.get(player_id=p, member_id=self)
            gang.member.amount += 1
            pm.save()

        def upgrade(self, player):
            pm = gang_items.objects.get(player_id=player, member_name=self)
            if player.money >= pm.cost:
                player.money -= pm.cost
                pm.member_level += 1
                player.save()
                pm.save()
            else:
                return False

    class player_upgrade(models.Model):
        player_name = player.name
        player_health = player.health
        player_armor = player.armor
        def upgrade(self, player):
            upl = gang_items.objects.get(player_id=player, player_name=self)
            if player.money >= upl.cost:
                player.money -= upl.cost
                upl.player_health += 10
                upl.player_armor += 10
                player.save()
                upl.save()
            else:
                return False


class gang_items(models.Model):
    player_id = models.ForeignKey(player)
    weapon_id = models.ForgeinKey(gang)
    member_id = models.ForeignKey(gang)
    member_level = models.IntegerField()
    weapon_level = models.IntegerField()
    cost = models.BigIntegerField()