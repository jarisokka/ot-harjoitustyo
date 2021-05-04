import unittest
from datetime import datetime
from services.singlestockdata import SingleStockData


class TestStockData(unittest.TestCase):
    def setUp(self):
        self.stock = SingleStockData('NDA-FI.HE')

    def test_ticker_is_set_correctly(self):
        self.assertEqual(str(self.stock.get_ticker_symbol()), 'NDA-FI.HE')

    def test_there_is_price_set_previousday(self):
        self.stock.stock_get_one_day_prices()
        self.assertNotEqual(str(self.stock.get_price_previous_day()), None)
    
    def test_there_is_price_set_now(self):
        self.stock.stock_get_one_day_prices()
        self.assertNotEqual(str(self.stock.get_price_now()), None)

    def test_there_is_price_set_start_of_year(self):
        self.stock.stock_ytd()
        self.assertNotEqual(str(self.stock.get_price_ytd()), None)
    
    def test_there_is_price_set_year(self):
        self.stock.stock_year()
        self.assertNotEqual(str(self.stock.get_price_year()), None)
    
    def test_stockGetOneDayPrices_error_works(self):
        self.false = SingleStockData('xx')
        self.assertEqual(str(self.false.stock_get_one_day_prices()), 'False')
    
    def test_stockYTD_error_works(self):
        self.false = SingleStockData('xx')
        self.assertEqual(str(self.false.stock_ytd()), 'False')
    
    def test_stockYear_error_works(self):
        self.false = SingleStockData('xx')
        self.assertEqual(str(self.false.stock_year()), 'False')

    def test_count_money_works(self):
        self.now = 10
        self.old = 5
        self.assertEqual(str(self.stock.get_count_change_money(self.now, self.old)), '5.00')
    
    def test_count_procent_works(self):
        self.now = 10
        self.old = 5
        self.assertEqual(str(self.stock.get_count_change_procent(self.now, self.old)), '100.00')
    
    def test_get_day_works(self):
        self.day = datetime.today().strftime("%d.%m.%Y")
        self.assertEqual(self.stock.get_day(), self.day)
    
    def test_get_time_works(self):
        self.time = datetime.today().strftime("%H:%M:%S")
        self.assertEqual(self.stock.get_time(), self.time)