from django.urls import path
from .views import listing_api_view, listing_detail_api_view, create_api_view 
from .views import (contact_api_view, contact_detail_api_view, 
contact_create_api_view, Contact_Filter_APIView)
app_name = 'v1.1'

urlpatterns = [
    path('contacto/list', contact_api_view, name='list_contactos'),
    path('contacto/create',contact_create_api_view, name = 'create_contact'),
    path('contacto/<int:pk>', contact_detail_api_view, name='contact_detail'),
    path('contacto/filter/',Contact_Filter_APIView.as_view(), name='contacto_filtes'),  

    path('listing/list', listing_api_view, name='list_listing'),
    path('listing/<int:pk>', listing_detail_api_view, name='listing_detail'),
    path('api/create',create_api_view, name = 'create_contact'),
]




