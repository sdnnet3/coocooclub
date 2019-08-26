from django.db import models

# Create your models here.
class Coupon(models.Model):
	identification = models.IntegerField(primary_key=True, unique = True)
	first = models.CharField(max_length = 80)
	last = models.CharField(max_length = 80, default="")
	active = models.BooleanField(default = True)
	email = models.EmailField(max_length=70, null=True, blank=True, unique=True)

	def __str__(self):
		return self.last