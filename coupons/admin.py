from django.contrib import admin
from .models import Coupon



class CouponAdmin(admin.ModelAdmin):
	list_distplay = ['identification', 'active']
	list_filter = ['active']
	search_fields = ['identification']
# Register your models here.
admin.site.register(Coupon, CouponAdmin)