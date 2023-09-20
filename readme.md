before the work

1. create and fill .env
   (see .env.example)
2. create empty database
3. execute:  python manage.py create_su (createsuperuser)
4. execute:  python manage.py create_moderator
5. execute:  python manage.py create_ordinary_user

for create new ordinary user use POST
http://127.0.0.1:8000/users/

for see full users-list use GET
http://127.0.0.1:8000/users/

for take JWT token use POST
http://127.0.0.1:8000/users/token/


for create payment
http://localhost:8000/classes/payment/create/ (POST method)
with {"course_id": "XXX, "payment_method": "card"}
API will return url for paying and pk 
use this pk for checking status with command 
http://localhost:8000/classes/payment/status/10/ (GET method)

for handmade check whether payment successful use
"python manage.py check_payments"

