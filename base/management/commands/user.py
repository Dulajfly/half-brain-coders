from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group
from django.conf import settings


class Command(BaseCommand):
    help = "Create sample user: admin & user"

    def add_arguments(self, parser):
        parser.add_argument('--delete', action='store_true', help='Delete users: admin & user from local database.')

    def handle(self, *args, **options):
        try:
            for item in settings.SAMPLE_USERS:
                if options['delete']:
                    User.objects.filter(username=item[0]).delete()
                    print('Removed user: {}'.format(item[0]))
                    continue
                if User.objects.filter(username=item[0]).exists():
                    print('User with this username: {} already exists!'.format(item[0]))
                    continue
                if item[0] == 'admin':
                    user = User.objects.create_superuser(
                        item[0], '', item[1]
                    )
                else:
                    user = User.objects.create_user(
                        item[0], '', item[1]
                    )
                print('Successfully created an account\nlogin: {login}\npassword: {passw}'.format(login=item[0], passw=item[1]))
        except:
            print('Error! Check if the database exists.')
