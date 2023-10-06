import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Transaction

@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        # Read the STK Callback response from the request
        stkCallbackResponse = request.body.decode('utf-8')

        # Log the response to a JSON file (optional)
        log_file = "Mpesastkresponse.json"
        with open(log_file, "a") as log:
            log.write(stkCallbackResponse)

        # Parse the JSON data
        data = json.loads(stkCallbackResponse)

        # Extract relevant fields from the JSON data
        merchant_request_id = data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = data['Body']['stkCallback']['CheckoutRequestID']
        result_code = data['Body']['stkCallback']['ResultCode']
        result_desc = data['Body']['stkCallback']['ResultDesc']
        amount = data['Body']['stkCallback']['CallbackMetadata']['Item'][0]['Value']
        transaction_id = data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']
        user_phone_number = data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

        # Check if the transaction was successful (ResultCode == 0)
        if result_code == 0:
            # Store the transaction details in the database
            Transaction.objects.create(
                merchant_request_id=merchant_request_id,
                checkout_request_id=checkout_request_id,
                result_code=result_code,
                amount=amount,
                transaction_id=transaction_id,
                phone_number=user_phone_number,
            )

        return JsonResponse({"message": "Callback received"})

    return JsonResponse({"message": "Unsupported method"}, status=405)
