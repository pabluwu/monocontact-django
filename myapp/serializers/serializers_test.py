from rest_framework import serializers
from mono_base.models import User, Account
from myapp.models.models_mono_99 import Event, UserRole, AccountUser

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
    
 