
from turtle import st
from rest_framework.authentication import BaseAuthentication
from models.models_mono_base import Account

class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):

        token = request.META.get('HTTP_AUTHORIZATION', '')
        stamp = request.META.get('HTTP_STAMP')
        sig = request.META.get('HTTP_SIG')
        
        #buscar cuenta:
        try:
            acc = Account.objects.filter(api_token = token)
        except:
            print('no hay cuenta')
        
        secret = acc.api_secret

        if request.META.get('HTTP_Test', ''):
            print(request.META.get('HTTP_Test', ''))
        else:
            print('nada')

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
