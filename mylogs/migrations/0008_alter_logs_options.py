# Generated by Django 3.2.3 on 2021-06-15 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mylogs', '0007_auto_20210615_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logs',
            options={'ordering': ['path', 'method']},
        ),
    ]