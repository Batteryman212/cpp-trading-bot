'''
Testbench
'''

import unittest
import historicalTesting
import websocketHandler
import dataManager
import coreAI
import restAPIHandler
from cryptobot import *


    

    # 2. Test coreAI.py
    # a. coreAI
    # b. AIInterface

    # 3. Test dataManager.py

    # 4. Test websocketHandler.py

    # 5. Test restAPIHandler.py

class TestStringMethods(unittest.TestCase):
    # For each function, use one of the following:
    # self.assertEqual(func(), retvar)
    # self.assertFalse(func())
    # self.assertTrue(func())
    # with self.assertRaises(TypeError):
    #   func()

    '''
    1. Test cryptobot.py
        a. Test (historical) run
        b. Sandbox run
        c. Live run
    '''
    def test_hist(self):
        startDate = "2018-12-07 21:21:00"
        endDate = "2018-12-08 21:23:00"
        dates = [startDate, endDate]
        symbols = ['BTCUSD', 'ETHUSD']
        start_investments = {"BTC": 1.0, "ETH": 0.5}
        self.assertTrue(hist_run(dates, symbols, start_investments))

    # def test_sandbox(self):

    # def test_live(self):
        

if __name__ == '__main__':
    unittest.main()