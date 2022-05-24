from django import db
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view  

from dynamic_db_router import in_database

from myapp.serializers import Event_Serializer

from myapp.models.models_mono_99 import Event
#Selección bd.


@api_view(['GET'])
def event_api_view(request):
    if request.method == 'GET':
        events  = Event.objects.all()
        event_serializer = Event_Serializer(events, many=True)
        return Response(event_serializer.data)