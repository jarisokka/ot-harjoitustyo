from services.singlestockdata import SingleStockData
from repositories.reader import ReadStockListFromFile

class MarketData:
    """Osakelistauksen sovelluslogiikasta vastaava luokka.

    Attributes:
        file: tiedosto joka perusteella listaus muodostetaan.
        newstock: SingleStockData olio.
        stocks: sanakirja joka on luotu luetusta tiedostosta,
            siltää ticker-tunnuksen ja osakkeen nimen.
        result: sanakirja joka sisältää listan osakkeista.
    """

    def __init__(self):
        """Luokan konstruktori, joka luo uuden osakelistauksen.
        """
        self.file = None
        self.newstock = None
        self.stocks = None
        self.result = {}

    def initialize_read(self, file):
        """Palauttaa ReadStockListFromFile-luokkaa käyttäen listan
            osakkeista ja niiden ticker-tunnukset.

        Args:
            file: Merkkijonoarvo joka kuvaa tiedoston nimeä.

        Returns:
            Palauttaa sanakirjan aakkosjärjestyksessä.
        """
        self.file = file
        self.stocks = ReadStockListFromFile(file)
        self.stocks = self.stocks.read_file()
        return self.stocks

    def stock_create_stock_list(self):
        """Haetaan kaikille stock listauksen osakkeille arvot.
        """
        for stock in self.stocks:
            self.newstock = SingleStockData(stock)
            self.newstock.stock_create_all()
            self.result[stock] = []
            name = self.stocks[stock]

            #Prices today
            try:
                prev = self.newstock.get_price_previous_day()
                now = self.newstock.get_price_now()
                changedayprice = self.newstock.get_count_change_money(now, prev)
                changedayprocent = float(self.newstock.get_count_change_procent(now, prev))
                changedayprocent = self._format_line(changedayprocent)
                self.result[stock].append(name)
                self.result[stock].append(prev)
                self.result[stock].append(now)
                self.result[stock].append(str(changedayprice) + ' €')
                self.result[stock].append(str(changedayprocent) + ' %')
            except:
                return False


            #Prices ytd (beginning of the year)
            try:
                prevytd = self.newstock.get_price_ytd()
                changeytdprice = self.newstock.get_count_change_money(now, prevytd)
                changeytdprocent = float(self.newstock.get_count_change_procent(now, prevytd))
                changeytdprocent = self._format_line(changeytdprocent)
                self.result[stock].append(prevytd)
                self.result[stock].append(str(changeytdprice) + ' €')
                self.result[stock].append(str(changeytdprocent) + ' %')
            except:
                return False

            #Prices One year
            try:
                prevyear = self.newstock.get_price_year()
                changeyearprice = self.newstock.get_count_change_money(now, prevyear)
                changeyearprocent = float(self.newstock.get_count_change_procent(now, prevyear))
                changeyearprocent = self._format_line(changeyearprocent)
                self.result[stock].append(prevyear)
                self.result[stock].append(str(changeyearprice) + ' €')
                self.result[stock].append(str(changeyearprocent) + ' %')
            except:
                return False

    def _format_line(self, value):
        """Muokkaa float arvon merkkijonoksi. Lisää + merkin eteen, jos positiivinen.

        Args:
            value: Float arvo

        Returns:
            Merkkijono, palauttaa muokatun arvon.
        """
        if value > 0:
            value = '+' + str(value)
            return value
        else:
            return value

    def get_list(self):
        """Palauttaa tiedostosta luetun sanakirjan.

        Returns:
            Sanakirja aakkojärjestyksessä.
        """
        return self.stocks

    def get_name_with_ticker(self, ticker: str):
        """Palauttaa osakkeen nimen.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo osakkeen nimen.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][0]
        except (KeyError, IndexError):
            return 'NaN'

    def get_close_price_prev_day_with_ticker(self, ticker: str):
        """Palauttaa osakkeen edellisen päivän kurssin.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Float, joka kertoo osakkeen edellisen päivän kurssin.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][1]
        except (KeyError, IndexError):
            return 'NaN'

    def get_now_price_with_ticker(self, ticker: str):
        """Palauttaa osakkeen edellisen päivän kurssin.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Float, joka kertoo osakkeen nykyisen kurssin.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][2]
        except (KeyError, IndexError):
            return 'NaN'

    def get_money_change_day_with_ticker(self, ticker: str):
        """Palauttaa osakkeen osakkeen päiväkohtaisen kehityksen euroissa.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo osakkeen päiväkohtaisen kehityksen euroissa.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][3]
        except (KeyError, IndexError):
            return 'NaN'

    def get_procent_change_day_with_ticker(self, ticker: str):
        """Palauttaa osakkeen osakkeen päiväkohtaisen kehityksen prosentteina.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo osakkeen päiväkohtaisen kehityksen prosentteina.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][4]
        except (KeyError, IndexError):
            return 'NaN'

    def get_close_price_ytd_with_ticker(self, ticker: str):
        """Palauttaa osakkeen kurssin vuoden alussa.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Float, joka kertoo osakkeen kurssin vuoden alussa.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][5]
        except (KeyError, IndexError):
            return 'NaN'

    def get_money_change_ytd_with_ticker(self, ticker: str):
        """Palauttaa osakkeen osakkeen kehityksen vuoden alusta euroissa.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo osakkeen kehityksen vuoden alusta euroissa.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][6]
        except (KeyError, IndexError):
            return 'NaN'

    def get_procent_change_ytd_with_ticker(self, ticker: str):
        """Palauttaa osakkeen osakkeen kehityksen vuoden alusta prosentteina.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo osakkeen kehityksen vuoden alusta prosentteina.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][7]
        except (KeyError, IndexError):
            return 'NaN'

    def get_close_price_year_with_ticker(self, ticker: str):
        """Palauttaa osakkeen kurssin vuosi sitten.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Float, joka kertoo osakkeen kurssin vuosi sitten.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][8]
        except (KeyError, IndexError):
            return 'NaN'

    def get_money_change_year_ticker(self, ticker: str):
        """Palauttaa osakkeen osakkeen kehityksen vuoden takaiseen tilanteeseen euroissa.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo osakkeen kehityksen vuoden takaiseen tilanteeseen euroissa.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][9]
        except (KeyError, IndexError):
            return 'NaN'

    def get_procent_change_year_ticker(self, ticker: str):
        """Palauttaa osakkeen osakkeen kehityksen vuoden takaiseen tilanteeseen prosentteina.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo osakkeen kehityksen vuoden takaiseen tilanteeseen prosentteina.

        Except:
            KeyError, IndexError: Virhe, jolloin tietoa ei löytynyt ja palautetaan NaN.
        """
        try:
            return self.result[ticker][10]
        except (KeyError, IndexError):
            return 'NaN'
