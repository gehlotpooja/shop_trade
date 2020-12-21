1)Install all the requirements from the requirement.txt file.
2)Go the settings.py file and change Database configuration according to your system (i have used PGAdmin as DB)
3)Navigate to project folder which has manage.py and Run below commands:
	a)python manage.py makemigrations
	b)python manage.py migrate
	c)python manage.py runserver 127.0.0.1:<port_no> 

5)Once server is up and running , go and hit the urls (present in store1/urls.py) using postman

ex:
http://127.0.0.1:9000/store1/get_order_details/

List of apis created and their usage (All api calls are made using Postman):

1)save_user_using_csv_api - Imports and save a list of customers from a CSV file (/store1/media/user_detail.csv)

2)save_product_using_csv_api - Imports and save a list of products from a CSV file (/store1/media/product_detail.csv)

3)place_order_api - Places order
Param used:
user_id
item_ids
order_obj_id

Note : i)In case of new order , user_id and item_ids are passed
	   ii) If any extra item needs to be added to an existing order then all the above three params are passed.

4)get_order_details_api - Get the order details based on the params passed.
Param used:
user_id
start_date
end_date

Note : i)This api is used for fetching and updating data for shopify application

5)update_user_api - Update user email on the basis of user_id
Param used :
user_id
email

Note : i)Take user_id to identify customer and email is used to update email address of that customer in both (shopify and store1) stores
	   ii)This api call is  make from shopify application for updating user.
