from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User, Group
from django.conf import settings
from django.core import management
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = "Delete all migration from migrations folder, with param --all delete including db.sqlite3"

    def add_arguments(self, parser):
        parser.add_argument('--all', action='store_true', help='Delete db.sqlite3 from project folder.')

    def __get_migration_directory(self):
        return os.chdir(os.getcwd()+'\\base\\migrations\\')

    def __get_project_directory(self):
        return os.chdir(os.getcwd())

    def handle(self, *args, **options):
        self.__get_project_directory()
        if options['all']:
            if 'db.sqlite3' in os.listdir():
                print('Remove database: db.sqlite3')
                os.remove('db.sqlite3')
        self.__get_migration_directory()
        for file in os.listdir():
            if file.startswith('0') and file.endswith('initial.py'):
                print('Removed file: {}'.format(file))
                os.remove(file)
