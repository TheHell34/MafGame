from django.test import TestCase

# Create your tests here.
from Player.models import player
from Unit.models import player_Unit, Unit


class PlayerTestCase(TestCase):
    def setUp(self):
        Unit.objects.create(name="gf", dmg=50, armor=50, cost=100, carry=200)
        Unit.objects.create(name="maf", dmg=10, armor=10, cost=10, carry=20)
        Unit.objects.create(name="sniper", dmg=100, armor=0, cost=50, carry=0)

    def test_register(self):
        player.register("Mike", "ditwachtwoordisgeheim")
        p = player.objects.get(name="Mike")
        pu = player_Unit.objects.all().filter(player_id=p.player_id).count()
        self.assertEqual(pu, 3)