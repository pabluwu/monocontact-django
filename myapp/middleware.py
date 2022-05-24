from django.db import connections
import threading
data = threading.local()
class RoutingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, args, kwargs):
        data.account = 99
        db_name = 'mono_'+str(data.account)
        connections.databases[db_name]={
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': 'root',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '3306'}

    def process_response(self, request, response):
        if hasattr(data, 'acount'):
            del data.account
        
        return response

class DatabaseRouter(object):
    def _default_db(self):
        from django.conf import settings
        if hasattr(data, 'account'):
            return 'mono_'+str(data.account)
        else:
            
            print(data)

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'myapp':
            return self._default_db()
        else: 
            return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'myapp':
            return self._default_db()
        else: 
            return 'default'

