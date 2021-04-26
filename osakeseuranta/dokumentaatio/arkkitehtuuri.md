# Arkkitehtuurikuvaus

## Rakenne

Ohjelman rakenne on hyvin samankaltainen opintomariaalissa olevan referenssi soveluksen kanssa. Ohjelman rakenne noudattelee täten kolmitasoista kerrosarkkitehtuuria. Koodin pakkausrakenne on seuraava:

![Pakkausrakenne](./kuvat/pakkausrakenne.jpg)

Koodi on jaoteltu paukkauksiin seuraavasti: _ui_ käyttöliittymä, _services_ sovelluslogiikka ja _repositories_ tietojen pysyväistallennus sekä sieltä lukeminen. Pakkaus _entities_ sisältää luokkia, jotka kuvastavat sovelukksen käyttämiä tietokohteita.

## Käyttöliittymä

Kättöliittymä sisältää käyttäjän näkökulmasta kolme erillistä näkymää:

- Päänäkymä osakekursseista
- Uuden käyttäjätunnuksen luominen/kirjautuminen
- Kirjautuneen käyttäjän näkymä

Jokainen näkymä on toteutettu omana luokkanaan. Päänäkymä muodostuu itse asiassa kolmesta eri luokasta. Näitä ovat [Päivä](../src/ui/day_view.py), [Vuoden alusta](../src/ui/ytd_view.py) sekä [Vuosi](../src/ui/year_view.py) -luokat. Näkymien vaihtaminen tapahtuu _button_ painikkeiden avulla. Näkymien näyttämisestä vastaa [UI](../src/ui/ui.py)-luokka. Kirjautumista varten aukeaa uusi näkymä, joka toteutetaan [Kirjaudu](../src/ui/create_user_login_view.py) -luokan avulla. Kirjautuneelle käyttäjälle aukeaa uusi näkymä [Omat osakkeet](../src/ui/user_view.py) -luokkaa käyttäen. Maksimissaan on näyvissä käyttäjälle kaksi näkymää yhtä aikaa.

Käyttöliittymä on pyritty eristämään täysin sovelluslogiikasta. Se ainostaan kutsuu _services_ pakkauksessa olevia luokkia ja metodeja.

## Tietojen pysyväistallennus ja lataus

Pakkauksen _repositories_ luokat `StockRepository` ja `UserRepository` huolehtivat tietojen tallentamisesta SQLite-tietokantaan.

Pakkauksen _repositories_ luokka `ReadStockListFromFile` vastaa CSV-tiedostojen avaamisesta ja lukemisesta. Näiden CSV-tiedostojen avulla voidaan hallita, mitä osakkeita sovelluksessa voidaan käyttää.

### Tiedostot

Käyttäjät tallennetaan SQLite-tietokannan tauluu `users` ja kirjautuneen käyttäjän osakkeet tauluun `stocks`. Tietokannat alustetaan [initialize_database.py](https://github.com/jarisokka/ot-harjoitustyo/blob/master/osakeseuranta/src/initialize_database.py) -tietostossa.

Soveluksessa käytettäviä osakkeita hallitaan CSV-tiedostojen avulla, jotka sijaitsevat _data_ kansiossa.

Tiedostojen formaatin tulee olla seuraavassa muodossa:
```
ticker;nimi
```
Sovelluksessa käytetään _yfinance_ kirjastoa, jonka avulla haetaan osakkeiden tiedot Yahoo Finance-palvelusta. Tämä haku tapahtuu _ticker_:eiden avulla ja tämän takia sen tulee olla täsmällinen. Osakkeen nimen voi määritellä haluamakseen, mutta tähän sovellukseen nyt laitetut nimet ovat yrityksien virallisia nimiä.

## Päätoiminnallisuudet

Seuraavassa käydään läpi sovelluksen toimintalogiikkaa muutaman päätoiminnallisuuden osalta sekvenssikaaviona.

### Uuden käyttäjän luominen

Jotta sovellukseen voi tallentaa omia osakkeita, tulee siihin ensin luoda käyttäjätunnus, jolla voidaan kirjautua sovellukseen. Päänäkymästä [UI](../src/ui/ui.py) päästään kirjautumis sivulle [Kirjaudu](../src/ui/create_user_login_view.py) klikkaamalla _Kirjaudu_ painiketta. Tältä sivulta voidaan luoda tunnus klikkaamalla _Luo tunnus_ painiketta.

Alla kuvattu sekvenssikaavio uuden käyttäjätunnuksen luomisesta. 

![](./kuvat/sekvenssi-uusitunnus.png)

[Tapahtumankäsitettelijä](https://github.com/jarisokka/ot-harjoitustyo/blob/master/osakeseuranta/src/ui/create_user_login_view.py#L19) kutsuu sovelluslogiikan metodia [create_user](https://github.com/jarisokka/ot-harjoitustyo/blob/master/osakeseuranta/src/services/user_services.py#L35) antaen parametriksi luotavan käyttäjän tiedot. Sovelluslogiikka selvittää `UserRepository`:n avulla, onko käyttäjätunnus jo olemassa. Jos ei, niin sovelluslogiikka luo uuden _User_-olion ja tallentaa sen kutsumalla `UserRepository`:n metodia `create`. Onnistuneen tunnuksen luonnin jälkeen käyttöliittymä avaa _messagebox_:n jossa informoidaan uuden tunnuksen luonnin onnistumisesta ja että käyttäjä voi nyt kirjautua sovellukseen.

### Käyttäjän kirjautuminen

Kirjautuminen tapahtuu [Kirjaudu](../src/ui/create_user_login_view.py) näkymästä, jonne päästään klikkaamalla päänäkymän _Kirjaudu_ painiketta. Kirjautuminen sovellukseen tapahtuu Kirjaudu näkymästä klikkaamalla _Kirjaudu_ painiketta.

Alla kuvattu sekvenssikaavio sovellukseen kirjautumisesta. 

![](./kuvat/sekvenssi-kirjautuminen.png)

[Tapahtumankäsitettelijä](https://github.com/jarisokka/ot-harjoitustyo/blob/master/osakeseuranta/src/ui/create_user_login_view.py#L19) kutsuu sovelluslogiikan metodia [login](https://github.com/jarisokka/ot-harjoitustyo/blob/master/osakeseuranta/src/services/user_services.py#L17) antaen parametriksi käyttäjätunnuksen ja salasanan. Sovelluslogiikka selvittää `UserRepository`:n avulla, onko käyttäjätunnus olemassa. Jos on, tarkastetaan täsmääkö salasana. Onnistuneen tarkastuksen jälkeen, käyttöliittymä avaa uuden näkymän `UserView`:n avulla. Tässä näkymässä käyttäjä voi hallinoida omien osakkeiden seurantaa. 



