from celery import task

from Building.models import generate_money
from Player.models import player

@task()
def generate_money():
    generate_money()