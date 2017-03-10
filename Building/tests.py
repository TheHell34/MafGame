from django.test import TestCase
# Create your tests here.

from Building.models import building, player_building, generate_money
from Player.models import player


class BuildingTestCase(TestCase):
    def setUp(self):
        building.objects.create(name="fabriek1", perminute=1, cost=100, multiplier=1.1, requiredxp=0)
        building.objects.create(name="fabriek2", perminute=10, cost=1000, multiplier=1.2, requiredxp=0)
        building.objects.create(name="fabriek3", perminute=100, cost=10000, multiplier=1.3, requiredxp=0)
        building.objects.create(name="fabriek4", perminute=1000, cost=100000, multiplier=1.4, requiredxp=0)

    def test_generate_money(self):
        b = building.objects.all()
        player.register("Mike2", "ditwachtwoordisgeheim")
        p = player.objects.get(name="Mike2")
        p.give_money(111000)
        for i in b:
            i.upgrade(p)
        self.assertEqual(p.money, 0)
        generate_money()
        p = player.objects.get(name="Mike2")
        self.assertEqual(p.money, 1111)

    def test_upgrade(self):
        b = building.objects.get(name="fabriek1")
        player.register("Mike2", "ditwachtwoordisgeheim")
        p = player.objects.get(name="Mike2")
        p.give_money(900)
        b.upgrade(p)
        b.upgrade(p)
        pb = player_building.objects.get(player_id=p.player_id, building_id=b.building_id)
        self.assertEqual(p.money, 790)
        self.assertEqual(pb.cost, 121)

    def test_upgrade_mutiple(self):
        b = building.objects.get(name="fabriek1")
        player.register("Mike2", "ditwachtwoordisgeheim")
        p = player.objects.get(name="Mike2")
        p.give_money(900)
        for i in range(0, 5):
            b.upgrade(p)
        pb = player_building.objects.get(player_id=p.player_id, building_id=b.building_id)
        self.assertEqual(p.money, 390)
        self.assertEqual(pb.cost, 160)
        self.assertEqual(pb.level, 5)