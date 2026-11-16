# Kokemuksia agentin käytöstä

## Minkälaisen ohjetiedoston agentti generoi, ja mitä jouduit korjaamaan?

Agentti ei generoinut ohjetiedostoa. Projektin
`.github/copilot-instructions.md` luotiin tässä työskentelyssä ennen
storyjen toteutusta. Ohjeessa kuvataan Flask-sovelluksen rakenne,
`uv`-komennot, Robot Framework -testien suorittaminen sekä se, missä
kerroksessa reitit, validointi ja muistissa oleva repository sijaitsevat.
Ohjetiedostoon ei tarvinnut tehdä korjauksia.

Ensimmäisen storyn toteutuksessa agentti lisäsi `UserService.validate`-
metodiin `password.isalpha()`-tarkistuksen ja virheilmoituksen. Muutos oli
pyynnön mukainen, eikä ylimääräisiä sovellustiedostoja muutettu.

## Noudattiko agentti pyyntöä kirjoittaa testit ennen toteutusta?

Ensimmäisen storyn osalta noudatti. Agentti lisäsi ensin neljä
Robot Framework -testiä `register.robot`-tiedostoon ja ajoi ne ennen
toteutuksen muuttamista. Kaksi uutta hylkäystestiä epäonnistui odotetusti.
Vasta tämän jälkeen agentti toteutti toiminnallisuuden, minkä jälkeen kaikki
kahdeksan rekisteröitymistestiä menivät läpi.

Toisen storyn testivaihe oli käynnistetty, mutta se keskeytettiin ennen
valmistumista käyttäjän pyynnöstä. Siksi siitä ei ole valmista testivaiheen
tulosta eikä toteutusta tässä työvaiheessa.

## Kuinka paljon jouduit ohjaamaan agenttia matkan varrella?

Ohjaus oli melko vähäistä mutta tarkkaa. Agentille annettiin erikseen
testivaiheen ja toteutusvaiheen tehtävät, rajattiin muokattavat tiedostot,
vaadittiin sovelluksen ja testien ajamista sekä pyydettiin raportoimaan
komennot ja tulokset. Lisäksi muutokset tarkistettiin `git diff`-komennolla
ennen seuraavaa vaihetta.

## Hajosivatko testit, kun rikoit toteutuksen tarkoituksella?

Tässä keskeytetyssä työvaiheessa tarkoituksellisia mutaatiotestejä ei ehditty
tehdä. Siksi tästä ei voi rehellisesti raportoida onnistunutta varmennusta.
Ensimmäinen story varmennettiin kuitenkin ensin epäonnistuvilla testeillä
ennen toteutusta ja lopuksi kahdeksalla läpi menneellä testillä.

## Mitä uutta opit?

Opin käyttämään hyväksymistestivetoista työskentelyä niin, että uuden
toiminnallisuuden puuttuminen todistetaan ensin epäonnistuvalla testillä.
Opin myös, että Robot Framework -testien testiympäristö alustetaan
`/tests/reset`-reitillä ja että Flask-sovellus täytyy pitää käynnissä
portissa 5001 erillisessä prosessissa. Lisäksi opin tarkistamaan agentin
muutosten rajauksen diffistä sen sijaan, että luottaisin pelkkään agentin
raporttiin.
