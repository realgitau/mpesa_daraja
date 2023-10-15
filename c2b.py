import requests
# files 
import keys
import accesstoken

access_token = accesstoken.my_access_token
api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
headers = { "Authorization": f"Bearer {access_token}" }
request = {
    "ShortCode": keys.business_shortcode,
    "ResponseType": "Completed",
    "ConfirmationURL": "https://fullstackdjango.com/confirmation",
    "ValidationURL": "https://fullstackdjango.com/validation_url"
}

response = requests.post(api_url, json = request, headers=headers)

print(response.text)