# Generated by Django 2.1.7 on 2019-03-28 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(blank=True),
        ),
    ]
