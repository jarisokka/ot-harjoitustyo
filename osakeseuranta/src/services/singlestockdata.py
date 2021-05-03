from datetime import datetime, timedelta
import yfinance as yf

class SingleStockData:
    """Yksittäisen osakkeen sovelluslogiikasta vastaava luokka.

    Attributes:
        tickersymbol: Merkkijono, joka kertoo ticker-tunnuksen.
        price_previous_day: Float arvo, joka kertoo edellisenpäivän kurssin.
        price_now: Float arvo, joka kertoo tämän päivän kurssin.
        price_ytd: Float arvo, joka kertoo kurssin vuoden alussa.
        price_year: Float arvo, joka kertoo vuoden takaisen kurssin.
        today: Merkkijono, joka kertoo pävämäärä muodossa dd:mm:yy
        time: Merkkijono, joka kertoo kellonajan muodossa hh:mm:ss
    """

    def __init__(self, tickersymbol: str):
        """Luokan konstruktori. Luo uuden yksittäisen osake olion.

        Args:
            tickersymbol: Merkkijono, joka kertoo ticker-tunnuksen.
        """
        self.tickersymbol = tickersymbol
        self.price_previous_day = None
        self.price_now = None
        self.price_ytd = None
        self.price_year = None
        self.today = datetime.today().strftime("%d.%m.%Y")
        self.time = datetime.today().strftime("%H:%M:%S")

    def stock_create_all(self):
        """Haetaan osakkeelle kaikki arvot.
        """
        self.stock_get_one_day_prices()
        self.stock_ytd()
        self.stock_year()

    def stock_get_one_day_prices(self):
        """Haetaan osakkeelle price_now sekä price_previous_day arvot.

        Returns:
            False jos tietoja ei pystytty hakemaan.
        """
        try:
            data = yf.download(self.tickersymbol, period='2d')
            self.price_previous_day = "{:.2f}".format(data['Adj Close'][0])
            self.price_previous_day = float(self.price_previous_day)
            self.price_now = "{:.2f}".format(data['Close'][1])
            self.price_now = float(self.price_now)
        except:
            print('Couldn´t download the wanted one day data')
            return False

    def stock_ytd(self):
        """Haetaan osakkeelle price_ytd arvo.

        Returns:
            False jos tietoja ei pystytty hakemaan.
        """
        try:
            data = yf.download(self.tickersymbol, start='2021-1-4', end='2021-1-5')
            self.price_ytd = "{:.2f}".format(data['Close'][0])
            self.price_ytd = float(self.price_ytd)
        except:
            print('Couldn´t download the wanted YTD data')
            return False

    def stock_year(self):
        """Haetaan osakkeelle price_year arvo.

        Returns:
            False jos tietoja ei pystytty hakemaan.
        """
        try:
            data = yf.download(self.tickersymbol, period='1y')
            self.price_year = "{:.2f}".format(data['Close'][0])
            self.price_year = float(self.price_year)
        except:
            print('Couldn´t download the wanted year data')
            return False

    def get_ticker_symbol(self):
        """Palauttaa ticker-tunnuksen.

        Returns:
            Merkkijono, joka kertoo ticker-tunnuksen.
        """
        return self.tickersymbol

    def get_price_previous_day(self):
        """Palauttaa edellisen päivän kurssin.

        Returns:
            Float, joka kertoo edellisen päivän kurssin.
        """
        return self.price_previous_day

    def get_price_now(self):
        """Palauttaa tämän hetken kurssin.

        Returns:
            Float, joka kertoo edellisen päivän kurssin.
        """
        return self.price_now

    def get_price_ytd(self):
        """Palauttaa vuoden alun kurssin.

        Returns:
            Float, joka kertoo kurssin vuoden alussa.
        """
        return self.price_ytd

    def get_price_year(self):
        """Palauttaa vuoden takaisen kurssin.

        Returns:
            Float, joka kertoo kurssin vuosi sitten.
        """
        return self.price_year

    def get_count_change_money(self, now: float, old: float):
        """Laskee ja palauttaa kahden annetun arvon erotuksen.

        Args:
            now: Float arvona annettu nykyinen kurssi.
            old: Float arvona annettu aikaisempi kurssi.

        Returns:
            Float, joka kertoo kahden arvon erotuksen.
        """
        result = "{:.2f}".format(now - old)
        return result

    def get_count_change_procent(self, now: float, old: float):
        """Laskee ja palauttaa kahden annetun arvon erotuksen prosentteina.

        Args:
            now: Float arvona annettu nykyinen kurssi.
            old: Float arvona annettu aikaisempi kurssi.

        Returns:
            Float, joka kertoo kahden arvon erotuksen prosentteina.
        """
        result = "{:.2f}".format(((now - old)/old)*100)
        return result

    def get_day(self):
        """Palauttaa nykyisen päivämäärän.

        Returns:
            Merkkijono, joka kertoo päivämäärän muodossa dd:mm:yy.
        """
        return self.today

    def get_time(self):
        """Palauttaa tämän hetken kellonajan.

        Returns:
            Merkkijono, joka kertoo kellonajan muodossa hh:mm:ss.
        """
        return self.time
