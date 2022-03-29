from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        print(User.objects.get(is_superuser=True).first_name,end=' ')
        print(User.objects.get(is_superuser=True).last_name)