'''
Handle .CSV files for 1-min historical data in the following manner:
    Given:
    - Historical range of data to test (start, end date)
    - Symbol(s) to test
    - Core AI algorithm
    - Start investments
    Return:
    - Change in investments at each time step
    - Net change of portfolio value
'''

"""
TODO
- Refactor/simplify code
- Check date travelling bugs
- Check usd conversion bugs

"""
import csv
from coreAI import coreAI

def run_data(startDate, endDate, symbols, start_investments):

    candle_ohlc_data = {} # Form: {"SYMBOL": [open, high, low, close]}
    market_files = {} # Form: {"SYMBOL": file}
    file_readers = {} # Form: {"SYMBOL": reader}
    cur_investments = start_investments # Form: {"SYMBOL": amount}
    startYear = startDate.split(' ')[0].split('-')[0]

    # For each symbol, open first file
    for symbol in symbols:
        # Append symbol and initial OHLC to candle_ohlc_data
        candle_ohlc_data[symbol] = [0.,0.,0.,0.]
        path_to_file = './Gemini_Data/'+symbol+'/gemini_'+symbol+'_'+startYear+'_1min.csv'

        try:
            file = open(path_to_file, 'r')
        except FileNotFoundError:
            print("Error: could not open historical data for "+symbol+" in "+startYear)
            return start_investments

        market_files[symbol] = file
        file_readers[symbol] = reversed(list(csv.reader(file, delimiter=',')))
      
    # Get each reader to start date
    for symbol in symbols:
        reader = file_readers[symbol]
        row = next(reader)
        i = 0
        oldrow = row
        while(row[1] < startDate):
            oldrow = row
            row = next(reader)
        if row[1] != startDate:
            print("Error: "+symbol+" dataset jumps from "+str(oldrow[1])+" to "+str(row[1]))
            return start_investments
        candle_ohlc_data[symbol] = row[3:6]

    # Call AI with first Candle data
    cur_investments = coreAI(cur_investments, candle_ohlc_data)

    # Continue through dates
    curDate = startDate
    curYear = startYear
    while curDate < endDate:

        if curDate == curYear+'-12-31 23:59:00':
            curYear = str(int(curYear) + 1)
            
            for symbol in symbols:
                # Close this file, try to open new file
                market_files[symbol].close()

                path_to_file = './Gemini_Data/'+symbol+'/gemini_'+symbol+'_'+curYear+'_1min.csv'

                try:
                    file = open(path_to_file, 'r')
                except FileNotFoundError:
                    print("Error: could not open historical data for "+symbol+" in "+startYear)
                    return start_investments

                market_files[symbol] = file
                file_readers[symbol] = reversed(list(csv.reader(file, delimiter=',')))
            
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

    if curDate != endDate:
        print("Error: dataset jumps to "+curDate)
        return start_investments
    for symbol in symbols:
        market_files[symbol].close()

    return cur_investments

# Calculate net worth from investment volumes
def net_worth(date, investments):
    net_worth = 0.0
    year = date.split(' ')[0].split('-')[0]

    for coin in investments:
        path_to_file = './Gemini_Data/'+coin+'USD/gemini_'+coin+'USD_'+year+'_1min.csv'

        try:
            file = open(path_to_file, 'r')
        except FileNotFoundError:
            print("Error: could not open historical data for "+coin+"USD in "+year)
            return investments

        reader = reversed(list(csv.reader(file, delimiter=',')))
        row = next(reader)

        while(row[1] < date):
            oldrow = row
            row = next(reader)
        if row[1] != date:
            print("Error: "+coin+"USD dataset jumps from "+str(oldrow[1])+" to "+str(row[1]))
            return investments
        
        # USD = close value at date
        usd_conversion = float(row[6])

        # Multiply volume by usd conversion
        net_worth += investments[coin] * usd_conversion
    
    return net_worth


def historical_test(startDate, endDate, symbols, start_investments):

    print("Start net worth on "+startDate+": "+str(net_worth(startDate, start_investments)))

    # End investments
    end_investments = run_data(startDate, endDate, symbols, start_investments)
    print("End net worth on "+startDate+": "+str(net_worth(endDate, end_investments)))

    return

    
