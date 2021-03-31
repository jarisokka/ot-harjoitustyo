import yfinance as yf
from services.singlestockdata import SingleStockData


class MarketData:

    def __init__(self, stocks: list):
        self.newstock = None
        self.stocks = stocks
        self.result = {}
        self.tickerdata = None

    def stockCreateStockList(self):
        for stock in self.stocks:
            self.newstock = SingleStockData(stock)
            self.newstock.stockCreateAll()
            self.result[stock] = []
            self._name = self.stocks[stock]

            #Prices today
            self._prev = self.newstock.getPricePreviousDay()
            self._now = self.newstock.getPriceNow()
            self._changedayprice = self.newstock.getCountChangeMoney(self._now, self._prev)
            self._changedayprocent = float(self.newstock.getCountChangeProcent(self._now, self._prev))
            self._changedayprocent = self._formatLine(self._changedayprocent)

            #Prices YTD (beginning of the year)
            self._prevytd = self.newstock.getPriceYTD()
            self._changeytdprice = self.newstock.getCountChangeMoney(self._now, self._prevytd)
            self._changeytdprocent = float(self.newstock.getCountChangeProcent(self._now, self._prevytd))
            self._changeytdprocent = self._formatLine(self._changeytdprocent)
  
            #Prices One year
            self._prevyear = self.newstock.getPriceYear()
            self._changeyearprice = self.newstock.getCountChangeMoney(self._now, self._prevyear)
            self._changeyearprocent = float(self.newstock.getCountChangeProcent(self._now, self._prevyear))
            self._changeyearprocent = self._formatLine(self._changeyearprocent)

            self.result[stock].append(self._name)
            self.result[stock].append(self._prev)
            self.result[stock].append(self._now)
            self.result[stock].append(str(self._changedayprice) + ' €')
            self.result[stock].append(str(self._changedayprocent) + ' %')
            self.result[stock].append(self._prevytd)
            self.result[stock].append(str(self._changeytdprice) + ' €')
            self.result[stock].append(str(self._changeytdprocent) + ' %')
            self.result[stock].append(self._prevyear)
            self.result[stock].append(str(self._changeyearprice) + ' €')
            self.result[stock].append(str(self._changeyearprocent) + ' %')

    def _formatLine(self, value):
        if value > 0:
            value = '+' + str(value)
            return value
        else:
            return value

    def getList(self):
        return self.stocks
    
    def printAll(self):
        return print(self.result)

    def getNameWithTicker(self, ticker: str):
        return self.result[ticker][0]

    def getClosePricePrevDayWithTicker(self, ticker: str):
        return self.result[ticker][1]

    def getNowPriceWithTicker(self, ticker: str):
        return self.result[ticker][2]

    def getMoneyChangeDayWithTicker(self, ticker: str):
        return self.result[ticker][3]

    def getProcentChangeDayWithTicker(self, ticker: str):
        return self.result[ticker][4]

    def getClosePriceYTDWithTicker(self, ticker: str):
        return self.result[ticker][5]

    def getMoneyChangeYTDWithTicker(self, ticker: str):
        return self.result[ticker][6]

    def getProcentChangeYTDWithTicker(self, ticker: str):
        return self.result[ticker][7]

    def getClosePriceYearWithTicker(self, ticker: str):
        return self.result[ticker][8]

    def getMoneyChangeYearTicker(self, ticker: str):
        return self.result[ticker][9]

    def getProcentChangeYearTicker(self, ticker: str):
        return self.result[ticker][10]



#Test
if __name__ == "__main__":
    stocks = {'TIETO.HE':'TietoEVRY Corporation', 'NDA-FI.HE':'Nordea Bank Abp', 'OUT1V.HE':'Outokumpu Oyj'}
    market = MarketData(stocks)
    market.stockCreateStockList()
    market.printAll()
    print(market.getNameWithTicker('NDA-FI.HE'))
    print(market.getClosePricePrevDayWithTicker('NDA-FI.HE'))
    print(market.getNowPriceWithTicker('NDA-FI.HE'))
    print(market.getMoneyChangeDayWithTicker('NDA-FI.HE'))
    print(market.getProcentChangeDayWithTicker('NDA-FI.HE'))
    print(market.getClosePriceYTDWithTicker('NDA-FI.HE'))
    print(market.getMoneyChangeYTDWithTicker('NDA-FI.HE'))
    print(market.getProcentChangeYTDWithTicker('NDA-FI.HE'))
    print(market.getClosePriceYearWithTicker('NDA-FI.HE'))
    print(market.getMoneyChangeYearTicker('NDA-FI.HE'))
    print(market.getProcentChangeYearTicker('NDA-FI.HE'))

