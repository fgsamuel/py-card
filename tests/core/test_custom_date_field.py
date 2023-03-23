import datetime

from datetime import date

import pytest

from py_card.core.api.v1.serializers import CreditCardSerializer
from py_card.core.models import CreditCard


class TestMonthYearSerializerField:
    @pytest.fixture
    def credit_card_data(self):
        return {
            "number": "4539578763621486",
            "holder": "John Doe",
            "exp_date": "01/2030",
            "cvv": "1234",
        }

    @pytest.mark.django_db
    def test_valid_date_format(self, credit_card_data):
        serializer = CreditCardSerializer(data=credit_card_data)
        assert serializer.is_valid(raise_exception=True)

    @pytest.mark.django_db
    def test_invalid_date_range(self, credit_card_data):
        credit_card_data["exp_date"] = "13/2030"
        serializer = CreditCardSerializer(data=credit_card_data)
        assert not serializer.is_valid()
        assert "exp_date" in serializer.errors

    @pytest.mark.django_db
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

    @pytest.mark.django_db
    def test_expired_date(self, credit_card_data):
        year = datetime.datetime.now().year - 1
        credit_card_data["exp_date"] = f"01/{year}"
        serializer = CreditCardSerializer(data=credit_card_data)
        assert not serializer.is_valid()
        assert "exp_date" in serializer.errors
