from django.test import TestCase

# Create your tests here.

from Player.models import player
from Gang.models import gang
from Gang.models import gang_items

class GangTestCase(TestCase):
    class weapon_test(TestCase):
        def weapon_setUp(self):
            gang.weapon.objects.create(weapon_name="AK-47", cost=500, capacity=45)
            # gang.member.objects.create(name="",)
            player.objects.create(name="Burhan", password="test", money=1000, xp=0, health=100, armor=100,
                                  registered="2012-09-28T16:41:12.9976565")

        def test_weapon_buy(self):
            w = gang.weapon.objects.get(name="AK-47")
            p = player.objects.get(name="Burhan")
            w.buy(p)
            self.assertEqual(p.money, 900)

        def test_weapon_upgrade(self):
            w = gang.weapon.objects.get(name="Ak-47")
            p = player.objects.get(name="Burhan")
            w.buy(p)
            w.upgrade(p)
            gi = gang_items.objects.get(player_id=p.player_id, weapon_id=w.weapon_id)
            self.assertEqual(p.money, 790)
            self.assertEqual(gi.cost, 121)

    class members_test(TestCase):
        def member_setUp(self):
            gang.member.objects.create(member_name="Santos", cost=350)
            player.objects.create(name="Burhan", password="test", money=1000, xp=0, health=100, armor=100,
                                  registered="2012-09-28T16:41:12.9976565")

        def member_upgrade(self):
            m = gang.member.objects.get(name="Santos")
            p = player.objects.get(name="Burhan")
            m.find_recruits(p)
            m.upgrade(p)
            gi = gang_items.objects.get(player_id=p.player_id, member_id=m.member_id)
            self.assertEqual(p.money, 790)
            self.assertEqual(gi.cost, 121)


    #class player_upgrade_test(TestCase):
    #    def player_setUp(self):
    #        player.objects.create(name="Burhan", password="test", money=1000, xp=0, health=100, armor=100,
    #                              registered="2012-09-28T16:41:12.9976565")
    #    def test_pl_upgrade(self):
    #        pu = gang.player_upgrade.objects.get(name="Ak-47")
    #        p = player.objects.get(name="Burhan")
    #        pu.upgrade(p)
    #        plu = gang_items.objects.get(player_id=p.player_id, player_id=pu.player_id)
    #        self.assertEqual(p.money, 790)
    #        self.assertEqual(plu.cost, 121)