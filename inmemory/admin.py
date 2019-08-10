from django.contrib import admin
from .models import People

# Register your models here.
admin.site.register(People)
admin.site.site_header = 'Memory Dashboard'