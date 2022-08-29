from django.urls import path
from .views import coffee_payment, payment_status,coffee_payment1
# from sgoapp_ebikes.views import CustoRead



urlpatterns = [
    path('pay', coffee_payment, name='coffee-payment'),
    path('dealerpay', coffee_payment1, name='coffee-payment'),
    path('payment-status', payment_status, name='payment-status'),

]
