from django import forms

from .models import Coupon

class CouponForm(forms.ModelForm):
	class Meta:
		model = Coupon
		fields = [
			'first',
			'last',
			'identification',
			'email'
			]

class CouponApplyForm(forms.ModelForm):
	class Meta:
		model = Coupon
		fields = [
		'identification',
		'active'
		]