from rest_framework import generics, permissions, authentication

from api.authentication import BearerTokenAuthentification
from .models import Product
from .serializers import ProductSerializer


class ListCreateProductApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication, BearerTokenAuthentification]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer: ProductSerializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = "Default content"
        serializer.save(content=content)


class ProductDetailsApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UpdateProductApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class DeleteProductApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
