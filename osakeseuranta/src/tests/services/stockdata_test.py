import unittest
from services.singlestockdata import SingleStockData

class TestStockData(unittest.TestCase):
    def setUp(self):
        self.stock = SingleStockData('NDA-FI.HE')

    def test_ticker_is_set_correctly(self):
        print(self.stock.getTickerSymbol())
        self.assertEqual(str(self.stock.getTickerSymbol()), 'NDA-FI.HE')

    def test_there_is_price_set_previousday(self):
        self.stock.stockGetOneDayPrices()
        self.assertNotEqual(str(self.stock.getPricePreviousDay()), 'xx')
    
    def test_there_is_price_set_now(self):
        self.stock.stockGetOneDayPrices()
        self.assertNotEqual(str(self.stock.getPriceNow()), None)