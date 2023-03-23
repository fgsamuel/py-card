import pytest

from py_card.custom_auth.models import CustomUser


class TestRegisterUserEndpoint:
    @pytest.mark.django_db
    def test_register_user(self, client):
        response = client.post("/api/v1/users/", data={"email": "a@a.com", "password": "123456"})
        assert response.status_code == 201
        assert CustomUser.objects.count() == 1
