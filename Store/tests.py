from django.test import TestCase
from django.conf import settings

from Store.models import store
from Player.models import player


class StoreTestCase(TestCase):
    def setUp(self):
        store.objects.create(name="AK-47", cost=150, requiredxp=0)
        player.objects.create(name="Glenn", password="Wopam", money=200, xp=25, health=100, armor=100, registered="2012-09-28T16:41:12.9976565")

    def test_store_buy(self):
        s = store.objects.get(name="AK-47")
        p = player.objects.get(name="Glenn")
        self.assertEqual(s.buy(p, 1), 50)
