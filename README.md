# Lesmateriaal HAVO-P

Publiek lesmateriaal bij het HAVO-P Profielproject: volledig leerlingmateriaal,
invulbare opdrachtbladen en beoordelingsrubrics, als kant-en-klare HTML-pagina's.

Open [index.html](index.html) voor het overzicht van alle projecten.

## Werken met de opdrachtbladen

Elk opdrachtblad bewaart ingevulde antwoorden automatisch in de browser van de
leerling (niet op een server). Gebruik daarom altijd je eigen device of inlog —
op een gedeeld apparaat overschrijft de volgende leerling de vorige antwoorden.
Download je werk als PDF via de knop rechtsboven en lever dat in.

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
