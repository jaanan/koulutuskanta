# Koulutuskanta
Tietokantasovellus-harjoitustyö loppukesä-2019

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
Sovelluksessa voi tällä hetkellä:

-Rekisteröityä käyttäjäksi

-Kirjautua sisään ja ulos

-Muuttaa omia tietojaan (nimi, käyttäjätunnus, salasana)

-Lisätä kursseja ja materiaaleja

-Liittää materiaaleja kursseihin eli lisätä kurssimateriaaleja

-Liittä kurssilaisia kursseihin eli lisätä kurssilaisia

-Nähdä, mitä kursseja, materiaaleja ja kurssimateriaaleja on jo lisätty

-Nähdä, kuinka monta osallistujaa on kullakin kurssilla


#### Admin-oikeuksilla voi

-Tehdä end userista adminin ja toisinpäin

-Poistaa käyttäjän

-Nähdä listauksia siitä, kuka työntekijä on milläkin kurssilla

-Nähdä listauksia siitä, mihin materiaaleihin ihmiset ovat käymiensä kurssien perusteella perehtyneet

### Koulutuskannasta löytyvät raportit Adminille:

- Järjestelmän tuntemista käyttäjistä ja heidän käyttäjätunnuksistaan

- Työntekijöiden käymistä kursseista

- Eri kursseilla käytetyistä materiaalien määristä

- Materiaaleista, joihin käyttäjät ovat kursseilla perehtyneet

### Use cases

+ Käyttäjät voivat lisätä kursseja, materiaaleja, materiaaleja kursseihin (kurssimateriaaleja) sekä käyttäjiä kursseihin (kurssilaisia). 
+ Käyttäjät voivat muuttaa omaa nimeään, käyttäjänimeään ja salasanaansa. 
+ Käyttäjät näkevät mitä materiaaleja, kursseja ja kurssimateriaaleja on lisätty sekä montako osallistujaa eri kursseilla on.
+ Käyttäjä näkee omilta sivuiltaan, mitä kursseja on itse käynyt. 
+ Vain admin-oikeuksilla näkee, kuka on käynyt minkäkin kurssin ja saa näkyvilleen taulun, josta käy myös selväksi, mitä materiaaleja kukakin on lukenut käymiensä kurssien perusteella.
+ Admin voi poistaa käyttäjiä ja muuttaa näiden käyttäjäoikeuksia end userista adminiksi ja toisinpäin.



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
