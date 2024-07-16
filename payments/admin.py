from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("transaction_id", "user", "company", "amount", "date", "status")
    search_fields = (
        "transaction_id",
        "user__username",
        "company__name",
        "amount",
        "status",
    )
