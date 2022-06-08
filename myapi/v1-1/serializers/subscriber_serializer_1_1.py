from typing import List
from rest_framework import serializers
from myapi.models import Subscriber, Listing, Contact

#Importado de versión 1.1
from .contact_serializer_1_1 import ContactNestedSerializer
from .listing_serializer_1_1 import ListingNestedSerializer

class SubscriberColumnsSerializer(serializers.Serializer):
    contacto = ContactNestedSerializer(many=False)
    listing = ListingNestedSerializer(many=False)

    def create(self, validated_data):        
        
        return None
        
class SubscriberCreateSerializer(serializers.Serializer):
    model = serializers.CharField(max_length=255, allow_blank = False, allow_null = False )
    columns = SubscriberColumnsSerializer(many=False)
    
    def create(self, validated_data):   
        dic = validated_data.get('columns')
        list = Listing.objects.get(name=dic['listing']['name'])
        code = Contact.objects.get(code=dic['contacto']['code'])
        subscriber = Subscriber(
            listing_id = list.id,
            contact_id = code.id,
            unsubscribed = 0,
            bounced = 0,
            spam = 0,
            manually = 0,
        )
        
        return None