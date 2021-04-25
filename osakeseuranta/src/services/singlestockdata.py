from datetime import datetime, timedelta
import yfinance as yf

class SingleStockData:

    def __init__(self, tickersymbol: str):
        self.tickersymbol = tickersymbol
        self.price_previous_day = None
        self.price_now = None
        self.price_ytd = None
        self.price_year = None
        self.today = datetime.today().strftime("%d.%m.%Y")
        self.time = datetime.today().strftime("%H:%H:%S")

    def stock_create_all(self):
        self.stock_get_one_day_prices()
        self.stock_ytd()
        self.stock_year()

    def stock_get_one_day_prices(self):
        try:
            data = yf.download(self.tickersymbol, period='2d')
            self.price_previous_day = "{:.2f}".format(data['Adj Close'][0])
            self.price_previous_day = float(self.price_previous_day)
            self.price_now = "{:.2f}".format(data['Close'][1])
            self.price_now = float(self.price_now)
        except:
            print('Couldn´t download the wanted one day data')
            return False

    def stock_ytd(self):
        try:
            data = yf.download(self.tickersymbol, start='2021-1-4', end='2021-1-5')
            self.price_ytd = "{:.2f}".format(data['Close'][0])
            self.price_ytd = float(self.price_ytd)
        except:
            print('Couldn´t download the wanted YTD data')
            return False

    def stock_year(self):
        try:
            #start = (datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d")
            #end = (datetime.today() - timedelta(days=364)).strftime("%Y-%m-%d")
            data = yf.download(self.tickersymbol, period='1y')
            self.price_year = "{:.2f}".format(data['Close'][0])
            self.price_year = float(self.price_year)
        except:
            print('Couldn´t download the wanted year data')
            return False

    def get_ticker_symbol(self):
        return self.tickersymbol

    def get_price_previous_day(self):
        return self.price_previous_day

    def get_price_now(self):
        return self.price_now

    def get_price_ytd(self):
        return self.price_ytd

    def get_price_year(self):
        return self.price_year

    def get_count_change_money(self, now: float, old: float):
        result = "{:.2f}".format(now - old)
        return result

    def get_count_change_procent(self, now: float, old: float):
        result = "{:.2f}".format(((now - old)/old)*100)
        return result

    def get_day(self):
        return self.today

    def get_time(self):
        return self.time

#Test
if __name__ == "__main__":
    stocktest = SingleStockData('^OMXH25')
    #stock = SingleStockData('xx')
    #stock.stock_create_all()
    stocktest.stock_get_one_day_prices()
