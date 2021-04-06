import yfinance as yf
from datetime import datetime, timedelta

class SingleStockData:

    def __init__(self, tickersymbol: str):
        self.tickersymbol = tickersymbol
        self.pricePreviousDay = None
        self.priceNow = None
        self.priceYTD = None
        self.priceYear = None
        self.today = datetime.today().strftime("%d.%m.%Y")
        self.time = datetime.today().strftime("%H:%H:%S")

    def stockCreateAll(self):
        self.stockGetOneDayPrices()
        self.stockYTD()
        self.stockYear()

    def stockGetOneDayPrices(self):
        try:
            data = yf.download(self.tickersymbol, period='2d')
            self.pricePreviousDay = "{:.2f}".format(data['Adj Close'][0])
            self.pricePreviousDay = float(self.pricePreviousDay)
            self.priceNow = "{:.2f}".format(data['Close'][1])
            self.priceNow = float(self.priceNow)
        except:
            print('Couldn´t download the wanted one day data')
            pass

    def stockYTD(self):
        try:
            data = yf.download(self.tickersymbol, start='2021-1-4', end='2021-1-5')
            self.priceYTD = "{:.2f}".format(data['Close'][0])
            self.priceYTD = float(self.priceYTD)          
        except:
            print('Couldn´t download the wanted YTD data')
            pass

    def stockYear(self):
        try:
            start = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")
            end = (datetime.today() - timedelta(days=364)).strftime("%Y-%m-%d")
            data = yf.download(self.tickersymbol, start=start, end=end)
            self.priceYear = "{:.2f}".format(data['Close'][0]) 
            self.priceYear = float(self.priceYear)
        except:
            print('Couldn´t download the wanted year data')
            pass

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

    def getDay(self):
        return self.today
    
    def getTime(self):
        return self.time

#Test
if __name__ == "__main__":
    stock = SingleStockData('^OMXH25')
    #stock.stockCreateAll()
    stock.stockGetOneDayPrices()
    #stock.stockYTD()
    #stock.stockYear()
    print(stock.getPricePreviousDay())
    print(stock.getPriceNow()) 
    #print(stock.getPriceYTD())
    #print(stock.getPriceYear())
    #print(stock.getCountChangeMoney(stock.getPricePreviousDay(), stock.getPriceNow()))
    #print(stock.getCountChangeProcent(stock.getPricePreviousDay(), stock.getPriceNow()))