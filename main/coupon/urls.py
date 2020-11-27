
from django.urls import path
from .views import order_detail_coupon,orders_list,remove_coupon
urlpatterns = [

    path('order_detail/<id>', order_detail_coupon, name='order_detail_coupon'),
    path('remove/<id>', remove_coupon, name='remove_coupon'),
    path('orders/',orders_list,name='orders_list'),

]
