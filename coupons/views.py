from django.shortcuts import render
from .forms import CouponForm
# Create your views here.

def coupon_view(request):
	form = CouponForm(request.POST or None)
	if form.is_valid():
		from.save()
	context = {
		'form' : form
	}
	return render(request, 'coupons/coupon.html', context)