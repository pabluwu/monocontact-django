from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from myapp.models.models_mono_99 import Listing
from myapp.serializers.listing_serializer import ListingSerializer

@api_view(['GET'])
def listing_api_view(request):
    if request.method == 'GET':
        listings = Listing.objects.get_all_listing()

        listing_serializer = ListingSerializer(listings, many=True)

        return Response(listing_serializer.data)

@api_view(['GET'])
def listing_detail_api_view(request, pk=None):
    list = Listing.objects.get(pk=pk)
    #Obtener detalle de la lista
    if request.method == 'GET':
        if list != None:
            listing_serializer = ListingSerializer(list)
            return Response(listing_serializer.data)
        return Response('No hay contacto con ese id')
    return Response