# Generated by Django 2.1.7 on 2019-03-29 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190328_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstTitle', models.CharField(max_length=50)),
                ('firstText', models.TextField(max_length=300)),
                ('firstPhoto', models.ImageField(blank=True, default='default.jpg', upload_to='')),
                ('secondTitle', models.CharField(max_length=50)),
                ('secondText', models.TextField(max_length=300)),
                ('secondPhoto', models.ImageField(blank=True, default='default.jpg', upload_to='')),
                ('thirdTitle', models.CharField(max_length=50)),
                ('thirdText', models.TextField(max_length=300)),
                ('thirdPhoto', models.ImageField(blank=True, default='default.jpg', upload_to='')),
                ('fourthTitle', models.CharField(max_length=50)),
                ('fourthText', models.TextField(max_length=300)),
                ('fourthPhoto', models.ImageField(blank=True, default='default.jpg', upload_to='')),
            ],
        ),
    ]
