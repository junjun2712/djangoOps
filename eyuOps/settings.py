"""
Django settings for eyuOps project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import djcelery
djcelery.setup_loader()



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cjq%!qvyor*84yldkz)g2)wv^z&*+e-3eji#xmj7xkdhvcnf_5'

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
    'owgame',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eyuOps.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,  'templates')],
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

WSGI_APPLICATION = 'eyuOps.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS  = (os.path.join(BASE_DIR,'static'),)

# TEMPLATE_DIRS = (
#     os.path.join(BASE_DIR,  'templates'),
#     'owgame',
# )


ANSIBLE_HOST_DIR = os.path.join(BASE_DIR,'AnsibleHostFolder')

OWGAME_ANSIBLE_HOST_DIR = os.path.join(BASE_DIR,'ansibleHostFile')


##log setting
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        # 'special': {
        #     '()': 'project.logging.SpecialFilter',
        #     'foo': 'bar',
        # }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'default':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/all.log',
            'maxBytes':'1024*1024*5',
            'backupCount':'5',
            'formatter':'verbose',
        },
        'error':{
            'level':'ERROR',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/err.log',
            'maxBytes':'1024*1024*5',
            'backupCount':'5',
            'formatter':'verbose',

        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'request_handler':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/requst.log',
            'maxBytes':'1024*1024*5',
            'backupCount':'5',
            'formatter':'verbose',
        },
        'script_handler':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/script.log',
            'maxBytes':'1024*1024*5',
            'backupCount':'5',
            'formatter':'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['special']
        },
        'signals':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/signals.log',
            'maxBytes':'1024*1024*5',
            'backupCount':'5',
            'formatter':'verbose',
            },
        'owgame_ansible_host':{
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/owgame_ansible_host.log',
            'maxBytes':'1024*1024*5',
            'backupCount':'5',
            'formatter':'verbose',
            },
        'tasks':{
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename':'logs/tasks.log',
            'maxBytes':'1024*1024*5',
            'backupCount':'5',
            'formatter':'verbose',
        },

    },
    'loggers': {
        'django': {
            'handlers': ['default','console'],
            'propagate': False,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'ERROR',
            'propagate': False,
        },
        'owgame.signals':{
            'handlers':['signals','console'],
            'level':'DEBUG',
            'propagate':True,
        },
        'owgame.owgame_ansible_host':{
            'handlers':['owgame_ansible_host','console'],
            'level':'DEBUG',
            'propagate':True,
        },
        'owgame.tasks':{
            'handlers':['tasks','console'],
            'level':'DEBUG',
            'propagate':True,
        }
    }
}


####celery setting
BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ENABLE_UTC = True