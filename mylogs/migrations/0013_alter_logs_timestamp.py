# Generated by Django 3.2.3 on 2021-06-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mylogs', '0012_alter_logs_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logs',
            name='timestamp',
            field=models.DateTimeField(verbose_name='timestamp'),
        ),
    ]
