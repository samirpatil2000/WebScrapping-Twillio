
from django.urls import path
from .views import order_detail_coupon,orders_list
urlpatterns = [

    path('c/<id>', order_detail_coupon, name='order_detail_coupon'),
    path('',orders_list,name='orders_list'),

]
