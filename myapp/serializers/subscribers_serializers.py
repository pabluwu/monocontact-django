
from re import sub
from rest_framework import serializers
from mono_base.models import Account
from myapp.models.models_mono_99 import Subscriber

class SubscriberCreateApiSerializers(serializers.Serializer):
    listing_id = serializers.IntegerField()
    account_id = serializers.IntegerField()
    contact_id = serializers.IntegerField()

    #Método para crear.
    def create(self, validated_data):
        subscriber = Subscriber(
            listing_id = validated_data.get('listing_id'),
            account_id = validated_data.get('account_id'),
            contact_id = validated_data.get('contact_id'),

            #Valores 0
            unsubscribed = 0,
            bounced = 0,
            spam = 0,
            manually = 0,
        )
        subscriber.save()
        
        return subscriber


#unsubscribed = 0
#bounced = 0
#spam, manually = 0
