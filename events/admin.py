from django.contrib import admin
from .models import event, information

# Register your models here.
admin.site.register(event)
admin.site.register(information)
admin.site.site_header = 'Event Dashboard'