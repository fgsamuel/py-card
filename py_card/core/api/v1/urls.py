from django.urls import include
from django.urls import path
from rest_framework import routers

from py_card.core.api.v1.views import CreditCardView

router = routers.DefaultRouter()
router.register(r"credit-card", CreditCardView)


urlpatterns = [
    path("", include(router.urls)),
]
