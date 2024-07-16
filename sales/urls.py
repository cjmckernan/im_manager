from django.urls import path
from .views import SaleCreateView, sale_checkout, checkout
from django.views.generic import TemplateView
urlpatterns = [
    path("sale/", SaleCreateView.as_view(), name="sale_create"),
    path("checkout/", checkout, name="checkout"),
    path("sale_checkout/", sale_checkout, name="sale_checkout"),
    path("payment_success/", TemplateView.as_view(template_name="sales/payment_success.html"), name="payment_success"),
]
