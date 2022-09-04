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


@api_view(['GET'])
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance: 
        data = ProductSerializer(instance).data
    return Response(data)