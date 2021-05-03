from repositories.reader import ReadStockListFromFile
from services.singlestockdata import SingleStockData
from repositories.stock_repository import (
    stock_repository as default_stock_repository
)

class InvalidValuesError(Exception):
    pass

class StockExistsError(Exception):
    pass

class GeneralError(Exception):
    pass

class StockServices:
    """Kirjautuneen käyttäjän osaketietojen sovelluslogiikasta
        vastaava luokka.
    """

    def __init__(self, stock_repository=default_stock_repository):
        """Luokan konstruktori, joka luo uuden osaketietojen tietokannan
            sovelluslogiikasta vastaavan palvelun.

        Args:
            stock_repository:
                Vapaaehtoinen, oletusarvoltaan StockRepository-olio.
                Olio, jolla on StockRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._stock_repository = stock_repository

    def initialize_data(self, user):
        """Palauttaa kirjautuneen käyttäjän stocks tietokannassa olevat tiedot.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.

        Returns:
            Palauttaa sanakirjan johon kerätty löydetyt tiedot.
        """
        return self._stock_repository.get_stocks_by_user(user)

    def get_stock_data(self, datalist):
        """Täydentää ja palauttaa datalist sanakirjan tiedot luomalla jokaisesta
            avaimesta (ticker-tunnus) SingleStockData-olion.

        Args:
            datalist: sanakirja, jossa avaimena ticker-tunnus.

        Returns:
            Palauttaa päivitetyn sanakirjan, johon tiedot haettu yfinance palvelusta.
            Lisätyt tiedot: päivän kurssi, erotus ostohintaan,
            prosenttuaalinen erotus ostohintaan.
        """
        for data in datalist:
            newstock = SingleStockData(data)
            newstock.stock_get_one_day_prices()
            now = newstock.get_price_now()
            if now is None:
                now = 0
            datalist[data].append(str(now))
            count = newstock.get_count_change_money(now, float(datalist[data][1]))
            datalist[data].append(str(count) + ' €')
            procent = newstock.get_count_change_procent(now, float(datalist[data][1]))
            datalist[data].append(str(procent) + ' %')
        return datalist

    def read_list(self, file):
        """Palauttaa ReadStockListFromFile-luokkaa käyttäen listan
            osakkeista ja niiden ticker-tunnukset.

        Args:
            file: Merkkijonoarvo joka kuvaa tiedoston nimeä.

        Returns:
            Palauttaa sanakirjan aakkosjärjestyksessä.
        """
        items = ReadStockListFromFile(file)
        items = items.read_file()
        return items

    def create_new(self, user, ticker, name, price, date):
        """Lisää tietokantaan kirjautuneen käyttäjän osakkeen.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.
            name: Merkkijono, joka kertoo osakkeen nimen.
            price: Merkkijono, joka kertoo osakkeen ostohinnan.
            date: Merkkijono, joka kertoo osakkeen ostopäivän

        Raises:
            StockExistsError: Virhe, joka tapahtuu, jos osake on jo tietokannassa.
        """
        stock = self._stock_repository.find_by_ticker(user, ticker)
        if stock:
            raise StockExistsError(f'Osake {name} on jo listassa')
        self._stock_repository.create(user, ticker, name, price, date)

    def check_values(self, ticker, name, price, date):
        """Tarkistaa että annetut tiedot on syötetty oikein.

        Args:
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.
            name: Merkkijono, joka kertoo osakkeen nimen.
            price: Merkkijono, joka kertoo osakkeen ostohinnan.
            date: Merkkijono, joka kertoo osakkeen ostopäivän

        Raises:
            InvalidValuesError: Virhe, joka tapahtuu, jos ticker tunnusta ei ole.
            InvalidValuesError: Virhe, joka tapahtuu, jos name kohta tyhjä.
            InvalidValuesError: Virhe, joka tapahtuu, jos price kohta tyhjä.
            InvalidValuesError: Virhe, joka tapahtuu, jos date kohta tyhjä.
            InvalidValuesError: Virhe, joka tapahtuu, jos price arvo väärässä muodossa.
        """
        if ticker is None:
            raise InvalidValuesError('Valitse osake ja paina Lisää osakkeen tiedot painiketta')
        if name is None:
            raise InvalidValuesError('Valitse osake ja paina Lisää osakkeen tiedot painiketta')
        if price == '':
            raise InvalidValuesError('Hintaa ei ole syötetty')
        if date == '':
            raise InvalidValuesError('Päivämäärää ei ole syötetty')
        try:
            float(price)
        except ValueError:
            raise InvalidValuesError(
                'Hinta väärässä muodossa, käytä pistettä desimaali eroittimena'
                )
        return

    def update_values(self, user, ticker, price, date):
        """Päivittää valitun osakkeen tiedot.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.
            price: Merkkijono, joka kertoo osakkeen ostohinnan.
            date: Merkkijono, joka kertoo osakkeen ostopäivän

        Raises:
            GeneralError: Virhe, joka tapahtuu jos päivitys ei onnistunut.
        """
        try:
            self._stock_repository.update(user, ticker, price, date)
            return
        except:
            raise GeneralError('Päivitys ei onnistunut')

    def remove_stock(self, user, ticker):
        """Poistaa valitun osakkeen tiedot.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Raises:
            GeneralError: Virhe, joka tapahtuu jos poisto ei onnistunut.
        """
        try:
            self._stock_repository.remove(user, ticker)
            return
        except:
            raise GeneralError('Poisto ei onnistunut')

stock_services = StockServices()
