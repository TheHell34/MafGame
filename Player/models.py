from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

import Building
from Unit.models import Unit, player_Unit


class player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    money = models.BigIntegerField()
    xp = models.BigIntegerField()
    health = models.IntegerField()
    armor = models.IntegerField()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            player.objects.create(user=instance, money=100, xp=0, health=100, armor=0)
            p = player.objects.get(user=instance)
            units = Unit.objects.all()
            buildings = Building.models.building.objects.all()
            for unit in units:
                player_Unit.objects.create(player_id=p, unit_id=unit, amount=0)
            for b in buildings:
                Building.models.player_building.objects.create(player_id=p, building_id=b, level=0, perminute=0,cost=b.cost)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.player.save()

    #for testing only
    def give_money(self, amount):
        self.money += amount
        self.save()

    def __str__(self):
        return self.user.username