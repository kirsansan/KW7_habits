from django.core.management import BaseCommand

from habit.services import cleaning_logs


class Command(BaseCommand):

    def handle(self, *args, **options):
        cleaning_logs()
