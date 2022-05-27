from rest_framework import serializers
from mono_base.models import Account
from myapp.models.models_mono_99 import Listing

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = 'id', 'name', 'created_on'
    
    def create(self, validated_data):
        listing  = validated_data
        return Listing.objects.create(**validated_data)