# Lesmateriaal HAVO-P

Publiek lesmateriaal bij het HAVO-P Profielproject: volledig leerlingmateriaal,
invulbare opdrachtbladen en beoordelingsrubrics, als kant-en-klare HTML-pagina's.

Open [index.html](index.html) voor het overzicht van alle projecten.

## Werken met de opdrachtbladen

Elk opdrachtblad bewaart ingevulde antwoorden automatisch in de browser van de
leerling (niet op een server). Gebruik daarom altijd je eigen device of inlog —
op een gedeeld apparaat overschrijft de volgende leerling de vorige antwoorden.
Download je werk als PDF via de knop rechtsboven en lever dat in.

## Privacy

Deze pagina's hebben geen backend en versturen niets automatisch. Alles wat je
invult — tekst, aangevinkte vakjes, geüploade foto's — blijft uitsluitend
opgeslagen in `localStorage` van je eigen browser, op je eigen apparaat. Er is
geen formulier, geen fetch-aanroep en geen inlogsysteem dat gegevens naar deze
repo, GitHub of wie dan ook stuurt. Deze repository bevat alleen de lege
sjablonen; ingevulde antwoorden van leerlingen komen hier nooit in terecht. De
enige manier waarop werk de browser verlaat, is wanneer de leerling zelf de
PDF downloadt en die inlevert bij de docent.

## Herkomst

Dit lesmateriaal wordt gebouwd met [Agent Studio](https://github.com/jduitsman/agent-studio),
een eigen werkomgeving voor het maken van lesmateriaal. Deze repo bevat alleen
het gepubliceerde eindresultaat — geen agent-configuratie of ander privé-materiaal.

## Bijwerken

Na het toevoegen of aanpassen van een project:

```bash
python3 bin/maak-index.py
git add -A && git commit -m "Bijwerken lesmateriaal" && git push
```
