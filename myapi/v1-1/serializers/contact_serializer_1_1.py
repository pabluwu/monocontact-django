from rest_framework import serializers
from mono_base.models import Account
from django.core.validators import EmailValidator 
from myapi.models import Contact, Option


class ContactNestedSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, allow_blank = True, allow_null = False )


class ContactEmptyCreateSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, allow_blank = True, allow_null = False )

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
        
        opt = Option.objects.get_contact_key().first()


        if int(opt.value) == 1:
            #Validamos que tenga el formato de un email
            try:
                EmailValidator()(validated_data.get('code'))
            except:
                raise serializers.ValidationError('El code debe ser un correo válido. Ej: email@email.cl')
        else:
            code = validated_data.get('code')
        contacto = Contact(
            ## Valores manuales.
            code = validated_data.get('code'),
            account_id = acc.id,
            email = validated_data.get('code'),
            ##Valores aumaticos de la api. 
            created_source = 4, 
            created_by = 0,
            updated_source = 4,
            updated_by = 0,
        )
        contacto.save()
        print(contacto)
        return contacto