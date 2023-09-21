from django.core.management import BaseCommand

from habit.services import cleaning_logs, send_telegram_message_rev_b


class Command(BaseCommand):

    def handle(self, *args, **options):
        send_telegram_message_rev_b()
