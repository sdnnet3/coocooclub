from django.shortcuts import render, redirect
from .models import Coupon
from .forms import CouponForm, CouponApplyForm
from django.views.generic import DetailView
from django.contrib import messages
# Create your views here.

def coupon_view(request):
	form = CouponForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = CouponForm()
	context = {
		'form' : form
	}
	return render(request, 'coupons/coupon.html', context)

class CouponRedeemDetail(DetailView):
	model = Coupon