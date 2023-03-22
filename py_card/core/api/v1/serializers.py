from rest_framework import serializers

from py_card.core.api.v1.fields import MonthYearSerializerField
from py_card.core.models import CreditCard


class CreditCardSerializer(serializers.ModelSerializer):
    exp_date = MonthYearSerializerField()

    class Meta:
        model = CreditCard
        fields = "__all__"
