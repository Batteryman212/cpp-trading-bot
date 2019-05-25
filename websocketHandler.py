'''
Websocket Handler
Handles info data over websocket connection, including:
 - Private order data
 - Public market data
*Does not handle actual order execution (as this is done with REST API), only information sharing.
'''

# Import libraries
import ssl
import websocket
import json
import base64
import hmac
import hashlib
import time
import re
import dataManager  # Import all names from dataManager

base_url = "wss://api.sandbox.gemini.com"

# Helper Functions:
# On message, print
def on_message(ws, message):
    # Update current OHLC
    symbol = re.split('/|\?', ws.url)[5]
    msg_split = re.split(':|,', message)
    if symbol not in dataManager.recent_trades:
        dataManager.recent_trades[symbol] = []
    time = int(msg_split[5])
    volume = float(re.split('"', msg_split[18])[1])
    price = float(re.split('"', msg_split[16])[1])
    dataManager.recent_trades[symbol].insert(0, [time, volume, price])
    print(dataManager.recent_trades)

# On error, print
def on_error(ws, error):
    print(error)

# On close, print
def on_close(ws):
    print("### closed ###")

# Create websocket nonce from timestamp
def ws_nonce():
    t = time.time()
    return int(t*1000)

# Encode payload in b64 (copied from REST handler)
def b64_encode(payload):
    encoded_payload = json.dumps(payload).encode() # UTF-8 default encoding
    return base64.b64encode(encoded_payload)

# Sign payload with SHA-384 hash (copied from REST handler)
def sign_payload(b64_payload, api_secret):
    return hmac.new(api_secret, b64_payload, hashlib.sha384).hexdigest()

# Build private request headers
def create_private_request(api_key, api_secret, payload):
    b64_payload = b64_encode(payload)
    payload_signature = sign_payload(b64_payload, api_secret)
    request_headers = {
        'X-GEMINI-APIKEY': api_key,
        'X-GEMINI-PAYLOAD': b64_payload.decode(),
        'X-GEMINI-SIGNATURE': payload_signature
        }
    return request_headers

# Socket sequence verifier (still need to integrate this check with errors)
def socket_sequence_verify(socket_sequence, last_num):
    if socket_sequence == last_num + 1:
        return True
    else:
        return False


# API Request Functions
# Get order events
def api_get_order_events(api_key, api_secret):
    endpoint = "/v1/order/events"
    url = base_url + endpoint
    payload = {
        "request": endpoint, 
        "nonce": ws_nonce()}

    request_headers = create_private_request(api_key, api_secret, payload)

    ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close, header=request_headers)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

    return ws

# Get market data
def api_get_market_data(symbol, heartbeat='false', top_of_book='false', bids='true', offers='true', trades='true', auctions='true'):

    endpoint = "/v1/marketdata/"+symbol+"?heartbeat="+heartbeat+"&top_of_book="+top_of_book+"&bids="+bids+"&offers="+offers+"&trades="+trades+"&auctions="+auctions
    url = base_url + endpoint

    ws = websocket.WebSocketApp(url, on_message=on_message, on_error=on_error, on_close=on_close)
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})
    print("Got this far")

    return ws


# Main function body
if __name__ == "__main__":

    # Get API Keys
    read_api_key = "mykey"
    read_api_secret = "1234abcd".encode()

    # # Get order events
    # ws_events = api_get_order_events(read_api_key, read_api_secret)
    # events = ws_events.recv()
    # print(events)
    # ws_events.close()

    # Get market data
    ws_data = api_get_market_data("BTCUSD", heartbeat='false', top_of_book='false', bids='false', offers='false', trades='true', auctions='false')
    # data = ws_data.recv()
    # print(data)
    # ws_data.close()



