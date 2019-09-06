# Koulutuskanta
Tietokantasovellus-harjoitustyö loppukesä-2019 
Sovellus löytyy osoitteesta https://koulutuskanta.herokuapp.com
Tietokantakaavio löytyy täältä: <lisää linkki>


## Työntekijöiden osaamisalueiden kartoittaminen yrityksen HR-henkilöiden ja myyjien käyttöön
Koulutuskanta on tehty yrityksen HR-henkilölle ja myyjille, jotka pystyvät Koulutuskannasta katsomaan, minkä nimisiä kursseja organisaation tyntekijät ovat käyneet ja minkälaisia materiaaleja kursseilla on käytetty. Näin he pysyvät perässä siitä, minkälaista osaamista yrityksestä löytyy, mitä osa-alueita pitäisi ehkä kehittää ja kenet voi lähettää mihinkin asiakasprojektiin Koulutuskannasta ilmenevän osaamisensa perusteella.

Testitunnukset sovelluksen tarkasteluun
*Admin*
käyttäjätunnus: Bill 
salasana: Windows

*End user*
käyttäjätunnus: Steve
salasana: Apple


## Toimintoja:
Sovelluksessa voi tällä hetkellä:
-Rekisteröityä käyttäjäksi
-Kirjautua sisään ja ulos
-Muuttaa omia tietojaan (nimi, käyttäjätunnus, salasana)
-Lisätä kursseja ja materiaaleja
-Liittää materiaaleja kursseihin eli lisätä kurssimateriaaleja
-Liittä kurssilaisia kursseihin eli lisätä kurssilaisia
-Nähdä, mitä kursseja, materiaaleja ja kurssimateriaaleja on jo lisätty
-Nähdä, kuinka monta osallistujaa on kullakin kurssilla

Admin oikeuksilla voi
-Tehdä end userista adminin ja toisinpäin
-Poistaa käyttäjän
-Nähdä listauksia siitä, kuka työntekijä on milläkin kurssilla
-Nähdä listauksia siitä, mihin materiaaleihin ihmiset ovat käymiensä kurssien perusteella perehtyneet

### Koulutuskannasta löytyvät raportit Adminille:
- Järjestelmän tuntemista käyttäjistä ja heidän käyttäjätunnuksistaan
- Työntekijöiden käymistä kursseista
- Eri kursseilla käytetyistä materiaalien määristä
- Materiaaleista, joihin käyttäjät ovat kursseilla perehtyneet


