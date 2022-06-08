
from rest_framework.response import Response
from rest_framework.decorators import api_view

from myapi.models import Listing, Contact, Subscriber
##Serializer de versión base. 1.0
from ..serializers import SubscriberCreateApiSerializers
##Serializer de versión 1.1
from ..serializers import (SubscriberCreateSerializer, 
ListingSerializer, ListingNestedSerializer,
ContactEmptyCreateSerializer)
    

def create_list(listing_name, request):
    token = request.META.get('HTTP_AUTHORIZATION', '')
    create_listing = ListingNestedSerializer(data={'name':listing_name}, context= {'token': token})
    if create_listing.is_valid(): #Validamos el serializador.
        #Guardamos el registro en la bd llamando con .save()
        listing = create_listing.save() 
        return listing

def create_contact(code, request):
    token = request.META.get('HTTP_AUTHORIZATION', '')
    create_contacto = ContactEmptyCreateSerializer(data={'code':code}, context= {'token': token})
    if create_contacto.is_valid(): #Validamos el serializador.
        #Guardamos el registro en la bd llamando con .save()
        contacto = create_contacto.save() 
        return contacto

@api_view(['POST'])
def create_api_view(request):
    ##Crear contacto a través de post.
    if request.method == 'POST':
        #Obtenemos el token enviado por header.
        token = request.META.get('HTTP_AUTHORIZATION', '')

        serializer = SubscriberCreateSerializer(data = request.data) 
        
        #Validación de json a travéz de serializer.
        if serializer.is_valid():
            #Obtenemos el modelo para comparar.
            model = serializer.validated_data.get('model')
            #Obtenemos las columnas del json.
            columns = serializer.validated_data.get('columns')
            if model.lower() == "listing":
                #Obtenemos el nombre ingresado vía JSON.
                listing_name = columns['listing']['name']
                if Listing.objects.filter(name=listing_name).exists():
                    return Response('Ya existe una lista con ese nombre.')
                else:
                    listing = create_list(listing_name, request)
                    listing_serializer = ListingSerializer(listing)
                    return Response(listing_serializer.data)

            elif model.lower() == "subscriber":
                print("subscriber")
                listing_name = columns['listing']['name']
                code = columns['contacto']['code']
                ##Verificar lista, si existe usar esa, si no crear una.
                if Listing.objects.filter(name=listing_name).exists():
                    listing = Listing.objects.get(name=listing_name)
                    
                else:
                    listing = create_list(listing_name, request)
                
                if code=="":
                    return Response('El code de contacto no puede estar vacío.')
                else:
                    ##Verificar contacto, si existe usar se, si no crear uno. 
                    if Contact.objects.filter(code=code).exists():
                        
                        contact = Contact.objects.get(code = code)
                    else:
                        contact = create_contact(code, request)
                

                print(listing)
                print(code)
                # Relación subscriber (contacto-listing)
                if Subscriber.objects.filter(contact_id=contact.id, listing_id=listing.id).exists():
                    return Response('Este subscriber ya existe.')
                else:
                    subscriber_serializer = SubscriberCreateApiSerializers(data={'listing_id': listing.id, 'account_id':contact.account.id, 'contact_id':contact.id})
                    if subscriber_serializer.is_valid():
                        subscriber = subscriber_serializer.save() #Aquí guardamos la relación con subscriber, para más info revisar myapp/serializers/subscriber_serializers.py   
                    return Response(subscriber_serializer.data)
            else:
                return Response("Model debe ser listing o subscriber.")
            # listing = Listing.objects.get(pk=serializer.validated_data.get('listing'))
        return Response(serializer.errors)




    


  