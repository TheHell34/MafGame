from django.core.management import BaseCommand

from Building.models import generate_money


class Command(BaseCommand):

    def handle(self, *args, **options):
        generate_money()


