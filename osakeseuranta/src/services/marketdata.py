import yfinance as yf
from services.singlestockdata import SingleStockData


class MarketData:

    def __init__(self, stocks: list):
        self.newstock = None
        self.stocks = stocks
        self.result = {}
        self.tickerdata = None

    def stockListStartClose(self):
        for stock in self.stocks:
            self.newstock = SingleStockData(stock)
            self.newstock.stockGetOneDayPrices()

            self.result[stock] = []
            name = self.stocks[stock]
            prev = self.newstock.getPricePreviousDay()
            now = self.newstock.getPriceNow()
            changeM = self.newstock.getCountChangeMoney(now, prev)
            changeP = float(self.newstock.getCountChangeProcent(now, prev))
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



