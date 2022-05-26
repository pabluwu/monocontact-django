
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from mono_base.models import Account
import hashlib

from django.contrib.auth.models import AnonymousUser

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get('HTTP_AUTHORIZATION', '')
            stamp = request.META.get('HTTP_STAMP')
            sig = request.META.get('HTTP_SIG')
        except:
            raise exceptions.AuthenticationFailed('Debe ingresar todas las credenciales.')
        user = AnonymousUser
        #buscar cuenta:
        try:
            acc = Account.objects.get(api_token = token)
            secret = acc.api_secret
            concat = token+stamp+secret
        except Account.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such token')
        
        
        dk = hashlib.sha256()
        dk.update(concat.encode('utf-8'))
        
        if(dk.hexdigest() == sig):
            user = AnonymousUser
        else:
            user = None
        return (user, None)

	#   $stamp = $_SERVER['HTTP_X_AUTH_TIMESTAMP'];
	# 	$token = $_SERVER['HTTP_X_AUTH_TOKEN'];
	# 	// $secret = self::SECRET; // get from Token
	# 	$sig = $_SERVER['HTTP_X_AUTH_SIGNATURE'];

	# 	// buscamos token en base de datos
	# 	$account = Account::model()->findByAttributes(array('api_token'=> $token));
	# 	if (!$account) $this->_sendResponse(401);

	# 	$secret = $account->api_secret;
	# 	$account_id = $account->id;

	# 	if (hash_hmac('SHA256', $stamp.$token, $secret) != $sig) $this->_sendResponse(401);
