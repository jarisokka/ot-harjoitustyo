#This code is from the course material
from entities.user import User
from database_connection import get_database_connection

def get_user_by_row(row):
    return User(row['username'], row['password']) if row else None

class UserRepository:
    """Luokka, joka vastaa users tietokannan hallinnasta.

    Attributes:
        connetion: yhteys tietokantaan.
    """

    def __init__(self, connection):
        """Luokan konstruktori, josssa määritellään yhteys tietokantaan.

        Args:
            connection: yhteys tietokantaan.
        """
        self._connection = connection

    def find_all(self):
        """Hakee tietokannasta kaikki käyttäjät

        Returns:
            Palauttaa listan User olioista.
        """
        cursor = self._connection.cursor()
        cursor.execute('select * from users')
        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))

    def find_by_username(self, username):
        """Hakee käyttäjän tietonannasta käyttättuksen avulla

        Args:
            username: Merkkijono, joka kertoo käyttätunnuksen

        Returns:
            Pauttaa löydetyn User olion.
        """
        cursor = self._connection.cursor()
        cursor.execute(
            'select * from users where username = ?',
            (username,)
        )
        row = cursor.fetchone()

        return get_user_by_row(row)

    def create(self, user):
        """Luo uuden käyttäjätunnuksen ja salasanan tietokantaan.

        Args:
            user: User olio, jonka arvoina käyttäjätunnus ja salasana.

        Returns:
            Palauttaa User olion
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into users (username, password) values (?, ?)',
            (user.username, user.password)
        )
        self._connection.commit()

        return user

    def delete_all(self):
        """Tyhjentää users tietokannan
        """
        cursor = self._connection.cursor()
        cursor.execute('delete from users')
        self._connection.commit()

user_repository = UserRepository(get_database_connection())
