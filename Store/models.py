from django.db import models


class store(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    requiredxp = models.BigIntegerField()

    def buy(self, player, amount):
        player.money -= self.cost * amount
        player.save()
        return player.money
