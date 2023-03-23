from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from py_card.core.api.v1.serializers import CreditCardDetailSerializer
from py_card.core.api.v1.serializers import CreditCardSerializer
from py_card.core.models import CreditCard


class CreditCardView(CreateModelMixin, RetrieveModelMixin, ListModelMixin, GenericViewSet):
    queryset = CreditCard.objects.all()
    serializer_class = CreditCardSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return CreditCardSerializer
        return CreditCardDetailSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        detail_serializer = CreditCardDetailSerializer(serializer.instance, context=self.get_serializer_context())
        return Response(detail_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
