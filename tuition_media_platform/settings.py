"""
Django settings for tuition_media_platform project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import dj_database_url
import environ

env = environ.Env()
environ.Env.read_env()  # Reads the .env file
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-1p0yh0iz6j0gd%)x@fch$%=*s!7ek&y3-69lw543!c3p-yl6t)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", ".vercel.app","http://127.0.0.1:5501"]


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #apps
    'tutor',
    'student',
    'apply_for_tuition',
    'tuition',
    'admin_panel',
    'contact',
    #rest framework
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    "corsheaders",
    #cloudinary
     'cloudinary_storage',
    'cloudinary',
    
]


MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = 'tuition_media_platform.urls'


#onrender csrf permission
CSRF_TRUSTED_ORIGINS = ['https://tution-media-platform-backend.vercel.app/',"https://tuitionmedia.netlify.app",]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:8000",  # Local development domain
     "http://127.0.0.1:5501",
     "https://tuitionmedia.netlify.app",
]

CORS_ALLOW_CREDENTIALS = True


CORS_ALLOW_HEADERS = [
    'authorization',
    'content-type',
    'accept',
    'origin',
    'x-csrftoken',
]


WSGI_APPLICATION = 'tuition_media_platform.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': env("DB_NAME"),
       'USER': 'postgres.soltvdfgpqtbsqqavsyt',
       'PASSWORD':env("DB_PASS"),
       'HOST': env("DB_HOST"),
       'PORT':env("DB_PORT"),
   }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres.soltvdfgpqtbsqqavsyt',
#         'PASSWORD': 'SKf6Ky7k*Brf8Mh',
#         'HOST': 'aws-0-ap-southeast-1.pooler.supabase.com',
#         'PORT': '6543'
#     }
# }

# Replace the SQLite DATABASES configuration with PostgreSQL:
# DATABASES = {
#     'default': dj_database_url.config(
    
#         default='postgresql://tuition_media_platform_ypwy_user:qwMTcKAIiu4KVKSuFvVucbfXP2KbMYVe@dpg-crrd3uij1k6c73eduh1g-a.oregon-postgres.render.com/tuition_media_platform_ypwy',
#         conn_max_age=600
#     )
# }

# SKf6Ky7k*Brf8Mh
# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# media settings
STATIC_URL = 'static/'
STATIC_ROOT=BASE_DIR / 'staticfiles'
MEDIA_URL = f'https://res.cloudinary.com/{env("CLOUD_NAME")}/'




REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}




#environments 



SECRET_KEY = env("SECRET_KEY")




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = env("EMAIL")
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")

import cloudinary
import cloudinary.uploader
import cloudinary.api

cloudinary.config(
    cloud_name=env("CLOUD_NAME"),
    api_key=env("API_KEY"),
    api_secret=env("API_SECRET_KEY"),
)
