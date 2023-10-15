# form python
import base64
import json
from datetime import datetime
# installed 
import requests
# files
import accesstoken
import keys
import stkpush

# Define the access token (import it from your accessToken.py file)
access_token = accesstoken.my_access_token

# Define the timestamp
unformatted_time = datetime.now()
formatted_time = unformatted_time.strftime('%Y%m%d%H%M%S')
# print(formatted_time)

data_to_encode = keys.business_shortcode + keys.passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())
decoded_password = encoded_string.decode('utf-8')
# print(decoded_password)
passkey = keys.passkey



query_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query'
business_shortcode = keys.business_shortcode
checkout_request_id = stkpush.checkout_request_id


# Define headers
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}' 
}

# Define the request data
payload = {
    "BusinessShortCode": business_shortcode,
    "Password": decoded_password,
    "Timestamp": formatted_time,
    "CheckoutRequestID": checkout_request_id
}

payload_json = json.dumps(payload)


response = requests.post(query_url, headers=headers, data=payload_json)


json_response = response.json()
print(response.text)
response_data = json.loads(response.text)
response_data = response_data.get("ResponseCode")
print(response_data)

# Process the response and get the result message
result_code = response_data
if result_code == 1037:
    message = "1037 Timeout in completing transaction"
elif result_code == 1032:
    message = "1032 Transaction has been canceled by the user"
elif result_code == "1":
    message = "1 The balance is insufficient for the transaction"
elif result_code == 0:
    message = "0 The transaction is successful"
else:
    message = "Unknown result code"

print(result_code)  