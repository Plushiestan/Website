# Generated by Django 3.2.2 on 2021-05-07 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210507_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dateStart',
            field=models.DateField(blank=True, null=True, verbose_name='Date Start'),
        ),
    ]
