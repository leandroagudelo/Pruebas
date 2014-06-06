"""
Django settings for inicio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

#import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), '..', 'templates').replace('\\','/'),)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%#k(v0jrqy=h61a*b$@#v#c=unnh^3-#)h_5ta(n&sek$lmh)6'

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
    'django.contrib.admin',
    'polls',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'inicio.urls'

WSGI_APPLICATION = 'inicio.wsgi.application'


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


# noinspection PyUnresolvedReferences
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),
                    "templates/js/tablesorter/tables.js",
                    "templates/js/jquery-1.10.2.js",
                    'templates/css/bootstrap.min.css',
                    "templates/css/sb-admin.css",
                    "templates/font-awesome/css/font-awesome.css",
                    "templates/font-awesome/fonts/FontAwesome.otf",
                    "templates/font-awesome/fonts/fontawesome-webfont.eot",
                    "templates/font-awesome/fonts/fontawesome-webfont.svg",
                    "templates/font-awesome/less/rotated-flipped.less",
                    "templates/js/tablesorter/jquery.tablesorter.js",
                    "templates/js/tablesorter/tables.js",
                    "templates/js/morris/chart-data-morris.js",





                    )


# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
