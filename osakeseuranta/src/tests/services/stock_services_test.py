import unittest
from repositories.stock_repository import stock_repository
from services.stock_services import stock_services, InvalidValuesError, StockExistsError

class FakeDatabase:
    def __init__(self):
        stock_repository.delete_all()
        self.user = 'test'
        self.ticker = 'NDA-FI.HE'
        self.name = 'Nordea'
        self.price = 10
        self.date = 'test date'
        stock_repository.create(self.user, self.ticker, self.name, self.price, self.date)


class TestStockServices(unittest.TestCase):
    def setUp(self):
        self.user = 'test'
        FakeDatabase()

    def test_inialize_data(self):
        testdata = stock_services.initialize_data(self.user)
        self.assertEqual(len(testdata), 1)

    def test_get_stock_data(self):
        testdata = stock_services.initialize_data(self.user)
        testdata = stock_services.get_stock_data(testdata)
        self.assertEqual(testdata['NDA-FI.HE'][0], 'Nordea')
        self.assertEqual(testdata['NDA-FI.HE'][1], '10.0')
        self.assertEqual(testdata['NDA-FI.HE'][2], 'test date')

    def test_create_new(self):
        self.assertEqual(
            stock_services.create_new(self.user, 'ADD NEW', 'Test', 5, 'double trouble'),
             None)

    def test_create_new_error(self):
        self.assertRaises(
            StockExistsError,
            lambda: stock_services.create_new(self.user, 'NDA-FI.HE', 'Nordea', 10, 'second time')
            )

    def test_check_ticker(self):
        self.assertRaises(
            InvalidValuesError,
            lambda: stock_services.check_values(None, 'Nordea', 10, 'new time')
            )
    
    def test_check_name(self):
        self.assertRaises(
            InvalidValuesError,
            lambda: stock_services.check_values('NDA-FI.HE', None, 10, 'new time')
            )
    
    def test_check_price_empty(self):
        self.assertRaises(
            InvalidValuesError,
            lambda: stock_services.check_values('NDA-FI.HE', 'Nordea', '', 'new time')
            )

    def test_check_date_empty(self):
        self.assertRaises(
            InvalidValuesError,
            lambda: stock_services.check_values('NDA-FI.HE', 'Nordea', 10, '')
            )
    
    def test_check_price_format(self):
        self.assertRaises(
            InvalidValuesError,
            lambda: stock_services.check_values('NDA-FI.HE', 'Nordea', '11,5', 'new time')
            )