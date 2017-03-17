from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from Player.models import player
from Unit.models import Unit, player_Unit


class UnitTestCase(TestCase):
    def setUp(self):
        Unit.objects.create(name="gf", dmg=50, armor=50, cost=100, carry=200)
        Unit.objects.create(name="maf", dmg=10, armor=10, cost=10, carry=20)
        Unit.objects.create(name="sniper", dmg=100, armor=0, cost=50, carry=0)
        Unit.objects.create(name="bodyguard", dmg=0, armor=100, cost=500, carry=0)
        User.objects.create_user('Mike', 'lennon@thebeatles.com', 'ditwachtwoordisgeheim')
        User.objects.create_user('Dominic', 'lennon@thebeatles.com', 'ditwachtwoordisgeheim')

    def test_buy(self):
        u = User.objects.get(username="Mike")
        p = player.objects.get(user=u)
        p.give_money(9900)
        gf = Unit.objects.get(name="gf")
        gf.buy(p, 10)
        pu1 = player_Unit.objects.get(player_id=p, unit_id=gf)
        self.assertEqual(p.money, 9000)
        self.assertEqual(pu1.amount, 10)

    def test_attack_enough_money_win(self):
        u1 = User.objects.get(username="Mike")
        p1 = player.objects.get(user=u1)
        u2 = User.objects.get(username="Dominic")
        p2 = player.objects.get(user=u2)
        gf = Unit.objects.get(name="gf")
        sniper = Unit.objects.get(name="sniper")
        p1.give_money(9900)
        p2.give_money(9900)
        sniper.buy(p2, 5)
        gf.buy(p1, 10)
        Unit.attack(p1, p2)
        self.assertEqual(p1.money, 11000)
        self.assertEqual(p2.money, 7750)

    def test_attack_not_enough_money_win(self):
        u1 = User.objects.get(username="Mike")
        p1 = player.objects.get(user=u1)
        u2 = User.objects.get(username="Dominic")
        p2 = player.objects.get(user=u2)
        gf = Unit.objects.get(name="gf")
        sniper = Unit.objects.get(name="sniper")
        p1.give_money(9900)
        p2.give_money(900)
        sniper.buy(p2, 5)
        gf.buy(p1, 10)
        Unit.attack(p1, p2)
        self.assertEqual(p1.money, 9750)
        self.assertEqual(p2.money, 0)

    def test_defend(self):
        u1 = User.objects.get(username="Mike")
        p1 = player.objects.get(user=u1)
        u2 = User.objects.get(username="Dominic")
        p2 = player.objects.get(user=u2)
        gf = Unit.objects.get(name="gf")
        bodyguard = Unit.objects.get(name="bodyguard")
        p1.give_money(9900)
        p2.give_money(9900)
        bodyguard.buy(p2, 10)
        gf.buy(p1, 10)
        Unit.attack(p1, p2)
        pu1 = player_Unit.objects.get(player_id=p1, unit_id=gf)
        self.assertEqual(p1.money, 9000)
        self.assertEqual(p2.money, 5000)
        self.assertEqual(pu1.amount, 0)