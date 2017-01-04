from django.db import models


def receive_reward(self, player):
    player.money += self.reward
    player.xp += self.reward
    player.save()

def pay_cost(self, player):
    if player.money >= self.cost:
        player.money -= self.cost
        player.save()
    else:
        return False

def victory(self, player):
    receive_reward(self, player)


class activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.BigIntegerField()
    reward = models.BigIntegerField()