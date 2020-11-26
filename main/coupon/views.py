from django.shortcuts import render
from .models import Coupon,Order
# Create your views here.

def orders_list(request):
    context={
        'objects':Order.objects.all()
    }
    return render(request,'coupon/orders.html',context)
def coupon(request):

    context={

    }
    return render(request,'coupon/coupon.html',context)