import unittest
from datetime import datetime
from services.singlestockdata import SingleStockData
from services.marketdata import MarketData

class TestStockData(unittest.TestCase):
    def setUp(self):
        self.market = MarketData()
        self.market.initialize_read('OMX25H_test.csv')
        self.market.stock_create_stock_list()

    def test_filename_correct(self):
        self.assertEqual(str(self.market.file), 'OMX25H_test.csv')

    def test_invoke_single_stock_correct(self):
        self.assertEqual(str(self.market.newstock.tickersymbol), 'VALMT.HE')
    
    def test_stock_size_correct(self):
        self.assertEqual(len(self.market.stocks), 3)

    def test_result_list_created(self):
        self.assertEqual(len(self.market.result), 3)
    
    def test_get_list(self):
        self.assertNotEqual(str(self.market.get_list()), None)
    
    def test_format_correct_when_positive(self):
        value = 1
        self.assertEqual(str(self.market._format_line(value)), '+1')

    def test_format_correct_when_negative(self):
        value = -1
        self.assertEqual(str(self.market._format_line(value)), '-1')

    def test_get_name_ticker(self):
        self.market.result['VALMT.HE'][0] = 'test'
        self.assertEqual(str(self.market.get_name_with_ticker('VALMT.HE')), 'test')
    
    def test_get_close_price_prev_day(self):
        self.market.result['VALMT.HE'][1] = 1
        self.assertEqual(self.market.get_close_price_prev_day_with_ticker('VALMT.HE'), 1)

    def test_get_now_price_prev_day(self):
        self.market.result['VALMT.HE'][2] = 2
        self.assertEqual(self.market.get_now_price_with_ticker('VALMT.HE'), 2)
    
    def test_get_money_change_day(self):
        self.market.result['VALMT.HE'][3] = 3
        self.assertEqual(self.market.get_money_change_day_with_ticker('VALMT.HE'), 3)

    def test_get_procent_change_day(self):
        self.market.result['VALMT.HE'][4] = 4
        self.assertEqual(self.market.get_procent_change_day_with_ticker('VALMT.HE'), 4)
    
    def test_get_close_price_ytd(self):
        self.market.result['VALMT.HE'][5] = 5
        self.assertEqual(self.market.get_close_price_ytd_with_ticker('VALMT.HE'), 5)
    
    def test_get_money_change_ytd(self):
        self.market.result['VALMT.HE'][6] = 6
        self.assertEqual(self.market.get_money_change_ytd_with_ticker('VALMT.HE'),6)
    
    def test_get_procent_change_ytd(self):
        self.market.result['VALMT.HE'][7] = 7
        self.assertEqual(self.market.get_procent_change_ytd_with_ticker('VALMT.HE'),7)

    def test_get_close_price_year(self):
        self.market.result['VALMT.HE'][8] = 8
        self.assertEqual(self.market.get_close_price_year_with_ticker('VALMT.HE'),8)
    
    def test_get_money_change_year(self):
        self.market.result['VALMT.HE'][9] = 9
        self.assertEqual(self.market.get_money_change_year_ticker('VALMT.HE'),9)
    
    def test_get_procent_change_year(self):
        self.market.result['VALMT.HE'][10] = 10
        self.assertEqual(self.market.get_procent_change_year_ticker('VALMT.HE'),10)
    
    def test_error_get_name(self):
        self.assertEqual(self.market.get_name_with_ticker('TEST'), 'NaN')
    
    def test_error_close_price_day(self):
        self.assertEqual(self.market.get_close_price_prev_day_with_ticker('TEST'), 'NaN')

    def test_error_now_price_day(self):
        self.assertEqual(self.market.get_now_price_with_ticker('TEST'), 'NaN')

    def test_error_change_money_day(self):
        self.assertEqual(self.market.get_money_change_day_with_ticker('TEST'), 'NaN')
    
    def test_error_change_procent_day(self):
        self.assertEqual(self.market.get_procent_change_day_with_ticker('TEST'), 'NaN')

    def test_error_close_price_ytd(self):
        self.assertEqual(self.market.get_close_price_ytd_with_ticker('TEST'), 'NaN')
    
    def test_error_change_money_ytd(self):
        self.assertEqual(self.market.get_money_change_ytd_with_ticker('TEST'), 'NaN')
    
    def test_error_change_procent_ytd(self):
        self.assertEqual(self.market.get_procent_change_ytd_with_ticker('TEST'), 'NaN')
    
    def test_error_close_price_year(self):
        self.assertEqual(self.market.get_close_price_year_with_ticker('TEST'), 'NaN')
    
    def test_error_change_money_year(self):
        self.assertEqual(self.market.get_money_change_year_ticker('TEST'), 'NaN')
    
    def test_error_change_procent_year(self):
        self.assertEqual(self.market.get_procent_change_year_ticker('TEST'), 'NaN')
    