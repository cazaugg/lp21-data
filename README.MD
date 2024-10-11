# Open LP21 - Offener Lehrplan 21 

Dieses Repository enthält den Lehrplan 21 in verschidenen maschienenlesbaren Formaten.

Der Lehrplan 21 ist der am weitesten verbreitete Lehrplan der Schweiz. Die Datenquelle für dieses Projekt ist die [Berner Version des Plans](https://be.lehrplan.ch/) im PDF Format.

## Struktur und Formate

Im Moment werden die Daten aus den JSON files abgeleitet. 

Aus JSON wird mit einem Skript die Sqlite Datenbank erstellt. Daraus werden die CSV und Karteikarten generiert. Es werden Python Skripte verwendet. Die PDF werden mit Typst erzeugt. 

### CSV

- Enthält sowohl einzelne Tabellen als auch einen kompletten Zusammenzug 'lp21.json'
- UTF8 encodierte CSV Daten. Excel verwendet als Standard Windows 1252 kann UTF8 lesen. Nicht alle im Lehrplan 21 verwendet Schriftzeichen können mit dem Windows Text Encoding dargestellt werden.
- Kommasepariert mit Anführungszeichen. Texte enthalten zum Teil Zeilenumbrüche.

## Sprache

Dokumentation und Inhalt sind in Deutsch gehalten. Code, Datenbank, Header und JSON Keys sind Englisch.

## Aufteilung

Zusammenfassung Lehrplan 21 nach Klassen:

| Jahr | Anzahl Ziele | Optional | Zyklus Code |
| ---- | ------------ | -------- | ----------- |
| Kindergarten - 2. Klasse | 360 | nein | 1 |
| Kindergarten - 4. Klasse | 82 | nein | 1,2a |
| Kindergarten - 6. Klasse | 14 | nein | 1,2 |
| 1. - 2. Klasse | 72 | nein | 1b |
| 1. - 4. Klasse | 19 | nein | 1b,2a |
| 3. - 4. Klasse | 194 | nein | 2a |
| 3. - 6. Klasse | 85 | nein | 2 |
| 3. - 8. Klasse | 5 | nein | 2,3a |
| 3. - 9. Klasse | 15 | nein | 2,3 |
| 5. - 6. Klasse | 156 | nein | 2b |
| 5. - 8. Klasse | 138 | nein | 2b,3a |
| 5. - 8. Klasse | 1 | ja | 2b,3ao |
| 5. - 9. Klasse | 2 | nein | 2b,3 |
| 7. - 8. Klasse | 138 | nein | 3a |
| 7. - 8. Klasse | 3 | ja | 3ao |
| 7. - 9. Klasse | 61 | nein | 3 |
| 7. - 9. Klasse | 19 | ja | 3o |
| 9. Klasse | 23 | nein | 3b |
| 9. Klasse | 117 | ja | 3bo |


## Stand Oktober 24

Nicht der Ganze Lehrplan ist erfasst. Zur Zeit sind alle Kompentenzen erfasst. Ziele sind für alle Fächser erfasst, welche für den 1. Zyklus relevant sind. 

### Offene Punkte

- [ ] 1. Fremdsprache (Französisch)
- [ ] 2. Fremdsprache (Englisch)
- [ ] 3. Fremdsprache (Italjenisch)
- [ ] NMG Nachfolgefächer ab dem 3. Zyklus
