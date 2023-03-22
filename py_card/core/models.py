from django.db import models


class CreditCard(models.Model):
    number = models.CharField(max_length=16, unique=True)
    holder = models.CharField(max_length=100)
    exp_date = models.DateField()
    cvv = models.CharField(max_length=4, blank=True)
    brand = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):  # pragma: no cover
        return self.holder
