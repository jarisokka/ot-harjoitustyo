from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)

class InvalidCredentialsError(Exception):
    pass

class UsernameExistsError(Exception):
    pass

class UserServices:
    """Käyttäjän sovelluslogiikasta vastaava luokka."""

    def __init__(self, user_repository=default_user_repository):
        """Luokan konstruktori, joka luo uuden käyttäjätunnuksen
            sovelluslogiikasta vastaavan palvelun.

        Args:
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._user_repository = user_repository

    def login(self, username, password):
        """Kirjaa käyttäjän sisään.
        Args:
            username: Merkkijono, joka kertoo käyttätunnuksen.
            password: Merkkijono, joka kertoo salasanan.
        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        Raises:
            InvalidCredentialsError:
                Virhe, joka tapahtuu, kun käyttäjätunnus ja salasana eivät täsmää.
        """
        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError('Väärä käyttäjätunnus tai salasana')
        self._user = user

        return user

    def get_current_user(self):
        """Paluttaa kirjautuunen käyttäjän.

        Returns:
            Kirjautunut käyttäjä User-olion muodossa.
        """
        return self._user

    def get_users(self):
        """Palauttaa kaikki käyttäjät.

        Returns:
            User-oliota sisältä lista kaikista käyttäjistä.
        """
        return self._user_repository.find_all()

    def logout(self):
        """Kirjaa nykyisen käyttäjän ulos."""
        self._user = None

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja tarvittaessa kirjaa sen sisään.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            login:
                Vapaahtoinen, oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.

        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, kun käyttäjätunnus on jo käytössä.

        Returns:
            Luotu käyttäjä User-olion muodossa.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f'Käyttäjätunnus {username} on jo olemassa')

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

        return user

user_services = UserServices()
