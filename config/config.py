import os
# install as python-dotenv
from dotenv import load_dotenv


load_dotenv()

DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_USER = os.getenv('POSTGRES_USER')
DB_PORT = int(os.getenv('POSTGRES_PORT'))
DB_BASE_NAME = os.getenv('POSTGRES_BASE')
DB_HOST = os.getenv('POSTGRES_HOST')


MY_EMAIL = os.getenv('MY_EMAIL')
MY_EMAIL_PASSWORD = os.getenv('MY_EMAIL_PASSWORD')
MY_EMAIL_HOST = os.getenv('MY_EMAIL_HOST')
MY_EMAIL_PORT = int(os.getenv('MY_EMAIL_PORT'))
if os.getenv('EMAIL_SENDING_SIMULATION_MODE') == 'False':
    EMAIL_SENDING_SIMULATION_MODE = False
else:
    EMAIL_SENDING_SIMULATION_MODE = True



DJANGO_SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

TXT_LOG = '~/mailing_service.log'

MAX_PRODUCTS_PER_PAGE = 3
THRESHOLD_VIEW_FOR_EMAIL = 10

ALLOWED_LINKS = [
    'youtube.com',
    'linux.org'
]

STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')

DELTA_DAYS_FOR_DEACTIVATE = 30