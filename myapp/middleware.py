from django.db import connections
import threading

from django.shortcuts import get_object_or_404
data = threading.local()
from mono_base.models import Account
from rest_framework import exceptions
class RoutingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, args, kwargs):
        token = request.META.get('HTTP_AUTHORIZATION', '')
        try:
            acc = Account.objects.get(api_token = token)
            # acc = get_object_or_404(Account, api_token = token)
            print(acc.id)
        except Exception as e:
            msj = 'Ingrese un token válido o que perteneza a una cuenta'
            return exceptions.JsonResponse(status=404, data={'status':'false', 'message':msj})

        
        data.account = acc.id
        db_name = 'mono_'+str(acc.id)
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

    def allow_relation(self, obj1, obj2, **hints):
        return True

