import yfinance as yf

class MarketInfo:

    def __init__(self, tickersymbol: str):
        self.tickersymbol = tickersymbol
        self.tickerdata = None
        self.tickerinfo = None
        self.name = None
        self.indexPreviousDay = None
        self.indexNow = None

    def stockMarketSearch(self, tickersymbol):
        self.tickerdata = yf.Ticker(self.tickersymbol)
        self.tickerinfo = self.tickerdata.info
        self.name = self.tickerinfo['shortName']
        self.indexPreviousDay = self.tickerinfo['regularMarketPreviousClose']
        self.indexNow = self.tickerinfo['regularMarketPrice']

    def getSymbol(self):   
        return self.tickersymbol

    def getName(self):   
        return self.name

    def getClose(self):
        return self.indexPreviousDay 

    def getNow(self):
        return self.indexNow

    def getChange(self):
        valuePoints = "{:.2f}".format(self.indexNow - self.indexPreviousDay)
        valueProcent = "{:.2f}".format(((self.indexNow - self.indexPreviousDay)/self.indexPreviousDay)*100)
        return print('Change: ' + str(valuePoints) + ' ' + str(valueProcent) + '%')
    
    def getOpenNow(self):
        return print('Close previous day: ' + str(self.indexPreviousDay) + ' Now: ' + str(self.indexNow))

if __name__ == "__main__":
    market = MarketInfo('^OMXH25')
    market.stockMarketSearch(market.getSymbol())
    print(market.getName())
    market.getChange()
    market.getOpenNow()
