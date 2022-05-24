from typing import List
from rest_framework import serializers
from dynamic_db_router import in_database
from .models.models_mono_base import User

from .models.models_mono_99 import Contact, Event, UserRole, AccountUser, Listing



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        contact = validated_data
                
        return Contact.objects.create(**validated_data)

class Contact_Update_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = 'email', 'firstname', 'lastname', 'company', 'title', 'phone', 'address', 'city', 'region', 'country'

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.firstname = validated_data.get('firstname', instance.firstname)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.company = validated_data.get('company', instance.company)
        instance.title = validated_data.get('title', instance.company)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.region = validated_data.get('region', instance.region)
        instance.country = validated_data.get('country', instance.country)
        
        instance.save()
        return instance

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = '__all__'
    
    def create(self, validated_data):
        listing  = validated_data
        return Listing.objects.create(**validated_data)

class Event_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        event = validated_data
            
        return Event.objects.create(**validated_data)  



##Serializador User Role
class User_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = 'overseer', 'crm', 'area_id'

class User_Serializer(serializers.ModelSerializer):
    # user_role = User_Role_Serializer()
    class Meta:
        model = User
        fields = '__all__'

class User_Filter_Serializer(serializers.ModelSerializer):

    class Meta:
        overseer = serializers.PrimaryKeyRelatedField(queryset=AccountUser.objects.all())

        model = User
        fields = '__all__'
    
 