
def buy(player, building):
    player.money = player.money - building.cost
    player.save()

def calc():
    pass


# buy(p,b)
#
# print(p.money)