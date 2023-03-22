import re

from rest_framework import serializers

from py_card.core.api.v1.fields import MonthYearSerializerField
from py_card.core.models import CreditCard


class CreditCardSerializer(serializers.ModelSerializer):
    exp_date = MonthYearSerializerField()

    class Meta:
        model = CreditCard
        fields = "__all__"

    def validate_holder(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("The field must have at least 2 characters.")
        return value

    def validate_cvv(self, value):
        pattern = re.compile(r"^\d{3,4}$")
        if not pattern.match(value):
            raise serializers.ValidationError("The field must have 3 or 4 digits.")
        return value
