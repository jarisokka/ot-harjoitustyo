import os
from collections import OrderedDict

dirname = os.path.dirname(__file__)

class ReadStockListFromFile:
    """Luokka, jonka avulla luetaan csv-tiedostoja data kansiosta.

    Attributes:
        file: tiedoston nimi.
        file_path: tiedoston sijainti
        stocks: sanakirja, johon tiedot kerätään
    """

    def __init__(self, file):
        """Luokan konstruktori, joka määrittelee tiedoston lukemista varten
            tarvittavat muuttujat.

        Args:
            file: Merkkijonoarvo joka kuvaa tiedoston nimeä.
        """
        self.file = file
        self._file_path = os.path.join(dirname, "..", "data", self.file)
        self.stocks = {}

    def read_file(self):
        """Lataa tiedoston ja lukee tiedostosta tiedot sekä lisää nämä sanakirjaan.

        Returns:
            Palauttaa sanakirjan aakkosjärjestyksessä.
        """
        with open(self._file_path) as file:
            for stock in file:
                stock = stock.replace('\n', '')
                stock = stock.split(';')
                symbol = stock[0]
                name = stock[1]
                self.stocks[symbol] = name
        return OrderedDict(sorted(self.stocks.items()))
 