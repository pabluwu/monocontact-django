from rest_framework import serializers
from mono_base.models import Account
from myapp.models.models_mono_99 import Contact, Listing
from django.core import validators

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        contact = validated_data
                
        return Contact.objects.create(**validated_data)

class ContactCreateAPISerializer(serializers.Serializer):
    code = serializers.CharField(max_length=255, allow_blank = False, allow_null = False )
    firstname = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    lastname = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    company = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    title = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    phone = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    address = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    city = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    region = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    country = serializers.CharField(max_length=255, allow_blank=True, allow_null=True)
    listing = serializers.IntegerField(required = True)

    ##Método para validar que el code sea único.
    def validate_code(self, value):
        get_token = self.context.get('request').META.get('HTTP_AUTHORIZATION', '')
        acc = Account.objects.get(api_token=get_token)
        #Validamos que la cuenta sea de barnechea, si es de barnechea su code debe ser el rut y no un email.
        if acc.id != 74:
            #Validamos que tenga el formato de un email
            validator = validators.EmailValidator(message='Ingrese un email válido.')
            validator(value)

            lower_email = value.lower()
            if Contact.objects.filter(code__iexact=lower_email).exists():
                raise serializers.ValidationError('El code envíado ya existe.')
            return lower_email
        else:
            return value
    
    #Válidamos que exista una lista con el id ingresado.
    def validate_listing(self, value):
        if Listing.objects.filter(id=value).exists():
            return value
        raise serializers.ValidationError('No existe lista con ese id.')

    def create(self, validated_data):
        get_token = self.context.get('request').META.get('HTTP_AUTHORIZATION', '')
        acc = Account.objects.get(api_token=get_token)
        contacto = Contact(
            ## Valores manuales.
            code = validated_data.get('code'),
            account_id = acc.id,
            email = validated_data.get('code'),
            firstname = validated_data.get('firstname'),
            lastname = validated_data.get('lastname'),
            company = validated_data.get('company'),
            title = validated_data.get('title'),
            phone = validated_data.get('phone'),
            address = validated_data.get('address'),
            region = validated_data.get('region'),
            country = validated_data.get('country'),
            ##Valores aumaticos de la api. 
            created_source = 4, 
            created_by = 0,
            updated_source = 4,
            updated_by = 0,
        )
        contacto.save()
        return contacto

class ContactUpdateSerializer(serializers.ModelSerializer):
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
        