from django.conf.urls import url
from . import views

app_name = 'Building'

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<building_id>[^/]+)/buy/$', views.buy, name='buy'),
]