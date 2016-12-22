from django.test import TestCase
from django.conf import settings

from Player.models import player
from Activities.models import activity

class ActivityTestCase(TestCase):
    def setUp(self):
        player.objects.create(name="Mike", password="Kaas", money=100, xp=0, health=100, armor=100, registered="2012-09-28T16:41:12.9976565")
        activity.objects.create(name="RPS", cost=50, reward=100)

    def test_give_reward(self):
        p = player.objects.get(name="Mike")
        y = activity.objects.get(name="RPS")
        self.assertEqual(y.give_reward(p), 200)
