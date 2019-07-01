from django.db import models

# Create your models here.
class Coupon(models.Model):
	first = models.CharField(max_length = 80)
	last = models.CharField(max_length = 80, default="")
	identification = models.IntegerField(unique = True)
	redeemed = models.BooleanField(default = False)
	email = models.EmailField(max_length=70, null=True, blank=True, unique=True)

	def __str__(self):
		return self.last