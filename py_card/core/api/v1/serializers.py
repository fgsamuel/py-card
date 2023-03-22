import re

import creditcard

from creditcard.exceptions import BrandNotFound
from rest_framework import serializers

from py_card.core.api.v1.fields import MonthYearSerializerField
from py_card.core.models import CreditCard


class CreditCardSerializer(serializers.ModelSerializer):
    exp_date = MonthYearSerializerField()

    class Meta:
        model = CreditCard
        fields = ["id", "number", "holder", "exp_date", "cvv"]

    def validate_holder(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("The field must have at least 2 characters.")
        return value

    def validate_cvv(self, value):
        pattern = re.compile(r"^\d{3,4}$")
        if not pattern.match(value):
            raise serializers.ValidationError("The field must have 3 or 4 digits.")
        return value

    def validate_number(self, value):
        cc = creditcard.CreditCard(value)
        if not cc.is_valid():
            raise serializers.ValidationError("The field must have a valid credit card number.")
        return value

    def validate(self, attrs):
        try:
            attrs["brand"] = creditcard.CreditCard(attrs["number"]).get_brand()
        except BrandNotFound:
            attrs["brand"] = ""

        return attrs


class CreditCardDetailSerializer(CreditCardSerializer):
    class Meta:
        model = CreditCard
        fields = ["id", "number", "holder", "exp_date", "cvv", "brand", "created_at"]
