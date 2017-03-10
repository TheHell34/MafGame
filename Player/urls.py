from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/$', views.player_new, name='player_new'),
    # url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.view_profile, name='view_profile'),
]