from .models import *
from rest_framework import serializers


class GetOrderDetailsSerializer(serializers.ModelSerializer):
    order_id = serializers.IntegerField(source='id')
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    phone = serializers.CharField(source='user.phone')
    order_items = serializers.SerializerMethodField()

    def get_order_items(self, order_obj):
        product_obj = ProductOrderMapping.objects.filter(order_id = order_obj.id)
        return GetProductDetailsSerializer(product_obj, many=True).data

    class Meta:
        model = OrderDetails
        fields = ('order_id', 'order_date', 'user_id', 'first_name',
                  'last_name', 'email', 'phone', 'order_items')


class GetProductDetailsSerializer(serializers.ModelSerializer):
    item_name = serializers.SerializerMethodField()
    item_price = serializers.SerializerMethodField()

    def get_item_name(self,obj):
        item_obj = Product.objects.filter(id = obj.product_id)
        return item_obj[0].name

    def get_item_price(self,obj):
        item_obj = Product.objects.filter(id = obj.product_id)
        return item_obj[0].price

    class Meta:
        model = ProductOrderMapping
        fields = ('product_id', 'item_name', 'item_price')
