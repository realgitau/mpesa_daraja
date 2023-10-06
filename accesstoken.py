import requests
from requests.auth import HTTPBasicAuth


# files
import keys

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secret 
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
headers = { 'Authorization': 'Bearer cFJZcjZ6anEwaThMMXp6d1FETUxwWkIzeVBDa2hNc2M6UmYyMkJmWm9nMHFRR2xWOQ==' }

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
# print(r.text)
json_response = r.json()
my_access_token = json_response['access_token']
# print(my_access_token)