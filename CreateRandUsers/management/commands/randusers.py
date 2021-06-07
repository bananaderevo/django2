import random
import string
import sys

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from faker import Faker

fake = Faker()


def createpassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))


class Command(BaseCommand):
    help = 'Creating some users'

    def add_arguments(self, parser):
        parser.add_argument('num', type=int)

    def handle(self, *args, **options):
        if not 1 <= options['num'] <= 10:
            sys.stdout.write('Error, wrong number: number should be in 1 to 10.\n')
        else:
            for i in range(options['num']):
                User.objects.create_user(username=fake.name().replace(' ', '').lower(),
                                         email=fake.name().replace(' ', '') + '@gmail.com',
                                         password=createpassword())
