from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .controllers import *


@api_view(['POST'])
def get_order_details_api(request):
    data = {
        'success': False,
        'msg': 'No order available',
        'data': 'NA'
    }
    try:
        data = get_order_details(request)
    except Exception as e:
        print(e.args)
    return Response(data = data, status=status.HTTP_200_OK)


@api_view(['POST'])
def save_user_details_api(request):
    data = {
        'success': False,
        'msg': 'No data received',
    }
    try:
        data = save_user_details(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_order_api(request):
    data = {
        'success':False,
        'msg':'No data to fetch',
        'data':[]
    }
    try:
        data = get_user_order(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_order_list_api(request):
    data = {
        'success':False,
        'msg':'No data to fetch',
        'data':[]
    }
    try:
        data = get_order_list(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
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


@api_view(['POST'])
def save_store_details_api(request):
    data = {
        'success': False,
        'msg': 'No data received',
    }
    try:
        data = save_store_details(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)
