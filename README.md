# koulutuskanta
Tietokantasovellus-harjoitustyö loppukesä-2019 
Sovellus löytyy osoitteesta https://koulutuskanta.herokuapp.com

Testitunnukset sovelluksen tarkasteluun
käyttäjätunnus: Bill 
salasana: 666

(nimi: Bill Gates)

Sovelluksessa voi tällä hetkellä:
-Lisätä uusia käyttäjiä
-Kirjautua sisään ja ulos
-Lisätä kursseja ja materiaaleja
-Lisätä materiaaleja kursseihin
-Lisätä käyttäjiä kursseihin
-Nähdä, mitä kursseja ja materiaaleja on jo lisätty
-Nähdä, ketkä ovat milläkin kurssilla ja mitä materiaaleja milläkin kurssilla on käytetty

Admin (käyttäjä id:llä 1) voi:
-Lisätä käyttäjärooleja
-Liittää käyttäjille käyttäjärooleja

## Aihe: Työntekijöiden suorittamien koulutusten hallinta ja seuranta. 

Koulutuskanta on järjestelmä, jolla voidaan seurata työpaikalla suoritettuja koulutuksia sekä työntekijöiden osaamista. Järjestelmää on tarkoitus käyttää tehostamaan rekrytointia ja myyntiä. Toimitusjohtaja saa järjestelmältä yhteenvetoja suoritetuista koulutuksista henkilöittäin ja aiheittain. Kukin koulutuksia suorittava henkilö kirjaa järjestelmän suorittamansa koulutuksen ja siihen liittyvät materiaalit tai lisää itselleen suorituksen jo jonkun muun lisäämästä kurssista. Työntekijä näkee vain omat suorituksensa. Toimitusjohtaja voi hakea tietoa myös henkilöittäin.

### Toimintoja:
* Rekisteröityminen
* Kirjautuminen
* Kurssin lisäämine
* Materiaalin lisääminen
* Materiaalin liittäminen kurssiin
* Käyttäjän liittäminen kurssille

### Toimintoja vain adminille:
* Käyttäjäroolin lisääminen
* Käyttäjän liittäminen käyttäjärooliin

### Koulutuskannasta löytyvät raportit:
- Järjestelmän tuntemista käyttäjistä
- Järjestelmään lisätyistä kurssimateriaaleista
- Järjestelmään lisätyistä kurssilaisista
- Materiaaleista, joihin käyttäjät ovat kursseilla perehtyneet



