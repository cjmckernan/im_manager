from django.db import models
from im_users.models import ImCompany


class InventoryItem(models.Model):
    item_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=200)
    expiration_date = models.DateField()
    company = models.ForeignKey(ImCompany, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ("company", "item_name")

    def __str__(self):
        return self.item_name
