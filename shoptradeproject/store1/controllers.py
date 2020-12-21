from .serializers import *
import csv
from.models import UserDetails, Product, OrderDetails, ProductOrderMapping


def save_user_using_csv(request):
    """Imports and save a list of customers from a CSV file"""
    success = False
    msg = 'No data saved'
    try:
        csvfile = request.FILES.get('file').read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csvfile)

        for row in csv_reader:
            user_obj = UserDetails()
            user_obj.first_name = row.get('first_name')
            user_obj.last_name = row.get('last_name')
            user_obj.email = row.get('email')
            user_obj.phone = row.get('phone')
            user_obj.save()
            success = True
            msg = 'Data saved successfully'

    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def save_product_using_csv(request):
    """Imports and save a list of products from a CSV file"""
    success = False
    msg = 'No product to save'
    try :
        csvfile = request.FILES.get('file').read().decode('utf-8').splitlines()
        csv_reader = csv.DictReader(csvfile)
        obj_list = []
        for row in csv_reader:
            product_obj = Product()
            product_obj.name = row.get('name')
            product_obj.price = row.get('price')
            obj_list.append(product_obj)
        Product.objects.bulk_create(obj_list)
        success = True
        msg = 'Data saved successfully'

    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def place_order(request):
    """Placing order"""
    success = False
    msg = 'No order placed'
    try:
        post_data = request.data
        user_id = post_data.get('user_id')
        order_obj_id = post_data.get('order_obj_id')
        item_list = post_data.get("item_ids")
        if user_id and order_obj_id is None:
            order_obj = OrderDetails()
            order_obj.user_id = user_id
            order_obj.save()
            order_id = order_obj.id
        elif order_obj_id:
            order_id = order_obj_id

        add_item_list = []
        for item in item_list:
            product_order_obj = ProductOrderMapping()
            product_order_obj.order_id = order_id
            product_order_obj.product_id = item
            add_item_list.append(product_order_obj)
        ProductOrderMapping.objects.bulk_create(add_item_list)
        success = True
        msg = 'Data saved successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def get_order_details(request):
    """Getting order details"""
    success = False
    msg = 'No data available'
    data = []
    try:
        get_data = request.GET
        user_id = get_data.get('user_id')
        start_date = get_data.get('start_date')
        end_date = get_data.get('end_date')
        if user_id and start_date and end_date:
            order_obj = OrderDetails.objects.filter(user_id=user_id, order_date__gt=start_date, order_date__lt=end_date)
        elif start_date and end_date:
            order_obj = OrderDetails.objects.filter(order_date__gt=start_date, order_date__lt=end_date)
        elif user_id:
            order_obj = OrderDetails.objects.filter(user_id=user_id)
        else:
            order_obj = OrderDetails.objects.filter()
        serializer = GetOrderDetailsSerializer(order_obj, many= True)
        data = serializer.data
        success = True
        msg = 'Data fetched'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg, 'data':data}


def update_user(request):
    """Update user email on the basis of user_id"""
    success = False
    msg = 'failed to update user details'
    try:
        post_data = request.GET
        user_data = UserDetails.objects.filter(id=post_data.get('user_id'))
        user_data = user_data[0]
        user_data.email = post_data.get('email')
        user_data.save()

        success = True
        msg = 'User data updated successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}