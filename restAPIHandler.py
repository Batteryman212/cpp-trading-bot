'''
REST API Handler
Handles order management and execution.
*Does not handle actual information sharing (as this 
is done with websocket API), only order execution.
'''

# Import libraries
import requests
import json
import base64
import hmac
import hashlib
import datetime, time


# Helper Functions:
# Create nonce from current timestamp
def nonce():
    t = datetime.datetime.now()
    return str(int(time.mktime(t.timetuple())*1000))

# Encode payload in b64
def b64_encode(payload):
    encoded_payload = json.dumps(payload).encode() # UTF-8 default encoding
    return base64.b64encode(encoded_payload)

# Sign payload with SHA-384 hash
def sign_payload(b64_payload, api_secret):
    return hmac.new(api_secret, b64_payload, hashlib.sha384).hexdigest()

# Build request headers
def create_request(api_key, api_secret, payload):
    b64_payload = b64_encode(payload)
    payload_signature = sign_payload(b64_payload, api_secret)
    request_headers = {
        'Content-Type': "text/plain",
        'Content-Length': "0",
        'X-GEMINI-APIKEY': api_key,
        'X-GEMINI-PAYLOAD': b64_payload,
        'X-GEMINI-SIGNATURE': payload_signature,
        'Cache-Control': "no-cache"
        }
    return request_headers


# API Request Functions:
# Get past trades (migrating to websocket handler)
def api_get_past_trades(api_key, api_secret, base_url):
    endpoint = "/v1/mytrades"
    url = base_url + endpoint
    payload = {
        "request": endpoint, 
        "nonce": nonce()}
    request_headers = create_request(api_key, api_secret, payload)

    response = requests.post(url, headers=request_headers)

    return response.json()

# Place new order
def api_new_order(api_key, api_secret, client_id, symbol, amount, price, side, type="exchange limit"):
    # Example: api_new_order(trade_api_key, trade_api_secret, client_id, base_url, symbol="btcusd", amount=2, price=3633.00, side="buy", type="exchange limit")
    endpoint = "/v1/order/new"
    url = base_url + endpoint
    payload = {
        "request": endpoint, 
        "nonce": nonce(),
        "client_order_id": client_id,
        "symbol": symbol,
        "amount": str(amount),
        "price": str(price),
        "side": side,
        "type": type
        }
    request_headers = create_request(api_key, api_secret, payload)

    response = requests.post(url, headers=request_headers)

    return response.json()

