from .models import *
from rest_framework import serializers


class GetOrderCountDetailSerializer(serializers.ModelSerializer):
    total_orders = serializers.SerializerMethodField()

    def get_total_orders(self, obj):
        total_orders = Order.objects.filter(user_id=obj.id).count()
        return total_orders

    class Meta:
        model = UserDetails
        fields = ('id', 'user_store_id', 'first_name', 'last_name', 'email', 'total_orders')


class GetOrderListSerializer(serializers.ModelSerializer):
    total_amount = serializers.SerializerMethodField()

    def get_total_amount(self, obj):
        order_item_list = OrderItem.objects.filter(order_id = obj.id)
        total_amount = 0
        for order_item in order_item_list:
            total_amount += order_item.item_price
        return total_amount

    class Meta:
        model = Order
        fields = ('id', 'user_id', 'order_number', 'order_date', 'total_amount')
