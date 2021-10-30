from django.core.management.base import BaseCommand, CommandError
from django.core import management


class Command(BaseCommand):
    help = "Run makemigrations, migrate and create sample users"

    def handle(self, *args, **options):
        try:
            print('Running makemigrations...')
            management.call_command('makemigrations')
            print('Running migrate...')
            management.call_command('migrate')
            print('Creating sample users...\n')
            management.call_command('user')
            print('\nThe command completed the work successfully, now you can run project')
        except:
            print('ERROR!')