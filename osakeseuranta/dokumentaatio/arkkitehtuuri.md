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
