from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET", "POST"])
def home(request, *args, **kwargs):
    if request.method == "GET":
        # chose randome product from db
        product = Product.objects.all().order_by("?").first()
        data = ProductSerializer(product).data
        return Response(data)
    elif request.method == "POST":
        # verify that given data is correct
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)
