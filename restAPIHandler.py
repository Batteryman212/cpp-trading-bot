'''
REST API Handler
Handles order management and execution.
*Does not handle actual information sharing (as this 
is done with websocket API), only order execution.
'''

"""
To-Dos
- Edit code to add buying
- Edit code to add selling
"""

# Import libraries
import requests
import json
import base64
import hmac
import hashlib
import datetime, time

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


# Get URL and API Public/Private keys
url = "https://api.gemini.com/v1/mytrades"
gemini_api_key = "mykey"
gemini_api_secret = "1234abcd".encode() # UTF-8 default encoding

# Create payload
payload = {"request": "/v1/mytrades", "nonce": nonce()}

# Properly encode payload and create signature
b64_payload = b64_encode(payload)
signature = sign_payload(b64_payload, gemini_api_secret)

# Create request headers
request_headers = {
    'Content-Type': "text/plain",
    'Content-Length': "0",
    'X-GEMINI-APIKEY': gemini_api_key,
    'X-GEMINI-PAYLOAD': b64_payload,
    'X-GEMINI-SIGNATURE': signature,
    'Cache-Control': "no-cache"
    }

# Store HTTP POST response
http_response = requests.post(url, headers=request_headers)

# Convert to .JSON and print
my_trades = http_response.json()
print(my_trades)