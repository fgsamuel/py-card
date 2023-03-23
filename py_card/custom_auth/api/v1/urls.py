from django.urls import include
from django.urls import path
from rest_framework import routers

from py_card.custom_auth.api.v1.views import RegisterUserView

router = routers.DefaultRouter()
router.register(r"users", RegisterUserView)


urlpatterns = [
    path("", include(router.urls)),
]
