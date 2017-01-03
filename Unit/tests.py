from django.test import TestCase

# Create your tests here.
from Player.models import player
from Unit.models import Unit, player_Unit


class PlayerTestCase(TestCase):
    def setUp(self):
        Unit.objects.create(name="gf", dmg=50, armor=50, cost=100, carry=200)
        Unit.objects.create(name="maf", dmg=10, armor=10, cost=10, carry=20)
        Unit.objects.create(name="sniper", dmg=100, armor=0, cost=50, carry=0)
        player.register("Mike", "ditwachtwoordisgeheim")
        player.register("Dominic", "ditwachtwoordisgeheim")

    def test_buy(self):
        p1 = player.objects.get(name="Mike")
        p1.give_money(9900)
        gf = Unit.objects.get(name="gf")
        gf.buy(p1, 10)
        pu1 = player_Unit.objects.get(player_id=p1, unit_id=gf)
        self.assertEqual(p1.money, 9000)
        self.assertEqual(pu1.amount, 10)

    def test_attack(self):
        p1 = player.objects.get(name="Mike")
        p2 = player.objects.get(name="Dominic")
        pass

    def test_defend(self):
        pass