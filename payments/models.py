from django.db import models
from django.conf import settings
from im_users.models import ImCompany
from inventory.mixins import CompanyFilterMixin


class Payment(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE
    )
    company = models.ForeignKey(ImCompany, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_id} - {self.amount}"
