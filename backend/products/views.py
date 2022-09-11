from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    def perform_create(self, serializer):
        print(serializer.validated_data)

        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)


class ProoductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProoductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProoductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)




# class ProoductListAPIView(generics.ListAPIView):
    """
    NOT gonna use this method, use ListCreateAPIView used
    """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


"""
    Function based view (Create and list)
"""
# @api_view(['GET', 'POST'])
# def product_alt_view(request, pk = None, *args, **kwargs):
#     method = request.method 

#     if method == 'GET':
#         if pk is not None:
#             # detail view
#             product = get_object_or_404(Product, pk = pk)
#             data = ProductSerializer(product, many=False).data
#             return Response(data)

#         queryset = Product.objects.all() # QS
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == 'POST':
#         # create item
#         serializer = ProductSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content') or None
#             if content is None:
#                 content = title
#             serializer.save(content = content)
#             return Response(serializer.data)
#         return Response({"invalid": "Not good data"}, status=400)

