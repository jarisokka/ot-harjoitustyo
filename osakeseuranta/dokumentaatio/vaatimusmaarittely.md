# Vaatimusmäärittely

# Sovelluksen tarkoitus

Sovelluksen avulla voidaan seurata valitun pörssin pörssikursseja sekä pitää listaa omista osakkeista ja seurata niiden kehitystä.

# Käyttäjät

Sovelluksessa on kaksi käyttäjätasoa; _normaali käyttäjä_, sekä _kirjautunut käyttäjä_.


## Perusversion tarjoamat toiminnallisuudet

### Perusnäkymä

* Oletusnäkymänä OMXH25 (Helsinki) päivätasolla.
* Kurssien seurantatasot:
    * Viimeisen päivän kurssit.
    * Kurssit vuoden alusta.
    * YTD kurssit.
* Kirjautuminen:
    * Avautuu ikkuna, jossa voidaan kirjautua järjestelmään tai luoda uusi tunnus.
    * Jos käyttäjää ei olemassa, tai salasana ei täsmää, ilmoittaa järjestelmä tästä.

### Näkymä kirjautuneelle käyttäjälle

* Voidaan valita näkymä, jossa omat osakkeet.
* Voidaan lisätä uusia osakkeita:
    * Alasvetoikkuna, josta valitaan haluttu osake joka halutaan lisätä omalle listalle. Perusversiossa vain rajattu määrä osakkeita.
    * Osakkeelle annetaan ostopäivä ajankohta sekä hankintahinta.
    * Osakkeen tietojen muokkaaminen mahdollista ajankohdan ja hankintahinnan osalta.
* Näytetään omien osakkeiden kehitys; päivän kurssi - ostohinta euroissa ja prosentteina.
* Ohjataan käyttäjän tomintaa virheilmoituksin, jos annettavat syötteet ovat virheellisiä tai puutteellisia.


## Jatkokehitysideoita
* Sovelluslogiikan selkeyttäminen niin, että osakkeesta muodostetaan oma luokka ja palvelut eriytetään omaan luokkaansa.
* Voidaan valita pörssi, jonka kurssit näytetään. Oletusnäkymänä OMXH25 (Helsinki). Valittavana esim. pohjoismaiden pörssit.
* Osakelistauksien laajentaminen, jolloin voidaan valita muitakin osakkeita kuin Helsingin pörssin.
* Visuaalisien elementtien tuominen mukaan, kurssigraafit ym.
* Omien osakkeiden vertailu toiseen osakkeeseen tai yleisindeksiin. Tämä voidaan esittää kurssigraafin avulla.
* Lisätään omiin osakkeisiin myös kappalemäärät sekä kaikkien osakkeiden kokonaiskehitys.
* Pörssin kurssien päivitys esim. viiden minuutin välein.
* Erillaisten tunnuslukujen lisääminen osakkeisiin, esim. P/E ja volatiliteetti.
* Värien hyväksikäyttö; punaisella minuuskehitys, vihreällä plussalla olevat.
