'''
Crypto Bot
Written by Austin J. Born, Summer '19

Purpose: To automatically trade cryptocurrencies on 
open exchanges and take advantage of the rising crypto market
value.

Challenge: Extract significant value from the crypto industry, and
to hopefully generate passive income.

Examples of use:
python cryptobot.py -live
python cryptobot.py -test "2018-12-07 21:21:00" "2018-12-08 21:23:00"
'''

import argparse
import threading
from websocketHandler import api_get_market_data, api_get_order_events
from coreAI import AIInterface
from dataManager import data_mgmt
from historicalTesting import historical_test

def live_run():
    # Start data management
    data_mgmt()
    
    # Get Websocket Info
    ws_api_key = "mykey"
    ws_api_secret = "1234abcd".encode()
    ws_symbol = "BTCUSD"
    url = "wss://api.gemini.com"

    #Thread run
    api_get_market_data(ws_symbol, url)

    #Thread run
    api_get_order_events(ws_api_key, ws_api_secret, url)

    # Get AI Info
    ai_api_key = "mykey"
    ai_api_secret = "1234abcd".encode() # UTF-8 default encoding
    client_id = "Batteryman212"

    # Thread run
    AIInterface(ai_api_key, ai_api_secret, client_id, url)

    return True

def sandbox_run():
    # Start data management
    data_mgmt()
    
    # Get Websocket Info
    ws_api_key = "mykey"
    ws_api_secret = "1234abcd".encode()
    ws_symbol = "BTCUSD"
    url = "wss://api.sandbox.gemini.com"

    #Thread run
    api_get_market_data(ws_symbol, url)

    #Thread run
    api_get_order_events(ws_api_key, ws_api_secret, url)

    # Get AI Info
    ai_api_key = "mykey"
    ai_api_secret = "1234abcd".encode() # UTF-8 default encoding
    client_id = "Batteryman212"

    # Thread run
    AIInterface(ai_api_key, ai_api_secret, client_id, url)

    return True

def hist_run(dates, symbols, start_investments):
    # Start data management
    # data_mgmt()

    # Run historical testing
    historical_test(dates[0], dates[1], symbols, start_investments)

    return True

# Start program with python cryptobot.py (>= Python 3.5 ONLY)
if __name__ == "__main__":
    
    # Parse Arguments
    parser = argparse.ArgumentParser(prog='Cryptocurrency Trading Bot', description='Crypto bot that trades cryptocurrencies on the Gemini exchange.')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-live', action='store_true', help='Start a live exchange run')
    group.add_argument('-sandbox', action='store_true', help='Start a live sandbox run')
    group.add_argument('-hist', action='store_true', dest='date', nargs=2, type=str, help='Test with historical dates of form "YYYY-MM-DD HH:MM:SS"')

    args = parser.parse_args()

    print(args)
    if args.hist:
        symbols = ['BTCUSD', 'ETHUSD']
        start_investments = {"BTC": 1.0, "ETH": 0.5}
        test_run(args.date, symbols, start_investments) # Start test with dates
    else:
        
        if args.live:
            live_run() # Start live run
        if args.sandbox:
            sandbox_run() # Start live sandbox run