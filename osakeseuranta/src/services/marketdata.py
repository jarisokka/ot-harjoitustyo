import yfinance as yf

class MarketData:

    def __init__(self, stocks: list):
        self.stocks = stocks
        self.result = {}
        self.tickerdata = None

    def stockListStartClose(self):
        for stock in self.stocks:
            symbol = stock
            name = self.stocks[stock]
            self.result[stock] = []
            data = yf.download(symbol, period='2d')
            prev = "{:.2f}".format(data['Adj Close'][0])
            prev = float(prev)          
            now = "{:.2f}".format(data['Close'][1])
            now = float(now)
            changeM = "{:.2f}".format(now - prev)
            changeP = float("{:.2f}".format(((now - prev)/prev)*100))
            if changeP > 0:
                changeP = '+' + str(changeP)
            self.result[stock].append(name)
            self.result[stock].append(prev)
            self.result[stock].append(now)
            self.result[stock].append(str(changeM) + ' €')
            self.result[stock].append(str(changeP) + ' %')

    def getList(self):
        return self.stocks
    
    def printAll(self):
        return print(self.result)
    
    def getNameWithTicker(self, ticker: str):
        return self.result[ticker][0]

    def getClosePriceWithTicker(self, ticker: str):
        return self.result[ticker][1]

    def getNowPriceWithTicker(self, ticker: str):
        return self.result[ticker][2]

    def getMoneyChangeWithTicker(self, ticker: str):
        return self.result[ticker][3]

    def getProcentChangeWithTicker(self, ticker: str):
        return self.result[ticker][4]

#Test
if __name__ == "__main__":
    stocks = {'TIETO.HE':'TietoEVRY Corporation', 'NDA-FI.HE':'Nordea Bank Abp'}
    market = MarketData(stocks)
    market.stockListStartClose()
    market.printAll()
    print(market.getNameWithTicker('NDA-FI.HE'))
    print(market.getClosePriceWithTicker('NDA-FI.HE'))
    print(market.getNowPriceWithTicker('NDA-FI.HE'))
    print(market.getMoneyChangeWithTicker('NDA-FI.HE'))
    print(market.getProcentChangeWithTicker('NDA-FI.HE'))


