from django.http import HttpResponse, JsonResponse
import requests
from requests.auth import HTTPBasicAuth
import json
from . safaricom_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment
from django.conf import settings
# start of the stk integration
def getAccessToken(request):
    consumer_key= settings.c2b_consumer_key #input your consumer key from the sandbox  
    consumer_secret  = "" #input your consumer secret from the sandbox
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    mpesa_access_token = r.json()
    validated_mpesa_access_token = mpesa_access_token['access_token']
    
    return HttpResponse(validated_mpesa_access_token)


def lipa_na_mpesa_online(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": 254714919899,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254791418947,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "hacker",
        "TransactionDesc": "Testing stk push"
    }
    response = requests.post(api_url, json=request, headers=headers)
    
    return HttpResponse(response)

# end of the stk integration

#start of C2B mpesa payments

@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
   
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://02ea-105-163-1-124.ngrok-free.app/api/v1/c2b/confirmation",
               "ValidationURL": "https://02ea-105-163-1-124.ngrok-free.app/api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    print(response)
    return HttpResponse(response.text)
@csrf_exempt
def call_back(request):
    pass
@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
  
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))

#end of C2B mpesa payments


#start of B2C mpesa payments

# def b2c_payments(request):
#     access_token = MpesaAccessToken.validated_mpesa_access_token
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     Body = {
#         "InitiatorName": "testapi",
#         "SecurityCredential": "bkg6VGNIs58rDVdIPIgfPYZ/GZzhvez/5pOjt64IX67DnQw9EkPZr5E9SvelO+W62oboDw6IqNSTulOD5T/FJI6vn4T/lyp9dLWuelQWaE4JF/6aN1S7zYI/NL3+j5a988sJe9wQQ9BsHs/4Ny2sQs0OuYAYKI23PzvLGzLCUZmwhajzduruPFKUwyn7HGI8PApsvg898Gk1m/UbctXyPo8Yowp5LnIiyGGEkyb3EUuafL58q/fl0GzayZZkfXJ6a7P1HBQ0CIWoTdc90D1hOfIav8JPo/ZSTP1XYmUYLChJdnFUOQwkveF3dZ06uJMS2gSM4cXIYImUbypySGf0cA==",
#         "CommandID": "BusinessPayment",
#         "Amount": 1,
#         "PartyA": 600980,
#         "PartyB": LipanaMpesaPpassword.Test_c2b_shortcode,
#         "PhoneNumber": 254791417147, 
#         "Remarks": "Test remarks",
#         "QueueTimeOutURL": "https://mydomain.com/b2c/queue",
#         "ResultURL": "https://mydomain.com/b2c/result",
#         "Occassion": "null" 
#     }
#     response = requests.post(api_url, json=Body, headers=headers)
    
#     return HttpResponse(response)


# def timeView (request):
#     return HttpResponse(response)


# def resultsView (request):
#     return HttpResponse(response)




