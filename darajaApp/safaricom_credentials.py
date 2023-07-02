import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

 
class MpesaC2bCredential:
   
    consumer_key= "" #input your consumer key from the sandbox  
    consumer_secret  = "" #input your consumer secret from the sandbox
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class LipanaMpesaPpassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379" #for stk push
    Test_c2b_shortcode = "600344" #for C2B 
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'  #input your passkey from the safaricom dev portal
    security_credential = "bkg6VGNIs58rDVdIPIgfPYZ/GZzhvez/5pOjt64IX67DnQw9EkPZr5E9SvelO+W62oboDw6IqNSTulOD5T/FJI6vn4T/lyp9dLWuelQWaE4JF/6aN1S7zYI/NL3+j5a988sJe9wQQ9BsHs/4Ny2sQs0OuYAYKI23PzvLGzLCUZmwhajzduruPFKUwyn7HGI8PApsvg898Gk1m/UbctXyPo8Yowp5LnIiyGGEkyb3EUuafL58q/fl0GzayZZkfXJ6a7P1HBQ0CIWoTdc90D1hOfIav8JPo/ZSTP1XYmUYLChJdnFUOQwkveF3dZ06uJMS2gSM4cXIYImUbypySGf0cA=="
    data_to_encode = Business_short_code + passkey + lipa_time

    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')