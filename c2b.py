import requests
from requests.auth import HTTPBasicAuth


# files 
import keys

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret  
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
print(r.json())
print(r.text)
json_response = r.json()
my_access_token = json_response['access_token']
print(my_access_token)
access_token = my_access_token

def register_url():
    api_url = 'https://api.line.me/v2/bot/message/push'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }
    request = {    
    "ShortCode": keys.short_code,
    "ResponseType":"[Cancelled/Completed]",
    "ConfirmationURL":"[confirmation URL]",
    "ValidationURL":"[validation URL]"
    }

    response = requests.post(api_url, headers=headers, data=request)
    print(response.status_code)

register_url()