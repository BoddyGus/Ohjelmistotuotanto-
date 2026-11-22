# TDD ja AI -reflektio

## Toteutus

Ostoskori toteutettiin testivetoisesti. Muutokset rajattiin
`Ostoskori`-luokan toteutukseen; `Ostos`- ja `Tuote`-luokkien koodia
ei muutettu.

## Testit

Testit kattavat:

- tyhjän korin
- yhden ja kahden tuotteen lisäämisen
- saman tuotteen lukumäärän
- hintojen laskemisen
- tuotteen poistamisen
- ostoskorin tyhjentämisen
- ostoslistan sisällön

Kaikki testit ajettiin projektin omassa `.venv`-ympäristössä
komennolla `uv run pytest`.

## TDD ja refaktorointi

Toteutus rakennettiin pienin askelin testien perusteella.
Refaktorointivaiheessa logiikka keskitettiin samaa tuotetta etsivään
`_etsi_ostos`-metodiin. Tämä vähentää toistuvaa koodia ja säilyttää
julisen rajapinnan toiminnan.

## Havaintoja agentista

Toteutuksessa pysyttiin rajauksessa `ostoskori.py`-tiedoston
muutoksissa. Testit säilytettiin muuttumattomina. Minimitoteutuksella
rakennettiin vain vaadittua toimintaa ja vältyttiin ylimääräisten
metodien, kovakoodatun arvon ja muiden tiedostojen muutoksilta.