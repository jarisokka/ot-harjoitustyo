import os
from collections import OrderedDict

dirname = os.path.dirname(__file__)

class ReadStockListFromFile:

    def __init__(self, file):
        self.file = file
        self._file_path = os.path.join(dirname, "..", "data", self.file)
        self.stocks = {}

    def read_file(self):
        with open(self._file_path) as file:
            for stock in file:
                stock = stock.replace('\n', '')
                stock = stock.split(';')
                symbol = stock[0]
                name = stock[1]
                self.stocks[symbol] = name
        return OrderedDict(sorted(self.stocks.items()))


#Test
if __name__ == "__main__":
    stocktest = ReadStockListFromFile('OMX25H.csv')
    stocktest.read_file()
    