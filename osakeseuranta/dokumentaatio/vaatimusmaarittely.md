# Vaatimusmäärittely

# Sovelluksen tarkoitus

Sovelluksen avulla voidaan seurata valitun pörssin pörssikursseja sekä pitää listaa omista osakkeista ja seurata niiden kehitystä.

# Käyttäjät

Sovelluksessa on kaksi käyttäjätasoa; _normaali käyttäjä_, sekä _kirjautunut käyttäjä_.


## Perusversion tarjoamat toiminnallisuudet

### Perusnäkymä

* Oletusnäkymänä OMXH25 (Helsinki) päivätasolla
* Kurssien seurantatasot:
    * Viimeisen päivän kurssit.
    * Kurssit vuoden alusta.
    * YTD kurssit.
* Kirjautuminen:
    * Avautuu ikkuna, jossa voidaan kirjautua järjestelmään tai luoda uusi tunnus.


### Näkymä kirjautuneelle käyttäjälle

* Voidaan valita näkymä, jossa omat osakkeet.
* Voidaan lisätä uusia osakkeita:
    * Hakutoiminto, jolla haetaan haluttu osake. Perusversiossa vain Helsingin pörssin osakkeet.
    * Osakkeelle annetaan ostopäivä sekä hankintahinta.
    * Osakkeen tietojen muokkaaminen.
* Näytetään omien osakkeiden kehitys; päivän kurssi - ostohinta.
* Uloskirjautuminen, paluu perusnäkymään.

## Jatkokehitysideoita
* Voidaan valita pörssi, jonka kurssit näytetään. Oletusnäkymänä OMXH25 (Helsinki). Valittavana pohjoismaiden pörssit.
* Pörssien määrän lisääminen sekä osakkeiden määrän lisääminen kattamaan esim. Pohjoismaat.
* Visuaalisien elementtien tuominen mukaan, kurssigraafit ym.
* Omien osakkeiden vertailu toiseen osakkeeseen tai yleisindeksiin. Tämä voidaan esittää kurssigraafin avulla.
* Pörssin kurssien päivitys esim. viiden minuutin välein.
* Erillaisten tunnuslukujen lisääminen osakkeisiin, esim. P/E ja volatiliteetti. 

