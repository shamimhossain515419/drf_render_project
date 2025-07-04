from django.urls import path, include
from .views import hello_world

from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("hello/", hello_world),
    path("", include(router.urls)),
]
