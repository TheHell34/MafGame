from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from Player.models import player
from .models import building, player_building

global result
result = ""

def post_list(request):
    u = User.objects.get(username=request.user)
    p = player.objects.get(user=u)
    pbs = player_building.objects.filter(player_id=p).all()
    result2 = result
    global result
    result = ""
    return render(request, 'building/post_list.html', {'pbs': pbs, 'result': result2})


def buy(request, building_id):
    global result
    p = player.objects.get(user=User.objects.get(username=request.user))
    b = building.objects.get(name=building_id)
    pb = player_building.objects.get(building_id=b, player_id=p)
    if pb.building_id.upgrade(p) != False:
        result += "Transaction successfull"
    else:
        result += "Not enough money"
    return redirect('/building')