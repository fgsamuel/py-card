from django.db import models


class CreditCard(models.Model):
    number = models.CharField(max_length=16)
    holder = models.CharField(max_length=100)
    exp_date = models.DateField()
    cvv = models.CharField(max_length=4, blank=True)
    brand = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.holder
