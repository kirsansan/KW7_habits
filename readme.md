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


+ log for tlg bot
+ Test tlg bot
- auto scheduling
- Tests 
- Coverage
- Manual documentation
- Readme
- Fine8

