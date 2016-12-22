from django.test import TestCase
from django.conf import settings

# Create your tests here.
from Building.models import building
from Player.models import player


class BuildingTestCase(TestCase):
    def setUp(self):
        building.objects.create(name="fabriek", perhour=1, cost=100, multiplier=1.1, requiredxp=0)
        player.objects.create(name="Mike", password="Kaas", money=100, xp=0, health=100, armor=100, registered="2012-09-28T16:41:12.9976565")

    def test_building_buy(self):
        b = building.objects.get(name="fabriek")
        p = player.objects.get(name="Mike")
        self.assertEqual(b.buy(p), 0)