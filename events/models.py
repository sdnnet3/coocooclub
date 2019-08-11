from django.db import models
from django.utils.text import slugify

# Create your models here.

class event(models.Model):
	title = models.CharField(max_length = 160)
	body = models.TextField(max_length = 700)
	date = models.DateTimeField(auto_now_add=False, blank=True)
	created = models.DateTimeField(auto_now_add = True)
	thumb = models.ImageField(default = 'default.jpg', blank = True)
	slug = models.SlugField(blank = True)

	def __str__(self):
		return self.title

	def body_preview(self):
		return self.body[:50]

class information(models.Model):
	Title = models.CharField(max_length = 150)
	Text = models.TextField(max_length = 300)
	Photo = models.ImageField(default = 'default.jpg', blank = True)
	slug = models.SlugField(blank = True)

	def __str__(self):
		return self.Title