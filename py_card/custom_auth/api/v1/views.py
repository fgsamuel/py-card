from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from py_card.custom_auth.models import CustomUser
from py_card.custom_auth.serializers import CustomUserRegisterSerializer


class RegisterUserView(CreateModelMixin, GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserRegisterSerializer
