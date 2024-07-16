from django.urls import path
from .views import InventoryListView, InventoryUpdateView, InventoryDeleteView, InventoryCreateView

urlpatterns = [
    path("", InventoryListView.as_view(), name="inventory_list"),
    path('edit/<int:pk>/', InventoryUpdateView.as_view(), name='inventory_edit'),
    path('add/', InventoryCreateView.as_view(), name='inventory_create'),
    path('delete/<int:pk>/', InventoryDeleteView.as_view(), name='inventory_delete'),
]
