from django.db import models


class activity(models.Model):
    activity_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cost = models.BigIntegerField()
    reward = models.BigIntegerField()

    def give_reward(self, player):
        player.money += self.reward
        player.save()
        return player.money
