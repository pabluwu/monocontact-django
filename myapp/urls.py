from django.urls import URLPattern, path, include
from myapp.views.contact_view import contact_api_view, contact_detail_api_view, contact_create_api_view, Contact_Filter_APIView
from myapp.views.event_view import event_api_view
from myapp.views.user_role_view import user_api_view, User_Filter_APIView


urlpatterns = [
    path('contacto/list',contact_api_view, name = 'list_contacts'),
    path('contacto/',contact_create_api_view, name = 'create_contact'),
    path('contacto/<int:pk>', contact_detail_api_view, name='contact_detail'),
    path('contacto/filter/',Contact_Filter_APIView.as_view(), name='contacto_filtes'),  

    path('event/list', event_api_view, name='list_events'),


    path('user/<int:pk>', user_api_view, name='list_users'),
    path('user/filter/',User_Filter_APIView.as_view(), name='user_filtes'),  
    
]
