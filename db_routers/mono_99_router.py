
import threading
from django.http import Http404

data = threading.local()
class DatabaseRouter(object):
    def _default_db(self):
        from django.conf import settings
        if hasattr(data, 'account'):
            print(data)
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