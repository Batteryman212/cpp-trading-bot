'''
Test core AI with historical data from .csv files
'''

"""
Handle .CSV files for 1-min historical data in the following manner:
    Given:
    - Historical range of data to test (start, end date)
    - Symbol(s) to test
    - Core AI algorithm
    - Start investments
    Return:
    - Change in investments at each time step
    - Net change of portfolio value
"""
import csv

def run_data(startDate, endDate, symbols, start_investments):

    candle_ohlc_data = {} # Form: {"SYMBOL": [open, high, low, close]}
    market_files = {} # Form: {"SYMBOL": file}
    file_readers = {} # Form: {"SYMBOL": reader}
    cur_investments = start_investments
    startYear = startDate.split(' ')[0].split('-')[0]

    # For each symbol, open first file
    for symbol in symbols:
        # Append symbol and initial OHLC to candle_ohlc_data
        candle_ohlc_data[symbol] = [0.,0.,0.,0.]
        path_to_file = './Gemini_Data/'+symbol+'/gemini_'+symbol+'_'+startYear+'_1min.csv'

        try:
            file = open(path_to_file, 'r')
        except FileNotFoundError:
            print("Error: could not open historical data for "+symbol)
            return cur_investments

        market_files[symbol] = file
        file_readers[symbol] = csv.reader(file, delimiter=',')
      
    # Get each reader to start date
    for symbol in symbols:
        reader = file_readers[symbol]
        title = next(reader)
        headers = next(reader)
        row = next(reader)
        print(row)
        print(startDate)
        while(row[1] != startDate):
            row = next(reader)
        candle_ohlc_data[symbol] = row[3:6]

    # Call AI with first Candle data
    cur_investments = coreAI(cur_investments, candle_ohlc_data)

    # Continue through dates
    curDate = startDate
    curYear = startYear
    while curDate != endDate:

        if curDate == '12/31/'+curYear+' 23:59':
            curYear += 1
            
            for symbol in symbols:
                # Close this file, try to open new file
                market_files[symbol].close()

                path_to_file = './Gemini_Data/'+symbol+'/gemini_'+symbol+'_'+curYear+'_1min.csv'

                try:
                    file = open(path_to_file, 'r')
                except FileNotFoundError:
                    print("Error: could not open historical data for "+symbol)
                    return cur_investments

                market_files[symbol] = file
                file_readers[symbol] = csv.reader(file, delimiter=',')
                title = next(reader)
                headers = next(reader)
            
        curDateSet = False 
        for symbol in symbols:
            reader = file_readers[symbol]
            row = next(reader)
            if not curDateSet:
                curDate = row[1]
                curDateSet = True
            
            # Update market_data
            candle_ohlc_data[symbol] = row[3:6]

        # Call AI and update investments
        cur_investments = coreAI(cur_investments, candle_ohlc_data)
    

    return cur_investments

# Calculate net worth from investment volumes
def net_worth(date, investments):
    net_worth = 0.0

    for coin in investments:
        # Find current value of coin using close value on date
        usd_conversion = 0

        # Multiply volume by usd conversion
        net_worth += investments[coin] * usd_conversion
    
    return net_worth


if __name__ == "__main__":

    # Start and end times
    startDate = "2018-12-7 9:12:00"
    endDate = "2018-12-7 9:13:00"

    # Symbols in workspace
    symbols = ['BTCUSD', 'ETHUSD']

    # Current investments
    start_investments = {"BTC": 1.0, "ETH": 0.5}
    print("Start net worth: "+str(net_worth(startDate, start_investments)))

    # End investments
    end_investments = run_data(startDate, endDate, symbols, start_investments)
    print("Start net worth: "+str(net_worth(endDate, end_investments)))

    
