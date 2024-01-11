# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings  # Import settings directly

import stripe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePayment(APIView):
    def post(self, request, *args, **kwargs):
        try:
            amount = request.data.get('amount')  # Amount in cents
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
            )
            return Response({'client_secret': intent.client_secret})
        except Exception as e:
            return Response({'error': str(e)}, status=500)

@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers['HTTP_STRIPE_SIGNATURE']
    endpoint_secret = settings.ENDPOINT_SECRET

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the event
    if event['type'] == 'payment_intent.succeeded':
        # Payment succeeded, handle accordingly
        pass
    elif event['type'] == 'payment_intent.payment_failed':
        # Payment failed, handle accordingly
        pass

    return HttpResponse(status=200)


def payment_form(request):
    return render(request, 'payment.html')

