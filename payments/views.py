from .models import Payment
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = "payments/payment_list.html"



