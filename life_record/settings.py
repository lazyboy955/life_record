"""
Django settings for life_record project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import acm
import json
from datetime import timedelta

# 使用ACM做配置管理
ENDPOINT = "acm.aliyun.com"
NAMESPACE = "ad3407ed-74a3-4c77-8b58-42766da45679"
AK = os.getenv('ACCESS_KEY')
SK = os.getenv('SECRET_KEY')
GROUP = "DEFAULT_GROUP"


# 获取配置中心参数
class ACM(acm.ACMClient):
    def get_value(self, date_id: str, group: str, default=None):
        value = self.get(date_id, group)
        try:
            value = json.loads(value)
        finally:
            return value if value else default


acm_client = ACM(ENDPOINT, NAMESPACE, AK, SK)
MYSQL_CONFIG = acm_client.get_value("MYSQL_CONFIG", GROUP)
REDIS_PWD = acm_client.get_value("REDIS_PWD", GROUP)
REDIS_HOST = acm_client.get_value("REDIS_HOST", GROUP)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')z7c^y-=)$j0(8_=qh)js3hdj#dbbbj_aav%@5wgvm_l^%6sb7'

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
    # apps
    'home',
    # the third package
    'rest_framework',
    'django_filters',
    'django_celery_results',
    'django_celery_beat',
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

REST_FRAMEWORK = {
    # 异常处理
    'EXCEPTION_HANDLER': 'utils.exceptions.exception_handler',
    # 视图层面可以筛选
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

ROOT_URLCONF = 'life_record.urls'

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

WSGI_APPLICATION = 'life_record.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': MYSQL_CONFIG['HOST'],
        'PORT': MYSQL_CONFIG['PORT'],
        'USER': MYSQL_CONFIG['USER'],
        'PASSWORD': MYSQL_CONFIG['PASSWORD'],
        'NAME': MYSQL_CONFIG['NAME'],
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PWD
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": REDIS_PWD
        }
    }
}

# Celery Config
CELERY_BROKER_URL = f"redis://:{REDIS_PWD}@{REDIS_HOST}:6379/2"
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'default'
CELERY_RESULT_SERIALIZER = 'json'  # 结果序列化方案
CELERY_TASK_ROUTES = [(
    ('home.tasks.*', {'queue': 'home',
                      'routing_key': 'home'}),
), ]
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
# CELERY_BEAT_SCHEDULE = {
#     "task_test": {
#         'task': 'home.tasks.add_test',
#         'schedule': timedelta(minutes=1, seconds=10),
#         'args': (1, 2),
#     }
# }
CELERY_MESSAGE_COMPRESSION = 'zlib'  # 是否壓縮
CELERY_MAX_TASKS_PER_CHILD = 3  # 每個worker最多執行3個任務就摧毀，避免記憶體洩漏
CELERY_TIMEZONE = 'Asia/Shanghai'
DJANGO_CELERY_BEAT_TZ_AWARE = False

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "session"

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,  # 是否禁用已经存在的日志器
    'formatters': {  # 日志信息显示的格式
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(module)s %(lineno)d %(message)s'
        },
    },
    'filters': {  # 对日志进行过滤
        'require_debug_true': {  # django在debug模式下才输出日志
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {  # 日志处理方法
        'console': {  # 向终端中输出日志
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "life_record/logs/life.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
        'home_log': {  # 向文件中输出日志
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(BASE_DIR), "life_record/logs/home.log"),  # 日志文件的位置
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 10,
            'formatter': 'verbose'
        },
    },
    'loggers': {  # 日志器
        'django': {  # 定义了一个名为django的日志器
            'handlers': ['console', 'file'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
        'home': {
            'handlers': ['home_log'],  # 可以同时向终端与文件中输出日志
            'propagate': True,  # 是否继续传递日志信息
            'level': 'INFO',  # 日志器接收的最低日志级别
        },
    }
}

# use the User model I set
AUTH_USER_MODEL = 'home.User'
