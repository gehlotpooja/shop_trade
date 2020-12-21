from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .controllers import *
# Create your views here.


@api_view(['POST'])
def save_user_using_csv_api(request):
    data = {
        'success': False,
        'msg': 'No data saved'
    }
    try:
        data = save_user_using_csv(request)
    except Exception as e:
        print(e.args)
    return Response(data = data, status=status.HTTP_200_OK)


@api_view(['POST'])
def save_product_using_csv_api(request):
    data = {
        'success': False,
        'msg': 'No product available'
    }
    try:
        data = save_product_using_csv(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def place_order_api(request):
    data = {
        'success': False,
        'msg': 'No order available'
    }
    try:
        data = place_order(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete_order_detail_entry(request):
    try:
        request_data = request.data.get('id')

        OrderDetails.objects.filter(id = request_data).delete()
        data = "data deleted"
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_order_details_api(request):
    data ={
        'success': False,
        'msg': 'No data',
        'data': 'NA'
    }
    try:
        data = get_order_details(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def update_user_api(request):
    data = {
        'success':False,
        'msg':'No data to fetch'
    }
    try:
        data = update_user(request)
    except Exception as e:
        print(e.args)
    return Response(data = data,status=status.HTTP_200_OK)