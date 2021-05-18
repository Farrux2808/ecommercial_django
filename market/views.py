from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .view.category import CategoryView
from .view.measurement import MeasurementView
from .view.products import PrductView

@api_view(['POST'])
def add_category(request):
    response = CategoryView.add(request.data)
    return Response(response)

@api_view(['GET'])
def get_categorys(request):
    response = CategoryView.get_all()
    return Response(response)

@api_view(['GET'])
def get_category(request):
    response = CategoryView.get(request.GET['id'])
    return Response(response)

@api_view(['DELETE'])
def del_category(request):
    response = CategoryView.delete(request.GET['id'])
    return Response(response)

@api_view(['PUT'])
def update_category(request):
    response = CategoryView.update(request.GET['id'], request.data)
    return Response(response)



@api_view(['POST'])
def add_measurement(request):
    response = MeasurementView.add(request.data)
    return Response(response)

@api_view(['GET'])
def get_measurements(request):
    response = MeasurementView.get_all()
    return Response(response)

@api_view(['GET'])
def get_measurement(request):
    response = MeasurementView.get(request.GET['id'])
    return Response(response)

@api_view(['DELETE'])
def del_measurement(request):
    response = MeasurementView.delete(request.GET['id'])
    return Response(response)

@api_view(['PUT'])
def update_measurement(request):
    response = MeasurementView.update(request.GET['id'], request.data)
    return Response(response)


@api_view(['POST'])
def add_product(request):
    response = PrductView.add_product(request.data)
    return response

@api_view(['GET'])
def get_products(request):
    response = PrductView.get_products(request.data)
    return response