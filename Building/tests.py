from django.test import TestCase
from django.conf import settings

# Create your tests here.
from django.utils import timezone

from Building.models import building
from Player.models import player
from Building.models import player_building


class BuildingTestCase(TestCase):
    def setUp(self):
        building.objects.create(name="fabriek", perhour=1, cost=100, multiplier=1.1, requiredxp=0)
        player.objects.create(name="Mike", password="Kaas", money=1000, xp=0, health=100, armor=100, registered=timezone.now())

    def test_building_buy(self):
        b = building.objects.get(name="fabriek")
        p = player.objects.get(name="Mike")
        b.buy(p)
        self.assertEqual(p.money, 900)
        self.assertEqual(p.xp, b.cost)

    def test_generate_money(self):
        b = building.objects.get(name="fabriek")
        p = player.objects.get(name="Mike")
        b.generate_money(p)
        self.assertEqual(p.money, 1001)

    def test_upgrade(self):
        b = building.objects.get(name="fabriek")
        p = player.objects.get(name="Mike")
        b.buy(p)
        b.upgrade(p)
        pb = player_building.objects.get(player_id=p.player_id, building_id=b.building_id)
        self.assertEqual(p.money, 790)
        self.assertEqual(pb.cost, 121)

    def test_upgrade_mutiple(self):
        b = building.objects.get(name="fabriek")
        p = player.objects.get(name="Mike")
        b.buy(p)
        for i in range(0, 4):
            b.upgrade(p)
        pb = player_building.objects.get(player_id=p.player_id, building_id=b.building_id)
        self.assertEqual(p.money, 390)
        self.assertEqual(pb.cost, 160)