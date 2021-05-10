## Helsingin yliopisto:
# Ohjelmistotekniikka, kevät 2021

## Yleistä
Oma sovellukseni Helsingin yliopiston Tietojenkäsittelytieteen kurssiin. Kurssilla tutustutaan ohjelmistokehityksen periaatteisiin sekä menetelmiin ja sovelletaan niitä toteuttamalla pienehkö harjoitustyö.

### Osakeseuranta sovellus
Sovelluksen avulla voidaan seurata Helsingin pörssin OMXH25 osakkeiden kehitystä. Käyttäjällä on mahdollista katsoa päiväkohtaista kehitystä, vuoden alkuun verrattavaa kehitystä tai vuoden taikaiseen tilanteeseen verrattavaa kehitystä. Kehitys näytetään sekä euroissa että prosentteina. Näkyvissä on myös jokaiselle osakkeelle päivän sen hetkinen kurssi. Käyttäjä voi myös luoda sovellukseen omat tunnukset ja tallentaa siihen omia osakkeita. Osakkeelle annetaan ostoajankohta sekä ostohinta. Omalla listalla oleville osakkeille näytetään kehitysluvut verrattuna tämän hetken kurssiin. Listalla olevia osakkeita voidaan muokata sekä poistaa.  

## Huomio Python-versiosta
Sovelluksen toiminta on testattu Python-versiolla `3.6.0` Windows- ja Linux-järjestelmissä.

## Dokumentaatio
- [Käyttöohje](./osakeseuranta/dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./osakeseuranta/dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./osakeseuranta/dokumentaatio/arkkitehtuuri.md)
- [Testusdokumentti](./osakeseuranta/dokumentaatio/testaus.md)
- [Työaikakirjanpito](./osakeseuranta/dokumentaatio/tuntikirjanpito.md)


## Asennus
Suorita seuraavat komennot _osakeseuranta_-hakemistossa.

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:
```bash
poetry run invoke build
```

```bash
poetry shell
```

Koska sovelluksessa käytettävä yfinance-kirjasto ei suostu asentumaan poetry:n avulla, asennetaan se erikseen.

```bash
pip3 install yfinance 
```

3. Käynnistä sovellus komennoilla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Testaus
Testit voidaan suorittaa komennolla:

```bash
poetry run invoke test
```

### Testikattavuus
Testikattavuusraportti generoidaan komennolla:

```bash
poetry run invoke coverage-report
```

Raportti generoituu _htmlcov_-hakemistoon, tiedoston nimi on _index.html_. 

### Pylint
Tiedoston _.pylintrc_ määrittelemät tarkastukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
