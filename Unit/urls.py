from django.conf.urls import url
from . import views

app_name = 'Unit'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<unit_id>[^/]+)/buy/$', views.buy, name='buy'),
    url(r'^players/$', views.players, name='players'),
    url(r'^players/attack/$', views.attack, name='attack')
]