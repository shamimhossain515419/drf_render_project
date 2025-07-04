from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Product
from api.serializers import ProductSerializer

from rest_framework import viewsets


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "Hello, World!"})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
