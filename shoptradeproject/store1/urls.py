from django.urls import path
from . import views

urlpatterns = [
    path(r'save_user_using_csv/', views.save_user_using_csv_api, name='save_user_using_csv'),
    path(r'save_product_using_csv/', views.save_product_using_csv_api, name='save_product_using_csv'),
    path(r'place_order/', views.place_order_api, name='place_order'),
    path(r'delete_order_detail_entry/', views.delete_order_detail_entry, name='delete_order_detail_entry'),
    path(r'get_order_details/', views.get_order_details_api, name='get_order_details'),
    path(r'update_user/', views.update_user_api, name='update_user'),
]