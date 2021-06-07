from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from faker import Faker
import random
import string
fake = Faker()


def createpassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))


class Command(BaseCommand):
    help = 'The Zen of Python'

    def add_arguments(self, parser):
        parser.add_argument(
            '-1','-2','-3','-4','-5','-6','-7','-8','-9','-10',
            action='store_true',
            default=False,
            help='Вывод короткого сообщения'

        )

    def handle(self, *args, **options):

        for i in range():
            User.objects.create_user(username=fake.name().replace(' ', '').lower(),
                                        email=fake.name().replace(' ', '') + '@gmail.com',
                                        password=createpassword())



