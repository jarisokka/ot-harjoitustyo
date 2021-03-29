from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError
import pandas as pd
import datetime

def stocktesting(tickersymbol):  
    today = datetime.datetime.today().isoformat()

    try:
        sdata = data.DataReader(tickersymbol, 'yahoo', start='2021-3-26', end=today[:10])
        print(sdata)
    except RemoteDataError:
        print('didn´t work')
    #today = datetime.datetime.today().isoformat()
    #sday = datetime.datetime(2021,3,26)
    #eday = datetime.datetime(2021,3,26)

    #print(today)
    #print(name)
    #tickerDF = tickerdata.history(period='1d', start='2020-1-1', end=today[:10])
    #priceLast = tickerDF['Close'].iloc[-1]
    #priceYest = tickerDF['Close'].iloc[-2]
    #change = priceLast - priceYest
    #print(name + ' ' + str(priceLast))
    #print('Price change = ' + str(change))


stock = 'TELIA1.HE'
stocktesting(stock)
stock = 'NDA-FI.HE'
stocktesting(stock)
stock = 'TIETO.HE'
stocktesting(stock)