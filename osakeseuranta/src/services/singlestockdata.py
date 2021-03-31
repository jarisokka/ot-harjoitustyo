import yfinance as yf
from datetime import datetime, timedelta

class SingleStockData:

    def __init__(self, tickersymbol: str):
        self.tickersymbol = tickersymbol
        self.pricePreviousDay = None
        self.priceNow = None
        self.priceYTD = None
        self.priceYear = None

    def stockCreateAll(self):
        self.stockGetOneDayPrices()
        self.stockYTD()
        self.stockYear()

    def stockGetOneDayPrices(self):
        data = yf.download(self.tickersymbol, period='2d')
        self.pricePreviousDay = "{:.2f}".format(data['Adj Close'][0])
        self.pricePreviousDay = float(self.pricePreviousDay)        
        self.priceNow = "{:.2f}".format(data['Close'][1])
        self.priceNow = float(self.priceNow)

    def stockYTD(self):
        data = yf.download(self.tickersymbol, start='2021-1-4', end='2021-1-5')
        self.priceYTD = "{:.2f}".format(data['Close'][0])
        self.priceYTD = float(self.priceYTD)

    def stockYear(self):
        start = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")
        end = (datetime.today() - timedelta(days=364)).strftime("%Y-%m-%d")
        data = yf.download(self.tickersymbol, start=start, end=end)
        self.priceYear = "{:.2f}".format(data['Close'][0]) 
        self.priceYear = float(self.priceYear)

    def getTickerSymbol(self):
        return self.tickersymbol

    def getPricePreviousDay(self):
        return self.pricePreviousDay
    
    def getPriceNow(self):
        return self.priceNow

    def getPriceYTD(self):
        return self.priceYTD
    
    def getPriceYear(self):
        return self.priceYear

    def getCountChangeMoney(self, now: float, old: float):
        result = "{:.2f}".format(now - old)
        return result

    def getCountChangeProcent(self, now: float, old: float):
        result = "{:.2f}".format(((now - old)/old)*100)
        return result      


#Test
if __name__ == "__main__":
    stock = SingleStockData('NDA-FI.HE')
    stock.stockCreateAll()
    print(stock.getPricePreviousDay())
    print(stock.getPriceNow()) 
    print(stock.getPriceYTD())
    print(stock.getPriceYear())
    print(stock.getCountChangeMoney(stock.getPricePreviousDay(), stock.getPriceNow()))
    print(stock.getCountChangeProcent(stock.getPricePreviousDay(), stock.getPriceNow()))