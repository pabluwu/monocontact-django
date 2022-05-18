from django import db
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view  

from dynamic_db_router import in_database
from myapp.connection import connection_db
from myapp.serializers import Event_Serializer

from myapp.models.models_mono_99 import Event
#Selección bd.
db_name = connection_db(99)

@api_view(['GET'])
def event_api_view(request):
    if request.method == 'GET':
        events  = Event.objects.using(db_name).all()
        event_serializer = Event_Serializer(events, many=True)
        return Response(event_serializer.data)