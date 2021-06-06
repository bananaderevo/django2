import random
import string


from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from faker import Faker


fake = Faker()


class Articles(models.Model):
    text = models.IntegerField('Число юзеров', validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Создание юзеров'


def createpassword():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))
