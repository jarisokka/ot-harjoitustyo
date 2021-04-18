## Helsingin yliopisto:
# Ohjelmistotekniikka, kevät 2021

## Yleistä
Oma sovellukseni Helsingin yliopiston Tietojenkäsittelytieteen kurssiin. Kurssilla tutustutaan ohjelmistokehityksen periaatteisiin sekä menetelmiin ja sovelletaan niitä toteuttamalla pienehkö harjoitustyö. Harjoitustyönä toteutan osakkeiden seuranta sovelluksen, johon voi myös tallentaa omia osakkeita seurantaa varten.

### Tilannekatsaus
Ohjelmaan on tehty luokat, jotka noutavat osakkeiden kursseja yfinance kirjaston avulla. Testejä tehty _singlestockdata_-luokalle jotka ovat jo melko kattavia. Oletusnäkymälle tehty graaffinen käyttöliittymän, jossa näkyvissä Helsingin pörssin OMX25 listaus kurssitietoineen. Tällä hetkellä ei haeta jokaista OMX25-osaketa, jotta sovellus avautuu nopeammin ja kehitystyö on näin sujuvampaa. Oletusnäkymässä mahdollista katsoa tämän päivän kurssit sekä kurssikehitys, kurssikehitys vuoden alusta, sekä kurssikehitys vuoden takaiseen tilanteeseen nähden. Näkyvissä myös Helsingin pörssin yleisindeksi ja kehitysprosentti. Kättäjä pystyy luomaan uudet tunnukset sekä kijautumaan sovellukseen. Tämän jälkeen käyttäjälle aukeaa uusi näkymä.

Seuraavana työvaiheena tietokantojen lisääminen käyttäjän omille osakkeille sekä käyttöliittymä näiden hallintaa varten.

## Dokumentaatio
- [Vaatimusmäärittely](./osakeseuranta/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./osakeseuranta/dokumentaatio/tuntikirjanpito.md)
- [Arkkitehtuurikuvaus](./osakeseuranta/dokumentaatio/arkkitehtuuri.md)

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
