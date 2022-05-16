import code
from queue import Empty
from django import db
from requests import request
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view

from dynamic_db_router import in_database
from yaml import serialize
from myapp.connection import connection_db, select_db

from myapp.models.models_mono_99 import Contact, ContactTag
from myapp.serializers import ContactSerializer, Contact_Update_Serializer
from django.db import connections

# db = select_db(10)
db_name = connection_db(99)

@api_view(['GET'])
def contact_api_view(request):
    #Listar todos los contactos.
    if request.method == 'GET':
        contacts = Contact.objects.using(db_name).all()
        contacts_serializer = ContactSerializer(contacts, many=True)
        return Response(contacts_serializer.data)   

    

@api_view(['POST'])
def contact_create_api_view(request):
    ##Crear contacto a través de post.
    if request.method == 'POST':
        contact_serializer = ContactSerializer(data = request.data)
        with in_database(db_name):
            if contact_serializer.is_valid():
                contact_serializer.save()
                return Response(contact_serializer.data)
        return Response(contact_serializer.errors)

    


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail_api_view(request, pk=None):
    contact = Contact.objects.using(db_name).filter(pk=pk).first()

    #Obtener detalle del contacto
    if request.method == 'GET':
        contact_serializer = ContactSerializer(contact)
        return Response(contact_serializer.data)

    #Modificar contacto
    elif request.method == 'PUT':
        contact_serializer = Contact_Update_Serializer(contact, data=request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(contact_serializer.data)
        return Response(contact_serializer.errors)
    #Eliminar contacto
    elif request.method == 'DELETE':
        with in_database(db_name):
            Contact.objects.using(db_name).filter(pk=pk).delete()
            return Response('Eliminado')

class Contact_Filter_APIView(APIView):
    def get(self, request, *args, **kwargs): 
        queryset = Contact.objects.using(db_name).all()

        code_filter = self.request.query_params.get('code', None)
        email_filter = self.request.query_params.get('email', None)
        firstname_filter = self.request.query_params.get('firstname', None)
        lastname_filter = self.request.query_params.get('lastname', None)
        company_filter = self.request.query_params.get('company', None)
        title_filter = self.request.query_params.get('title', None)
        phone_filter = self.request.query_params.get('phone', None)
        address_filter = self.request.query_params.get('address', None)
        city_filter = self.request.query_params.get('city', None)
        region_filter = self.request.query_params.get('region', None)
        country_filter = self.request.query_params.get('country', None)

        
        if code_filter:
            queryset=queryset.filter(code=code_filter)
        if email_filter:
            queryset=queryset.filter(email=email_filter)
        if firstname_filter:
            queryset=queryset.filter(firstname=firstname_filter)
        if lastname_filter:
            queryset=queryset.filter(lastname=lastname_filter)
        if company_filter:
            queryset=queryset.filter(company=company_filter)
        if title_filter:
            queryset=queryset.filter(title=title_filter)
        if phone_filter:
            queryset=queryset.filter(phone=phone_filter)
        if address_filter:
            queryset=queryset.filter(address=address_filter)
        if city_filter:
            queryset=queryset.filter(city=city_filter)
        if region_filter:
            queryset=queryset.filter(region=region_filter)
        if country_filter:
            queryset=queryset.filter(country=country_filter)

    
        if queryset:
            serializer = ContactSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response('Registro no encontado.')


    


  