from django import views
from django.urls import path
from .views import *

urlpatterns = [
   path('', CreatePayment.as_view(), name='home'),
    path('payment/', payment_form, name='payment_form'),
]
