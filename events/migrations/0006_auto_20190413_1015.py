# Generated by Django 2.1.7 on 2019-04-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20190328_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='information',
            name='Title',
            field=models.CharField(max_length=150),
        ),
    ]
