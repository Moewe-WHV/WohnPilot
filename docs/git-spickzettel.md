# Git-Spickzettel

Für alle, die zum ersten Mal mit Git und GitHub arbeiten. Oft nachschauen ist völlig okay, das machen alle so.

## Die fünf Wörter

| Wort | Bedeutung | Vergleich |
|---|---|---|
| Repository | Unser Projektordner mit dem kompletten Verlauf | Der Familienordner mit allen Unterlagen und einem Protokoll, wer wann was geändert hat |
| Commit | Ein Speicherpunkt mit kurzer Nachricht | Ein Foto vom aktuellen Stand |
| Branch | Deine eigene Arbeitskopie, getrennt vom Rest | Eine Kopie des Einkaufszettels, auf der du planst, ohne das Original vollzukritzeln |
| Pull Request (PR) | Bitte an andere: „Schaut euch meine Änderung an, bevor sie in `main` kommt“ | Ein Zweiter liest den Zettel gegen, bevor er an die ganze Familie geht |
| `main` | Der gemeinsame, fertige Stand. Er muss immer laufen | Der Original-Wochenplan an der Pinnwand |

## Einmalig: das Projekt holen

Auf GitHub beim Repository auf den grünen Knopf **Code** klicken, die Adresse kopieren und im Terminal eingeben:

```bash
git clone <kopierte-Adresse>
```

Danach den neuen Ordner in VS Code öffnen. Wie es weitergeht, steht im [README](../README.md).

## Jede Aufgabe: die 7 Schritte

1. **Aktuell werden:** `git checkout main` und dann `git pull`
2. **Branch anlegen:** `git checkout -b feature/t08-login` (der Name enthält die Aufgabennummer)
3. **Arbeiten.** Zwischendurch zeigt `git status`, was sich geändert hat.
4. **Speichern:** `git add .` und dann `git commit -m "feat: Login-Seite zeigt Formular"`
5. **Hochladen:** `git push -u origin feature/t08-login` (beim ersten Mal, später reicht `git push`)
6. **Pull Request öffnen:** Auf GitHub erscheint oben ein Knopf **Compare & pull request**. Sonst: Reiter **Pull requests** und **New pull request**. Titel mit Aufgabennummer, dazu zwei Sätze: Was ist neu? Wie habe ich es getestet?
7. **Prüfen lassen.** Ein anderes Paar schaut drüber. Nach dem Merge: `git checkout main`, `git pull` und weiter mit der nächsten Aufgabe.

## Wenn etwas komisch aussieht

- Zuerst `git status` ausführen. Es sagt fast immer, was los ist.
- Nie direkt auf `main` arbeiten und nie `--force` benutzen.
- **Merge-Konflikt** (Git meldet „CONFLICT“): nicht raten, den **Git-Wart** holen. Das kommt vor und ist kein Fehler von dir.
- Fehlermeldung mit `index.lock`: Meist läuft noch ein anderes Git-Programm (z. B. in VS Code oder GitKraken). Schließen und nochmal probieren. Hilft das nicht, den Git-Wart fragen.
- Etwas falsch gespeichert oder kaputt? Nichts löschen, erst fragen.

## Mehr

Regeln für Branch-Namen, Commit-Nachrichten und Pull Requests stehen in der [CONTRIBUTING.md](../CONTRIBUTING.md), Abschnitt 7.
