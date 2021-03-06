
from os.path import dirname, join

import core
from core import common
import example

ADMINS = (
    ('Jaroslava Schovancova', 'jschovan@gmail.com'),
)
MANAGERS = ADMINS


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
LANGUAGE_NAME = 'English'
LANGUAGE_NAME_LOCAL = 'English'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # for AJAX POST protection with csrf
    'django.contrib.auth.middleware.AuthenticationMiddleware',
### added
    'django.contrib.auth.middleware.RemoteUserMiddleware',  # for APIs: htcondorapi
### END added
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
#### django-debug-toolbar
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
###
#    'django.middleware.common.CommonMiddleware',
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',  # for AJAX POST protection with csrf
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#    # Uncomment the next line for simple clickjacking protection:
#    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

VERSIONS = {
    'core': core.__versionstr__,
    'example': example.__versionstr__,
}

# installed apps
INSTALLED_APPS_DJANGO_FRAMEWORK = (
    ### Django framework
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#### django-debug-toolbar
#    'debug_toolbar',
)
INSTALLED_APPS_DJANGO_PLUGINS = (
    ### Django plugins
    'rest_framework',  #pip install djangorestframework, version 2.3.10
    'django_datatables_view',  #pip install django-datatables-view, version 1.6
    'djangojs',  #pip install django.js, version 0.8.1
)
COMMON_INSTALLED_APPS = \
    INSTALLED_APPS_DJANGO_FRAMEWORK + \
    INSTALLED_APPS_DJANGO_PLUGINS
    
INSTALLED_APPS_BIGPANDAMON_EXAMPLE = (
    ### BigPanDAmon core
#    'core.common',
#    'core.table',
#    'core.graphics', #NOT-IMPLEMENTED
 #   'core.pandajob',
 #   'core.resource',
#    'core.htcondor', #NOT-NEEDED-IN-ATLAS
    'core.datatables',
#    'core.gspread', #NOT-NEEDED-IN-ATLAS?

    ### example.todoview: Placeholder for views which need to be implemented
    ### as part of cross-linking between jobs and tasks monitoring

#    'django_tables2',#pip install django_tables2
)
INSTALLED_APPS = COMMON_INSTALLED_APPS + INSTALLED_APPS_BIGPANDAMON_EXAMPLE

JS_I18N_APPS = ()
JS_I18N_APPS_EXCLUDE = INSTALLED_APPS_BIGPANDAMON_EXAMPLE
JS_I18N_APPS_EXCLUDE += ('django_tables2',)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request', #django-tables2	
)

ROOT_URLCONF = 'example.urls'

SITE_ID = 3

# email
EMAIL_SUBJECT_PREFIX = 'bigpandamon-example: '


