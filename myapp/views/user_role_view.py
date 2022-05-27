from django import db
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view  



from myapp.serializers.serializers_test import User_Serializer

from myapp.models.models_mono_99 import UserRole
from mono_base.models import User, AccountUser

#Selección bd.

@api_view(['GET'])
def user_api_view(request, pk=None):
    #Listar todos los contactos.
    try:
        user_role = UserRole.objects.all()
        for u in user_role:
            if u.account_user.user_id == pk:
                user = User.objects.get(pk=u.account_user.user_id)
                break
        
        if request.method == 'GET':
            user_serializer = User_Serializer(user)
            return Response(user_serializer.data)   
    except:
       return Response('Usuario no existe.')


class User_Filter_APIView(APIView):
    def get(self, request, *args, **kwargs):
        

        id_filter = self.request.query_params.get('id', None)
        print(id_filter)
        if id_filter:
            queryset = UserRole.objects.using(db_name).all()
            for u in queryset:
                print('inicio')
                print(u.account_user.user_id, id_filter)
                if str(u.account_user.user_id) == str(id_filter):
                    print('test')
                    queryset = User.objects.filter(pk=u.account_user.user_id).first()
                    break
                print('prueba')

        if queryset:
            serializer = User_Serializer(queryset, many=False)
            return Response(serializer.data)
        else:
            return Response('Registro no encontrado.')




