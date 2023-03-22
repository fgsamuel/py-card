from datetime import date

import pytest

from py_card.core.api.v1.serializers import CreditCardSerializer
from py_card.core.models import CreditCard


class TestMonthYearSerializerField:
    @pytest.fixture
    def credit_card_data(self):
        return {
            "number": "1234567890123456",
            "holder": "John Doe",
            "exp_date": "01/2030",
            "cvv": "1234",
        }

    def test_valid_date_format(self, credit_card_data):
        serializer = CreditCardSerializer(data=credit_card_data)
        assert serializer.is_valid()

    def test_invalid_date_range(self, credit_card_data):
        credit_card_data["exp_date"] = "13/2030"
        serializer = CreditCardSerializer(data=credit_card_data)
        assert not serializer.is_valid()
        assert "exp_date" in serializer.errors

    def test_invalid_date_format(self, credit_card_data):
        credit_card_data["exp_date"] = "01/30"
        serializer = CreditCardSerializer(data=credit_card_data)
        assert not serializer.is_valid()
        assert "exp_date" in serializer.errors

    @pytest.mark.django_db
    def test_saved_data_format_last_month_day(self, credit_card_data):
        serializer = CreditCardSerializer(data=credit_card_data)
        assert serializer.is_valid()
        serializer.save()
        credit_card = CreditCard.objects.first()
        assert credit_card.exp_date == date(2030, 1, 31)
