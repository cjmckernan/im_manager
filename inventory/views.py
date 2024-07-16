from django.contrib.auth.mixins import LoginRequiredMixin
from .models import InventoryItem
from .forms import InventoryItemForm
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .mixins import CompanyFilterMixin, CompanyObjectMixin, CompanyCreateMixin

class InventoryListView(LoginRequiredMixin, CompanyFilterMixin, ListView):
    model = InventoryItem
    template_name = "inventory/inventory_list.html"


class InventoryUpdateView(LoginRequiredMixin, CompanyObjectMixin, UpdateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/inventory_edit.html'
    success_url = reverse_lazy('inventory_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Edit'
        return context

class InventoryDeleteView(LoginRequiredMixin, CompanyObjectMixin, DeleteView):
    model = InventoryItem
    template_name = 'inventory/inventory_confirm_delete.html'
    success_url = reverse_lazy('inventory_list')

class InventoryCreateView(LoginRequiredMixin, CompanyCreateMixin, CreateView):
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'inventory/inventory_add.html'
    success_url = reverse_lazy('inventory_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action'] = 'Create'
        return context

