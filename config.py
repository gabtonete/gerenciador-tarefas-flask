import secrets

API_HOST = '127.0.0.1'
API_PORT = 5000
API_BASE_URL = '/api'
API_DEBUG = True

SECRET_KEY = secrets.token_urlsafe(32)

MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DATABASE = 'example'
