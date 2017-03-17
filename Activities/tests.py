from django.test import TestCase
from django.conf import settings
from django.utils import timezone

from Player.models import player
from Activities.models import activity


class ActivityTestCase(TestCase):
    pass
    # def setUp(self):
    #     player.objects.create(name="Mike", password="Kaas", money=100, xp=0, health=100, armor=100,
    #                           registered=timezone.now())
    #     activity.objects.create(name="RPS", cost=50, reward=100)
    #
    # def test_pay_cost(self):
    #     p = player.objects.get(name="Mike")
    #     a = activity.objects.get(name="RPS")
    #     a.pay_cost(p)
    #     self.assertEqual(p.money, 50)
    #
    # def test_receive_reward(self):
    #     p = player.objects.get(name="Mike")
    #     a = activity.objects.get(name="RPS")
    #     a.receive_reward(p)
    #     self.assertEqual(p.money, 200)
    #
    # def test_victory(self):
    #     p = player.objects.get(name="Mike")
    #     a = activity.objects.get(name="RPS")
    #     a.victory(p)
    #     self.assertEqual(p.money, 200)
