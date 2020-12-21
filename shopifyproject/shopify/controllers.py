import requests
from .models import *
from .serializers import GetOrderCountDetailSerializer, GetOrderListSerializer
from django.db.models import Q


def get_order_details(request):
    """
    1. Trigger a customer & order ingestion from the store on the basis of user_id, start and end date.
    """
    success = False
    msg = 'no data to save'
    try:
        post_data = request.POST
        user_id = post_data.get('user_id')
        start_date = post_data.get('start_date')
        end_date = post_data.get('end_date')
        store_id = post_data.get('store_id')
        if store_id:
            store_obj = StoreDetails.objects.filter(id=store_id).values_list('store_domain', flat=True)
            if store_obj:
                store_domain = store_obj[0]
                url_data = requests.get(store_domain + 'store1/get_order_details/',
                                        params={"user_id": user_id, "start_date": start_date,
                                                "end_date": end_date})
                json_data = url_data.json()
                data = json_data.get("data")
                success = True
                msg = 'Order data saved successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg, 'data': data}


def save_user_details(request):
    """Gets data of users,order and order item from store1. Check for existing data , if data does not exist then creates
    the entry of new data in DB tables"""
    success = False
    msg = 'no new data to save'
    try :
        post_data = request.POST
        user_id = post_data.get('user_id')
        start_date = post_data.get('start_date')
        end_date = post_data.get('end_date')
        store_id = post_data.get('store_id')
        if store_id:
            store_obj = StoreDetails.objects.filter(id=store_id).values_list('store_domain', flat=True)
            if store_obj:
                store_domain = store_obj[0]
                url_data = requests.get(store_domain + 'store1/get_order_details/',
                                        params={"user_id": user_id, "start_date": start_date,
                                                "end_date": end_date})
                json_data = url_data.json()
                json_data = json_data.get("data")
                if len(json_data)>0:

                    for i in json_data:
                        json_data_user_id = i.get('user_id')
                        json_data_order_number = i.get('order_id')
                        user_obj = UserDetails.objects.filter(user_store_id=json_data_user_id)
                        old_order_obj = Order.objects.filter(order_number=json_data_order_number)
                        if not old_order_obj:
                            if not user_obj:
                                new_user_obj = UserDetails()
                                new_user_obj.user_store_id = json_data_user_id
                                new_user_obj.first_name = i.get("first_name")
                                new_user_obj.last_name = i.get("last_name")
                                new_user_obj.email = i.get("email")
                                new_user_obj.phone = i.get("phone")
                                new_user_obj.save()
                            else:
                                new_user_obj = user_obj[0]
                            order_obj = Order()
                            order_obj.user_id = new_user_obj.id
                            order_obj.order_date = i.get("order_date")
                            order_obj.order_number = i.get("order_id")
                            order_obj.save()
                            if len(i.get('order_items')) > 0:
                                order_item_list = i.get('order_items')
                                for j in order_item_list:
                                    order_item_obj = OrderItem()
                                    order_item_obj.order_id = order_obj.id
                                    order_item_obj.item_name = j.get('item_name')
                                    order_item_obj.item_price = j.get('item_price')
                                    order_item_obj.save()
                            success = True
                            msg = 'Data saved successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def get_user_order(request):
    """02.View a list of Customers alongside their aggregated order count / total
    Customer can be searched on the basis of email or name"""
    success = False
    msg = 'Enter valid user id'
    data = []
    try:
        get_data = request.GET
        name = get_data.get('name', None)
        email = get_data.get('email', None)
        extra_filter = Q()
        if name or email:
            if name and ' ' in name:
                first_name, last_name = name.split(' ')
            else:
                first_name = name
                last_name = name
            if first_name or last_name:
                extra_filter = Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name)
            if email:
                extra_filter.add(Q(email__icontains=email), Q.OR)
        user_obj = UserDetails.objects.filter(extra_filter)
        serializer = GetOrderCountDetailSerializer(user_obj, many=True)
        data = serializer.data
        success = True
        msg = 'Data fetched successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg, 'data': data}


def get_order_list(request):
    """03. View a list of orders over a certain threshold"""
    success = False
    msg = 'Enter valid user id'
    data = []
    try:
        order_obj = Order.objects.filter()
        serializer = GetOrderListSerializer(order_obj, many=True)
        data = serializer.data
        success = True
        msg = 'Data fetched successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg, 'data': data}


def update_user(request):
    """04. Update customer information both in store (through the API) """
    try:
        success = False
        msg = 'failed to update user details'
        data = []
        json_msg = []
        post_data = request.POST
        user_id = post_data.get('user_id')
        email = post_data.get('email')
        user_data = UserDetails.objects.filter(id=user_id)
        if user_data:
            user_data = user_data[0]
            user_data.email = email
            store_id = post_data.get('store_id')
            if store_id:
                store_obj = StoreDetails.objects.filter(id=store_id).values_list('store_domain', flat=True)
                if store_obj:
                    store_domain = store_obj[0]
                    url_data = requests.get(store_domain + 'store1/update_user/',
                                            params={"user_id": user_data.user_store_id,
                                                    "email": email})
                    json_data = url_data.json()
                    json_msg = json_data.get("msg")
                    user_data.save()
                    success = True
                    msg = 'User data updated successfully'
        data = {"shopify_data": msg, "store1": json_msg}

    except Exception as e:
        print(e.args)
    return {'success': success, 'data': data}


def save_store_details(request):
    """Saves the private api credentials for stores"""
    success = False
    msg = 'No data to save'
    try:
        post_data = request.POST
        api_key = post_data.get('api_key')
        api_password = post_data.get('api_password')
        shared_secret = post_data.get('shared_secret')
        store_domain = post_data.get('store_domain')
        store_obj = StoreDetails()
        store_obj.api_key = api_key
        store_obj.api_password = api_password
        store_obj.store_domain = store_domain
        store_obj.shared_secret = shared_secret
        store_obj.save()
        success = True
        msg = 'Store data updated successfully'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}
