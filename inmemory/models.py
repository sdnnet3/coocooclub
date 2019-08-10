from django.db import models

# Create your models here.

class People(models.Model):
	firstName = models.CharField(max_length = 60)
	lastName = models.CharField(max_length = 60)
	born = models.DateField(auto_now_add=False, blank=True)
	passed = models.DateField(auto_now_add=False, blank=True)
	created = models.DateTimeField(auto_now_add = True)
	photo = models.ImageField(default = 'default.jpg', blank = True)

	def __str__(self):
		return self.firstName