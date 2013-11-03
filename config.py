import os

HOST = os.getenv('HOST', 'http://127.0.0.1')
PORT = os.getenv('PORT', 8080)

DB_SQL_PASSWORD = os.getenv('DOTCLOUD_DB_SQL_PASSWORD', '')
SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URI', 'postgresql://root:' + DB_SQL_PASSWORD + '@floatingpoints-petri.azva.dotcloud.net:1912/floatingpoints')


del os