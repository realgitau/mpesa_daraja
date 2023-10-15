import requests
# files 
import keys
import accesstoken



def register_url():
    access_token = accesstoken.my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = { "Authorization": f"Bearer {access_token}" }
    request = {
        "ShortCode": keys.short_code,
        "ResponseType": "Completed",
        "ConfirmationURL": "https://fullstackdjango.com/confirmation",
        "ValidationURL": "https://fullstackdjango.com/validation_url"
    }

    response = requests.post(api_url, json = request , headers=headers)

    print(response.text)

register_url()

# simulate
def simulate_c2btransaction():
    access_token = accesstoken.my_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
    headers = { "Authorization": f"Bearer {access_token}" }
    request = {
        "ShortCode": keys.short_code,
        "CommandID": "CustomerPayBillOnline",
        "Amount": "2",
        "Msisdn": keys.phone_number,
        "BillRefNumber": "12345678"
    }

    response = requests.post(api_url, json = request, headers=headers)

    print(response.text)

simulate_c2btransaction()