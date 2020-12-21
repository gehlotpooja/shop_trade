from django.urls import path
from . import views

urlpatterns = [
    path(r'get_order_details/', views.get_order_details_api, name='get_order_details'),
    path(r'save_user_details/', views.save_user_details_api, name='save_user_details'),
    path(r'get_user_order/', views.get_user_order_api, name='get_user_order'),
    path(r'get_order_list/', views.get_order_list_api, name='get_order_list'),
    path(r'update_user/', views.update_user_api, name='update_user'),
    path(r'save_store_details/', views.save_store_details_api, name='save_store_details'),
]