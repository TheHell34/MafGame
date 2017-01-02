from django.shortcuts import render

# Create your views here.
from .models import building

def post_list(request):
    buildings = building.objects.all().order_by('building_id')
    print(buildings)
    return render(request, 'building/post_list.html', {'buildings': buildings})