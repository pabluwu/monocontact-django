from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from myapp.models.models_mono_99 import Listing
from myapp.serializers import ListingSerializer

@api_view(['GET'])
def listing_api_view(request):
    if request.method == 'GET':
        listings = Listing.objects.get_all_listing()

        listing_serializer = ListingSerializer(listings, many=True)

        return Response(listing_serializer.data)