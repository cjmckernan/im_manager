from django.db import models
from django.contrib.auth.models import AbstractUser


class ImCompany(models.Model):
    business_name = models.CharField(max_length=100)
    contact_email = models.CharField(max_length=255)
    contact_phone_number = models.CharField(max_length=55)

    def __str__(self):
        return self.business_name

class CustomUser(AbstractUser):
    company = models.ForeignKey(ImCompany, null=True, on_delete=models.DO_NOTHING)
    is_manager = models.BooleanField(default=False)
