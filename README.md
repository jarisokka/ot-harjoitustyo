## Helsingin yliopisto:
# Ohjelmistotekniikka, kevät 2021

## Yleistä
Oma sovellukseni Helsingin yliopiston Tietojenkäsittelytieteen kurssiin. Kurssilla tutustutaan ohjelmistokehityksen periaatteisiin sekä menetelmiin ja sovelletaan niitä toteuttamalla pienehkö harjoitustyö.

### Tilannekatsaus
Ohjelmaan on tehty luokat, jotka noutavat osakkeiden kursseja yfinance kirjaston avulla. Ensimmäiset testit luotu yhdelle näistä luokista, joskin vasta alustavat, jotta voidaan havainnoida poetryn asetuksien oikeellisuus ja toimivuus. Oletusnäkymälle tehty graaffinen käyttöliittymän, jossa näkyvissä Helsingin pörssin OMX25 listaus kurssitietoineen.

## Dokumentaatio
- [Vaatimusmäärittely](./osakeseuranta/dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./osakeseuranta/dokumentaatio/tuntikirjanpito.md)

## Asennus

1. Asenna riippuvuudet komennolla:
```bash
poetry install
```

2. Käynnistä sovellus komennoilla:
```bash
poetry shell
```
Tämän jälkeen suorita komento

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


