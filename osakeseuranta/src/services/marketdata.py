from services.singlestockdata import SingleStockData
from repositories.reader import ReadStockListFromFile

class MarketData:

    def __init__(self):
        self.file = None
        self.newstock = None
        self.stocks = None
        self.result = {}
        self.tickerdata = None

    def initialize_read(self, file):
        self.file = file
        self.stocks = ReadStockListFromFile(file)
        self.stocks = self.stocks.read_file()
        return self.stocks

    def stock_create_stock_list(self):
        for stock in self.stocks:
            self.newstock = SingleStockData(stock)
            self.newstock.stock_create_all()
            self.result[stock] = []
            name = self.stocks[stock]

            #Prices today
            try:
                prev = self.newstock.get_price_previous_day()
                now = self.newstock.get_price_now()
                changedayprice = self.newstock.get_count_change_money(now, prev)
                changedayprocent = float(self.newstock.get_count_change_procent(now, prev))
                changedayprocent = self._format_line(changedayprocent)
                self.result[stock].append(name)
                self.result[stock].append(prev)
                self.result[stock].append(now)
                self.result[stock].append(str(changedayprice) + ' €')
                self.result[stock].append(str(changedayprocent) + ' %')
            except:
                print('Single stock data day failed')


            #Prices ytd (beginning of the year)
            try:
                prevytd = self.newstock.get_price_ytd()
                changeytdprice = self.newstock.get_count_change_money(now, prevytd)
                changeytdprocent = float(self.newstock.get_count_change_procent(now, prevytd))
                changeytdprocent = self._format_line(changeytdprocent)
                self.result[stock].append(prevytd)
                self.result[stock].append(str(changeytdprice) + ' €')
                self.result[stock].append(str(changeytdprocent) + ' %')
            except:
                print('Single stock data ytd failed')

            #Prices One year
            try:
                prevyear = self.newstock.get_price_year()
                changeyearprice = self.newstock.get_count_change_money(now, prevyear)
                changeyearprocent = float(self.newstock.get_count_change_procent(now, prevyear))
                changeyearprocent = self._format_line(changeyearprocent)
                self.result[stock].append(prevyear)
                self.result[stock].append(str(changeyearprice) + ' €')
                self.result[stock].append(str(changeyearprocent) + ' %')
            except:
                print('Single stock data year failed')

    def _format_line(self, value):
        if value > 0:
            value = '+' + str(value)
            return value
        else:
            return value

    def get_list(self):
        return self.stocks

    def print_all(self):
        return print(self.result)

    def get_name_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][0]
        except IndexError:
            return 'NaN'

    def get_close_price_prev_day_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][1]
        except IndexError:
            return 'NaN'

    def get_now_price_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][2]
        except IndexError:
            return 'NaN'

    def get_money_change_day_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][3]
        except IndexError:
            return 'NaN'

    def get_procent_change_day_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][4]
        except IndexError:
            return 'NaN'

    def get_close_price_ytd_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][5]
        except IndexError:
            return 'NaN'

    def get_money_change_ytd_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][6]
        except IndexError:
            return 'NaN'

    def get_procent_change_ytd_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][7]
        except IndexError:
            return 'NaN'

    def get_close_price_year_with_ticker(self, ticker: str):
        try:
            return self.result[ticker][8]
        except IndexError:
            return 'NaN'

    def get_money_change_year_ticker(self, ticker: str):
        try:
            return self.result[ticker][9]
        except IndexError:
            return 'NaN'

    def get_procent_change_year_ticker(self, ticker: str):
        try:
            return self.result[ticker][10]
        except IndexError:
            return 'NaN'



#Test
if __name__ == "__main__":
    stocktest = {'NDA-FI.HE':'Nordea test', 'CGCBV.HE':'Rikkinainen tiedosto',
     'OUT1V.HE':'Outokumpu Oyj'}
    market = MarketData(stocktest)
    market.stock_create_stock_list()
    market.print_all()
    print(market.get_name_with_ticker('NDA-FI.HE'))
    print(market.get_close_price_prev_day_with_ticker('NDA-FI.HE'))
    print(market.get_now_price_with_ticker('NDA-FI.HE'))
    