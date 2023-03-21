from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from py_card.core.api.v1.serializers import CreditCardSerializer
from py_card.core.models import CreditCard


class CreditCardView(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer
