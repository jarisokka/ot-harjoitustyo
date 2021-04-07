import unittest
from services.singlestockdata import SingleStockData
from datetime import datetime

class TestStockData(unittest.TestCase):
    def setUp(self):
        self.stock = SingleStockData('NDA-FI.HE')

    def test_ticker_is_set_correctly(self):
        self.assertEqual(str(self.stock.getTickerSymbol()), 'NDA-FI.HE')

    def test_there_is_price_set_previousday(self):
        self.stock.stockGetOneDayPrices()
        self.assertNotEqual(str(self.stock.getPricePreviousDay()), None)
    
    def test_there_is_price_set_now(self):
        self.stock.stockGetOneDayPrices()
        self.assertNotEqual(str(self.stock.getPriceNow()), None)

    def test_there_is_price_set_start_of_year(self):
        self.stock.stockYTD()
        self.assertNotEqual(str(self.stock.getPriceYTD()), None)
    
    def test_there_is_price_set_year(self):
        self.stock.stockYear()
        self.assertNotEqual(str(self.stock.getPriceYear()), None)
    
    def test_stockGetOneDayPrices_error_works(self):
        self.false = SingleStockData('xx')
        self.assertEqual(str(self.false.stockGetOneDayPrices()), 'False')
    
    def test_stockYTD_error_works(self):
        self.false = SingleStockData('xx')
        self.assertEqual(str(self.false.stockYTD()), 'False')
    
    def test_stockYear_error_works(self):
        self.false = SingleStockData('xx')
        self.assertEqual(str(self.false.stockYear()), 'False')

    def test_count_money_works(self):
        self.now = 10
        self.old = 5
        self.assertEqual(str(self.stock.getCountChangeMoney(self.now, self.old)), '5.00')
    
    def test_count_procent_works(self):
        self.now = 10
        self.old = 5
        self.assertEqual(str(self.stock.getCountChangeProcent(self.now, self.old)), '100.00')
    
    def test_get_day_works(self):
        self.day = datetime.today().strftime("%d.%m.%Y")
        self.assertEqual(self.stock.getDay(), self.day)
    
    def test_get_time_works(self):
        self.time = datetime.today().strftime("%H:%H:%S")
        self.assertEqual(self.stock.getTime(), self.time)