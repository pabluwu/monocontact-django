from rest_framework import serializers
from mono_base.models import Account
from myapi.models import Listing



class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = 'id', 'name', 'created_on'
    
    def create(self, validated_data):
        listing  = validated_data
        return Listing.objects.create(**validated_data)

class ListingNestedSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, allow_blank = False, allow_null = False )

    def get_token(self):
        get_token = ""
        PREFIX = 'Bearer '
        token = self.context.get('token')
        if token.startswith(PREFIX):
            get_token = token[len(PREFIX):]
        return get_token

    def create(self, validated_data):
        get_token = self.get_token()
        acc = Account.objects.get(api_token=get_token)
        listing = Listing(
            name = validated_data.get('name'),
            account_id = acc.id,
            flag = 0
        )
        listing.save()
        return listing

