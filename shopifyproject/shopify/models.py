from django.db import models


# Create your models here.
class UserDetails(models.Model):
    user_store_id = models.IntegerField(null = True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'tbl_shopify_user_details'


class Order(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.DO_NOTHING)
    order_number = models.IntegerField()
    order_date = models.DateTimeField(null=True, blank= True)

    class Meta:
        db_table = 'tbl_shopify_order_details'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING)
    item_name = models.CharField(max_length=255)
    item_price = models.IntegerField()

    class Meta:
        db_table = 'tbl_order_item'


class StoreDetails(models.Model):
    api_key = models.CharField(max_length=255)
    api_password = models.CharField(max_length=255)
    shared_secret = models.CharField(max_length=255)
    store_domain = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_store_details'