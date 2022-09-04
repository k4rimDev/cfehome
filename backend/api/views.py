import json
from django.forms.models import model_to_dict

from rest_framework.response import Response
from rest_framework.decorators import api_view

from products.models import Product
from products.serializers import ProductSerializer


# def api_home(request, *args, **kwargs):
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass

#     print(data)
#     data['headers'] = dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)


@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data = request.data)
    instance = Product.objects.all().order_by("?").first()
    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        return Response(serializer.data)
    # data = {}
    # if instance: 
    #     data = ProductSerializer(instance).data
    # return Response(data)