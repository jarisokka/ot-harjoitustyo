import unittest
from repositories.stock_repository import stock_repository


class TestStockRepository(unittest.TestCase):
    def setUp(self):
        stock_repository.delete_all()
        self.user = 'test'
        self.ticker = 'NDA-FI.HE'
        self.name = 'Nordea'
        self.price = 5
        self.date = 'test date'
    
    def test_create(self):
        testdata = stock_repository.create(self.user, self.ticker, self.name, self.price, self.date)
        self.assertEqual(testdata, True)
    
    def test_get_list_by_user(self):
        stock_repository.create(self.user, self.ticker, self.name, self.price, self.date)
        testdata = stock_repository.get_stocks_by_user(self.user)
        self.assertEqual(len(testdata), 1)
        self.assertEqual(testdata[self.ticker][0], self.name)
        self.assertEqual(testdata[self.ticker][1], '5.0')
        self.assertEqual(testdata[self.ticker][2], self.date)
    
    def test_find_by_ticker(self):
        stock_repository.create(self.user, self.ticker, self.name, self.price, self.date)
        testdata = stock_repository.find_by_ticker(self.user, self.ticker)
        self.assertEqual(len(testdata), 5)
    
    def test_update(self):
        stock_repository.create(self.user, self.ticker, self.name, self.price, self.date)
        testdata = stock_repository.update(self.user, self.ticker, self.price, 'new date')
        self.assertEqual(testdata, True)
        datecheck = stock_repository.get_stocks_by_user(self.user)
        self.assertEqual(datecheck[self.ticker][2], 'new date')

    def test_remove(self):
        stock_repository.create(self.user, self.ticker, self.name, self.price, self.date)
        testdata = stock_repository.remove(self.user, self.ticker)
        self.assertEqual(testdata, True)
        checkdata = stock_repository.get_stocks_by_user(self.user)
        self.assertEqual(len(checkdata), 0)