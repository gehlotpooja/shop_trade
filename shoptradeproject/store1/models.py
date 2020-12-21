from django.db import models
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    class Meta:
        db_table = 'tbl_product_details'


class UserDetails(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        db_table = 'tbl_user_details'


class OrderDetails(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.DO_NOTHING)
    order_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tbl_order_details'


class ProductOrderMapping(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(OrderDetails, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'tbl_product_order_map'
