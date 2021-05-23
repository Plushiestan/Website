# Generated by Django 3.2.2 on 2021-05-07 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_datestart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='hasDate',
        ),
        migrations.AlterField(
            model_name='event',
            name='dateEnd',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='hashtag',
            field=models.CharField(blank=True, default='#', max_length=100, null=True, verbose_name='Hashtag'),
        ),
        migrations.AlterField(
            model_name='event',
            name='isRecurringAnnually',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Annually'),
        ),
        migrations.AlterField(
            model_name='event',
            name='isRecurringMonthly',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Monthly?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='isRecurringWeekly',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Weekly?'),
        ),
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.CharField(blank=True, default='@', max_length=100, null=True, verbose_name='Hashtag Organizer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='recurringDay',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Recurring Week Day'),
        ),
    ]
