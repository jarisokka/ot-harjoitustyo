import os
from collections import OrderedDict

dirname = os.path.dirname(__file__)

class readStockListFromFile:

    def __init__(self, file_path):
        self._file_path = os.path.join(dirname, "..", "data", "OMX25H.csv")
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
        #return self.stocks

#Test
if __name__ == "__main__":
    stock = readStockListFromFile('OMX25H.csv')
    stock.read_file()
