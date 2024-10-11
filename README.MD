# Open LP21 - Offener Lehrplan 21 

Dieses Repository enthält den Lehrplan 21 in verschidenen maschienenlesbaren Formaten.

Der Lehrplan 21 ist der am weitesten verbreitete Lehrplan der Schweiz. Die Datenquelle für dieses Projekt ist die [Berner Version des Plans](https://be.lehrplan.ch/) im PDF Format.

## Struktur

Im Moment werden die Daten aus den JSON files abgeleitet. 

Aus JSON wird mit einem Skript die Sqlite Datenbank erstellt. Daraus werden die CSV und Karteikarten generiert. Es werden Python Skripte verwendet. Die PDF werden mit Typst erzeugt. 

## Sprache

Dokumentation und Inhalt sind in Deutsch gehalten. Code, Datenbank, Header und JSON Keys sind Englisch.

## Stand Oktober 24

Nicht der Ganze Lehrplan ist erfasst. Zur Zeit sind alle Kompentenzen erfasst. Ziele sind für alle Fächser erfasst, welche für den 1. Zyklus relevant sind. 

### Offene Punkte

- [ ] 1. Fremdsprache (Französisch)
- [ ] 2. Fremdsprache (Englisch)
- [ ] 3. Fremdsprache (Italjenisch)
- [ ] NMG Nachfolgefächer ab dem 3. Zyklus
