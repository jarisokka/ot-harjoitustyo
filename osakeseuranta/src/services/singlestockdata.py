import yfinance as yf

class SingleStockData:

    def __init__(self, tickersymbol: str):
        self.tickersymbol = tickersymbol
        self.tickerinfo = None
        self.indexPreviousDay = None
        self.indexNow = None

    def stockSearchDay(self):
        self.tickerdata = yf.Ticker(self.tickersymbol)
        self.tickerinfo = self.tickerdata.info 
        self.indexPreviousDay = self.tickerinfo['regularMarketPreviousClose']
        self.indexNow = self.tickerinfo['regularMarketPrice']

    def getTickerSymbol(self):
        return self.tickersymbol

    def getPricePreviousDay(self):
        return self.indexPreviousDay
    
    def getPriceNow(self):
        return self.indexNow    

#Test
if __name__ == "__main__":
    stock = SingleStockData('NDA-FI.HE')
    stock.stockSearchDay()
    print(stock.getPricePreviousDay())
    print(stock.getPriceNow())  