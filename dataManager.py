'''
Internal Data Manager
Handles data storage and upkeep:
- Market OHLC
- My current orders
'''


# Instantiate data
current_OHLC = {} # Form: {"SYMBOL": [open, high, low, close]}
recent_trades = {} # Form: {"SYMBOL": [[timestamp, volume, price]]}, newer trades in front
current_orders = {} # Form: {"SYMBOL": ...}

time_space = 60 # seconds for relevancy

def coin_value(trade):
    return trade[2] / trade[1]

# # Main function
def data_mgmt():
    while True:
        # Continuously update recent_trades to include only those in specific timestamp frame
        for symbol in recent_trades:
            trades_list = recent_trades[symbol]
            newest_time = trades_list[0][0]
            for trade_num in range(len(trades_list)):
                trade_time = trades_list[trade_num][0]
                if trade_time + time_space < newest_time:
                    del trades_list[trade_num:]
            
            # Calculate OHLC
            open = coin_value(trades_list[-1])
            close = coin_value(trades_list[0])

            high = open
            low = open
            for trade in trades_list:
                trade_value = coin_value(trade)
                if trade_value > high:
                    high = trade_value
                if trade_value < low:
                    low = trade_value
            
            current_OHLC[symbol] = [open, high, low, close]
            


    # Update current_orders with websocket message??

    


