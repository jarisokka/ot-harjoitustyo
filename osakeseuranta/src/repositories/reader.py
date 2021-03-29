import os

dirname = os.path.dirname(__file__)

class readStockListFromFile:

    def __init__(self, file_path):
        self._file_path = os.path.join(dirname, "..", "data", "OMX25H.csv")
        self.stocks = []

    def read_file(self):    
        with open(self._file_path) as file:
            for stock in file:
                stock = stock.split("\n")
                self.stocks.append(stock[0])

        return self.stocks

#Test
if __name__ == "__main__":
    stock = readStockListFromFile('OMX25H.csv')
    stock.read_file()