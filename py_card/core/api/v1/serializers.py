from rest_framework.serializers import ModelSerializer

from py_card.core.models import CreditCard


class CreditCardSerializer(ModelSerializer):
    class Meta:
        model = CreditCard
        fields = "__all__"
