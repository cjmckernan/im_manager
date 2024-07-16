import json, uuid
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from inventory.mixins import CompanyFilterMixin
from payments.models import Payment
from inventory.models import InventoryItem
from .forms import CreditCardForm
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


class SaleCreateView(LoginRequiredMixin, CompanyFilterMixin, ListView):
    model = InventoryItem
    template_name = "sales/sale_generate.html"
    context_object_name = "inventory_items"


@login_required
def checkout(request):
    if request.method == "POST":
        data = json.loads(request.body)
        items = data.get("items", [])
        total = data.get("total", 0.0)

        request.session["checkout_items"] = items
        request.session["checkout_total"] = total

        return JsonResponse({"success": True})
    return JsonResponse({"success": False}, status=400)


@login_required
def sale_checkout(request):
    items = request.session.get("checkout_items", [])
    total = request.session.get("checkout_total", 0.0)

    if request.method == "POST":
        form = CreditCardForm(request.POST)
        if form.is_valid():
            company = request.user.company
            transaction_id = str(uuid.uuid4())
            Payment.objects.create(
                transaction_id=transaction_id,
                user=request.user,
                company=company,
                amount=total,
                status="Success",
            )

            for item in items:
                inventory_item = InventoryItem.objects.get(id=item["itemId"])
                inventory_item.quantity -= item["quantity"]
                inventory_item.save()

            return redirect("payment_success")
    else:
        form = CreditCardForm()

    return render(
        request,
        "sales/sale_checkout.html",
        {"items": items, "total": total, "form": form},
    )
