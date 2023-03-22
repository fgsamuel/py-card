import pytest

from py_card.core.api.v1.serializers import CreditCardSerializer


class TestCreditCardSerializer:
    @pytest.fixture
    def credit_card_data(self):
        return {
            "number": "1234567890123456",
            "holder": "John Doe",
            "exp_date": "01/2030",
            "cvv": "1234",
        }

    def test_min_length_holder(self, credit_card_data):
        credit_card_data["holder"] = "A"
        serializer = CreditCardSerializer(data=credit_card_data)
        assert not serializer.is_valid()
        assert "holder" in serializer.errors

    def test_min_length_cvv(self, credit_card_data):
        credit_card_data["cvv"] = "12"
        serializer = CreditCardSerializer(data=credit_card_data)
        assert not serializer.is_valid()
        assert "cvv" in serializer.errors

    def test_max_length_cvv(self, credit_card_data):
        credit_card_data["cvv"] = "12345"
        serializer = CreditCardSerializer(data=credit_card_data)
        assert not serializer.is_valid()
        assert "cvv" in serializer.errors
