from database_connection import get_database_connection

class StockRepository:
    """Luokka, joka vastaa stocks tietokannan hallinnasta.

    Attributes:
        connetion: yhteys tietokantaan.
        userlist: sanakirja, johon tiedot kerätään
    """
    def __init__(self, connection):
        """Luokan konstruktori, josssa määritellään yhteys tietokantaan.

        Args:
            connection: yhteys tietokantaan.
        """

        self._connection = connection
        self._userlist = {}

    def get_stocks_by_user(self, user):
        """Hakee tietokannasta kaikki käyttäjän osakkeet

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.

        Returns:
            Palauttaa sanakirjan johon kerätty löydetyt tiedot.
            Avaimena käytetään ticker tunnusta, arvot ovat järjestyksessä:
            nimi, hinta ja päivämäärä.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from stocks where user = ?',
            (user,)
        )
        rows = cursor.fetchall()
        self._userlist = {}
        for row in rows:
            self._userlist[row[1]] = []
            self._userlist[row[1]].append(str(row[2]))
            self._userlist[row[1]].append(str(row[3]))
            self._userlist[row[1]].append(str(row[4]))
        return self._userlist

    def find_by_ticker(self, user, ticker):
        """Haetaan tietokannasta tiedot käyttäjä- sekä ticker-tunnuksien
            perusteella.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            Palauttaa tietokanta haun tulokset.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'select * from stocks where user = ? and ticker = ?',
            (user, ticker)
        )
        result = cursor.fetchone()
        return result

    def create(self, user, ticker, name, price, date):
        """Lisää uudet arvot tietokantaan.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.
            name: Merkkijono, joka kertoo osakkeen nimen.
            price: Merkkijono, joka kertoo osakkeen ostohinnan.
            date: Merkkijono, joka kertoo osakkeen ostopäivän.

        Returns:
            True jos tietokantaan luonti onnistui.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'insert into stocks (user, ticker, name, price, date) values (?, ?, ?, ?, ?)',
            (user, ticker, name, price, date)
        )
        self._connection.commit()
        return True

    def update(self, user, ticker, price, date):
        """Päivittää tietokantaan osakkeen tiedot. Osake määritellään
            käyttäjätunnuksen ja ticker-tunnuksen avulla.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.
            price: Merkkijono, joka kertoo osakkeen ostohinnan.
            date: Merkkijono, joka kertoo osakkeen ostopäivän.

        Returns:
            True jos tietokannan päivitys onnistui.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'update stocks set price = ?, date = ? where user = ? and ticker = ?',
            (price, date, user, ticker)
        )
        self._connection.commit()
        return True

    def remove(self, user, ticker):
        """Poistaa valitun osakkeen. Osake määritellään
            käyttäjätunnuksen ja ticker-tunnuksen avulla.

        Args:
            user: Merkkijono, joka kertoo käyttätunnuksen.
            ticker: Merkkijono, joka kertoo ticker-tunnuksen.

        Returns:
            True jos tietokannasta poisto onnistui.
        """

        cursor = self._connection.cursor()
        cursor.execute(
            'delete from stocks where user = ? and ticker = ?',
            (user, ticker)
        )
        self._connection.commit()
        return True

    def delete_all(self):
        """Tyhjentää stocks tietokannan
        """
        cursor = self._connection.cursor()
        cursor.execute('delete from stocks')
        self._connection.commit()

stock_repository = StockRepository(get_database_connection())
