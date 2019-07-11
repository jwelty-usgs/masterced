"""
Django settings for ced project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

with open(BASE_DIR + '/config/sgceConfig.json', 'r') as f:
    config = json.load(f)
    SBUSER = config['DEFAULT']['SBUSER']
    SBPASS = config['DEFAULT']['SBPASS']
    SECRET_KEY = config['DEFAULT']['SECRETKEY']
    ALLOWED_HOST = config['DEFAULT']['ALLOWED_HOST']
    EMAIL_HOST = config['DEFAULT']['EMAIL_HOST']
    EMAIL_HOST_USER = config['DEFAULT']['EMAILHOSTUSER']
    EMAIL_HOST_PASSWORD = config['DEFAULT']['EMAILHOSTPASSWORD']
    EMAIL_PORT= config['DEFAULT']['EMAIL_PORT']
    APPDEBUG = config['DEFAULT']['APPDEBUG']
    SERVER_EMAIL = config['DEFAULT']['SERVER_EMAIL']
    DEFAULT_FROM_EMAIL = config['DEFAULT']['DEFAULT_FROM_EMAIL']
    DBHOST = config['DEFAULT']['DBHOST']
    DBUSER = config['DEFAULT']['DBUSER']
    DBPASSWORD = config['DEFAULT']['DBPASSWORD']
    # DBUSER1 = config['DEFAULT']['DBUSER1']
    # DBPASSWORD1 = config['DEFAULT']['DBPASSWORD1']
    DBNAME = config['DEFAULT']['DBNAME']
    ENVIRONMENT = config['DEFAULT']['ENVIRONMENT']

#DEBUG = APPDEBUG
DEBUG = False
#TEMPLATE_DEBUG = True

ACCOUNT_ACTIVATION_DAYS=7
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
ALLOWED_HOSTS = [ALLOWED_HOST,'LocalHost'];

# Password requirements
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 16
PASSWORD_COMPLEXITY = { "UPPER":  2, "LOWER":  2, "DIGITS": 2, "NON ASCII": 2, "WORDS": 1 }

# Application definition

INSTALLED_APPS = (
    'ced_main',
    'accounts',
    'welcome',
    'profiles',
    'grsgmap',
    'djangosecure',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'sslserver', # Comment this out for production
    'registration',
    'form_utils',
    'jquery',
    'django_tables2',
    'djangoformsetjs', 
    'phonenumber_field',  
    'bootstrap3',
)

# MIDDLEWARE_CLASSES = ( #python 2.7
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'djangosecure.middleware.SecurityMiddleware', python 2.7
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ced.urls'
WSGI_APPLICATION = 'ced.wsgi.application'
AUTH_PROFILE_MODULE = 'accounts.userprofile'

# LOGOUT_URL = '/welcome'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/sgce/accounts/loginpage/'

SESSION_EXPIRE_AT_BROWSER_CLOSE=True
SESSION_COOKIE_HTTPONLY = True

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    
    'default': {
          'ENGINE':'django.db.backends.mysql',
          'NAME': DBNAME,
          #Uncomment for production
          'USER': DBUSER,
          'PASSWORD': DBPASSWORD,
          # #Comment out for production
          # 'USER': DBUSER1,
          # 'PASSWORD': DBPASSWORD1,
          
          'HOST': DBHOST,
          'PORT': 3306,
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Denver'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_FRAME_DENY = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR
STATIC_URL = "/static/"


STATIC_DIR = os.path.join(BASE_DIR, 'ced_main/static')


STATICFILES_FINDERS = ( 
     'django.contrib.staticfiles.finders.FileSystemFinder',
     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
     #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

TEMPLATES = [
    {    
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
        os.path.join(BASE_DIR, 'ced_main/Templates'),
        os.path.join(BASE_DIR, 'welcome/Templates'),
        os.path.join(BASE_DIR, 'accounts/Templates'), 
        os.path.join(BASE_DIR, 'grsgmap/Templates'), 
        os.path.join(BASE_DIR, 'Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            # 'debug': DEBUG, # Comment out debug line before production
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
