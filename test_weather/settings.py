"""
Django settings for test_weather project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0ikoprw$t6(crapq%d)r1y#w4z8bvo36^bzz3x5a$d-svmsw&@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 新应用
    'apis.apps.AppConfig',
    'authorization.apps.AuthorizationConfig',
    # 第三方应用
    'django_crontab'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'module.middleware.StatisticsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_weather.urls'

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

WSGI_APPLICATION = 'test_weather.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     },
#     'slave': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'weixin',
#         'USER': 'slim',
#         'HOST': '193.112.37.221',
#         'PORT': '3306',
#         'PASSWORD': '123456'
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'weixin',
        'USER': 'slim',
        'HOST': '193.112.37.221',
        'PORT': '3306',
        'PASSWORD': '123456'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'


RESOURCE_DIR = os.path.join(BASE_DIR, 'resource')
IMAGES_DIR = os.path.join(RESOURCE_DIR, 'images')
WX_APP_SECRET = '21a20b5bb35a34c0231a2ad46c7891ff'

USE_PROXY = False

# session过期时间
SESSION_COOKIE_AGE = 60*60*24*1

# 缓存设置
CACHES = {
    'default': {
        # 1. MemCache
        # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        # 'LOCATION': '127.0.0.1:11211',

        # 2. DB Cache
        # 'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        # 'LOCATION': 'my_cache_table',

        # 3. Filesystem Cache
        # 'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        # 'LOCATION': '/var/tmp/django_cache',

        # 4. Local Mem Cache
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'backend-cache'
    }
}

LOG_DIR = os.path.join(BASE_DIR, 'log')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    # 日志格式
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s: %(thread)d]'
                      '%(pathname)s:%(funcName)s:%(lineno)d %(levelname)s - %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(message)s'
        }
    },
    # 过滤器
    'filters': {

    },
    # 处理器
    'handlers':{
        'console_handler': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'file_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'backend.log'),
            'maxBytes': 1024*1024*1024,
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf8'
        },
        'statistics_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'statistics.log'),
            'maxBytes': 1024*1024*5,
            'backupCount': 5,
            'formatter': 'simple',
            'encoding': 'utf-8'
        }
    },
    # 日志实例
    'loggers': {
        'django': {
            'handlers': ['console_handler', 'file_handler'],
            'level': 'DEBUG'
        },
        'statistics': {
            'handlers': ['statistics_handler'],
            'level': 'DEBUG'
        }
    }
}

CRONJOBS = [
    ('*/1 * * * * ','cron.jobs.report_by_email')
]


# QQ邮箱配置

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465   # 不加密为25，加密SSL为465
EMAIL_HOST_USER = '936534130@qq.com'
EMAIL_HOST_PASSWORD = 'hmerxvhppfltbbac'
#开启TLS
EMAIL_HOST_TLS = True
EMAIL_FROM = "936534130@qq.com"

STATISTICS_SPLIT_FLAG = "||"
