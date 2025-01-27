# Open LP21 - Offener Lehrplan 21

Dieses Repository enthält den Lehrplan 21 in verschidenen maschienenlesbaren Formaten.

Der Lehrplan 21 ist der am weitesten verbreitete Lehrplan der Schweiz. Die Datenquelle für dieses Projekt ist die [Berner Version des Plans](https://be.lehrplan.ch/) im PDF Format.

Dokumentation und Inhalt sind in Deutsch gehalten. Code, Datenbank, Header und JSON Keys sind Englisch.

## PDF

- [Karteikarten Kindergarten](content/pdf/Karteikarten%20Kindergarten.pdf)
- [Karteikarten 1-2. Klasse Grundanforderungen](content/pdf/Karteikarten%201-2.%20Klasse%20Grundanforderungen.pdf)
- [Karteikarten 1-2. Klasse Optional](content/pdf/Karteikarten%201-2.%20Klasse%20Optional.pdf)
- [Karteikarten 3-4. Klasse Grundanforderungen](content/pdf/Karteikarten%203-4.%20Klasse%20Grundanforderungen.pdf)
- [Karteikarten 3-4. Klasse Optional](content/pdf/Karteikarten%203-4.%20Klasse%20Optional.pdf)
- [Karteikarten 5-6. Klasse Grundanforderungen](content/pdf/Karteikarten%205-6.%20Klasse%20Grundanforderungen.pdf)
- [Karteikarten 5-6. Klasse Optional](content/pdf/Karteikarten%205-6.%20Klasse%20Optional.pdf)
- [Karteikarten 7-8. Klasse Grundanforderungen](content/pdf/Karteikarten%207-8.%20Klasse%20Grundanforderungen.pdf)
- [Karteikarten 7-8. Klasse Optional](content/pdf/Karteikarten%207-8.%20Klasse%20Optional.pdf)
- [Karteikarten 9. Klasse Grundanforderungen](content/pdf/Karteikarten%209.%20Klasse%20Grundanforderungen.pdf)
- [Karteikarten 9. Klasse Optional](content/pdf/Karteikarten%209.%20Klasse%20Optional.pdf)

## Aufteilung

### Zusammenfassung Lehrplan 21 nach Klassen

| Jahr                     | Anzahl Ziele | Optional | Zyklus Code |
| ------------------------ | ------------ | -------- | ----------- |
| Kindergarten - 2. Klasse | 360          | nein     | 1           |
| Kindergarten - 4. Klasse | 82           | nein     | 1,2a        |
| Kindergarten - 6. Klasse | 14           | nein     | 1,2         |
| 1. - 2. Klasse           | 72           | nein     | 1b          |
| 1. - 4. Klasse           | 19           | nein     | 1b,2a       |
| 3. - 4. Klasse           | 194          | nein     | 2a          |
| 3. - 6. Klasse           | 85           | nein     | 2           |
| 3. - 8. Klasse           | 5            | nein     | 2,3a        |
| 3. - 9. Klasse           | 15           | nein     | 2,3         |
| 5. - 6. Klasse           | 156          | nein     | 2b          |
| 5. - 8. Klasse           | 138          | nein     | 2b,3a       |
| 5. - 8. Klasse           | 1            | ja       | 2b,3ao      |
| 5. - 9. Klasse           | 2            | nein     | 2b,3        |
| 7. - 8. Klasse           | 138          | nein     | 3a          |
| 7. - 8. Klasse           | 3            | ja       | 3ao         |
| 7. - 9. Klasse           | 61           | nein     | 3           |
| 7. - 9. Klasse           | 19           | ja       | 3o          |
| 9. Klasse                | 23           | nein     | 3b          |
| 9. Klasse                | 117          | ja       | 3bo         |

Zyklus Code Erklärung

- 1 bis 3: Zyklus Nummer
- a: erste Hälfte des Zylus
- b: zweite Hälfte des Zylus
- o: optionales Ziel

Viele Ziele sind mehreren Zyklen zugeordnet. Dort spielt es keine Rolle wann sie erledigt werden.

### Anzahl Ziele nach Fach und Zyklus

| Fach \ Zyklus | 1   | 1,2 | 1,2a | 1b  | 1b,2a | 2   | 2,3 | 2,3a | 2a  | 2b  | 2b,3 | 2b,3a | 2b,3ao | 3   | 3a  | 3ao | 3b  | 3bo | 3o  |
| ------------- | --- | --- | ---- | --- | ----- | --- | --- | ---- | --- | --- | ---- | ----- | ------ | --- | --- | --- | --- | --- | --- |
| BG            | 29  | 9   | 0    | 0   | 0     | 30  | 11  | 0    | 0   | 0   | 0    | 0     | 0      | 30  | 0   | 0   | 0   | 0   | 8   |
| BS            | 69  | 0   | 25   | 0   | 0     | 0   | 0   | 0    | 40  | 5   | 0    | 27    | 0      | 0   | 38  | 0   | 0   | 32  | 0   |
| D             | 52  | 0   | 11   | 10  | 6     | 0   | 0   | 0    | 27  | 22  | 0    | 21    | 0      | 0   | 29  | 0   | 0   | 25  | 1   |
| MA            | 55  | 0   | 17   | 12  | 3     | 2   | 0   | 0    | 36  | 31  | 2    | 21    | 1      | 4   | 32  | 3   | 16  | 27  | 4   |
| MI            | 11  | 0   | 2    | 0   | 0     | 0   | 0   | 0    | 6   | 15  | 0    | 7     | 0      | 0   | 13  | 0   | 1   | 9   | 0   |
| MU            | 42  | 0   | 7    | 9   | 1     | 0   | 0   | 0    | 25  | 16  | 0    | 15    | 0      | 0   | 26  | 0   | 6   | 24  | 0   |
| NMG           | 76  | 0   | 20   | 41  | 9     | 26  | 0   | 5    | 60  | 67  | 0    | 47    | 0      | 0   | 0   | 0   | 0   | 0   | 0   |
| TTG           | 26  | 5   | 0    | 0   | 0     | 27  | 4   | 0    | 0   | 0   | 0    | 0     | 0      | 27  | 0   | 0   | 0   | 0   | 6   |
| Total         | 360 | 14  | 82   | 72  | 19    | 85  | 15  | 5    | 194 | 156 | 2    | 138   | 1      | 61  | 138 | 3   | 23  | 117 | 19  |

## Stand Oktober 24

Nicht der Ganze Lehrplan ist erfasst. Zur Zeit sind alle Kompentenzen erfasst. Ziele sind für alle Fächser erfasst, welche für den 1. Zyklus relevant sind.

### Offene Punkte

- [ ] 1. Fremdsprache (Französisch)
- [ ] 2. Fremdsprache (Englisch)
- [ ] 3. Fremdsprache (Italjenisch)
- [ ] NMG Nachfolgefächer ab dem 3. Zyklus
