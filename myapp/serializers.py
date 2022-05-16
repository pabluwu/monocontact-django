from rest_framework import serializers
from dynamic_db_router import in_database
from django.db import connections
from myapp.connection import connection_db, select_db

from .models.models_mono_99 import Contact

db_name = connection_db(99)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        # fields = 'code', 'email', 'firstname', 'lastname', 'company', 'title', 'phone', 'address', 'city', 'region', 'country'

    # def validate(self, data):
    #     if data.get('account_id', None) == None:
    #         data['account_id']=99
    #     return data

    def create(self, validated_data):
        contact = validated_data
                
        return Contact.objects.using(db_name).create(**validated_data)

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
        with in_database(db_name):
            instance.save(using=db_name)
        return instance


 