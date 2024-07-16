from .models import Payment
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from inventory.mixins import CompanyFilterMixin


class PaymentListView(LoginRequiredMixin, CompanyFilterMixin, ListView):
    model = Payment
    template_name = "payments/payment_list.html"
