from django.test import TestCase
from Player.models import player
from Activities.models import activity

class ActivityTestCase(TestCase):
    def setuptest(self):
        player.objects.create(name="Do", password="test123", money=500000, xp=0, health=100, armor=100, registered="2016-12-22")
        activity.objects.create(name="RPS", cost=50, reward=100)
    def Test_Give_Reward(self):
        x = player.objects.get(name="Do")
        y = activity.objects.get(name="RPS")
        self.assertEqual(y.give_reward(x), 0)
