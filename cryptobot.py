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

# Start program with python cryptobot.py (>= Python 3.5 ONLY)
if __name__ == "__main__":
    
    # Parse Arguments
    parser = argparse.ArgumentParser(prog='Cryptocurrency Trading Bot', description='Crypto bot that trades cryptocurrencies on the Gemini exchange.')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-live', action='store_true', help='Start a live run')
    group.add_argument('-test', dest='date', nargs=2, type=str, help='Test with historical dates of form "YYYY-MM-DD HH:MM:SS"')

    args = parser.parse_args()

    print(args)
    if args.live:
        print("Live now")
        # Start live run
    else:
        print("Test now")
        print("Date 1: "+args.date[0])
        print("Date 2: "+args.date[1])
        # Start test with dates