<h2>Main idea</h2>

In 2018, James Clear wrote the book Atomic Habits, which is about acquiring new good habits and eradicating old bad habits. This project implements the server part of the healthy habits tracker as an API server.

In the book, a good example of a habit is described as a specific action that can be summarized in one sentence:

I will be [ACTIVE] at [TIME] in [PLACE]

For every useful habit you need to reward yourself or immediately after do a pleasant habit. But at the same time, the habit should not take more than 2 minutes to complete.

The tracker will remind you to perform a certain action through a telegram bot

<h3>What does this project do.</h3>

this project realise a micro service with API interface. 
writen by kirill.s (aka Mr.K) 2023.


<h3>How to prepare.</h3>
this project use next components:
- python as a base platform
- celery (integrated package)
- postgresql database - EXTERNAL
- redis-server - EXTERNAL
- sending telegram message for registered users  


<h3>How to install.</h3>
- clone project to own disk in new directory
- activate virtual environment (python -m venv venv)
- install all needs packages (pip install -r requirements.txt)
- see next step for configure

<h3>How to configure.</h3>
Please pay your attention to configure .env file.
You can find example in root of your project directory (.env.example)
please fill all parameters with your data and save the changed file as .env

after that you need create empty database.
you may use command
>psql -U postgres;
>CREATE DATABASE <database_name>

or 
> createdb -U postgres <database_name>

alternatively you can use pgadmin or other interface app.

Use next commands for tables creation
>python manage.py migrate


Next step helps you create superuser user. With this user login you will be able to create and change timing for periodic tasks
>python manage.py createsuperuser

or
> python manage.py create_su

Be sure that you have started redis server. Congratulation, we ready for start!

<h3>Ноw it works.</h3>

Start the server with
>python manage.py runserver

also start the celery with both commands 
>celery worker --app=KW7_habits --pool=eventlet --loglevel=INFO;
celery --app=KW7_habits worker --loglevel=INFO --scheduler=django --pool=eventlet


you will find API documentation from front-end connecting  
http://127.0.0.1:8000/swagger/ or 
http://127.0.0.1:8000/redoc/
use it with any browser what you like


Easy way for a work start:
- create new user: http://localhost:8000/users/
POST {
        "email": "your@e.mail",
        "password": "your_password",
        "last_name": "Any",
        "telegram_username": "your_telegram_name"
    }
NOTE: your_telegram_name must be created in telegram app settings 
- take a token via http://localhost:8000/users/token/ 
POST {
        "email": "your@e.mail",
        "password": "your_password"
    }
- add access token as Bearer for your next requests
- create your first habit http://localhost:8000/habit/create/ . For instance: 
POST {
    "title": "my first habit",
    "place": "home sweet home",
    "time": "12:52:00",
    "action": "jazz up before lunch",
    "time_for_action": "0:01:30",
    "frequency": 5,
    "is_useful": false
} 


if you want to test this product with little database which already have some data you be able to tap 
> python manage.py loaddata all_apps_unix.json

Testing

To run the tests, ensure that you have pytest installed in your virtual environment. If you don't have it, you can install it using: pip install pytest pytest-django
Next, navigate to the root directory of your project and execute: pytest


For create docker image use:
build docker image
>docker build -t habit-app .

for run container execute:
>docker run habit-app



Have a nice day! See you!
with best wishes, kirill.s
