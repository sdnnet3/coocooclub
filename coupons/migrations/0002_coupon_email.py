# Generated by Django 2.1.7 on 2019-06-30 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='email',
            field=models.EmailField(blank=True, max_length=70, null=True, unique=True),
        ),
    ]