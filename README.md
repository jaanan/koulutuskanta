# Koulutuskanta
Tietokantasovellusharjoitustyö loppukesä-2019

Sovellus löytyy osoitteesta https://koulutuskanta.herokuapp.com

Tietokantakaavio löytyy täältä: https://github.com/jaanan/koulutuskanta/blob/master/documentation/Untitled%20Diagram.png


## Työntekijöiden osaamisalueiden kartoittaminen yrityksen HR-henkilöiden ja myyjien käyttöön
Koulutuskanta on tehty yrityksen HR-henkilölle ja myyjille, jotka pystyvät Koulutuskannasta katsomaan, minkä nimisiä kursseja organisaation tyntekijät ovat käyneet ja minkälaisia materiaaleja kursseilla on käytetty. Näin he pysyvät perässä siitä, minkälaista osaamista yrityksestä löytyy, mitä osa-alueita pitäisi ehkä kehittää ja kenet voi lähettää mihinkin asiakasprojektiin Koulutuskannasta ilmenevän osaamisensa perusteella.

Testitunnukset sovelluksen tarkasteluun

*Admin*

käyttäjätunnus: Bill 

salasana: Windows

*End user*

käyttäjätunnus: Steve

salasana: Apple


## Toimintoja
### Use cases kaikille käyttäjille

+ Rekisteröityä käyttäjäksi
+ Kirjautua sisään ja ulos
+ Käyttäjät voivat lisätä kursseja, materiaaleja, materiaaleja kursseihin (kurssimateriaaleja) sekä käyttäjiä kursseihin (kurssilaisia). 
+ Käyttäjät voivat muuttaa omaa nimeään, käyttäjänimeään ja salasanaansa. 
+ Käyttäjät näkevät mitä materiaaleja, kursseja ja kurssimateriaaleja on lisätty sekä montako osallistujaa eri kursseilla on.
+ Käyttäjä näkee omilta sivuiltaan, mitä kursseja on itse käynyt. 

### Use cases admineille
+ Admin voi poistaa käyttäjiä
+ Admin voi muuttaa näiden käyttäjäoikeuksia end userista adminiksi ja toisinpäin.

### Koulutuskannasta löytyvät raportit Adminille:

+ Järjestelmän tuntemista käyttäjistä ja heidän käyttäjätunnuksistaan
+ Työntekijöiden käymistä kursseista
+ Eri kursseilla käytetyistä materiaalien määristä
+ Materiaaleista, joihin käyttäjät ovat kursseilla perehtyneet

### SQL queries


Listaa käyttäjien nimet ja käyttäjätunnukset:
```
SELECT Account.username, Account.name FROM Account;
```

Listaa kurssilaiset ja heidän käymänsä kurssit:
```
SELECT Account.name AS Työntekijä, Course.name AS Kurssi FROM Account, Course, kurssilainen
WHERE Course.id = kurssilainen."course.id"
AND Account.id = kurssilainen."account.id"
ORDER BY Account.name;
```

Kuinka monta kurssilaista kullakin kurssilla on:
```
SELECT Course.name, COUNT(*) total FROM Course, kurssilainen
WHERE kurssilainen."course.id" = Course.id
GROUP BY Course.id;
```

Kurssilla käytettyjen materiaalien määrä:
```
SELECT Course.name AS kurssi, COUNT(*) AS materiaaleja FROM Course, kurssimateriaali
WHERE Course.id = kurssimateriaali."course.id"'
GROUP BY Course.name
ORDER BY Course.name;
```

Näen mitä materiaaleja eri käyttäjät ovat milläkin kurssilla lukeneet:
```
SELECT Account.name AS Työntekijä, Course.name AS Kurssi, Material.name AS Materiaali FROM Account
LEFT JOIN kurssilainen ON kurssilainen."account.id" = Account.id
LEFT JOIN Course ON kurssilainen."course.id" = Course.id
LEFT JOIN kurssimateriaali ON kurssilainen."course.id" = kurssimateriaali."course.id"
LEFT JOIN Material ON kurssimateriaali."material.id" = Material.id
WHERE Material.name IS NOT NULL'
ORDER BY Account.name, Course.name, Material.name
```

Käyttäjän itsensä käymät kurssit:
```
SELECT Course.name AS Kurssi FROM Course
LEFT JOIN kurssilainen ON kurssilainen."course.id" = Course.id
WHERE kurssilainen."account.id" = {} '.format(id)
```

Kursseilla käytetty materiaali, eli kurssimateriaalit:
```
SELECT Course.name AS Kurssi, Material.name AS Materiaali FROM Course, Material, kurssimateriaali
WHERE Course.id = kurssimateriaali."course.id" 
AND Material.id = kurssimateriaali."material.id"
```

# Sovelluksen käyttöönotto
Sinun tulee ladata python, pip ja sqlite3, jotta saat ohjelman toimimaan. 
Klootaa tämä github reporitorio tai lataa zip-tiedosto tämän projektin githubista. 
Navigoi tiedoston juurikansioon.
Luo python virtuaaliympäristö käskyllä python -m venv venv
Käynnistä se seuraavin käskyin: -Linux/Mac: source venv/bin/activate -Windows: venv\Scripts\activate.bat
Asenna riippuvuudet ajamalla pip install -r requirements
Kirjoita python run.py terminaaliin ja paina enter.
