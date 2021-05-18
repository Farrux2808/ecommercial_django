from django.http import response
from ..models import Products
from rest_framework.response import Response
from rest_framework import status
from ..models import Category
from ..models import Measurement


class PrductView:
    def add_product(req):
        try:
            Products(
                category_id = Category.objects.get(id=req.get('category_id', 0)),
                name = req.get('name',''),
                price = req.get('price', 0),
                voluem = req.get('voluem', 0),
                measurement_id = Measurement.objects.get(id=req.get('measurement_id', 0)),
                info = req.get('info', ''),
            ).save()
            return Response({
                "status": "success"
            },
            status=status.HTTP_201_CREATED)
        except:
            return Response({
                "status": "data couldn't added"
            }, status=status.HTTP_400_BAD_REQUEST)
    
    def get_products(req):
        res = Products.objects.all().values()
        return Response(res, status=status.HTTP_200_OK)
