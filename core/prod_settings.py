import socket
from .base_settings import *
import dj_database_url
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


DATABASES = {
    		'default': dj_database_url.config(default='postgres://localhost/mydb')
			}