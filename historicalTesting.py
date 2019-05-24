'''
Test core AI with historical data from .csv files
'''

"""
TODO
- Rewrite to handle .csv files for 1-min historical data in the following manner:
    Given:
    - Historical range of data to test (start, end date)
    - Symbol(s) to test
    - Core AI algorithm
    - Current investments
    Return:
    - Change in investments at each time step
    - Net change of portfolio value

"""

def run_data(startDate, endDate, symbols, ai, start_investments):
    # For each symbol, open first file
    for symbol in symbols:
        try:
            # TODO open first file in sequence
            fh = open('/path/to/file', 'r')
        except FileNotFoundError:
            # If failed, return with error
            return None
        # If file opens, read

# Calculate net worth from investment volumes
def net_worth(investments):
    net_worth = 0.0

    for coin in investments:
        # Find current value of coin
        usd_conversion = 

        # Multiply volume by usd conversion
        net_worth += investments[coin] * usd_conversion
    
    return net_worth


if __name__ == "__main__":

    # Start and end times
    startDate = "12/31/2015 23:59"
    endDate = "12/7/2015 8:44"

    # Symbols in workspace
    symbols = [BTCUSD, ETHUSD]

    # Core_AI
    ai = core_AI()

    # Current investments
    start_investments = {"BTC": 1.0, "ETH": 0.5}
    print("Start net worth: "+str(net_worth(start_investments)))

    # End investments
    end_investments = run_data(startDate, endDate, symbols, ai, start_investments)
    print("Start net worth: "+str(net_worth(end_investments)))

    
