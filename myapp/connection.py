from django.db import connections

def select_db(account):
    db_name = 'mono_'+str(account)
    external_db = {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306',
    }

    return external_db

def connection_db(account_id):
    db_name = 'mono_'+str(account_id)
    connections.databases[db_name]={
    'ENGINE': 'django.db.backends.mysql',
    'NAME': db_name,
    'USER': 'root',
    'PASSWORD': 'admin',
    'HOST': 'localhost',
    'PORT': '3306'}

    return db_name