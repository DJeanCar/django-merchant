"""
Django settings for DjangoMerchant project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8*=j&t!=$^uwewrzh_$+gr-hsdr(n8anx1km(gw7@+wov+c3zm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
    'billing',
    'paypal.standard.pdt',
)



MERCHANT_TEST_MODE = False
PAYPAL_TEST = MERCHANT_TEST_MODE

MERCHANT_SETTINGS = {
    'pay_pal': {
         "WPP_USER" : 'MJeanC.104-facilitator_api1.gmail.com',
         "WPP_PASSWORD" : '1389214837',
         "WPP_SIGNATURE" : 'AFcWxV21C7fd0v3bYYYRCpSSRl31AufnRRMjuSxxQqDr3my.8vnwlXf1',
         "RECEIVER_EMAIL" : 'MJeanC.104@gmail.com',
         # Below attribute is optional
     }
}
PAYPAL_RECEIVER_EMAIL = MERCHANT_SETTINGS['pay_pal']['RECEIVER_EMAIL']

PAYPAL_IDENTITY_TOKEN = 'Aci-qsCo2poDfxGk4qdX5mD7-whlGb9JW9RbWm8hfQK0wmG1bfgCkqa7BAe'


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'DjangoMerchant.urls'

WSGI_APPLICATION = 'DjangoMerchant.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
