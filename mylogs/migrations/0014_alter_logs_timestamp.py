# Generated by Django 3.2.3 on 2021-06-16 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylogs', '0013_alter_logs_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]