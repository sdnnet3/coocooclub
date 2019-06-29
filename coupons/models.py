from django.db import models

# Create your models here.
class Coupon(models.Model):
	firstName = models.CharField(max_length = 80)
	identification = models.IntegerField(unique = True)
	redeemed = models.BooleanField(default = False)