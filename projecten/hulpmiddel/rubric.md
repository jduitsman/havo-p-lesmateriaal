# Beoordelingsrubric — Hulpmiddel voor scootmobielgebruikers

**Vak:** HAVO-P Profielproject
**Klas:** HAVO 4
**Duur:** 10 lessen van 200 minuten

Deze rubric hoort bij het projectdocument. Lees hem vóórdat je begint: dan weet je precies waarop je wordt beoordeeld en kun je jezelf onderweg controleren.

**Zo werkt het:** er zijn 6 criteria. Elk criterium heeft 4 niveaus. Je moet een niveau kunnen *aantonen* — met je logboek, je CAD-bestanden, je foto's, je testresultaten en je eindproduct. Wat je niet kunt laten zien, telt niet mee.

| Criterium | Weging | Label |
|---|---|---|
| 1. Gebruikersonderzoek & Programma van Eisen | 15 % | 🔄 Proces |
| 2. CAD-ontwerp in Onshape | 20 % | 🔧 Product |
| 3. 3D-printkennis toegepast | 15 % | 🔧 Product |
| 4. Iteratie & testen | 20 % | 🔄 Proces |
| 5. Eindproduct: functie, veiligheid & pasvorm | 20 % | 🔧 Product |
| 6. Onderbouwing, presentatie & samenwerking | 10 % | 🔄 Proces |
| **Totaal** | **100 %** | |

---

## 1. Gebruikersonderzoek & Programma van Eisen — 15 % 🔄 Proces

*Is je ontwerp gebaseerd op een écht probleem van een échte gebruiker, en heb je dat vertaald naar eisen die je kunt meten?*

| Onvoldoende | Voldoende | Goed | Uitstekend |
|---|---|---|---|
| Het probleem is een aanname van jezelf. Geen interview, geen observatie, of alleen "ik dacht dat dit handig zou zijn". Het PvE ontbreekt, of bevat alleen niet-meetbare wensen ("moet stevig zijn", "moet mooi zijn"). | Er is een interview gedaan en het probleem is beschreven. Het PvE bevat de harde eisen (120 mm, 4 uur, 3 onderdelen, factor 3×, schud-test) plus minstens 3 eigen gebruikerseisen, waarvan de meeste meetbaar zijn (met een getal, een maat of een test). | Interview én observatie/film én empathie-oefening zijn gedaan en leiden aantoonbaar tot hetzelfde probleem. Je laat zien wat de gebruiker zei én wat je zelf zag — en waar die twee van elkaar verschilden. Alle eigen eisen zijn meetbaar geformuleerd. | Je hebt een probleem gevonden dat de gebruiker zelf niet benoemde, en je bewijst met je observatie of empathie-oefening dát het een probleem is. Je PvE bevat een eis die uit jouw eigen waarneming komt en die je met een concrete test kunt controleren. De 3 concepten zijn tegen het PvE afgewogen, niet op smaak gekozen. |

---

## 2. CAD-ontwerp in Onshape — 20 % 🔧 Product

*Kun je nauwkeurig meten aan een bestaand product en die maten correct vertalen naar een aanpasbaar 3D-model?*

| Onvoldoende | Voldoende | Goed | Uitstekend |
|---|---|---|---|
| Maten zijn geschat, overgenomen van internet of één keer gemeten. Geen maatschets. Het model is een losse verzameling vormen; wanddikte < 2,5 mm of boutgaten ontbreken. Het model is niet aanpasbaar zonder opnieuw te tekenen. | Er is met de schuifmaat gemeten en er is een maatschets. Het model gebruikt sketch, dimensions, extrude en extrude-remove correct. Wanddikte ≥ 2,5 mm, boutgaten Ø4,3 mm voor M4, fillets op de buitenhoeken. Het model past binnen 120 × 120 × 120 mm. | Gemeten op 3 plekken × 2 richtingen, met min- én maxwaarde genoteerd, en het model is op de **max**waarde ontworpen. De maatschets bevat ook de omgeving (kabels, hendels, bewegende delen). `#buisD` en `#speling` staan als variabelen in het model. | Het model is echt parametrisch: één variabele wijzigen past het hele model correct aan, zonder fouten in de feature-tree. Constructieve keuzes zijn zichtbaar doordacht — materiaal weggehaald waar het niet draagt, fillets waar spanning zit, en het ontwerp is aantoonbaar aangepast op een obstakel dat je bij het meten van de omgeving ontdekte. |

---

## 3. 3D-printkennis toegepast — 15 % 🔧 Product

*Snap je hoe een FDM-print zich gedraagt, en stuur je dat bewust met oriëntatie, materiaal en supports?*

| Onvoldoende | Voldoende | Goed | Uitstekend |
|---|---|---|---|
| Het model is geprint zoals de slicer het neerlegde; oriëntatie is niet gekozen maar overkomen. Geen materiaalkeuze gemaakt of "PLA want dat lag er". Support onder het klemvlak. Het bestand printte niet in één keer door een exportfout of een te grote/te lange print. | Het bestand is correct geëxporteerd (STL/3MF) en print binnen 4 uur. De printoriëntatie is bewust gekozen en je kunt uitleggen waarom. Infill 30–40 %, 4 wanden. Prototype in PLA, eindproduct in PETG (of een afwijking die je onderbouwt). Geen support op klemvlakken. | Je legt de oriëntatie uit met anisotropie: je benoemt de belastingsrichting en laat zien dat je lagen dáár niet loodrecht op staan. De 45°-regel is toegepast. De materiaalkeuze is onderbouwd met eigenschappen (bros vs. taai, ~55–60 °C vs. ~75 °C, UV), niet met "PETG is beter". | Je hebt supports **wegontworpen** door te kantelen, af te schuinen of te splitsen — en laat zien welk probleem je daarmee voorkwam. Je onderbouwt je oriëntatie met je eigen breekproef-data (bij hoeveel newton bezweken de twee haakjes?), niet alleen met de theorie uit het projectdocument. |

---

## 4. Iteratie & testen — 20 % 🔄 Proces

*Twee iteratierondes zijn verplicht. Kun je aantonen wát er misging, wát je daarom veranderde in je CAD-model, en of dát werkte?*

| Onvoldoende | Voldoende | Goed | Uitstekend |
|---|---|---|---|
| Minder dan 2 iteraties, of "iteratie" betekent alleen: opnieuw geprint zonder het model te wijzigen. Geen testresultaten. Er ging volgens het verslag niets mis — en dat is niet geloofwaardig, want de eerste print past nooit meteen. Geen belastingstest. | 2 iteraties met bewijs in het logboek: per ronde staat er wat er misging, wat er in het CAD-model veranderde en wat het resultaat was. De testring is gebruikt. De belastingstest is uitgevoerd met de veerunster en het resultaat is genoteerd. | De analyse gaat over de **oorzaak**, niet over het symptoom: niet "hij paste niet" maar "hij paste 0,4 mm te krap omdat ik op de minmaat had ontworpen en de print bovendien krimpt". Het breukvlak is gefotografeerd en geanalyseerd (laagscheiding? te dunne wand?). De wijziging volgt logisch uit de meting. | Elke iteratie is een gerichte ingreep op één variabele, waardoor je wéét wat het effect was. Je meet vóór en na (mm, newton) en laat de verbetering met getallen zien. Je oriëntatieproef (twee haakjes, twee richtingen, allebei kapot) is uitgevoerd en de uitkomst heeft je eindontwerp aantoonbaar veranderd. Een mislukking is niet verstopt maar gebruikt. |

---

## 5. Eindproduct: functie, veiligheid & pasvorm — 20 % 🔧 Product

*Doet het wat het moet doen, past het op de échte scootmobiel, en is het veilig voor een échte gebruiker?*

| Onvoldoende | Voldoende | Goed | Uitstekend |
|---|---|---|---|
| Past niet op de scootmobiel, of valt eraf. Zakt door de schud-test of onder de 3×-last. Overtreedt een veiligheidsgrens: zit aan stuur/rem/gas, blokkeert zicht of bediening, of draagt lichaamsgewicht. Scherpe randen of uitstekende boutdraden. Lost het gekozen probleem niet op. | Het hulpmiddel zit vast op de scootmobiel, lost het probleem van de gebruiker op en voldoet aan het eigen PvE. Doorstaat de schud-test (30 s) en draagt 3× de bedoelde last zonder blijvende vervorming. Geen scherpe randen, dopmoeren gebruikt, blokkeert niets. Gaat er zonder gereedschap af. | De klemverbinding klopt: **de spleet tussen de helften blijft open** onder de aangedraaide bouten, nylock-moeren en carrosserieringen zitten erop, rubberstrip binnenin. De afwerking is netjes (ontbraamd, geschuurd). Het product is in PETG en blijft binnen de contour van de scootmobiel. | De gebruikerstest is echt uitgevoerd en het product doorstaat hem: bedienbaar met één hand, met handschoenen, zittend zonder op te staan. Het eindproduct is aantoonbaar aangepast op wat die test opleverde. Het is een product dat de gebruiker morgen kan gebruiken en niet meer wil missen — niet een schoolopdracht die toevallig past. |

---

## 6. Onderbouwing, presentatie & samenwerking — 10 % 🔄 Proces

*Kun je je keuzes uitleggen aan iemand die er niet bij was — en heb je je deel van het werk gedaan?*

| Onvoldoende | Voldoende | Goed | Uitstekend |
|---|---|---|---|
| Onderbouwing ontbreekt of beschrijft alleen wat je deed, niet waarom. Geen (eigen) logboek. STL-deadlines gemist, waardoor de printer stilstond. Geen aantoonbaar eigen CAD-werk. De presentatie is een verhaal waarin alles meteen goed ging. | Onderbouwing van 3–5 pagina's met probleem, PvE, ontwerpkeuzes, materiaalkeuze, beide iteraties, testresultaten en de 6 deelvragen beantwoord met bewijs uit het logboek. Eigen logboek per les. Deadlines gehaald. Presentatie van 8 minuten met probleem → oplossing → wat ging er mis. Elke leerling heeft aantoonbaar eigen CAD-werk geleverd. | Elke keuze is onderbouwd mét een reden en een bron: waarom déze speling (uit je testring), waarom déze oriëntatie (uit je breekproef), waarom PETG (uit de materiaaleigenschappen). Foto's van mislukte prints en breukvlakken staan erin. De taakverdeling staat in het logboek en klopt met wat er is opgeleverd. | Je legt eerlijk uit wat er misging én wat je er de vólgende keer anders in zou doen. Je onderbouwing kan een andere leerling gebruiken om jouw ontwerp na te bouwen. In de presentatie kun je een kritische vraag over een ontwerpkeuze beantwoorden met een getal of een testresultaat, niet met een mening. |

---

## Beoordelingstips voor de docent

**1. Vraag naar de mislukte print, niet naar het eindproduct.**
Het eindproduct laat zien of het werkt; de mislukte print laat zien of ze het begrijpen. Een groep die geen enkele fout kan laten zien, heeft óf niet getest óf het bewijs weggegooid — beide zijn een probleem bij criterium 4. Leg de v1-print naast de v2-print op tafel en laat ze het verschil aanwijzen en verklaren. Dat gesprek van twee minuten onderscheidt "Voldoende" van "Goed" beter dan het hele verslag.

**2. Toets de tolerantie met één vraag.**
"Welke buismaat heb je gemeten, en welke maat staat er in je CAD-model?" Het verschil moet 0,3–0,5 mm zijn, en de leerling moet dat verschil kunnen verklaren (krimp, elephant foot, meetfout). Kan hij het getal niet noemen of is het verschil 0,0 mm, dan is het CAD-model niet begrepen maar overgetekend — ongeacht hoe mooi het model eruitziet.

**3. Beoordeel criterium 5 fysiek, op de scootmobiel, met de veerunster erbij.**
Niet op foto en niet op het model. Hang het gewicht eraan (3× de bedoelde last), doe de schud-test van 30 seconden, en voel met je hand over de randen. Veiligheidsgrenzen zijn geen weging maar een drempel: een product dat aan de rem zit of waar een mens op kan steunen, is Onvoldoende op criterium 5 — hoe goed het CAD-werk ook is. Dat is geen strengheid, dat is de kern van het vak: een ontwerp dat gevaarlijk is, is geen goed ontwerp.
