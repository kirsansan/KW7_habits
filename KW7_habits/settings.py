"""
Django settings for this project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
from config.config import DB_PASSWORD, DJANGO_SECRET_KEY, DB_BASE_NAME, DB_USER, DB_PORT, DB_HOST

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    'drf_yasg',
    'corsheaders',
    'django_celery_beat',

    'users',
    'habit',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware'
]

ROOT_URLCONF = 'KW7_habits.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'KW7_habits.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # for working with SQLite
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',

        # for working with postreSQL
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_BASE_NAME,  # DB name
        # 'USER': 'postgres',  # default user
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,  # password for default user (get from .env )
        # 'HOST': '172.22.48.1',  # ip for unix domain socket
        'HOST': DB_HOST,
        'PORT': DB_PORT,  # port for DB
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True
# USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (
    BASE_DIR / 'static',
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# EMAIL_HOST = MY_EMAIL_HOST
# EMAIL_PORT = MY_EMAIL_PORT
# EMAIL_HOST_USER = MY_EMAIL
# EMAIL_HOST_PASSWORD = MY_EMAIL_PASSWORD
# EMAIL_USE_SSL = True

AUTH_USER_MODEL = 'users.User'
# LOGIN_REDIRECT_URL = '/'
# LOGOUT_REDIRECT_URL = '/'
# LOGIN_URL = '/users/'

CACHE_ENABLED = False

if CACHE_ENABLED:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
            "TIMEOUT": 30
        }
    }

# will be start it every 5 minutes
# CRONJOBS = [
#     ('*/5 * * * *', 'main.services.checking_and_send_emails', f'>> {TXT_LOG}')
# ]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=55),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:8000'  # Замените на адрес вашего фронтенд-сервера
]
CSRF_TRUSTED_ORIGINS = [
    "https://read-and-write.example.com"  # Замените на адрес вашего фронтенд-сервера
    # и добавьте адрес бэкенд-сервера
]
CORS_ALLOW_ALL_ORIGINS = False

CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/0'

# periodic tasks
CELERY_BEAT_SCHEDULE = {
    'cleaning_logs': {
        'task': 'habit.tasks.cleaning_logs',  # path to task
        'schedule': timedelta(hours=24),
    },
    'check_and_send_notes_telegram': {
        'task': 'habit.tasks.send_telegram_message_rev_b',  # path to task
        'schedule': timedelta(minutes=1),
    },
}
