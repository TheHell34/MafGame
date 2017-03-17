from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from Player.models import player
from Unit.models import player_Unit, Unit

global result
result = ""

def post_list(request):
    u = User.objects.get(username=request.user)
    p = player.objects.get(user=u)
    pus = player_Unit.objects.filter(player_id=p).all()
    result2 = result
    global result
    result = ""
    return render(request, 'unit/post_list.html', {'pus': pus, 'result': result2})


def buy(request, unit_id):
    global result
    p = player.objects.get(user=User.objects.get(username=request.user))
    u = Unit.objects.get(name=unit_id)
    pu = player_Unit.objects.get(unit_id=u, player_id=p)
    if pu.unit_id.buy(p, int(request.POST['amount'])) != False:
        result += "Transaction successfull"
    else:
        result += "Not enough money"
    return redirect('/unit')

def players(request):
    p = player.objects.exclude(user=User.objects.get(username="Admin")).all()
    result2 = result
    global result
    result = ""
    return render(request, 'unit/players.html', {'players': p, 'result': result2})

def attack(request):
    global result
    p1 = player.objects.get(user=User.objects.get(username=request.user))
    p2 = player.objects.get(user=User.objects.get(username=request.POST['defender']))
    if Unit.attack(p1, p2) == "attacker wins":
        result += "You have killed your target"
    else:
        result += "You have lost the battle"
    return redirect('/unit/players')