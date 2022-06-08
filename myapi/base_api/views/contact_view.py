from multiprocessing import context
from tokenize import Name
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.versioning import NamespaceVersioning

from myapi.models import Contact, Listing, Option
from ..serializers import ContactSerializer, ContactUpdateSerializer, ContactCreateAPISerializer
from ..serializers import SubscriberCreateApiSerializers


@api_view(['GET'])
def contact_api_view(request):
    
    #Listar todos los contactos.
    if request.method == 'GET':
        # contacts = Contact.objects.using(db_name).all()
        contacts = Contact.objects.get_all_contacts()
        contacts_serializer = ContactSerializer(contacts, many=True)
                
        return Response(contacts_serializer.data)   

    

@api_view(['POST'])
def contact_create_api_view(request):
    ##Crear contacto a través de post.
    if request.method == 'POST':
        contact_serializer = ContactCreateAPISerializer(data = request.data, context = {'request': request}) #Pasamos request para obtener el token del header en el serializador.
        #Validación de json a travéz de serializer.
        if contact_serializer.is_valid():
            #Método .save() retorna el objeto contacto, lo guardamos en una variable para poder crear relación de subscriber.
            contact = contact_serializer.save() #Guardado de contacto en la bd, para revisar la consulta ir a myapp/serializers/contact_serializer.py/ContactCreateAPISerializer
            listing = Listing.objects.get(pk=contact_serializer.validated_data.get('listing'))

            contact_serializer = ContactSerializer(contact) #Serializamos con el objeto, este serializador es el mismo que en el listing, y detail.
            
            #Relación subscriber (contacto-listing)
            subscriber_serializer = SubscriberCreateApiSerializers(data={'listing_id': listing.id, 'account_id':contact.account.id, 'contact_id':contact.id})
            if subscriber_serializer.is_valid():
                subscriber = subscriber_serializer.save() #Aquí guardamos la relación con subscriber, para más info revisar myapp/serializers/subscriber_serializers.py   
            return Response(contact_serializer.data)
        return Response(contact_serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail_api_view(request, pk=None):
    contact = Contact.objects.get_contact(pk=pk).first()

    #Obtener detalle del contacto
    if request.method == 'GET':
        if contact != None:
            contact_serializer = ContactSerializer(contact)
            return Response(contact_serializer.data)
        return Response('No hay contacto con ese id')

    #Modificar contacto
    elif request.method == 'PUT':
        contact_serializer = ContactUpdateSerializer(contact, data=request.data)
        if contact_serializer.is_valid():
            contact_serializer.save()
            return Response(contact_serializer.data)
        return Response(contact_serializer.errors)
    #Eliminar contacto
    elif request.method == 'DELETE':
        # with in_database(db_name):
        # Contact.objects.using(db_name).filter(pk=pk).delete()
        Contact.objects.get_contact(pk=pk).first().delete()
        return Response('Eliminado')

class Contact_Filter_APIView(APIView):
    def get(self, request, *args, **kwargs): 
        # queryset = Contact.objects.using(db_name).all()
        queryset = Contact.objects.get_all_contacts()
        #https://youtu.be/UQpxUN0y7QM Idea manual, en el futuro cambiar por libreria si es necesario.
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


    


  