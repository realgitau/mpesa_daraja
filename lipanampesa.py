import base64
from datetime import datetime
# installed
import requests
from requests.auth import HTTPBasicAuth
# files
import keys


unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime('%Y%m%d%H%M%S')
# print(formatted_time)

data_to_encode = keys.business_shortcode + keys.lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_string.decode('utf-8')

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret  
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
print(r.json())
print(r.text)
json_response = r.json()
my_access_token = json_response['access_token']
print(my_access_token)


def lipa_na_mpesa():
    access_token = my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer qkZn8V1PgGpv87TRzdz3VeUTcZt9'
    }
    payload = {
        "BusinessShortCode": keys.business_shortcode,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": 1,
        "PartyA": keys.PartyA,
        "PartyB": keys.business_shortcode,
        "PhoneNumber": keys.PartyA,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X" 
    }
    response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, data = payload)
    print(response.text.encode('utf8'))

#lipa_na_mpesa()