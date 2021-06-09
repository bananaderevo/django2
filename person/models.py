from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def get_absolute_url(self):
        return f'/person/{self.id}'

    class Meta:
        verbose_name = 'Person'
