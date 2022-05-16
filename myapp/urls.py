from django.urls import URLPattern, path, include
from myapp.views.contact_view import contact_api_view, contact_detail_api_view, contact_create_api_view, Contact_Filter_APIView


urlpatterns = [
    path('contacto/list',contact_api_view, name = 'list_contacts'),
    path('contacto/',contact_create_api_view, name = 'create_contact'),
    path('contacto/<int:pk>', contact_detail_api_view, name='contact_detail'),
    path('contacto/filter/',Contact_Filter_APIView.as_view(), name='contacto_filtes'),  
    
]
