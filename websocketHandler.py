'''
Websocket Handler
Handles info data over websocket connection, including:
 - Private order data
 - Public market data
*Does not handle actual order execution, only information sharing.
'''
"""
To-Dos
- Review current code
- Edit code to add private order data handling
- Edit code to include market data
"""

import ssl
import websocket
import json
import base64
import hmac
import hashlib
import time

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

gemini_api_key = "mykey"
gemini_api_secret = "1234abcd".encode()

payload = {"request": "/v1/order/events","nonce": int(time.time()*1000))}
encoded_payload = json.dumps(payload).encode()
b64 = base64.b64encode(encoded_payload)
signature = hmac.new(gemini_api_secret, b64, hashlib.sha384).hexdigest()


ws = websocket.WebSocketApp("wss://api.sandbox.gemini.com/v1/order/events",
                            on_message=on_message,
                            header={
                                'X-GEMINI-PAYLOAD': b64.decode(),
                                'X-GEMINI-APIKEY': gemini_api_key,
                                'X-GEMINI-SIGNATURE': signature
                            })
ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})