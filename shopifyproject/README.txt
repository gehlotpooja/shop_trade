1)Install all the requirements from the requirement.txt file.
2)Go the settings.py file and change Database configuration according to your system (i have used PGAdmin as DB)
3)Navigate to project folder which has manage.py and Run below commands:
	a)python manage.py makemigrations
	b)python manage.py migrate
	c)python manage.py runserver 127.0.0.1:<port_no>
4)Repeat step 1-3 for store1 under shoptrade project.	

5)Once server is up and running , go and hit the urls (present in shopify/urls.py) using postman

6)save_store_details_api need to be used first before any other activity to save store details.

ex:
http://127.0.0.1:9001/shopify/get_order_details/

List of apis created and their usage (All api calls are made using Postman):

Note : 
1)get_order_details_api -  01. Trigger a customer & order ingestion from the store on the basis of user_id, start and end date
Params used :
user_id
start_date
end_date

2)save_user_details_api - Gets data of users,order and order item from store1.Update data in shopify DB with new entries
Params used :
user_id
start_date
end_date
Note : i)if above params are passed , then data will be fetched as per the satisfying condition else all the data will be fetched
	   ii)This api can be used to create periodic tasks to update data.
	   
3)get_user_order_api - 02.View a list of Customers alongside their aggregated order count / total
Param used :
name/email

Note: i)If name or email is not passed then all customers will be fetched.
	  ii)Particular Customer can be searched on the basis of email or name

4)get_order_list_api - 03. View a list of orders over a certain threshold


5)update_user_api - 04. Update customer information both in store (through the API)
Param used :
user_id
email

Note : Take user_id to identify customer and email is used to update email address of that customer in both (shopify and store1) stores

6)save_store_details_api - Saves the private api credentials for stores
Param used :
api_key
api_password
shared_secret
store_domain