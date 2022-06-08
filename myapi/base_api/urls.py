from django.urls import re_path, path
from myapi.base_api.views import (contact_api_view, contact_detail_api_view, 
contact_create_api_view, Contact_Filter_APIView)
app_name = 'base_api'

urlpatterns = [
    path('contacto/list', contact_api_view, name='list_contactos'),
    path('contacto/create',contact_create_api_view, name = 'create_contact'),
    path('contacto/<int:pk>', contact_detail_api_view, name='contact_detail'),
    path('contacto/filter/',Contact_Filter_APIView.as_view(), name='contacto_filtes'),  
]




