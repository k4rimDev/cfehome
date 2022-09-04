from rest_framework import generics


from products.models import Product
from products.serializers import ProductSerializer


class ProoductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # lookup_field = 'pk'
    