# 🐍 Escape the Python

_Ein konsolenbasiertes Python-Spiel zum Erraten eines Lösungswortes mit Wikipedia-Hinweisen und schlangenstarker Visualisierung._

## 🎮 Spielidee

"Escape the Python" ist ein Hangman-artiges Text-Adventure, bei dem du aus Wikipedia-Titeln Buchstaben errätst, um ein geheimes Wort zu entschlüsseln. Das Spiel setzt auf ein raffiniertes **MVC-Architekturmodell** und nutzt eine einfache **CLI-Oberfläche mit Rich**.

### 🔥 Besonderheiten

- **Modulares MVC-Design** (Model, View, Controller)
- **Dynamische Hilfen** durch Wikipedia-Artikel (über `wikipedia`-API)
- **ASCII-Art-Schlange** als visuelle Darstellung der Gefahr 😱
- **Spannende Spielmechanik** mit Trials, Buchstabenlogik & Schwierigkeitsanpassung
- **Witzige Texte**, Typo-Animationen & Gamification-Elemente

---

## 🧠 Technologien

| Kategorie | Details |
|----------|---------|
| Programmiersprache | Python 3.10+ |
| Architektur | MVC |
| Bibliotheken | `rich`, `wikipedia`, `faker`, `random`, `re`, `time` |
| Ausführung | Terminal/Konsole |
| Eingabe | Benutzertext über CLI |

---

## 🧩 Spielmechanik

1. Das Spiel startet mit einem **Zufallswort** (z. B. eine deutsche Stadt).
2. Du bekommst eine Auswahl an **Wikipedia-Artikeln** zum Thema „Python (genus)“.
3. Wähle aus diesen Artikeln Buchstaben aus, um das Lösungswort zu erraten.
4. Jeder falsche oder doppelte Versuch kostet ein Leben.
5. Je nach Leistung **verringert sich der Abstand** zur tödlichen Python... 🐍

---

## 📁 Projektstruktur

