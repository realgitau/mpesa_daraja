# from python
import base64
from datetime import datetime
import json
# installed
import requests
from requests.auth import HTTPBasicAuth
# files
import keys
import accesstoken



unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime('%Y%m%d%H%M%S')
# print(formatted_time)
data_to_encode = keys.business_shortcode + keys.passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_string.decode('utf-8')
# print(decoded_password)

access_token = accesstoken.my_access_token
process_request_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
passkey = keys.passkey

headers = {
  'Content-Type': 'application/json',
  'Authorization': f'Bearer {access_token}' 
}
payload = {
    "BusinessShortCode": keys.business_shortcode,
    "Password": decoded_password,
    "Timestamp": formatted_time,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": 1,
    "PartyA": 254745291223,
    "PartyB": 174379,
    "PhoneNumber": 254745291223,
    "CallBackURL": "https://mydomain.com/path",
    "AccountReference": "GITAU TEST",
    "TransactionDesc": "Payment of X" 
  }

payload_json = json.dumps(payload)

response = requests.post(process_request_url, headers=headers, data=payload_json)
json_response = response.json()
print(response.text)
message = json_response['ResponseDescription']
print(message)

# print(response.text.encode('utf8'))