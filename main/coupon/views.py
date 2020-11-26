from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Coupon,Order
from .forms import CouponForm
# Create your views here.

def orders_list(request):
    context={
        'objects':Order.objects.all()
    }
    return render(request,'coupon/orders.html',context)
def order_detail_coupon(request,id):
    order=Order.objects.get(id=id)
    couponForm=CouponForm()
    if request.method=='POST':
        couponForm=CouponForm(request.POST)
        if couponForm.is_valid():
            coupon=couponForm.cleaned_data['coupon']
            try:
                coupon=Coupon.objects.get(code=coupon,
                                          valid_from__lte=timezone.now(),
                                          valid_to__gte=timezone.now(),
                                          is_active=True)
                order.coupon=coupon
                order.save()
                messages.success(request,f"Coupon has been successfully Applied with discount{coupon.discount}")

            except Coupon.DoesNotExist:
                messages.warning(request,"Invalid Coupon")

        return redirect('order_detail_coupon',id=id)




    context={
        'object':order,
        'form':couponForm,
    }
    return render(request,'coupon/coupon.html',context)

