import yfinance as yf

class MarketData:

    def __init__(self, stocks: list):
        self.stocks = stocks
        self.result = {}
        self.tickerdata = None
        self.tickerinfo = None

    def stockListStartClose(self, stocks):
        for stock in self.stocks:
            self.tickerdata = yf.Ticker(stock) 
            self.tickerinfo = self.tickerdata.info
            self.result[stock] = []
            prev = self.tickerinfo['regularMarketPreviousClose']
            now = self.tickerinfo['regularMarketPrice']
            changeM = "{:.2f}".format(now - prev)
            changeP = "{:.2f}".format(((now - prev)/prev)*100)
            self.result[stock].append(self.tickerdata.info['shortName'])
            self.result[stock].append(prev)
            self.result[stock].append(now)
            self.result[stock].append(str(changeM) + '€')
            self.result[stock].append(str(changeP) + '%')


    def getList(self):
        return self.stocks
    
    def printAll(self):
        return print(self.result)
    
    def getNameWithTicker(self, ticker: str):
        return print(self.result[ticker][0])

    def getClosePriceWithTicker(self, ticker: str):
        return print(self.result[ticker][1])

    def getNowPriceWithTicker(self, ticker: str):
        return print(self.result[ticker][2])

    def getMoneyChangeWithTicker(self, ticker: str):
        return print(self.result[ticker][3])

    def getProcentChangeWithTicker(self, ticker: str):
        return print(self.result[ticker][4])


if __name__ == "__main__":
    stocks = ['TIETO.HE', 'NDA-FI.HE', 'TELIA1.HE']

    market = MarketData(stocks)
    market.stockListStartClose(market.getList())
    market.printAll()
    market.getNameWithTicker('TELIA1.HE')
    market.getClosePriceWithTicker('TELIA1.HE')
    market.getNowPriceWithTicker('TELIA1.HE')
    market.getMoneyChangeWithTicker('TELIA1.HE')
    market.getProcentChangeWithTicker('TELIA1.HE')


