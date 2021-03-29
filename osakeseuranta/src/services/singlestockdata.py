import yfinance as yf

class SingleStockData:

    def __init__(self, tickersymbol: str):
        self.tickersymbol = tickersymbol
        self.indexPreviousDay = None
        self.indexNow = None

    def stockGetOneDayPrices(self):
        data = yf.download(self.tickersymbol, period='2d')
        self.indexPreviousDay = "{:.2f}".format(data['Adj Close'][0])
        self.indexPreviousDay = float(self.indexPreviousDay)          
        self.indexNow = "{:.2f}".format(data['Close'][1])
        self.indexNow = float(self.indexNow)


    def getTickerSymbol(self):
        return self.tickersymbol

    def getPricePreviousDay(self):
        return self.indexPreviousDay
    
    def getPriceNow(self):
        return self.indexNow 

    def getChangeMoney(self):
        result = "{:.2f}".format(self.indexPreviousDay - self.indexNow)
        return result  

    def getChangeProcent(self):
        result = "{:.2f}".format(((self.indexPreviousDay - self.indexNow)/self.indexPreviousDay)*100)
        return result  

#Test
if __name__ == "__main__":
    stock = SingleStockData('NDA-FI.HE')
    stock.stockGetOneDayPrices()
    print(stock.getPricePreviousDay())
    print(stock.getPriceNow()) 
    print(stock.getChangeMoney())
    print(stock.getChangeProcent())