'''
Testbench
Testing suite used to confirm proper behavior
and error handling for all cryptobot methods.
Tests are grouped by file.
'''

import unittest
import historicalTesting as histt
from websocketHandler import *
from dataManager import *
from coreAI import *
from restAPIHandler import *
from cryptobot import *

# For each function, use the following to confirm proper behavior:
    # self.assertEqual(func(), retvar)
    # self.assertFalse(func())
    # self.assertTrue(func())
    # with self.assertRaises(TypeError):
    #   func()

class TestFunctionMethods(unittest.TestCase):
    '''
    1. Test historicalTesting.py
        a. run_data
        b. net_worth
        c. historical_test
    '''
    def test_run_data(self):
        # Proper procedure
        symbols = ['BTCUSD', 'ETHUSD']
        start_investments = {"BTC": 1.0, "ETH": 0.5}
        startDate = "2018-12-07 21:21:00"
        endDate = "2018-12-08 21:23:00"

        end_investments = histt.run_data(startDate, endDate, symbols, start_investments)
        self.assertTrue(len(end_investments) == len(start_investments))
        self.assertTrue(end_investments["BTC"] > 0 and end_investments["ETH"] > 0)

        # Confirm error on out-of-order dates
        with self.assertRaises(AssertionError):
            end_investments = histt.run_data(endDate, startDate, symbols, start_investments)

    '''
    2. Test dataManager.py
        a. current_OHLC_daemon
        b. recent_trades_daemon
        c. current_orders_daemon
        d. start_data_mgmt
    '''

    '''
    3. Test websocketHandler.py
        a. on_message
        b. on_error
        c. on_close
        d. ws_nonce
        e. b64_encode
        f. sign_payload
        g. create_private_request
        h. socket_sequence_verify
        i. start_order_events_ws
        j. start_market_data_ws
    '''

    '''
    4. Test restAPIHandler.py
        a. nonce
        b. b64_encode
        c. sign_payload
        d. create_request
        e. api_get_past_trades
        f. api_new_order
    '''

    '''
    5. Test coreAI.py
        a. coreAI
        b. AIInterface
    '''

    '''
    6. Test cryptobot.py
        a. live_run
        b. sandbox_run
        c. hist_run
    ''' 

if __name__ == '__main__':
    unittest.main()