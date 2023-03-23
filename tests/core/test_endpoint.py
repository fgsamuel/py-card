import pytest

from py_card.core.api.v1.serializers import CreditCardSerializer
from py_card.core.models import CreditCard


class TestCreditCardEndpoint:
    @pytest.fixture
    def credit_card_data(self):
        return {
            "number": "4539578763621486",
            "holder": "John Doe",
            "exp_date": "01/2030",
            "cvv": "1234",
        }

    @pytest.mark.django_db
    def test_create_credit_card(self, admin_client, credit_card_data):
        response = admin_client.post("/api/v1/credit-card/", credit_card_data)
        assert response.status_code == 201
        assert response.data["number"] == credit_card_data["number"]
        assert response.data["holder"] == credit_card_data["holder"]
        assert response.data["exp_date"] == credit_card_data["exp_date"]
        assert response.data["cvv"] == credit_card_data["cvv"]
        assert response.data["brand"].lower() == "visa"
        assert CreditCard.objects.count() == 1

    @pytest.mark.django_db
    def test_list_credit_card(self, admin_client, credit_card_data):
        serializer = CreditCardSerializer(data=credit_card_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = admin_client.get("/api/v1/credit-card/")

        assert response.status_code == 200
        assert len(response.data) == 1
        assert response.data[0]["number"] == credit_card_data["number"]
        assert response.data[0]["holder"] == credit_card_data["holder"]
        assert response.data[0]["exp_date"] == credit_card_data["exp_date"]
        assert response.data[0]["cvv"] == credit_card_data["cvv"]
        assert response.data[0]["brand"].lower() == "visa"

    @pytest.mark.django_db
    def test_retrieve_credit_card(self, admin_client, credit_card_data):
        serializer = CreditCardSerializer(data=credit_card_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = admin_client.get(f"/api/v1/credit-card/{serializer.instance.id}/")

        assert response.status_code == 200
        assert response.data["number"] == credit_card_data["number"]
        assert response.data["holder"] == credit_card_data["holder"]
        assert response.data["exp_date"] == credit_card_data["exp_date"]
        assert response.data["cvv"] == credit_card_data["cvv"]
        assert response.data["brand"].lower() == "visa"

    @pytest.mark.django_db
    def test_non_authenticated_user_with_obsfuscated_number(self, client, credit_card_data):
        serializer = CreditCardSerializer(data=credit_card_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = client.get(f"/api/v1/credit-card/{serializer.instance.id}/")

        assert response.status_code == 200
        assert response.data["number"] == "4539********1486"
        assert response.data["cvv"] == "****"
