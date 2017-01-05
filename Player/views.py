from django.shortcuts import render

# Create your views here.
from Player.models import player
from Player.forms import RegisterForm, LoginForm
from django.shortcuts import redirect


def player_new(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            print(player.name)
            print(player.password)
            player.register(player.name, player.password)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'player/player_new.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            user = player.objects.get(name=p.name)
            return render(request, 'player/view_profile.html', {'user': user})
    else:
        form = LoginForm()
    return render(request, 'player/login.html', {'form': form})

def view_profile(request):
    return render(request, 'player/view_profile.html', {})