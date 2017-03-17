from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
from Player.forms import UserForm
from Player.models import player

def view_profile(request):
    return render(request, 'player/profile.html', {'player': player.objects.get(user=request.user)})

def index(request):
    return render(request, 'player/login.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return render(request, 'player/login.html', {'error_message': 'Invalid login'})
    return render(request, 'player/login.html', {})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'player/logget_out.html', context)