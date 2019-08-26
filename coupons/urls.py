from django.contrib import admin
from django.urls import path
from . views import coupon_view, CouponRedeemDetail



app_name = 'coupons'

urlpatterns = [
    path('', coupon_view, name = 'main'),
    path('redeem/<int:pk>/', CouponRedeemDetail.as_view(), name='redeem'),
]