# Generated by Django 3.2.2 on 2021-05-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0002_auto_20210507_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='instagramName',
            field=models.CharField(default='@', max_length=100, verbose_name='Instagram Account Name'),
        ),
    ]
