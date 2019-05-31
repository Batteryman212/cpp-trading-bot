'''
Market Indicators

File for market indicators used by the core AI, possibly including but not limited to:
- SMA (simple moving average)
- EMA (exponential moving average)
- MACD
- RSI
- Bollinger Bands
- Fibonacci Retracement
- Elliot Waves

Assume that the indicators have access to:
- VWAP (volume-weighted average price) array
- OHLC (open-high-low-close) array
'''

# Initialize classes

class SMA_Indicator:
    def __init__(self):
        self.short = self.SMA(5)
        self.long = self.SMA(15)
        self.diff = 0

    def update_diff(price_array):
        self.short.update(price_array[0], price_array[self.short.period])
        self.long.update(price_array[0], price_array[self.long.period])
        self.diff = self.short.avg - self.long.avg

class SMA:
    def __init__(self, period):
        self.period = period
        self.avg = 0

    def update(self, in_price, out_price):
        self.avg += (in_price - out_price)/self.period

class EMA_Indicator:
    def __init__(self):
        self.short = self.EMA(5, 2)
        self.long = self.EMA(15, 2)
        self.diff = 0

    def update_diff(price_array):
        self.short.update(price_array[0])
        self.long.update(price_array[0])
        self.diff = self.short.avg - self.long.avg

class EMA:
    def __init__(self, period, s_fac):
        self.period = period
        self.avg = 0
        self.s_fac = s_fac
        self.smooth = self.s_fac/(1+self.period)

    def update(self, in_price):
        self.avg = in_price*self.smooth + self.avg*(1-self.smooth)

class MACD_Indicator:
    def __init__(self):
        self.short = self.EMA(9, 2)
        self.medium = self.EMA(12, 2)
        self.long = self.EMA(26, 2)
        self.signal_diff = 0
        self.zero_diff = 0

    def update_diff(price_array):
        self.short.update(price_array[0])
        self.medium.update(price_array[0])
        self.long.update(price_array[0])
        self.zero_diff = self.medium.avg - self.long.avg
        self.signal_diff = self.zero_diff - self.short.avg

def initialize_indicators():
    sma_ind = SMA_Indicator()
    ema_ind = EMA_Indicator()
    macd_ind = MACD_Indicator()

def update_indicators(price_array):

    sma_ind.update_diff(price_array)
    ema_ind.update_diff(price_array)
    macd_ind.update)diff(price_array)

def rsi():
    return

def bollinger_bands():
    return
